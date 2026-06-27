# 🌐 Custom HTTP API Server (Pure Python)

We’ll build using only:

* `http.server`
* `socketserver`
* `urllib.parse`
* `json`
* `threading`

No Flask, no FastAPI, no external libs.

---

# 🧱 Architecture Overview

You’ll create:

* A threaded HTTP server
* A request router (manual)
* JSON request/response handling
* Simple middleware hooks (auth, rate limit, logging)

---

# 📁 Core Structure

```
project/
  server.py
  router.py
  handlers.py
  utils.py
  db.py
```

---

# 🚀 Step 1: Basic Threaded Server

```python
from http.server import BaseHTTPRequestHandler, HTTPServer
import socketserver
import json
from urllib.parse import urlparse, parse_qs
```

### Threaded server (important for real API behavior)

```python
class ThreadingHTTPServer(socketserver.ThreadingMixIn, HTTPServer):
    pass
```

---

# 🔁 Step 2: Router System (No Framework Replacement)

We manually map routes.

```python
ROUTES = {
    ("GET", "/tasks"): "get_tasks",
    ("POST", "/tasks"): "create_task",
    ("POST", "/users"): "create_user",
}
```

---

# 🧠 Step 3: Request Handler

This is the heart of your API.

```python
class APIHandler(BaseHTTPRequestHandler):

    def _send_json(self, code, data):
        self.send_response(code)
        self.send_header("Content-Type", "application/json")
        self.end_headers()
        self.wfile.write(json.dumps(data).encode())
```

---

# 📦 Step 4: Read Request Body

```python
    def _get_body(self):
        length = int(self.headers.get("Content-Length", 0))
        if length == 0:
            return {}
        body = self.rfile.read(length)
        return json.loads(body.decode())
```

---

# 🧭 Step 5: Route Resolver

```python
    def _resolve_route(self):
        key = (self.command, self.path.split("?")[0])
        return ROUTES.get(key, None)
```

---

# ⚙️ Step 6: GET / POST Handlers

### GET

```python
    def do_GET(self):
        handler_name = self._resolve_route()

        if not handler_name:
            return self._send_json(404, {"error": "Not found"})

        handler = getattr(self, handler_name, None)

        if not handler:
            return self._send_json(500, {"error": "Handler missing"})

        return handler()
```

---

### POST

```python
    def do_POST(self):
        handler_name = self._resolve_route()

        if not handler_name:
            return self._send_json(404, {"error": "Not found"})

        handler = getattr(self, handler_name, None)

        if not handler:
            return self._send_json(500, {"error": "Handler missing"})

        body = self._get_body()
        return handler(body)
```

---

# 🧪 Step 7: Example Handlers

### Users

```python
    def create_user(self, body):
        username = body.get("username")

        if not username:
            return self._send_json(400, {"error": "username required"})

        return self._send_json(201, {
            "message": "User created",
            "user": {"username": username}
        })
```

---

### Tasks

```python
    def create_task(self, body):
        title = body.get("title")

        if not title:
            return self._send_json(400, {"error": "title required"})

        return self._send_json(201, {
            "message": "Task created",
            "task": {"title": title}
        })
```

---

### GET tasks

```python
    def get_tasks(self):
        return self._send_json(200, {
            "tasks": []
        })
```

---

# 🏁 Step 8: Run Server

```python
def run():
    server = ThreadingHTTPServer(("0.0.0.0", 8080), APIHandler)
    print("Server running on http://localhost:8080")
    server.serve_forever()


if __name__ == "__main__":
    run()
```

---

# 🔥 What You Just Built

You now have a real mini backend system with:

✔ HTTP server
✔ Routing system
✔ JSON API
✔ Request parsing
✔ Modular handlers
✔ Threading support

This is basically a **mini Flask built from scratch**.

---

# 🌐 1. Serve a Basic HTML Page

Add a new route like:

```
GET /
```

---

## 🧱 Step 1: Create an HTML response

Inside your handler:

```python id="html1"
def home(self):
    html = """
    <!DOCTYPE html>
    <html>
    <head>
        <title>My Custom Server</title>
    </head>
    <body>
        <h1>🚀 Hello from Python Server</h1>
        <p>This page is served without any framework.</p>
    </body>
    </html>
    """

    self.send_response(200)
    self.send_header("Content-Type", "text/html")
    self.end_headers()
    self.wfile.write(html.encode())
```

---

## 🧭 Step 2: Add route mapping

In your `ROUTES`:

```python id="route2"
ROUTES = {
    ("GET", "/"): "home",
    ("GET", "/tasks"): "get_tasks",
}
```

---

# ▶️ 3. Run the server

```bash id="run1"
python server.py
```

Then open:

```
http://localhost:8080/
```

You’ll see your HTML page.

---

# 📄 4. Serving an actual `.html` file (better way)

Instead of writing HTML in Python, load a file.

---

## Create file:

```
index.html
```

```html id="file1"
<!DOCTYPE html>
<html>
<head>
    <title>My Site</title>
</head>
<body>
    <h1>Hello from file 🚀</h1>
</body>
</html>
```

---

## Load it in Python:

```python id="file2"
def home(self):
    with open("index.html", "r", encoding="utf-8") as f:
        html = f.read()

    self.send_response(200)
    self.send_header("Content-Type", "text/html")
    self.end_headers()
    self.wfile.write(html.encode())
```

---

# 📦 5. Serve CSS / JS too (important upgrade)

You can extend routing:

```python id="static1"
("GET", "/style.css"): "style",
("GET", "/app.js"): "script",
```

Then:

```python id="static2"
def style(self):
    with open("style.css", "rb") as f:
        self.send_response(200)
        self.send_header("Content-Type", "text/css")
        self.end_headers()
        self.wfile.write(f.read())
```

---

# ⚡ 6. Better approach: Static file handler (recommended)

Instead of writing many routes:

```python id="static3"
def serve_file(self, path, content_type):
    try:
        with open(path, "rb") as f:
            self.send_response(200)
            self.send_header("Content-Type", content_type)
            self.end_headers()
            self.wfile.write(f.read())
    except FileNotFoundError:
        self.send_error(404, "File not found")
```

Then:

```python id="static4"
def do_GET(self):
    if self.path == "/":
        return self.serve_file("index.html", "text/html")

    if self.path.endswith(".css"):
        return self.serve_file(self.path[1:], "text/css")

    if self.path.endswith(".js"):
        return self.serve_file(self.path[1:], "application/javascript")
```

---


