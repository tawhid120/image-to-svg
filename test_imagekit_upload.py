import requests

IMAGEKIT_PRIVATE_KEY  = "private_cJXcFIjPOZe+7yKDQCR74pSyNIE="
upload_url = "https://upload.imagekit.io/api/v2/files/upload"
auth = (IMAGEKIT_PRIVATE_KEY, "")

svg_content = '<svg xmlns="http://www.w3.org/2000/svg" width="100" height="100"><circle cx="50" cy="50" r="40" stroke="green" stroke-width="4" fill="yellow" /></svg>'
files = {"file": ("test_circle.svg", svg_content.encode("utf-8"), "image/svg+xml")}
data = {
    "fileName": "test_circle.svg",
    "folder": "/math_2nd_ch7/",
    "isPrivateFile": "false",
    "useUniqueFileName": "false"
}
res = requests.post(upload_url, auth=auth, files=files, data=data, timeout=30)
print("Status:", res.status_code)
print("Response:", res.json())
