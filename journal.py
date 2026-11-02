import tkinter as tk
from tkinter import scrolledtext, messagebox
import datetime

FILENAME = "journal.txt"

def save_note():
    note = entry.get("1.0", tk.END).strip()
    if not note:
        messagebox.showwarning("Empty", "Write something first.")
        return
    
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M")
    with open(FILENAME, "a", encoding="utf-8") as f:
        f.write(f"[{timestamp}] {note}\n\n")
    
    entry.delete("1.0", tk.END)
    load_notes()
    messagebox.showinfo("Saved", "Note saved!")

def load_notes():
    notes_area.config(state=tk.NORMAL)
    notes_area.delete("1.0", tk.END)
    try:
        with open(FILENAME, "r", encoding="utf-8") as f:
            notes_area.insert(tk.END, f.read())
    except FileNotFoundError:
        notes_area.insert(tk.END, "No notes yet.")
    notes_area.config(state=tk.DISABLED)

# Create the window
root = tk.Tk()
root.title("My Journal")
root.geometry("420x500")          # small window size
root.resizable(False, False)      # keep it fixed size

# Title
tk.Label(root, text="Personal Journal", font=("Arial", 14, "bold")).pack(pady=8)

# Write area
tk.Label(root, text="Write a note:").pack(anchor="w", padx=10)
entry = scrolledtext.ScrolledText(root, height=6, wrap=tk.WORD)
entry.pack(padx=10, pady=5, fill=tk.X)

# Save button
tk.Button(root, text="Save Note", command=save_note, bg="#4CAF50", fg="white").pack(pady=5)

# View past notes
tk.Label(root, text="Past notes:").pack(anchor="w", padx=10, pady=(10, 0))
notes_area = scrolledtext.ScrolledText(root, height=14, wrap=tk.WORD, state=tk.DISABLED)
notes_area.pack(padx=10, pady=5, fill=tk.BOTH, expand=True)

# Load existing notes when the window opens
load_notes()

# Start the window
root.mainloop()