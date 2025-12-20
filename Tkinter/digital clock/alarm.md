
## Step 1: Make the window + time display

Goal: show live time that updates every second.

```python
import tkinter as tk
from time import strftime

root = tk.Tk()
root.title("Alarm Clock")
root.geometry("520x320")

time_label = tk.Label(root, font=("Consolas", 60, "bold"))
time_label.pack(pady=20)

def tick():
    time_label.config(text=strftime("%H:%M:%S"))
    root.after(1000, tick)

tick()
root.mainloop()
```

---

## Step 2: Add inputs for the alarm time

We’ll let the user set:

* Hour
* Minute
* AM/PM (optional, but we’ll keep it simple with **24-hour** first)

Add under the clock:

```python
alarm_frame = tk.Frame(root)
alarm_frame.pack(pady=10)

hour_entry = tk.Entry(alarm_frame, width=4, font=("Arial", 18))
hour_entry.grid(row=0, column=0, padx=5)
hour_entry.insert(0, "07")

minute_entry = tk.Entry(alarm_frame, width=4, font=("Arial", 18))
minute_entry.grid(row=0, column=1, padx=5)
minute_entry.insert(0, "30")

tk.Label(alarm_frame, text="(HH  MM) 24-hour", font=("Arial", 12)).grid(row=1, column=0, columnspan=2, pady=6)
```

---

## Step 3: Add a “Set Alarm” button and status label

We need a place to show messages like:

* “Alarm set for 07:30”
* “Invalid time”
* “Alarm ringing!”

```python
status_label = tk.Label(root, text="No alarm set", font=("Arial", 14))
status_label.pack(pady=10)

set_btn = tk.Button(root, text="Set Alarm", font=("Arial", 14))
set_btn.pack(pady=6)
```

---

## Step 4: Store alarm time + validate input

We’ll store the alarm as a string like `"07:30"` (HH:MM).

Rules:

* hour must be 0–23
* minute must be 0–59

---

## Step 5: Check alarm every second + ring

Inside `tick()`:

1. Update the clock
2. If alarm is set, compare current `"HH:MM"`
3. If it matches and hasn’t already rung, ring it

“Ringing” options:

* simplest: `root.bell()` (system beep)
* show a pop-up message box
* keep beeping until Stop is pressed

---

## Step 6: Add Stop + Clear alarm buttons

* **Stop**: stops ringing
* **Clear**: removes the alarm

---

# ✅ Complete Alarm Clock App (working)

Copy/paste this whole script into `alarm_clock.py` and run it.

```python
import tkinter as tk
from tkinter import messagebox
from time import strftime


class AlarmClock(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Alarm Clock")
        self.geometry("520x340")
        self.resizable(False, False)

        # Alarm state
        self.alarm_time = None          # string like "07:30"
        self.alarm_ringing = False
        self.ring_job = None            # after() id for ringing loop
        self.rang_today_flag = False    # prevents ringing repeatedly within the same minute

        # --- UI ---
        self.time_label = tk.Label(self, font=("Consolas", 60, "bold"))
        self.time_label.pack(pady=18)

        alarm_box = tk.LabelFrame(self, text="Set Alarm (24-hour)", padx=12, pady=12)
        alarm_box.pack(padx=12, pady=8, fill="x")

        self.hour_entry = tk.Entry(alarm_box, width=4, font=("Arial", 18), justify="center")
        self.hour_entry.grid(row=0, column=0, padx=6)
        self.hour_entry.insert(0, "07")

        tk.Label(alarm_box, text=":", font=("Arial", 18)).grid(row=0, column=1)

        self.minute_entry = tk.Entry(alarm_box, width=4, font=("Arial", 18), justify="center")
        self.minute_entry.grid(row=0, column=2, padx=6)
        self.minute_entry.insert(0, "30")

        self.set_btn = tk.Button(alarm_box, text="Set Alarm", font=("Arial", 14), command=self.set_alarm)
        self.set_btn.grid(row=0, column=3, padx=10)

        self.clear_btn = tk.Button(alarm_box, text="Clear", font=("Arial", 14), command=self.clear_alarm)
        self.clear_btn.grid(row=0, column=4, padx=6)

        alarm_box.columnconfigure(5, weight=1)

        self.status_label = tk.Label(self, text="No alarm set", font=("Arial", 14))
        self.status_label.pack(pady=10)

        self.stop_btn = tk.Button(self, text="Stop Alarm", font=("Arial", 14), state="disabled", command=self.stop_alarm)
        self.stop_btn.pack(pady=6)

        # start clock updates
        self.tick()

    # -------- Alarm Logic --------
    def set_alarm(self):
        try:
            hour = int(self.hour_entry.get().strip())
            minute = int(self.minute_entry.get().strip())
            if not (0 <= hour <= 23 and 0 <= minute <= 59):
                raise ValueError
        except ValueError:
            messagebox.showerror("Invalid Time", "Enter a valid time:\nHour 0–23, Minute 0–59")
            return

        self.alarm_time = f"{hour:02d}:{minute:02d}"
        self.status_label.config(text=f"Alarm set for {self.alarm_time}")
        self.rang_today_flag = False  # allow alarm to ring when time matches again

    def clear_alarm(self):
        self.alarm_time = None
        self.rang_today_flag = False
        if self.alarm_ringing:
            self.stop_alarm()
        self.status_label.config(text="No alarm set")

    def start_ringing(self):
        if self.alarm_ringing:
            return
        self.alarm_ringing = True
        self.stop_btn.config(state="normal")
        self.status_label.config(text=f"⏰ ALARM! ({self.alarm_time})")

        # optional popup (comment out if you dislike popups)
        messagebox.showwarning("Alarm", "Wake up! Your alarm is ringing.")

        self._ring_loop()

    def _ring_loop(self):
        """Beep repeatedly until stopped."""
        if not self.alarm_ringing:
            return
        self.bell()  # system beep
        self.ring_job = self.after(700, self._ring_loop)

    def stop_alarm(self):
        self.alarm_ringing = False
        self.stop_btn.config(state="disabled")
        if self.ring_job is not None:
            self.after_cancel(self.ring_job)
            self.ring_job = None
        # Keep alarm set; user can clear it if they want
        if self.alarm_time:
            self.status_label.config(text=f"Alarm set for {self.alarm_time} (stopped)")
        else:
            self.status_label.config(text="No alarm set")

    # -------- Clock Update --------
    def tick(self):
        now_full = strftime("%H:%M:%S")
        now_hm = strftime("%H:%M")

        self.time_label.config(text=now_full)

        # Check alarm match
        if self.alarm_time and now_hm == self.alarm_time:
            # ring once per minute at most
            if not self.rang_today_flag and not self.alarm_ringing:
                self.rang_today_flag = True
                self.start_ringing()
        else:
            # reset flag once time moves away
            self.rang_today_flag = False

        self.after(200, self.tick)


if __name__ == "__main__":
    app = AlarmClock()
    app.mainloop()
```

---

