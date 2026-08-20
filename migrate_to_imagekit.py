# -*- coding: utf-8 -*-
"""
migrate_to_imagekit.py
======================
Migrates all question bank diagram images from Firebase Storage to ImageKit.io
using ImageKit REST API v2.

Dependencies:
    pip install requests
"""

import json
import os
import shutil
import logging
import re
import urllib.parse
from pathlib import Path
import requests

# ──────────────────────────────────────────────────────────────────────────────
# CONFIG
# ──────────────────────────────────────────────────────────────────────────────
IMAGEKIT_PRIVATE_KEY  = "private_cJXcFIjPOZe+7yKDQCR74pSyNIE="
IMAGEKIT_PUBLIC_KEY   = "public_a/+ZERwECWASrA1RqvhK+UlZxws="
IMAGEKIT_URL_ENDPOINT = "https://ik.imagekit.io/9fi8p9fvr"

RAW_JSON_PATH     = "question_bank_HSC_Admission_HSC_-_উচ্চতর_গণিত_২য়_পত্র_অধ্যায়-০৭ঃ_বিপরীত_ত্রিকোণমিতিক_ফাংশন_ও_ত্রিকোণমিতিক_সমীকরণ.json"
IMAGEKIT_FOLDER   = "/math_2nd_ch7/"
LOCAL_IMG_DIR     = "downloaded_diagrams"

DOWNLOAD_TIMEOUT  = 30
UPLOAD_TIMEOUT    = 60
# ──────────────────────────────────────────────────────────────────────────────

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s  %(levelname)-8s  %(message)s",
    datefmt="%H:%M:%S",
)
log = logging.getLogger(__name__)


def _verify_credentials() -> None:
    """Check ImageKit auth before running migration."""
    test_url = "https://api.imagekit.io/v1/files?limit=1"
    response = requests.get(
        test_url,
        auth=(IMAGEKIT_PRIVATE_KEY, ""),
        timeout=10,
    )
    if response.status_code == 401:
        raise RuntimeError("ImageKit auth failed (401). Check IMAGEKIT_PRIVATE_KEY.")
    if not response.ok:
        raise RuntimeError(f"ImageKit check failed — HTTP {response.status_code}: {response.text}")


def upload_via_rest_api(image_bytes: bytes, file_name: str, folder: str, mime_type: str = "image/png") -> str:
    """Upload binary directly through ImageKit REST API."""
    upload_url = "https://upload.imagekit.io/api/v2/files/upload"
    auth = (IMAGEKIT_PRIVATE_KEY, "")

    files = {
        "file": (file_name, image_bytes, mime_type),
    }
    data = {
        "fileName": file_name,
        "folder": folder,
        "isPrivateFile": "false",
        "useUniqueFileName": "false",
    }

    response = requests.post(
        upload_url,
        auth=auth,
        files=files,
        data=data,
        timeout=UPLOAD_TIMEOUT,
    )

    if not response.ok:
        raise RuntimeError(f"ImageKit upload failed HTTP {response.status_code}: {response.text}")

    result = response.json()
    url = result.get("url")
    if not url:
        raise ValueError(f"No URL in ImageKit response: {result}")
    return url


def sanitize_filename(name: str, fallback_idx: int) -> str:
    """Create a clean, safe filename for ImageKit."""
    clean = re.sub(r'[^a-zA-Z0-9_\-\.]', '_', name)
    clean = re.sub(r'_+', '_', clean).strip('_')
    if not clean or len(clean) < 3:
        clean = f"hsc_math2_qimg_{fallback_idx}"
    if not any(clean.lower().endswith(ext) for ext in [".png", ".jpg", ".jpeg", ".webp", ".svg"]):
        clean += ".png"
    return f"hsc_math2_{clean}"


def download_or_get_local(url: str, local_dir: str, fallback_name: str) -> bytes:
    """Download image from Firebase or read from local cache if exists."""
    os.makedirs(local_dir, exist_ok=True)
    local_path = os.path.join(local_dir, fallback_name)
    if os.path.exists(local_path) and os.path.getsize(local_path) > 100:
        with open(local_path, "rb") as f:
            return f.read()

    res = requests.get(url, timeout=DOWNLOAD_TIMEOUT)
    res.raise_for_status()
    data = res.content
    with open(local_path, "wb") as f:
        f.write(data)
    return data


def migrate_all():
    log.info("Verifying ImageKit credentials...")
    _verify_credentials()
    log.info("ImageKit credentials verified successfully!")

    HERE = os.path.dirname(os.path.abspath(__file__))
    json_path = os.path.join(HERE, RAW_JSON_PATH)

    with open(json_path, "r", encoding="utf-8") as fh:
        raw_text = fh.read()

    # Find all Firebase URLs
    pattern = r"https://firebasestorage\.googleapis\.com/v0/b/q-bank-95803\.appspot\.com/o/images%2F[^\"]+"
    firebase_urls = list(set(re.findall(pattern, raw_text)))
    log.info(f"Found {len(firebase_urls)} unique Firebase Storage URLs in question bank.")

    url_migration_map = {}
    migrated_count = 0
    error_count = 0

    for idx, fb_url in enumerate(firebase_urls, 1):
        # Extract filename from Firebase URL
        fn_match = re.search(r"images%2F([^?]+)", fb_url)
        raw_fn = urllib.parse.unquote(fn_match.group(1)) if fn_match else f"diagram_{idx}.png"
        safe_fn = sanitize_filename(raw_fn, idx)

        log.info(f"[{idx}/{len(firebase_urls)}] Processing: {safe_fn}")
        try:
            img_bytes = download_or_get_local(fb_url, os.path.join(HERE, LOCAL_IMG_DIR), safe_fn)
            mime_type = "image/svg+xml" if safe_fn.endswith(".svg") else "image/png"
            new_ik_url = upload_via_rest_api(
                image_bytes=img_bytes,
                file_name=safe_fn,
                folder=IMAGEKIT_FOLDER,
                mime_type=mime_type
            )
            url_migration_map[fb_url] = new_ik_url
            migrated_count += 1
            log.info(f"  --> Successfully uploaded to ImageKit: {new_ik_url}")
        except Exception as exc:
            log.error(f"  Failed for {fb_url}: {exc}")
            error_count += 1

    log.info(f"Uploading complete. Migrated: {migrated_count}, Errors: {error_count}")

    # Save migration map for reference
    map_file = os.path.join(HERE, "imagekit_migration_map.json")
    with open(map_file, "w", encoding="utf-8") as f:
        json.dump(url_migration_map, f, ensure_ascii=False, indent=2)
    log.info(f"Saved migration map to {map_file}")

    # Replace URLs in raw JSON
    backup_path = json_path.replace(".json", "_firebase_backup.json")
    if not os.path.exists(backup_path):
        shutil.copy2(json_path, backup_path)
        log.info(f"Created raw JSON backup at {backup_path}")

    modified_text = raw_text
    for old_url, new_url in url_migration_map.items():
        modified_text = modified_text.replace(old_url, new_url)

    with open(json_path, "w", encoding="utf-8") as fh:
        fh.write(modified_text)
    log.info(f"Successfully replaced all Firebase URLs with ImageKit URLs in {RAW_JSON_PATH}")


if __name__ == "__main__":
    migrate_all()
