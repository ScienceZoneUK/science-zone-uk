Alright — here’s a more complex Tkinter project: a CRUD desktop app with SQLite, search/filter, sorting, dialogs, keyboard shortcuts, status bar, and a clean multi-file structure (MVC-ish).

Project: Desktop Inventory Manager (Tkinter + SQLite)

Features
	•	✅ Add / Edit / Delete items (CRUD)
	•	🔎 Live search (name/category)
	•	🧮 Sort by clicking table headers
	•	💾 SQLite persistence (auto-creates DB)
	•	⌨️ Keyboard shortcuts (Ctrl+N, Ctrl+S, Del, Esc)
	•	📤 Export to CSV
	•	🧱 Multi-file, maintainable structure

⸻

📁 Folder Structure

inventory_manager/
│
├── main.py
├── app.py
├── db.py
├── models.py
├── ui_dialogs.py
└── utils.py


⸻

✅ main.py

from app import InventoryApp

if __name__ == "__main__":
    InventoryApp().run()


⸻

✅ db.py

import sqlite3
from pathlib import Path

DB_PATH = Path(__file__).with_name("inventory.sqlite3")

def get_conn():
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    return conn

def init_db():
    with get_conn() as conn:
        conn.execute("""
            CREATE TABLE IF NOT EXISTS items (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                category TEXT NOT NULL,
                quantity INTEGER NOT NULL DEFAULT 0,
                unit_price REAL NOT NULL DEFAULT 0.0,
                updated_at TEXT NOT NULL
            )
        """)
        conn.execute("CREATE INDEX IF NOT EXISTS idx_items_name ON items(name)")
        conn.execute("CREATE INDEX IF NOT EXISTS idx_items_category ON items(category)")


⸻

✅ models.py

from dataclasses import dataclass
from datetime import datetime

@dataclass(frozen=True)
class Item:
    id: int | None
    name: str
    category: str
    quantity: int
    unit_price: float
    updated_at: str

    @staticmethod
    def now_iso() -> str:
        return datetime.now().replace(microsecond=0).isoformat(sep=" ")


⸻

✅ utils.py

import csv
from tkinter import messagebox

