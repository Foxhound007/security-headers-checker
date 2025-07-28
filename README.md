# 🔐 Security Headers Checker

A simple Python tool that checks the presence of important HTTP security headers for any given domain.

## 🌐 What It Checks

- `Content-Security-Policy`
- `X-Frame-Options`
- `Strict-Transport-Security`
- `X-Content-Type-Options`

## 💡 Why Use It?

- No setup or logs needed — works on any live website
- Great as a quick audit or security assessment tool

## 🚀 Usage

```bash
python checker.py https://example.com
```

## 🛠 Requirements

```bash
pip install -r requirements.txt
```

## 📂 Files

- `checker.py`: CLI entrypoint
- `headers.py`: Header evaluation logic
- `README.md`: Project description
- `requirements.txt`: Dependencies

---

## ✨ Example Output

```
Checking headers for https://example.com

[✖] Content-Security-Policy is missing
[✔] X-Frame-Options is present
[✔] Strict-Transport-Security is present
[✖] X-Content-Type-Options is missing
```
