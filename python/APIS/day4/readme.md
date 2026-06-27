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

# 🚀 Next Upgrades (Highly Recommended)

If you want to push this into a serious project:

---

## 1. Middleware Layer (VERY important)

Add hooks like:

* auth check
* rate limiting
* logging

```python
def middleware(func):
    def wrapper(self, *args, **kwargs):
        print("Request:", self.command, self.path)
        return func(self, *args, **kwargs)
    return wrapper
```

---

## 2. Authentication (Tokens)

* `/login`
* generate `secrets.token_hex`
* store in DB

---

## 3. SQLite Integration

Add:

* users table
* tasks table
* logs table

---

## 4. Clean Routing Upgrade

Replace dict with decorator system:

```python
@route("POST", "/tasks")
def create_task(self, body):
    ...
```

---


