import tkinter as tk
from tkinter import ttk, messagebox, filedialog
import socket
import urllib.request
import subprocess
import platform
import threading


# ==========================================
# MAIN WINDOW
# ==========================================

root = tk.Tk()
root.title("IP Address & Network Tool")
root.geometry("800x600")
root.minsize(700, 500)


# ==========================================
# VARIABLES
# ==========================================

hostname_var = tk.StringVar(value="Loading...")
local_ip_var = tk.StringVar(value="Loading...")
public_ip_var = tk.StringVar(value="Loading...")
ipv4_var = tk.StringVar(value="Loading...")
ipv6_var = tk.StringVar(value="Loading...")
status_var = tk.StringVar(value="Ready")


# ==========================================
# GET HOSTNAME
# ==========================================

def get_hostname():
    try:
        return socket.gethostname()
    except Exception:
        return "Unavailable"


# ==========================================
# GET LOCAL IP
# ==========================================

def get_local_ip():
    try:
        # Create a UDP socket and determine
        # which local interface would be used.
        sock = socket.socket(
            socket.AF_INET,
            socket.SOCK_DGRAM
        )

        sock.connect(("8.8.8.8", 80))

        ip = sock.getsockname()[0]

        sock.close()

        return ip

    except Exception:
        return "Unavailable"


# ==========================================
# GET IPv4 ADDRESSES
# ==========================================

def get_ipv4_addresses():
    try:
        hostname = socket.gethostname()

        addresses = socket.getaddrinfo(
            hostname,
            None,
            socket.AF_INET
        )

        ips = set()

        for address in addresses:
            ips.add(address[4][0])

        if ips:
            return ", ".join(sorted(ips))

        return "Unavailable"

    except Exception:
        return "Unavailable"


# ==========================================
# GET IPv6 ADDRESSES
# ==========================================

def get_ipv6_addresses():
    try:
        hostname = socket.gethostname()

        addresses = socket.getaddrinfo(
            hostname,
            None,
            socket.AF_INET6
        )

        ips = set()

        for address in addresses:
            ips.add(address[4][0])

        if ips:
            return ", ".join(sorted(ips))

        return "No IPv6 address found"

    except Exception:
        return "Unavailable"


# ==========================================
# GET PUBLIC IP
# ==========================================

def get_public_ip():
    try:
        with urllib.request.urlopen(
            "https://api.ipify.org",
            timeout=5
        ) as response:

            return response.read().decode(
                "utf-8"
            )

    except Exception:
        return "Unavailable"


# ==========================================
# REFRESH INFORMATION
# ==========================================

def refresh_information():

    status_var.set(
        "Collecting network information..."
    )

    refresh_button.config(
        state="disabled"
    )

    def worker():

        hostname = get_hostname()
        local_ip = get_local_ip()
        public_ip = get_public_ip()
        ipv4 = get_ipv4_addresses()
        ipv6 = get_ipv6_addresses()

        root.after(
            0,
            lambda: update_gui(
                hostname,
                local_ip,
                public_ip,
                ipv4,
                ipv6
            )
        )

    threading.Thread(
        target=worker,
        daemon=True
    ).start()


def update_gui(
    hostname,
    local_ip,
    public_ip,
    ipv4,
    ipv6
):

    hostname_var.set(hostname)
    local_ip_var.set(local_ip)
    public_ip_var.set(public_ip)
    ipv4_var.set(ipv4)
    ipv6_var.set(ipv6)

    status_var.set(
        "Network information updated."
    )

    refresh_button.config(
        state="normal"
    )


# ==========================================
# PING HOST
# ==========================================

