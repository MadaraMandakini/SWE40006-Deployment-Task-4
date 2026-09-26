import os
from datetime import datetime, timezone

from flask import Flask, render_template_string

app = Flask(__name__)

PAGE = """
<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>Deployment Dashboard</title>
  <style>
    body {
      font-family: Arial, sans-serif;
      background: #eef2f7;
      color: #1b2735;
      margin: 0;
      padding: 50px 20px;
    }
    main {
      max-width: 650px;
      margin: auto;
      background: white;
      padding: 35px;
      border-radius: 14px;
      box-shadow: 0 8px 30px #1b27351a;
    }
    h1 { color: #174a8b; }
    .status { color: #167347; font-weight: bold; }
    dt { font-weight: bold; margin-top: 18px; }
    dd { margin: 5px 0 0; }
  </style>
</head>
<body>
  <main>
    <h1>Deployment Dashboard</h1>
    <p class="status">● Application running</p>
    <dl>
      <dt>Deployment environment</dt>
      <dd>{{ environment }}</dd>
      <dt>Server time (UTC)</dt>
      <dd>{{ current_time }}</dd>
      <dt>Container service</dt>
      <dd>Python Flask served by Gunicorn</dd>
    </dl>
  </main>
</body>
</html>
"""


@app.get("/")
def home():
    return render_template_string(
        PAGE,
        environment=os.getenv("APP_ENV", "local"),
        current_time=datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M:%S UTC"),
    )


@app.get("/health")
def health():
    return {"status": "ok", "service": "deployment-dashboard"}