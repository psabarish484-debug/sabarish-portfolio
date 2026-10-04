import json, os, re
from datetime import datetime, timezone
from flask import Flask, render_template, request, jsonify
from config import PROFILE, SOCIALS

app = Flask(__name__)
MSG_FILE = os.path.join(os.path.dirname(__file__), "messages.jsonl")

@app.route("/")
def home():
    return render_template("index.html", p=PROFILE, socials=SOCIALS)

@app.post("/contact")
def contact():
    d = request.get_json(silent=True) or request.form
    name, email, msg = (d.get(k, "").strip() for k in ("name", "email", "message"))
    if not name or not msg or not re.match(r"^[^@\s]+@[^@\s]+\.[^@\s]+$", email):
        return jsonify(ok=False, error="Enter your name, a valid email and a message."), 400
    entry = {"time": datetime.now(timezone.utc).isoformat(), "name": name[:100],
             "email": email[:150], "message": msg[:2000]}
    line = json.dumps(entry) + "\n"
    print("CONTACT_MESSAGE", line.strip())  # visible in Vercel > Logs
    for path in (MSG_FILE, "/tmp/messages.jsonl"):
        try:
            with open(path, "a", encoding="utf-8") as f:
                f.write(line)
            break
        except OSError:  # Vercel's filesystem is read-only
            continue
    return jsonify(ok=True)

if __name__ == "__main__":
    app.run(debug=True)
