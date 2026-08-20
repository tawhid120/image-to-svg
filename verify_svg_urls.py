import requests

test_urls = [
    "https://ik.imagekit.io/9fi8p9fvr/math_2nd_ch7/svg_q796.svg",
    "https://ik.imagekit.io/9fi8p9fvr/math_2nd_ch7/svg_q806.svg",
    "https://ik.imagekit.io/9fi8p9fvr/math_2nd_ch7/svg_sin_inv.svg"
]
for u in test_urls:
    r = requests.get(u)
    print(f"{u} -> HTTP {r.status_code}, type: {r.headers.get('content-type')}, bytes: {len(r.content)}")
