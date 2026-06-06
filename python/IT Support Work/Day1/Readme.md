# 🖥️ System Health Monitor (Python)

## What it does

A Python script that continuously monitors your system:

* CPU usage
* RAM usage
* Disk usage
* Running processes (optional)
* Alerts when thresholds are exceeded
* Logs everything to a file

---


# ⚙️ 1. Install Requirements

```bash
pip install psutil
```

 For alerts later

```bash
pip install plyer
```

---

# 2. Core Script (Basic Monitor)

```python
import psutil
import time
from datetime import datetime
```
```python
CPU_THRESHOLD = 80
RAM_THRESHOLD = 80
DISK_THRESHOLD = 90
```
```python

LOG_FILE = "system_health_log.txt"
```

```python

def log(message):
    with open(LOG_FILE, "a") as f:
        f.write(f"{datetime.now()} - {message}\n")
    print(message)

```
```python
def get_system_info():
    cpu = psutil.cpu_percent(interval=1)
    ram = psutil.virtual_memory().percent
    disk = psutil.disk_usage('/').percent

    return cpu, ram, disk
```
```python

def check_alerts(cpu, ram, disk):
    if cpu > CPU_THRESHOLD:
        log(f"⚠️ High CPU usage: {cpu}%")

    if ram > RAM_THRESHOLD:
        log(f"⚠️ High RAM usage: {ram}%")

    if disk > DISK_THRESHOLD:
        log(f"⚠️ High Disk usage: {disk}%")

```
```python
def monitor():
    log("System Monitor Started...")

    while True:
        cpu, ram, disk = get_system_info()

        log(f"CPU: {cpu}% | RAM: {ram}% | DISK: {disk}%")

        check_alerts(cpu, ram, disk)

        time.sleep(5)


if __name__ == "__main__":
    monitor()
```

---

# What You Just Built

This already behaves like a **mini IT monitoring agent**:

✔ Collects system metrics
✔ Runs continuously
✔ Logs system performance
✔ Detects resource spikes

---


# 🔔 3A. Desktop Notifications

```python
from plyer import notification

def notify(title, message):
    notification.notify(
        title=title,
        message=message,
        timeout=5
    )
```

Use it inside alerts:

```python
notify("CPU Alert", f"CPU usage is {cpu}%")
```

---

## B. Better Logging (CSV format)

```python
import csv

def log_csv(cpu, ram, disk):
    with open("system_log.csv", "a", newline="") as f:
        writer = csv.writer(f)
        writer.writerow([datetime.now(), cpu, ram, disk])
```

---

##  C. Process Monitor (IT Admin Feature)

```python
def top_processes():
    processes = []

    for p in psutil.process_iter(['pid', 'name', 'cpu_percent']):
        processes.append(p.info)

    processes = sorted(processes, key=lambda x: x['cpu_percent'], reverse=True)

    return processes[:5]
```

---

## 🌐 D. Web Dashboard (Big Upgrade)

Turn it into a web IT dashboard using Flask:

```bash
pip install flask
```

### Simple Flask server:

```python
from flask import Flask, jsonify
import psutil

app = Flask(__name__)

@app.route('/metrics')
def metrics():
    return jsonify({
        "cpu": psutil.cpu_percent(),
        "ram": psutil.virtual_memory().percent,
        "disk": psutil.disk_usage('/').percent
    })

if __name__ == "__main__":
    app.run(debug=True)
```

Now you have:
👉 `http://localhost:5000/metrics`

---

