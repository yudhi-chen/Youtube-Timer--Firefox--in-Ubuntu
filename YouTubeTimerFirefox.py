#!/usr/bin/env python3
import sys
import time
import subprocess
import tkinter as tk
from tkinter import messagebox

# ---------------- SETTINGS ----------------
YOUTUBE_URL = "https://www.youtube.com/"
YOUTUBE_KIDS_URL = "https://www.youtubekids.com/"

PROFILE_YOUTUBE = "mainYT"
PROFILE_KIDS = "kidsYT"

DURATIONS = [5, 10, 15, 25]
# ------------------------------------------

mode = sys.argv[1].lower() if len(sys.argv) > 1 else "youtube"

if mode == "kids":
    URL = YOUTUBE_KIDS_URL
    PROFILE = PROFILE_KIDS
    TITLE = "YouTube Kids"
    HEADER_ICON = "🧒"
else:
    URL = YOUTUBE_URL
    PROFILE = PROFILE_YOUTUBE
    TITLE = "YouTube"
    HEADER_ICON = "▶️"

# ---------- POPUP PICKER ----------
picker = tk.Tk()
picker.title(TITLE)
picker.attributes("-topmost", True)
picker.resizable(False, False)
picker.configure(bg="#f4f4f4")

W, H = 360, 360
sw = picker.winfo_screenwidth()
sh = picker.winfo_screenheight()
picker.geometry(f"{W}x{H}+{(sw-W)//2}+{(sh-H)//2}")

main = tk.Frame(picker, bg="#f4f4f4", padx=18, pady=18)
main.pack(fill="both", expand=True)

tk.Label(
    main,
    text=f"{HEADER_ICON}  {TITLE}",
    font=("Arial", 16, "bold"),
    bg="#f4f4f4",
    fg="#222222"
).pack(pady=(0, 6))

tk.Label(
    main,
    text="⏱️ Select Time",
    font=("Arial", 11),
    bg="#f4f4f4",
    fg="#555555"
).pack(pady=(0, 16))

grid = tk.Frame(main, bg="#f4f4f4")
grid.pack()

selected = {"minutes": None}

def click_sound():
    try:
        picker.bell()
    except Exception:
        pass

def choose(minutes):
    click_sound()
    selected["minutes"] = minutes
    picker.destroy()

tile_specs = [
    (5,  "#ff6b6b", "5 min"),
    (10, "#4dabf7", "10 min"),
    (15, "#51cf66", "15 min"),
    (25, "#f59f00", "25 min"),
]

for idx, (minutes, color, label) in enumerate(tile_specs):
    row = idx // 2
    col = idx % 2
    btn = tk.Button(
        grid,
        text=f"▶️\n{label}",
        font=("Arial", 12, "bold"),
        width=10,
        height=4,
        bg=color,
        fg="white",
        activebackground=color,
        activeforeground="white",
        relief="flat",
        bd=0,
        command=lambda m=minutes: choose(m),
        cursor="hand2"
    )
    btn.grid(row=row, column=col, padx=8, pady=8, sticky="nsew")

for i in range(2):
    grid.grid_columnconfigure(i, weight=1)
    grid.grid_rowconfigure(i, weight=1)

def cancel():
    click_sound()
    picker.destroy()

tk.Button(
    main,
    text="Cancel",
    font=("Arial", 10, "bold"),
    width=12,
    bg="#dddddd",
    fg="#222222",
    activebackground="#cccccc",
    relief="flat",
    bd=0,
    command=cancel,
    cursor="hand2"
).pack(pady=(16, 0))

picker.mainloop()

if selected["minutes"] is None:
    raise SystemExit(0)

duration_sec = selected["minutes"] * 60

# ---------- LAUNCH FIREFOX ----------
try:
    proc = subprocess.Popen(
        [
            "firefox",
            "--no-remote",
            "-P", PROFILE,
            "--new-window",
            URL
        ],
        stdout=subprocess.DEVNULL,
        stderr=subprocess.DEVNULL
    )
except Exception as e:
    root = tk.Tk()
    root.withdraw()
    messagebox.showerror(TITLE, f"Failed to launch Firefox:\n{e}")
    raise SystemExit(1)

# ---------- TIMER UI ----------
root = tk.Tk()
root.title(f"{TITLE} Timer")
root.attributes("-topmost", True)
root.resizable(False, False)
root.configure(bg="#f4f4f4")

W, H = 300, 190
sw = root.winfo_screenwidth()
root.geometry(f"{W}x{H}+{sw-W-20}+20")

panel = tk.Frame(root, bg="#f4f4f4", padx=14, pady=12)
panel.pack(fill="both", expand=True)

tk.Label(
    panel,
    text=f"{HEADER_ICON} Screen Time",
    font=("Arial", 12, "bold"),
    bg="#f4f4f4",
    fg="#222222"
).pack(pady=(0, 4))

time_lbl = tk.Label(
    panel,
    font=("Arial", 30, "bold"),
    bg="#f4f4f4",
    fg="#111111"
)
time_lbl.pack()

status_lbl = tk.Label(
    panel,
    text="Browser will close politely",
    font=("Arial", 9),
    bg="#f4f4f4",
    fg="#666666"
)
status_lbl.pack(pady=(4, 8))

closing = False
remaining = duration_sec
last_warning = None

def polite_close():
    global closing
    if closing:
        return
    closing = True

    try:
        root.bell()
    except Exception:
        pass

    status_lbl.config(text="Closing browser...")
    root.update()

    try:
        proc.terminate()
    except Exception:
        pass

    for _ in range(20):
        time.sleep(0.1)
        if proc.poll() is not None:
            break

    if proc.poll() is None:
        try:
            proc.kill()
        except Exception:
            pass

    root.destroy()

def fmt(sec):
    m, s = divmod(sec, 60)
    return f"{m}:{s:02d}"

def tick():
    global remaining, last_warning

    if closing:
        return

    time_lbl.config(text=fmt(remaining))

    if remaining <= 10 and remaining >= 1 and remaining != last_warning:
        try:
            root.bell()
        except Exception:
            pass
        last_warning = remaining

    if remaining <= 0:
        polite_close()
        return

    remaining -= 1
    root.after(1000, tick)

def on_close():
    messagebox.showinfo(f"{TITLE} Timer", "Use 'End Now' to close early.")

tk.Button(
    panel,
    text="⏹️ End Now",
    font=("Arial", 11, "bold"),
    width=14,
    bg="#e03131",
    fg="white",
    activebackground="#c92a2a",
    activeforeground="white",
    relief="flat",
    bd=0,
    command=polite_close,
    cursor="hand2"
).pack(pady=(4, 0))

root.protocol("WM_DELETE_WINDOW", on_close)

tick()
root.mainloop()
