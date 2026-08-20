#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Daricomma Question Bank Fetcher
================================

An interactive CLI tool that downloads question-bank questions from the
Daricomma (com.education.daricomma) backend and saves them locally.

HOW THE API WORKS (discovered from the app)
-------------------------------------------
1. AUTH
     POST https://daricomma.com/api/auth/login
     body  : { "mobile": "<number>", "password": "<sha256-hex of password>" }
     resp  : { status, code, message, access_token, refresh_token, sessionKey }
   NOTE: the app sends the SHA-256 hex digest of the password (not the plain
   password). The returned JWT must be attached as:
       Authorization: Bearer <access_token>

2. HIERARCHY (everything in one call)
     GET https://daricomma.com/api/field        (authenticated)
     resp: data.curriculums[].versions[].classes[].groups[].subjects[].chapters[]
     Each chapter has: { "id": <uuid>, "name": <string> }

3. QUESTION LIST (per chapter, paginated)
     GET https://daricomma.com/api/v2/question/<chapter_id>?page=<n>
     optional filters appended as  &<key>[]=<id>   (e.g. &question_type_id[]=...)
     optional search  appended as  &search=<text>
     resp: {
       status, code,
       data: {
         questions: [ { question_text, answer_text, explanation_text,
                        option[], id, topic, question_type, question_level,
                        mcq_solution_index, question_subsources,
                        user_reaction, question_priority, question_Rating }, ... ],
         total_questions: <int>, questionPerPage: <int(=25)>
       }
     }

4. FILTER OPTIONS (for building filter menus)
     GET https://daricomma.com/api/question/filter-options/<chapter_id>
     resp: { types[], levels[], topics[], sub_topics[], sources[],
             sub_sources[], years[], tags[] }

USAGE
-----
    python question_bank_fetcher.py

The program asks you to pick (by serial number):
    class -> group (if any) -> subject -> chapter -> (optional) filters
then downloads every page of questions and writes:
    * question_bank_<class>_<subject>_<chapter>.json  (exact API response format)
    * question_bank_<class>_<subject>_<chapter>.txt   (human-readable dump)

