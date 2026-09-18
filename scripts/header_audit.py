import argparse

import requests

SEC_HEADERS = [
    "Content-Security-Policy",
    "Strict-Transport-Security",
    "X-Content-Type-Options",
    "X-Frame-Options",
    "Referrer-Policy",
    "Permissions-Policy",
]

def main():
    ap = argparse.ArgumentParser(description="Quick security header check (authorized targets only).")
    ap.add_argument("--url", required=True, help="e.g. http://localhost:3000")
    args = ap.parse_args()

    r = requests.get(args.url, timeout=15, allow_redirects=True)
    print(f"URL: {r.url}")
    print(f"Status: {r.status_code}\n")

    for h in SEC_HEADERS:
        print(f"{h}: {r.headers.get(h, 'MISSING')}")

if __name__ == "__main__":
    main()
