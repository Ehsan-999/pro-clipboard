# Pro Clipboard 

A modern **Clipboard Manager** built with **Python** and **Tkinter**.  
Keep track of your copied texts, pin important items, search, and manage your clipboard easily!

---

## Features ✨

- Auto-detect clipboard changes every second  
- Store up to **20 recent items**  
- **Pin important items** to the top (displayed in red)  
- **Search** and highlight matching items  
- **Copy**, **Delete**, and **Clear** clipboard items with one click  
- **Dark Mode** friendly UI  
- **Persistent history**: Clipboard items are saved and loaded on app restart  

---

## Screenshots 🖼️

![Clipboard Manager Screenshot](screenshot.png)

---

## How to Use 🛠️

1. Run the program with Python:
    ```bash
    python pro_clipboard.py
    ```
2. Copy any text → it will automatically appear in the list  
3. Select an item and use the buttons to:
   - **Copy Selected** → copy back to clipboard  
   - **Delete Selected** → remove from list  
   - **Clear All** → remove all items  
   - **Pin Selected** → move to top and highlight in red  
4. Use the **Search** bar to find any item (highlighted in yellow)  

---

## Requirements 📦

- Python 3.x  
- Tkinter (usually included in standard Python distribution)  

---

## Build Executable 🔧

To create a standalone executable (Windows):

```bash
pip install pyinstaller
pyinstaller --onefile --noconsole pro_clipboard.py