Credentials and the API base URL can be edited in the CONFIG section below.
The access token is cached in .daricomma_session.json and re-used; a new
login happens automatically when it expires.
"""

import base64
import hashlib
import json
import os
import re
import sys
import time

import requests

# ---------------------------------------------------------------------------
# CONFIG
# ---------------------------------------------------------------------------
BASE_URL = "https://daricomma.com/api"
MOBILE = "01915575697"
PASSWORD = "6251@TAWHId"  # plain password; SHA-256 is computed automatically
SESSION_CACHE = os.path.join(os.path.dirname(os.path.abspath(__file__)), ".daricomma_session.json")
PAGE_DELAY_SECONDS = 1.2          # be gentle with the server rate limiter
TIMEOUT_SECONDS = 60
MAX_429_RETRIES = 4

INVALID_FILENAME_CHARS = re.compile(r'[<>:"/\\|?*\x00-\x1f]')

# ---------------------------------------------------------------------------
# Small console helpers
# ---------------------------------------------------------------------------
def _bprint(message: str) -> None:
    print(message)


def _ensure_utf8_stdout() -> None:
    try:
        sys.stdout.reconfigure(encoding="utf-8")
        sys.stderr.reconfigure(encoding="utf-8")
    except Exception:
        pass


def _read_input(prompt: str = "") -> str:
    """Read one line of input, stripping BOM/whitespace artifacts."""
    try:
        return input(prompt).strip().lstrip("\ufeff")
    except EOFError:
        _bprint("\nInput ended. Goodbye!")
        sys.exit(0)


def safe_filename(name: str) -> str:
    name = INVALID_FILENAME_CHARS.sub("_", name).strip().strip(".")
    name = re.sub(r"\s+", "_", name)
    return name or "unnamed"


def decode_jwt_payload(token: str):
    """Best-effort decode of a JWT payload (for the exp check)."""
    try:
        payload = token.split(".")[1]
        payload += "=" * (-len(payload) % 4)
        return json.loads(base64.urlsafe_b64decode(payload.encode()))
    except Exception:
        return {}


def draftjs_to_text(value) -> str:
    """Flatten a Draft.js payload (blocks[]) or a plain string to readable text."""
    if value is None:
        return ""
    if isinstance(value, str):
        return value
    if isinstance(value, dict):
        blocks = value.get("blocks") or []
        return "\n".join(b.get("text", "") for b in blocks if b.get("text"))
    if isinstance(value, list):
        return "\n".join(draftjs_to_text(item) for item in value)
    return str(value)


# ---------------------------------------------------------------------------
# Daricomma API client
# ---------------------------------------------------------------------------
class DaricommaClient:
    """Thin wrapper around the authenticated Daricomma REST API."""

    def __init__(self, base_url: str = BASE_URL, mobile: str = MOBILE,
                 password: str = PASSWORD, session_cache: str = SESSION_CACHE):
        self.base_url = base_url.rstrip("/")
        self.mobile = mobile
        self.password_digest = hashlib.sha256(password.encode("utf-8")).hexdigest()
        self.session_cache = session_cache
        self.session = requests.Session()
        self.session.headers.update({
            "Accept": "application/json",
            "User-Agent": "Dart/3.3 (dart:io)",
        })
        self.access_token = None
        self._load_cached_token()

    # -- token handling -------------------------------------------------
    def _load_cached_token(self) -> None:
        try:
            with open(self.session_cache, "r", encoding="utf-8") as fh:
                data = json.load(fh)
            if data.get("mobile") == self.mobile and data.get("access_token"):
                exp = decode_jwt_payload(data["access_token"]).get("exp", 0) or 0
                if exp - 60 > time.time():
                    self.access_token = data["access_token"]
        except Exception:
            pass

    def _save_cached_token(self) -> None:
        try:
            with open(self.session_cache, "w", encoding="utf-8") as fh:
                json.dump({"mobile": self.mobile, "access_token": self.access_token}, fh)
        except Exception:
            pass

    def login(self) -> None:
        """Authenticate with the API and store the access token."""
        resp = self.session.post(
            f"{self.base_url}/auth/login",
            json={"mobile": self.mobile, "password": self.password_digest},
            timeout=TIMEOUT_SECONDS,
        )
        if resp.status_code == 429:
            _bprint("! Rate limited during login; waiting a moment...")
            time.sleep(8)
            return self.login()
        body = self._try_json(resp)
        if resp.status_code == 401:
            msg = (body or {}).get("message") or body.get("code") or "Unauthorized"
            raise RuntimeError(
                f"Login failed ({resp.status_code}): {msg}. "
                f"Check MOBILE / PASSWORD in the CONFIG section."
            )
        if not resp.ok or not body.get("access_token"):
            raise RuntimeError(f"Login failed: HTTP {resp.status_code} -> {body}")
        self.access_token = body["access_token"]
        self._save_cached_token()
        _bprint("  Logged in as {} (role: {}).".format(
            self.mobile,
            decode_jwt_payload(self.access_token).get("role") or "?"))

    # -- low-level request ----------------------------------------------
    @staticmethod
    def _try_json(resp) -> dict:
        try:
            return resp.json()
        except Exception:
            return {}

    def _request(self, method: str, path: str, params=None, retry_auth: bool = True):
        headers = {}
        if self.access_token:
            headers["Authorization"] = f"Bearer {self.access_token}"
        url = f"{self.base_url}{path}"
        for attempt in range(MAX_429_RETRIES + 1):
            resp = self.session.request(method, url, headers=headers, params=params,
                                        timeout=TIMEOUT_SECONDS)
            if resp.status_code == 429:
                wait = 5 * (attempt + 1)
                _bprint(f"! Rate limited (429); retrying in {wait}s ...")
                time.sleep(wait)
                continue
            if resp.status_code == 401 and retry_auth:
                _bprint("! Token expired; re-logging in ...")
                self.access_token = None
                self.login()
                return self._request(method, path, params=params, retry_auth=False)
            return resp
        raise RuntimeError(f"Request to {url} kept failing with HTTP 429.")

    # -- API endpoints ---------------------------------------------------
    def get_field(self) -> list:
        """Return the full curriculum -> class -> subject -> chapter tree."""
        resp = self._request("GET", "/field")
        body = self._try_json(resp)
        if resp.status_code != 200:
            raise RuntimeError(f"GET /field failed: HTTP {resp.status_code} -> {body}")
        try:
            curriculums = body["data"]["curriculums"]
        except (KeyError, TypeError):
            raise RuntimeError(f"Unexpected /field response: {str(body)[:300]}")
        return curriculums or []

    def get_filter_options(self, chapter_id: str) -> dict:
        resp = self._request("GET", f"/question/filter-options/{chapter_id}")
        body = self._try_json(resp)
        if resp.status_code != 200:
            raise RuntimeError(
                f"GET filter-options failed: HTTP {resp.status_code} -> {body}")
        return body if isinstance(body, dict) else {}

    def get_question_page(self, chapter_id: str, page: int, filters=None) -> dict:
        params = {"page": page}
        for key, ids in (filters or {}).items():
            for value in ids:
                params[f"{key}[]"] = value
        resp = self._request("GET", f"/v2/question/{chapter_id}", params=params)
        body = self._try_json(resp)
        if resp.status_code != 200 or not isinstance(body.get("data"), dict):
            raise RuntimeError(
                f"GET questions (page {page}) failed: HTTP {resp.status_code} -> "
                f"{str(body)[:300]}")
        return body["data"]

    def get_all_questions(self, chapter_id: str, filters=None):
        """Download every page of a chapter's questions.

        Returns (questions, total_questions, per_page).
        """
        first = self.get_question_page(chapter_id, page=1, filters=filters)
        questions = list(first.get("questions") or [])
        total = first.get("total_questions") or len(questions)
        per_page = first.get("questionPerPage") or 25

        page = 2
        while len(questions) < total:
            time.sleep(PAGE_DELAY_SECONDS)
            chunk = self.get_question_page(chapter_id, page=page, filters=filters)
            chunk_questions = chunk.get("questions") or []
            if not chunk_questions:
                break
            questions.extend(chunk_questions)
            _bprint(f"    ... page {page}: {len(questions)} / {total} questions")
            page += 1
        if len(questions) > total:
            questions = questions[:total]
        return questions, total, per_page


# ---------------------------------------------------------------------------
# Interactive navigation helpers
# ---------------------------------------------------------------------------
def pick_one(title: str, items: list, key: str = "name") -> object:
    """Show a numbered menu and return the chosen item (or None to quit)."""
    while True:
        _bprint("")
        _bprint(title)
        for idx, item in enumerate(items, start=1):
            label = item.get(key) if isinstance(item, dict) else item
            _bprint(f"  {idx}. {label}")
        _bprint("  0. Quit")
        raw = _read_input("Enter serial number: ")
        if raw.lower() in ("q", "quit", "exit"):
            return None
        if not raw.isdigit() or not (1 <= int(raw) <= len(items)):
            _bprint(f"  Invalid choice. Enter a number between 1 and {len(items)}.")
            continue
        return items[int(raw) - 1]


def pick_many(title: str, items: list, key: str = "name"):
    """Multi-select menu; returns the list of chosen items (empty = nothing)."""
    chosen = []
    while True:
        _bprint("")
        _bprint(title)
        for idx, item in enumerate(items, start=1):
            label = item.get(key) if isinstance(item, dict) else item
            mark = " [x]" if idx in chosen else ""
            _bprint(f"  {idx}. {label}{mark}")
        _bprint("  0. Done / cancel")
        raw = _read_input("Enter serial numbers (comma separated): ")
        if not raw:
            continue
        if raw.lower() in ("q", "quit", "exit"):
            return None
        if raw == "0":
            break
        for token in raw.split(","):
            token = token.strip()
            if token.isdigit() and 1 <= int(token) <= len(items):
                idx = int(token)
                if idx in chosen:
                    chosen.remove(idx)
                else:
                    chosen.append(idx)
            else:
                _bprint(f"  Ignoring invalid number: {token!r}")
    return [items[i - 1] for i in chosen]


# ---------------------------------------------------------------------------
# Selection chain: class -> group -> subject -> chapter
# ---------------------------------------------------------------------------
def select_bank_chain(curriculums: list):
    """Walk the curriculum tree interactively; returns (meta, chapter)."""
    curriculum = pick_one("Select CURRICULUM:", curriculums)
    if curriculum is None:
        return None
    versions = curriculum.get("versions") or []
    if len(versions) > 1:
        version = pick_one("Select VERSION:", versions)
        if version is None:
            return None
    else:
        version = versions[0] if versions else {}
        _bprint(f"\nVERSION: {version.get('name')}")

    classes = version.get("classes") or []
    if not classes:
        _bprint("  No classes available under this version.")
        return None
    klass = pick_one("Select CLASS:", classes)
    if klass is None:
        return None

    groups = klass.get("groups") or []
    if len(groups) == 1:
        group = groups[0]
        _bprint(f"\nGROUP: {group.get('name')}")
    elif not groups:
        group = None
    else:
        group = pick_one("Select GROUP:", groups)
        if group is None:
            return None

    subjects = (group or {}).get("subjects") or []
    if not subjects:
        _bprint("  No subjects available for this selection.")
        return None
    subject = pick_one("Select SUBJECT:", subjects)
    if subject is None:
        return None

    chapters = subject.get("chapters") or []
    if not chapters:
        _bprint("  No chapters available for this subject.")
        return None
    chapter = pick_one("Select CHAPTER:", chapters)
    if chapter is None:
        return None

    meta = {
        "curriculum": curriculum.get("name"),
        "version": (version or {}).get("name"),
        "class": klass.get("name"),
        "group": (group or {}).get("name", ""),
        "subject": subject.get("name"),
    }
    return meta, chapter


# ---------------------------------------------------------------------------
# Optional filters
# ---------------------------------------------------------------------------
FILTER_MAP = [
    ("question_type_id", "question type", "types"),
    ("question_level_id", "question level", "levels"),
    ("topic_id", "topic", "topics"),
    ("sub_topic_id", "sub-topic", "sub_topics"),
    ("source_id", "source", "sources"),
    ("sub_source_id", "sub-source", "sub_sources"),
    ("year_id", "year", "years"),
    ("tag_id", "tag", "tags"),
]


def select_filters(client, chapter_id: str):
    """Optionally restrict the question set by type/level/year/..."""
    _bprint("")
    raw = _read_input("Apply additional filters? [y/N]: ").lower()
    if raw not in ("y", "yes"):
        return {}
    options = client.get_filter_options(chapter_id)
    filters = {}
    for key, label, section in FILTER_MAP:
        items = options.get(section) or []
        if not items:
            continue
        selected = pick_many(f"Filter by {label.upper()} (toggle serial numbers):", items)
        if selected is None:
            return None
        if selected:
            filters[key] = [item["id"] for item in selected]
    return filters


# ---------------------------------------------------------------------------
# Output
# ---------------------------------------------------------------------------
def save_outputs(meta, chapter, questions, total, per_page, filters):
    stem = safe_filename(f"{meta['class']}_{meta['subject']}_{chapter['name']}")
    stem = re.sub(r"[_]+", "_", stem).strip("_")
    json_path = f"question_bank_{stem}.json"
    txt_path = f"question_bank_{stem}.txt"

    payload = {
        "status": "success",
        "code": 200,
        "data": {
            "questions": questions,
            "total_questions": total,
            "questionPerPage": per_page,
        },
    }
    with open(json_path, "w", encoding="utf-8") as fh:
        json.dump(payload, fh, ensure_ascii=False, indent=2)

    lines = []
    lines.append("=" * 78)
    lines.append("DARICOMMA QUESTION BANK  -  downloaded questions")
    lines.append("=" * 78)
    for key, value in meta.items():
        if value:
            lines.append(f"{key.capitalize():>11}: {value}")
    lines.append(f"{'Chapter':>11}: {chapter['name']}")
    if filters:
        lines.append(f"{'Filters':>11}: " + ", ".join(
            f"{k.replace('_id', '')}={len(v)}" for k, v in filters.items()))
    lines.append(f"{'Count':>11}: {total}")
    lines.append("=" * 78)

    for idx, question in enumerate(questions, start=1):
        lines.append("")
        lines.append(f"[{idx}] {draftjs_to_text(question.get('question_text'))}")
        qtype = (question.get("question_type") or {}).get("name") or "?"
        mark = (question.get("question_type") or {}).get("mark")
        topic = (question.get("topic") or {}).get("name")
        level = (question.get("question_level") or {}).get("name")
        header = qtype + (f" ({mark} mark)" if mark else "")
        if topic:
            header += f" | Topic: {topic}"
        if level:
            header += f" | {level}"
        lines.append(f"    {header}")
        options = question.get("option") or []
        if options:
            correct = question.get("mcq_solution_index")
            for oi, option in enumerate(options, start=1):
                tag = ""
                if isinstance(correct, int) and correct >= 0 and oi - 1 == correct:
                    tag = "  <-- Correct"
                lines.append(f"    {chr(64 + oi)}. {option}{tag}")
        answer = draftjs_to_text(question.get("answer_text"))
        if answer:
            lines.append(f"    Answer: {answer}")
        explanation = draftjs_to_text(question.get("explanation_text"))
        if explanation:
            lines.append(f"    Explanation: {explanation}")
        sources = question.get("question_subsources") or []
        if sources:
            parts = []
            for sub in sources:
                sub_source = (sub.get("sub_source") or {}).get("name")
                year = (sub.get("year") or {}).get("name")
                if sub_source:
                    parts.append(sub_source)
                if year:
                    parts.append(year)
            if parts:
                lines.append(f"    Source: {', '.join(parts)}")

    with open(txt_path, "w", encoding="utf-8") as fh:
        fh.write("\n".join(lines))

    return json_path, txt_path, lines


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------
def main():
    _ensure_utf8_stdout()
    _bprint("=" * 78)
    _bprint("DARICOMMA QUESTION BANK FETCHER")
    _bprint("=" * 78)

    client = DaricommaClient()
    try:
        client.login()
    except RuntimeError as exc:
        _bprint(f"\nERROR: {exc}")
        sys.exit(1)

    _bprint("\nLoading the class/subject/chapter tree ...")
    curriculums = client.get_field()
    if not curriculums:
        _bprint("\nERROR: The API returned no curricula/subjects.")
        sys.exit(1)

    chain = select_bank_chain(curriculums)
    if chain is None:
        _bprint("\nQuit.")
        return
    meta, chapter = chain

    filters = select_filters(client, chapter["id"])
    if filters is None:
        _bprint("\nQuit.")
        return

    _bprint(f"\nDownloading questions for chapter '{chapter['name']}' ...")
    if filters:
        _bprint("  Using {} filter value(s): {}".format(
            sum(len(v) for v in filters.values()),
            ", ".join(f"{k}={v}" for k, v in filters.items())))
    questions, total, per_page = client.get_all_questions(chapter["id"], filters)
    if not questions:
        _bprint("\nNo questions found for this chapter" +
                (" with the selected filters." if filters else "."))
        return

    json_path, txt_path, lines = save_outputs(meta, chapter, questions, total, per_page, filters)
    _bprint(f"\nDone! {len(questions)} question(s) downloaded.")
    _bprint(f"  JSON (API format): {os.path.abspath(json_path)}")
    _bprint(f"  Readable dump    : {os.path.abspath(txt_path)}")
    _bprint("")
    _bprint("PREVIEW (first 3 questions):")
    preview = [line for line in lines if "[1]" in line or "[2]" in line or "[3]" in line]
    _bprint("\n".join(preview) if preview else lines[0])


if __name__ == "__main__":
    main()