def ping_host():

    host = ping_entry.get().strip()

    if not host:
        messagebox.showwarning(
            "Missing Host",
            "Enter a hostname or IP address."
        )
        return

    ping_button.config(
        state="disabled"
    )

    status_var.set(
        f"Pinging {host}..."
    )

    def worker():

        system = platform.system().lower()

        if system == "windows":
            command = [
                "ping",
                "-n",
                "4",
                host
            ]
        else:
            command = [
                "ping",
                "-c",
                "4",
                host
            ]

        try:
            result = subprocess.run(
                command,
                capture_output=True,
                text=True,
                timeout=15
            )

            output = result.stdout

            if result.stderr:
                output += "\n" + result.stderr

        except subprocess.TimeoutExpired:
            output = "Ping timed out."

        except Exception as error:
            output = str(error)

        root.after(
            0,
            lambda: show_ping_result(
                host,
                output
            )
        )

    threading.Thread(
        target=worker,
        daemon=True
    ).start()


def show_ping_result(host, output):

    ping_button.config(
        state="normal"
    )

    status_var.set(
        f"Ping test completed for {host}."
    )

    window = tk.Toplevel(root)

    window.title(
        f"Ping Result - {host}"
    )

    window.geometry(
        "650x450"
    )

    text = tk.Text(
        window,
        wrap="word",
        font=("Consolas", 10)
    )

    text.pack(
        fill="both",
        expand=True,
        padx=10,
        pady=10
    )

    text.insert(
        "1.0",
        output
    )

    text.config(
        state="disabled"
    )


# ==========================================
# DNS LOOKUP
# ==========================================

def dns_lookup():

    host = dns_entry.get().strip()

    if not host:
        messagebox.showwarning(
            "Missing Host",
            "Enter a domain name."
        )
        return

    try:

        addresses = socket.getaddrinfo(
            host,
            None
        )

        ips = sorted(
            set(
                address[4][0]
                for address in addresses
            )
        )

        result = "\n".join(ips)

        show_dns_result(
            host,
            result
        )

    except socket.gaierror:
        show_dns_result(
            host,
            "DNS lookup failed."
        )

    except Exception as error:
        show_dns_result(
            host,
            str(error)
        )


def show_dns_result(host, result):

    window = tk.Toplevel(root)

    window.title(
        f"DNS Lookup - {host}"
    )

    window.geometry(
        "500x300"
    )

    ttk.Label(
        window,
        text=f"DNS results for {host}",
        font=("Arial", 14, "bold")
    ).pack(pady=15)

    text = tk.Text(
        window,
        height=10,
        width=50
    )

    text.pack(
        padx=10,
        pady=10
    )

    text.insert(
        "1.0",
        result
    )

    text.config(
        state="disabled"
    )


# ==========================================
# COPY INFORMATION
# ==========================================

def copy_information():

    information = f"""
IP ADDRESS REPORT

Hostname:
{hostname_var.get()}

Local IP:
{local_ip_var.get()}

Public IP:
{public_ip_var.get()}

IPv4 Addresses:
{ipv4_var.get()}

IPv6 Addresses:
{ipv6_var.get()}
"""

    root.clipboard_clear()
    root.clipboard_append(information)
    root.update()

    messagebox.showinfo(
        "Copied",
        "Network information copied to clipboard."
    )


# ==========================================
# SAVE REPORT
# ==========================================

def save_report():

    filename = filedialog.asksaveasfilename(
        title="Save Network Report",
        defaultextension=".txt",
        filetypes=[
            ("Text Files", "*.txt"),
            ("All Files", "*.*")
        ]
    )

    if not filename:
        return

    information = f"""
========================================
       IP ADDRESS & NETWORK REPORT
========================================

Hostname:
{hostname_var.get()}

Local IP Address:
{local_ip_var.get()}

Public IP Address:
{public_ip_var.get()}

IPv4 Addresses:
{ipv4_var.get()}

IPv6 Addresses:
{ipv6_var.get()}

========================================
"""

    try:

        with open(
            filename,
            "w",
            encoding="utf-8"
        ) as file:

            file.write(information)

        messagebox.showinfo(
            "Report Saved",
            "Network report saved successfully."
        )

    except Exception as error:

        messagebox.showerror(
            "Error",
            f"Could not save report:\n{error}"
        )


# ==========================================
# STYLE
# ==========================================

style = ttk.Style()

try:
    style.theme_use("clam")
except tk.TclError:
    pass

