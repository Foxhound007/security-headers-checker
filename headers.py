def evaluate_headers(headers):
    required = [
        "Content-Security-Policy",
        "X-Frame-Options",
        "Strict-Transport-Security",
        "X-Content-Type-Options"
    ]

    print()
    for header in required:
        if header in headers:
            print(f"[✔] {header} is present")
        else:
            print(f"[✖] {header} is missing")
