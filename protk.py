import tkinter as tk

last_text = ""
HISTORY_FILE = "history.txt"
MAX_ITEMS = 20

window = tk.Tk()
window.title("Pro Clipboard")
window.geometry("700x600")
window.configure(bg="#2b2b2b")

lbl = tk.Label(window, text="Pro Clipboard", bg="#1f5f3c", fg="white", font=("Arial", 20), padx=10, pady=5)
lbl.pack(pady=(10, 5))

entry = tk.Entry(window, width=50, font=("Arial", 12), bg="#3b3b3b", fg="white", insertbackground="white")
entry.pack(pady=5)

def search():
    query = entry.get().lower()
    for i in range(clip.size()):
        item_text = clip.get(i).lower()
        if query in item_text:
            clip.itemconfig(i, bg="#ffeb3b", fg="black")
        else:
            # اگر آیتم پین نیست قرمز باقی بمونه
            fg_color = "red" if i == 0 and clip.itemcget(i, "bg") == "red" else "white"
            clip.itemconfig(i, bg="#2b2b2b", fg=fg_color)

search_btn = tk.Button(window, text="Search", width=15, bg="#4caf50", fg="white", font=("Arial", 12), command=search)
search_btn.pack(pady=5)

clip = tk.Listbox(window, width=80, height=20, font=("Arial", 12), bg="#2b2b2b", fg="white", selectbackground="#555555", activestyle="none")
clip.pack(pady=10)

def check_clipboard():
    global last_text
    try:
        text = window.clipboard_get()
    except:
        window.after(1000, check_clipboard)
        return
    if text != last_text:
        clip.insert(tk.END, text)
        if clip.size() > MAX_ITEMS:
            clip.delete(0)
        last_text = text
    window.after(1000, check_clipboard)

def copy_selected():
    try:
        index = clip.curselection()[0]
        text = clip.get(index)
        window.clipboard_clear()
        window.clipboard_append(text)
    except:
        pass

copy_btn = tk.Button(window, text="Copy Selected", width=20, bg="#2196f3", fg="white", font=("Arial", 12), command=copy_selected)
copy_btn.pack(pady=3)

def load_history():
    global last_text
    try:
        with open(HISTORY_FILE, "r", encoding="utf-8") as f:
            for line in f:
                text = line.strip()
                clip.insert(tk.END, text)
                last_text = text
    except:
        pass

load_history()

def clear_list():
    clip.delete(0, tk.END)

clear_btn = tk.Button(window, text="Clear All", width=20, bg="#f44336", fg="white", font=("Arial", 12), command=clear_list)
clear_btn.pack(pady=3)

def delet():
    global last_text
    try:
        index = clip.curselection()[0]
        text = clip.get(index)
        clip.delete(index)
        try:
            clipboard_text = window.clipboard_get()
            if clipboard_text == text:
                window.clipboard_clear()
                last_text = ""
        except:
            last_text = ""
    except:
        pass

delet_btn = tk.Button(window, text="Delete Selected", width=20, bg="#ff9800", fg="white", font=("Arial", 12), command=delet)
delet_btn.pack(pady=3)

def pin():
    try:
        index = clip.curselection()[0]
        text = clip.get(index)
        clip.delete(index)
        clip.insert(0, text)
        clip.itemconfig(0, bg="red", fg="white")
    except:
        pass

pin_btn = tk.Button(window, text="Pin Selected", width=20, bg="#9c27b0", fg="white", font=("Arial", 12), command=pin)
pin_btn.pack(pady=3)

check_clipboard()

def save_history():
    with open(HISTORY_FILE, "w", encoding="utf-8") as f:
        for i in range(clip.size()):
            f.write(clip.get(i) + "\n")

def on_close():
    save_history()
    window.destroy()

window.protocol("WM_DELETE_WINDOW", on_close)
window.mainloop()
