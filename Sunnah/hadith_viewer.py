#!/usr/bin/env python3
"""
A program which fetches the hadiths easily as a demonstration 
To run, open the folder containing hadith_viewer.py in terminal and run "python hadith_viewer.py" 
This is just a demonstration program, not really required as you can just check each json file's structure manually to use it,
Just thought to include this maybe it might help out Inshallah
"""
import os
import json
import re
import tkinter as tk
from tkinter import ttk, messagebox, filedialog, scrolledtext

DEFAULT_ROOT = os.path.join(os.getcwd(), "Sunnah")

class HadithViewer(tk.Tk):
    def __init__(self, root_folder=None):
        super().__init__()
        self.title("Hadith Viewer — Auto-list Books")
        self.geometry("900x650")

        self.root_folder = root_folder or DEFAULT_ROOT
        self.collections = []
        self.book_map = {}       # display_name
        self.hadiths = []        # list of hadith dicts for current book
        self.id_map = {}         # id (int) 
        self.current_collection = None
        self.current_bookfile = None

        #UI Not really needed for you, just to make stuff a bit easier
        top = ttk.Frame(self)
        top.pack(fill="x", padx=8, pady=6)

        ttk.Label(top, text="Sunnah folder:").pack(side="left")
        self.folder_lbl = ttk.Label(top, text=self.root_folder, foreground="blue")
        self.folder_lbl.pack(side="left", padx=(6,10))

        ttk.Button(top, text="Change...", command=self.change_folder).pack(side="left")
        ttk.Button(top, text="Refresh", command=self.scan_collections).pack(side="left", padx=6)

        mid = ttk.Frame(self)
        mid.pack(fill="x", padx=8, pady=6)

        ttk.Label(mid, text="Collection:").grid(row=0, column=0, sticky="w")
        self.collection_cb = ttk.Combobox(mid, state="readonly", width=30)
        self.collection_cb.grid(row=0, column=1, sticky="w", padx=6)
        self.collection_cb.bind("<<ComboboxSelected>>", lambda e: self.on_collection_selected())

        ttk.Label(mid, text="Book:").grid(row=1, column=0, sticky="w")
        self.book_cb = ttk.Combobox(mid, state="readonly", width=60)
        self.book_cb.grid(row=1, column=1, sticky="w", padx=6)
        self.book_cb.bind("<<ComboboxSelected>>", lambda e: self.on_book_selected())

        idframe = ttk.Frame(self)
        idframe.pack(fill="x", padx=8, pady=6)

        ttk.Label(idframe, text="Hadith ID:").pack(side="left")
        self.id_var = tk.StringVar(value="1")
        self.id_spin = ttk.Spinbox(idframe, from_=1, to=1, textvariable=self.id_var, width=8)
        self.id_spin.pack(side="left", padx=(6,4))
        ttk.Button(idframe, text="Go", command=self.fetch_by_id).pack(side="left", padx=4)
        ttk.Button(idframe, text="Prev", command=self.prev_hadith).pack(side="left", padx=4)
        ttk.Button(idframe, text="Next", command=self.next_hadith).pack(side="left", padx=4)

        self.total_lbl = ttk.Label(idframe, text="of 0")
        self.total_lbl.pack(side="left", padx=10)

        # Optional quick search in current book
        ttk.Label(idframe, text="Search:").pack(side="left", padx=(20,4))
        self.search_e = ttk.Entry(idframe, width=30)
        self.search_e.pack(side="left")
        ttk.Button(idframe, text="Find", command=self.search_current_book).pack(side="left", padx=4)

        # Display area
        disp_frame = ttk.Frame(self)
        disp_frame.pack(fill="both", expand=True, padx=8, pady=6)

        self.display = scrolledtext.ScrolledText(disp_frame, wrap=tk.WORD, font=("Segoe UI", 11))
        self.display.pack(fill="both", expand=True)

        # Status bar
        self.status = ttk.Label(self, text="Ready", relief="sunken", anchor="w")
        self.status.pack(fill="x", side="bottom")

        # initial scan
        self.scan_collections()

    # folder / scanning so that it auto scans stuff
    def change_folder(self):
        chosen = filedialog.askdirectory(initialdir=self.root_folder or os.getcwd(), title="Select Sunnah root folder")
        if chosen:
            self.root_folder = chosen
            self.folder_lbl.config(text=self.root_folder)
            self.scan_collections()

    def scan_collections(self):
        self.collections = []
        self.collection_cb.set("")
        self.book_cb.set("")
        self.book_cb['values'] = []
        self.hadiths = []
        self.id_map = {}
        self.update_status("Scanning collections...")
        root = self.root_folder
        if not root or not os.path.isdir(root):
            self.update_status("Sunnah folder not found — please select folder.")
            messagebox.showwarning("Folder not found", f"Couldn't find folder: {root}\nPlease choose the Sunnah root folder.")
            return

        entries = sorted(os.listdir(root))
        for name in entries:
            full = os.path.join(root, name)
            if os.path.isdir(full):
                self.collections.append(name)
        if not self.collections:
            self.update_status("No collections found in folder.")
            messagebox.showinfo("No collections", f"No subfolders found in {root}")
            self.collection_cb['values'] = []
            return

        self.collection_cb['values'] = self.collections
        self.collection_cb.current(0)
        self.update_status(f"Found {len(self.collections)} collections.")
        # auto load first colleciton s books
        self.on_collection_selected()

    #collections/books
    def on_collection_selected(self):
        col = self.collection_cb.get()
        if not col:
            return
        self.current_collection = col
        self.load_books_for_collection(col)

    def load_books_for_collection(self, collection):
        self.book_cb.set("")
        self.book_map = {}
        path = os.path.join(self.root_folder, collection)
        if not os.path.isdir(path):
            self.update_status("Collection folder missing.")
            return
        files = [f for f in sorted(os.listdir(path)) if f.lower().endswith(".json")]
        display_names = []
        for f in files:
            
            m = re.match(r"^(\d+)_?(.*)\.json$", f, re.I)
            if m:
                num = m.group(1)
                rest = m.group(2).replace("_", " ")
                display = f"{num} - {rest}"
            else:
                display = f
            display_names.append(display)
            self.book_map[display] = f
        if not display_names:
            self.update_status("No JSON books found in collection.")
            self.book_cb['values'] = []
            return
        self.book_cb['values'] = display_names
        self.book_cb.current(0)
        self.update_status(f"Found {len(display_names)} books in {collection}")
        self.on_book_selected()

    # Loading a book
    def on_book_selected(self):
        book_display = self.book_cb.get()
        if not book_display:
            return
        bookfile = self.book_map.get(book_display)
        if not bookfile:
            self.update_status("Book selection invalid.")
            return
        self.current_bookfile = bookfile
        self.load_book_json(self.current_collection, bookfile)

    def load_book_json(self, collection, filename):
        path = os.path.join(self.root_folder, collection, filename)
        self.update_status(f"Loading {filename} ...")
        try:
            with open(path, "r", encoding="utf-8-sig") as f:
                data = json.load(f)
        except Exception as e:
            messagebox.showerror("Load error", f"Failed to load {path}:\n{e}")
            self.update_status("Failed to load book.")
            return

        if not isinstance(data, list):
            messagebox.showerror("Format error", f"Expected a list of hadiths in {filename}")
            self.update_status("Book JSON is not a list.")
            return

        self.hadiths = data
        # build id map
        self.id_map = {}
        if data and isinstance(data[0], dict) and "id" in data[0]:
            for h in data:
                try:
                    hid = int(h.get("id"))
                    self.id_map[hid] = h
                except Exception:
                    
                    pass
            
            if len(self.id_map) != len(data):
                for i, h in enumerate(data, start=1):
                    if i not in self.id_map:
                        self.id_map[i] = h
        else:
            for i, h in enumerate(data, start=1):
                self.id_map[i] = h

        total = len(self.hadiths)
        self.id_spin.config(to=total)
        self.total_lbl.config(text=f"of {total}")
        self.id_var.set("1")
        self.update_status(f"Loaded {filename} ({total} hadiths)")
        self.show_hadith_by_id(1)

    # navigate/show
    def fetch_by_id(self):
        try:
            hid = int(self.id_var.get())
        except Exception:
            messagebox.showerror("Invalid ID", "Hadith ID must be a number.")
            return
        self.show_hadith_by_id(hid)

    def show_hadith_by_id(self, hid):
        h = self.id_map.get(hid)
        if not h:
            messagebox.showinfo("Not found", f"Hadith ID {hid} was not found in this book.")
            return
        self.id_var.set(str(hid))
        self.display.delete(1.0, tk.END)
        arabic = h.get("arabic","")
        english = h.get("english","")
        grade = h.get("grade","")
        ref = h.get("reference","")
        # display with simple headings
        self.display.insert(tk.END, f"Collection: {self.current_collection}\n")
        self.display.insert(tk.END, f"Book file: {self.current_bookfile}\n")
        self.display.insert(tk.END, f"Hadith ID: {hid}    Reference: {ref}\n")
        self.display.insert(tk.END, "-"*80 + "\n\n")
        if arabic:
            self.display.insert(tk.END, "Arabic:\n" + arabic + "\n\n")
        if english:
            self.display.insert(tk.END, "English:\n" + english + "\n\n")
        if grade:
            self.display.insert(tk.END, "Grade:\n" + grade + "\n\n")
        self.update_status(f"Showing hadith {hid}")

    def prev_hadith(self):
        try:
            hid = int(self.id_var.get())
        except:
            hid = 1
        if hid > 1:
            self.show_hadith_by_id(hid-1)

    def next_hadith(self):
        try:
            hid = int(self.id_var.get())
        except:
            hid = 1
        total = len(self.hadiths)
        if hid < total:
            self.show_hadith_by_id(hid+1)

    # manual search, not rlly needed
    def search_current_book(self):
        q = self.search_e.get().strip().lower()
        if not q:
            return
        if not self.hadiths:
            messagebox.showinfo("No book", "Load a book first.")
            return
        # find first occurrence in english/reference
        for hid, h in self.id_map.items():
            english = (h.get("english") or "").lower()
            ref = (h.get("reference") or "").lower()
            if q in english or q in ref:
                self.show_hadith_by_id(hid)
                return
        messagebox.showinfo("Not found", f"No hadith matching '{q}' in this book.")

    def update_status(self, text):
        self.status.config(text=text)

if __name__ == "__main__":
    app = HadithViewer()
    app.mainloop()