style.configure(
    "Title.TLabel",
    font=("Arial", 24, "bold")
)

style.configure(
    "Value.TLabel",
    font=("Arial", 12, "bold")
)


# ==========================================
# HEADER
# ==========================================

header = ttk.Frame(
    root,
    padding=15
)

header.pack(
    fill="x"
)

ttk.Label(
    header,
    text="🌐 IP Address & Network Tool",
    style="Title.TLabel"
).pack()

ttk.Label(
    header,
    text="IT Support Network Diagnostic Tool"
).pack(
    pady=5
)


# ==========================================
# INFORMATION PANEL
# ==========================================

info_frame = ttk.LabelFrame(
    root,
    text="Network Information",
    padding=15
)

info_frame.pack(
    fill="x",
    padx=15,
    pady=10
)


def create_info_row(
    parent,
    row,
    title,
    variable
):

    ttk.Label(
        parent,
        text=title + ":",
        font=("Arial", 10, "bold")
    ).grid(
        row=row,
        column=0,
        sticky="w",
        padx=10,
        pady=7
    )

    ttk.Label(
        parent,
        textvariable=variable,
        style="Value.TLabel"
    ).grid(
        row=row,
        column=1,
        sticky="w",
        padx=10,
        pady=7
    )


create_info_row(
    info_frame,
    0,
    "Computer Name",
    hostname_var
)

create_info_row(
    info_frame,
    1,
    "Local IP",
    local_ip_var
)

create_info_row(
    info_frame,
    2,
    "Public IP",
    public_ip_var
)

create_info_row(
    info_frame,
    3,
    "IPv4",
    ipv4_var
)

create_info_row(
    info_frame,
    4,
    "IPv6",
    ipv6_var
)


# ==========================================
# BUTTONS
# ==========================================

button_frame = ttk.Frame(
    root,
    padding=5
)

button_frame.pack()

refresh_button = ttk.Button(
    button_frame,
    text="Refresh Information",
    command=refresh_information
)

refresh_button.pack(
    side="left",
    padx=5
)

ttk.Button(
    button_frame,
    text="Copy Information",
    command=copy_information
).pack(
    side="left",
    padx=5
)

ttk.Button(
    button_frame,
    text="Save Report",
    command=save_report
).pack(
    side="left",
    padx=5
)


# ==========================================
# PING SECTION
# ==========================================

ping_frame = ttk.LabelFrame(
    root,
    text="Ping Test",
    padding=15
)

ping_frame.pack(
    fill="x",
    padx=15,
    pady=10
)

ttk.Label(
    ping_frame,
    text="Host/IP:"
).pack(
    side="left",
    padx=5
)

ping_entry = ttk.Entry(
    ping_frame,
    width=30
)

ping_entry.insert(
    0,
    "8.8.8.8"
)

ping_entry.pack(
    side="left",
    padx=5
)

ping_button = ttk.Button(
    ping_frame,
    text="Ping",
    command=ping_host
)

ping_button.pack(
    side="left",
    padx=5
)


# ==========================================
# DNS SECTION
# ==========================================

dns_frame = ttk.LabelFrame(
    root,
    text="DNS Lookup",
    padding=15
)

dns_frame.pack(
    fill="x",
    padx=15,
    pady=10
)

ttk.Label(
    dns_frame,
    text="Domain:"
).pack(
    side="left",
    padx=5
)

dns_entry = ttk.Entry(
    dns_frame,
    width=30
)

dns_entry.insert(
    0,
    "google.com"
)

dns_entry.pack(
    side="left",
    padx=5
)

ttk.Button(
    dns_frame,
    text="Lookup",
    command=dns_lookup
).pack(
    side="left",
    padx=5
)


# ==========================================
# STATUS
# ==========================================

status_bar = ttk.Label(
    root,
    textvariable=status_var,
    relief="sunken",
    anchor="w"
)

status_bar.pack(
    fill="x",
    side="bottom"
)


# ==========================================
# INITIAL LOAD
# ==========================================

refresh_information()


# ==========================================
# START
# ==========================================

root.mainloop()
