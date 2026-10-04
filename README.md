# Sabarish . P portfolio (Flask)

## Run locally (VS Code terminal)
    python -m venv .venv
    .venv\Scripts\activate        (Windows)   |   source .venv/bin/activate  (Mac/Linux)
    pip install -r requirements.txt
    python app.py                 -> http://127.0.0.1:5000

## Edit content
Change text and social links in config.py.

## Deploy
Push to GitHub, then import the repo at vercel.com/new (vercel.json is included).
Contact messages appear in Vercel > your project > Logs (search CONTACT_MESSAGE).
