import sys
import requests
from headers import evaluate_headers

def main(url):
    try:
        response = requests.get(url, timeout=5)
        evaluate_headers(response.headers)
    except Exception as e:
        print(f"❌ Error: {e}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python checker.py <url>")
    else:
        main(sys.argv[1])