def export_csv(filepath: str, rows: list[dict]):
    if not rows:
        messagebox.showinfo("Export", "Nothing to export.")
        return

    fieldnames = list(rows[0].keys())
    with open(filepath, "w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=fieldnames)
        w.writeheader()
        w.writerows(rows)

def safe_int(value: str, default: int = 0) -> int:
    try:
        return int(value)
    except Exception:
        return default

def safe_float(value: str, default: float = 0.0) -> float:
    try:
        return float(value)
    except Exception:
        return default


⸻

✅ ui_dialogs.py (Add/Edit dialog)

import tkinter as tk
from tkinter import ttk, messagebox
from models import Item
from utils import safe_int, safe_float

class ItemDialog(tk.Toplevel):
    def __init__(self, parent, title: str, initial: Item | None = None):
        super().__init__(parent)
        self.title(title)
        self.resizable(False, False)
        self.transient(parent)
        self.grab_set()

        self.result: Item | None = None
        self.initial = initial

        pad = {"padx": 10, "pady": 6}

        ttk.Label(self, text="Name").grid(row=0, column=0, sticky="w", **pad)
        ttk.Label(self, text="Category").grid(row=1, column=0, sticky="w", **pad)
        ttk.Label(self, text="Quantity").grid(row=2, column=0, sticky="w", **pad)
        ttk.Label(self, text="Unit Price").grid(row=3, column=0, sticky="w", **pad)

        self.var_name = tk.StringVar(value=initial.name if initial else "")
        self.var_category = tk.StringVar(value=initial.category if initial else "")
        self.var_quantity = tk.StringVar(value=str(initial.quantity) if initial else "0")
        self.var_price = tk.StringVar(value=f"{initial.unit_price:.2f}" if initial else "0.00")

        self.e_name = ttk.Entry(self, textvariable=self.var_name, width=30)
        self.e_category = ttk.Entry(self, textvariable=self.var_category, width=30)
        self.e_quantity = ttk.Entry(self, textvariable=self.var_quantity, width=30)
        self.e_price = ttk.Entry(self, textvariable=self.var_price, width=30)

        self.e_name.grid(row=0, column=1, **pad)
        self.e_category.grid(row=1, column=1, **pad)
        self.e_quantity.grid(row=2, column=1, **pad)
        self.e_price.grid(row=3, column=1, **pad)

        btns = ttk.Frame(self)
        btns.grid(row=4, column=0, columnspan=2, sticky="e", padx=10, pady=10)

        self.btn_save = ttk.Button(btns, text="Save", command=self.on_save)
        self.btn_cancel = ttk.Button(btns, text="Cancel", command=self.on_cancel)
        self.btn_save.grid(row=0, column=0, padx=(0, 8))
        self.btn_cancel.grid(row=0, column=1)

        self.bind("<Escape>", lambda e: self.on_cancel())
        self.bind("<Return>", lambda e: self.on_save())

        self.e_name.focus_set()

    def on_save(self):
        name = self.var_name.get().strip()
        category = self.var_category.get().strip()
        quantity = safe_int(self.var_quantity.get().strip(), 0)
        unit_price = safe_float(self.var_price.get().strip(), 0.0)

        if not name:
            messagebox.showwarning("Validation", "Name is required.")
            return
        if not category:
            messagebox.showwarning("Validation", "Category is required.")
            return
        if quantity < 0:
            messagebox.showwarning("Validation", "Quantity cannot be negative.")
            return
        if unit_price < 0:
            messagebox.showwarning("Validation", "Unit price cannot be negative.")
            return

        self.result = Item(
            id=self.initial.id if self.initial else None,
            name=name,
            category=category,
            quantity=quantity,
            unit_price=unit_price,
            updated_at=Item.now_iso(),
        )
        self.destroy()

    def on_cancel(self):
        self.result = None
        self.destroy()


⸻

✅ app.py (Main UI + controller logic)

import tkinter as tk
from tkinter import ttk, messagebox, filedialog
from db import init_db, get_conn
from models import Item
from ui_dialogs import ItemDialog
from utils import export_csv

class InventoryApp:
    def __init__(self):
        init_db()

        self.root = tk.Tk()
        self.root.title("Inventory Manager (Tkinter + SQLite)")
        self.root.geometry("900x520")

        self.sort_col = "updated_at"
        self.sort_desc = True

        self._build_style()
        self._build_ui()
        self.refresh()

    def run(self):
        self.root.mainloop()

    def _build_style(self):
        style = ttk.Style(self.root)
        # Use platform theme if available, otherwise fallback.
        try:
            style.theme_use("clam")
        except Exception:
            pass
        style.configure("Header.TLabel", font=("Segoe UI", 14, "bold"))

    def _build_ui(self):
        top = ttk.Frame(self.root, padding=12)
        top.pack(fill="x")

        ttk.Label(top, text="📦 Inventory Manager", style="Header.TLabel").pack(side="left")

        toolbar = ttk.Frame(self.root, padding=(12, 0, 12, 8))
        toolbar.pack(fill="x")

        self.var_search = tk.StringVar()
        ttk.Label(toolbar, text="Search:").pack(side="left")
        search_entry = ttk.Entry(toolbar, textvariable=self.var_search, width=35)
        search_entry.pack(side="left", padx=(6, 12))
        search_entry.bind("<KeyRelease>", lambda e: self.refresh())

        ttk.Button(toolbar, text="New (Ctrl+N)", command=self.add_item).pack(side="left", padx=(0, 8))
        ttk.Button(toolbar, text="Edit", command=self.edit_item).pack(side="left", padx=(0, 8))
        ttk.Button(toolbar, text="Delete (Del)", command=self.delete_item).pack(side="left", padx=(0, 8))
        ttk.Button(toolbar, text="Export CSV", command=self.export_items).pack(side="left", padx=(0, 8))
        ttk.Button(toolbar, text="Refresh", command=self.refresh).pack(side="left")

        main = ttk.Frame(self.root, padding=(12, 0, 12, 12))
        main.pack(fill="both", expand=True)

        cols = ("id", "name", "category", "quantity", "unit_price", "value", "updated_at")
        self.tree = ttk.Treeview(main, columns=cols, show="headings", height=16)
        self.tree.pack(side="left", fill="both", expand=True)

        vsb = ttk.Scrollbar(main, orient="vertical", command=self.tree.yview)
        vsb.pack(side="right", fill="y")
        self.tree.configure(yscrollcommand=vsb.set)

        headings = {
            "id": "ID",
            "name": "Name",
            "category": "Category",
            "quantity": "Qty",
            "unit_price": "Unit Price",
            "value": "Total Value",
            "updated_at": "Updated",
        }
        widths = {"id": 60, "name": 220, "category": 160, "quantity": 80, "unit_price": 110, "value": 120, "updated_at": 160}

        for c in cols:
            self.tree.heading(c, text=headings[c], command=lambda col=c: self.set_sort(col))
            self.tree.column(c, width=widths[c], anchor="w")

        self.tree.bind("<Double-1>", lambda e: self.edit_item())

        # Status bar
        self.status = tk.StringVar(value="Ready")
        status_bar = ttk.Label(self.root, textvariable=self.status, anchor="w", padding=(12, 6))
        status_bar.pack(fill="x", side="bottom")

        # Shortcuts
        self.root.bind("<Control-n>", lambda e: self.add_item())
        self.root.bind("<Control-s>", lambda e: self.edit_item())
        self.root.bind("<Delete>", lambda e: self.delete_item())
        self.root.bind("<Escape>", lambda e: self.root.focus_set())

    def set_sort(self, col: str):
        if self.sort_col == col:
            self.sort_desc = not self.sort_desc
        else:
            self.sort_col = col
            self.sort_desc = False if col in ("name", "category") else True
        self.refresh()

    def _query_items(self) -> list[dict]:
        q = self.var_search.get().strip().lower()
        order = "DESC" if self.sort_desc else "ASC"

        # Note: 'value' is computed in SQL, so we handle ordering carefully.
        sort_map = {
            "id": "id",
            "name": "name",
            "category": "category",
            "quantity": "quantity",
            "unit_price": "unit_price",
            "updated_at": "updated_at",
            "value": "(quantity * unit_price)",
        }
        sort_expr = sort_map.get(self.sort_col, "updated_at")

        sql = f"""
            SELECT
                id, name, category, quantity, unit_price,
                (quantity * unit_price) AS value,
                updated_at
            FROM items
            WHERE LOWER(name) LIKE ? OR LOWER(category) LIKE ?
            ORDER BY {sort_expr} {order}, id DESC
        """

        like = f"%{q}%"
        with get_conn() as conn:
            rows = conn.execute(sql, (like, like)).fetchall()
        return [dict(r) for r in rows]

    def refresh(self):
        for item in self.tree.get_children():
            self.tree.delete(item)

        rows = self._query_items()
        total_value = 0.0

        for r in rows:
            total_value += float(r["value"])
            self.tree.insert(
                "",
                "end",
                values=(
                    r["id"],
                    r["name"],
                    r["category"],
                    r["quantity"],
                    f"{float(r['unit_price']):.2f}",
                    f"{float(r['value']):.2f}",
                    r["updated_at"],
                ),
            )

        self.status.set(f"Items: {len(rows)} | Total value: {total_value:.2f} | Sort: {self.sort_col} ({'DESC' if self.sort_desc else 'ASC'})")

    def _selected_id(self) -> int | None:
        sel = self.tree.selection()
        if not sel:
            return None
        values = self.tree.item(sel[0], "values")
        return int(values[0])

    def add_item(self):
        dlg = ItemDialog(self.root, "Add Item")
        self.root.wait_window(dlg)
        if not dlg.result:
            return

        item = dlg.result
        with get_conn() as conn:
            conn.execute(
                "INSERT INTO items (name, category, quantity, unit_price, updated_at) VALUES (?, ?, ?, ?, ?)",
                (item.name, item.category, item.quantity, item.unit_price, item.updated_at),
            )
        self.refresh()

    def edit_item(self):
        item_id = self._selected_id()
        if item_id is None:
            messagebox.showinfo("Edit", "Select an item to edit.")
            return

        with get_conn() as conn:
            row = conn.execute("SELECT * FROM items WHERE id = ?", (item_id,)).fetchone()
        if not row:
            messagebox.showerror("Edit", "Item not found.")
            return

        initial = Item(
            id=row["id"],
            name=row["name"],
            category=row["category"],
            quantity=row["quantity"],
            unit_price=row["unit_price"],
            updated_at=row["updated_at"],
        )

        dlg = ItemDialog(self.root, "Edit Item", initial=initial)
        self.root.wait_window(dlg)
        if not dlg.result:
            return

        item = dlg.result
        with get_conn() as conn:
            conn.execute(
                """
                UPDATE items
                SET name=?, category=?, quantity=?, unit_price=?, updated_at=?
                WHERE id=?
                """,
                (item.name, item.category, item.quantity, item.unit_price, item.updated_at, item_id),
            )
        self.refresh()

    def delete_item(self):
        item_id = self._selected_id()
        if item_id is None:
            messagebox.showinfo("Delete", "Select an item to delete.")
            return

        if not messagebox.askyesno("Delete", f"Delete item ID {item_id}?"):
            return

        with get_conn() as conn:
            conn.execute("DELETE FROM items WHERE id = ?", (item_id,))
        self.refresh()

    def export_items(self):
        rows = self._query_items()
        path = filedialog.asksaveasfilename(
            title="Export CSV",
            defaultextension=".csv",
            filetypes=[("CSV Files", "*.csv")],
        )
        if not path:
            return

        export_csv(path, rows)
        messagebox.showinfo("Export", f"Exported {len(rows)} rows to:\n{path}")


⸻

▶️ Run It

From inside inventory_manager/:

python main.py

It will create inventory.sqlite3 automatically.

⸻

Want it even more complex?

Pick one and I’ll extend the code in that direction:
	1.	User accounts + login + roles (admin vs viewer)
	2.	Charts dashboard (matplotlib in Tkinter)
	3.	Import CSV + duplicate handling
	4.	Undo/redo stack
	5.	Multi-window app with tabs + settings + theme switch
	6.	Packaging into a single EXE (PyInstaller)

Tell me which option(s) you want and I’ll upgrade this project accordingly.
