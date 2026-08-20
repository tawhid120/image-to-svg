import json, time, urllib.request, hashlib, sys

BASE = "https://daricomma.com/api"
MOBILE = "01915575697"
PASSWORD_DIGEST = hashlib.sha256("6251@TAWHId".encode()).hexdigest()

def post(path, body):
    req = urllib.request.Request(BASE + path, data=json.dumps(body).encode(),
                                 headers={"Content-Type": "application/json",
                                          "Accept": "application/json",
                                          "User-Agent": "Dart/3.3 (dart:io)"})
    with urllib.request.urlopen(req, timeout=60) as r:
        return json.loads(r.read().decode())

def get(path, token, params=None):
    url = BASE + path
    if params:
        url += "?" + urllib.parse.urlencode(params)
    req = urllib.request.Request(url, headers={"Authorization": f"Bearer {token}",
                                               "Accept": "application/json",
                                               "User-Agent": "Dart/3.3 (dart:io)"})
    with urllib.request.urlopen(req, timeout=60) as r:
        return json.loads(r.read().decode())

import urllib.parse

resp = post("/auth/login", {"mobile": MOBILE, "password": PASSWORD_DIGEST})
token = resp.get("access_token")
if not token:
    print("LOGIN FAILED:", resp); sys.exit(1)
print("logged in")

field = get("/field", token)
curriculums = field["data"]["curriculums"]
targets = []
def walk(c):
    for v in c.get("versions") or []:
        for k in v.get("classes") or []:
            for g in k.get("groups") or []:
                for s in g.get("subjects") or []:
                    for ch in s.get("chapters") or []:
                        if "স্থির" in ch.get("name", ""):
                            targets.append(ch)
for c in curriculums:
    walk(c)
for t in targets:
    print("chapter:", t["id"], t["name"])
if not targets:
    print("CHAPTER NOT FOUND"); sys.exit(1)

want = {"f39e0608-5b38-4a0a-b250-5b1ab944fb80", "b1faeb6a-ba4e-4ca1-91fa-589caff5e5ff",
        "e1170f9b-7c01-4087-bff4-1f86edccb026", "710bdcfc-4b6d-4164-8a27-759ee16e245a"}
found = {}
for t in targets:
    data0 = get(f"/v2/question/{t['id']}", token, {"page": 1})
    print("  RAW:", json.dumps(data0, ensure_ascii=False)[:1500])
    for page in range(1, 40):
        data = get(f"/v2/question/{t['id']}", token,
                   {"page": page, "search": "B বিন্দুর প্রাবল্য"})
        qs = data.get("questions") or []
        if not qs:
            break
        for q in qs:
            print("  match:", q.get("id"), str(q.get("mcq_solution_index")))
            if q.get("id") in want:
                found[q["id"]] = q
        time.sleep(0.7)
    if len(found) == len(want):
        break

print("found:", len(found))
for qid in want:
    q = found.get(qid)
    if not q:
        print(qid, "-> NOT FOUND in first 5 pages"); continue
    print("=" * 70)
    print(qid)
    print("  index:", q.get("mcq_solution_index"))
    at = q.get("answer_text") or ""
    et = q.get("explanation_text") or ""
    def flat(v):
        if isinstance(v, dict):
            return "\n".join(b.get("text","") for b in v.get("blocks",[]) if b.get("text"))
        return v or ""
    print("  answer:", flat(at)[:2000])
    print("  explanation:", flat(et)[:3000])
