import tkinter as tk
import random
import time
import threading
import subprocess
import sys
import os

messages = [
    "Scanning system files...",
    "Checking boot sector...",
    "Suspicious activity detected in C:\\Windows\\System32...",
    "Decrypting registry keys...",
    "Unauthorized remote access attempt blocked...",
    "Downloading emergency security patch...",
    "WARNING: Unknown executable detected in memory",
    "Analyzing network traffic... anomaly found",
    "Virus signature match: TROJAN.WIN32.DARKGATE",
    "Isolating infected files...",
    "Attempting to remove malicious files... FAILED",
    "Rootkit detected in MBR sector...",
    "Firewall rules compromised...",
    "Keylogger process found running in background...",
    "Data exfiltration attempt detected...",
    "Encrypting backup files... ERROR",
    "System integrity check: FAILED",
    "BIOS tampering detected...",
    "Remote shell connection established by unknown host...",
    "Critical system files corrupted...",
    "Network adapter hijacked...",
    "Shadow copies being deleted...",
    "Ransomware payload found in temp folder...",
    "GPU driver compromised...",
    "CPU usage spike detected: possible cryptominer",
    "Memory dump in progress...",
]

glitch_chars = list("!@#$%^&*<>?/\\|[]{}~`")

def beep_loop():
    """Cross-platform beep using tkinter bell"""
    while not stop_event.is_set():
        try:
            root_ref.bell()
        except:
            pass
        time.sleep(random.uniform(1.5, 3.5))

def glitch_text(text):
    result = []
    for ch in text:
        if random.random() < 0.07:
            result.append(random.choice(glitch_chars))
        else:
            result.append(ch)
    return "".join(result)

def update_text():
    colors = ["lime", "#00ff99", "#00ffcc", "#ff0000", "#ff4444", "white"]
    while not stop_event.is_set():
        msg = random.choice(messages)
        glitched = glitch_text(msg)
        percent = random.randint(1, 99)
        bar_filled = int(percent / 5)
        bar = "█" * bar_filled + "░" * (20 - bar_filled)
        full_text = (
            f"{glitched}\n\n"
            f"[{bar}] {percent}%\n\n"
            f"Threat Level: {'■' * random.randint(3,8)}{'□' * random.randint(0,4)}"
        )
        try:
            label.config(text=full_text, fg=random.choice(colors))
        except:
            break
        time.sleep(random.uniform(0.4, 1.5))

def flicker_title():
    flicker_colors = ["red", "#ff4500", "#cc0000", "white", "red"]
    while not stop_event.is_set():
        try:
            title.config(fg=random.choice(flicker_colors))
        except:
            break
        time.sleep(random.uniform(0.1, 0.5))

def scroll_log():
    log_lines = []
    while not stop_event.is_set():
        entry = f"[{time.strftime('%H:%M:%S')}] {random.choice(messages)}"
        log_lines.append(entry)
        if len(log_lines) > 12:
            log_lines.pop(0)
        try:
            log_label.config(text="\n".join(log_lines))
        except:
            break
        time.sleep(random.uniform(0.6, 1.8))

def on_close():
    # Respawn a new window and then destroy this one
    try:
        subprocess.Popen([sys.executable, os.path.abspath(__file__)])
    except:
        pass
    stop_event.set()
    root.destroy()

stop_event = threading.Event()
root_ref = None

def main():
    global root, label, title, log_label, root_ref, stop_event
    stop_event = threading.Event()

    root = tk.Tk()
    root_ref = root
    root.title("System Security Alert")
    root.attributes("-fullscreen", True)
    root.configure(bg="black")

    # Override all close attempts
    root.protocol("WM_DELETE_WINDOW", on_close)
    root.bind("<Escape>", lambda e: on_close())

    # ── TOP HEADER ──
    header = tk.Frame(root, bg="#1a0000", pady=10)
    header.pack(fill="x")

    tk.Label(
        header,
        text="⚠  CRITICAL SECURITY BREACH DETECTED  ⚠",
        fg="red",
        bg="#1a0000",
        font=("Consolas", 28, "bold")
    ).pack()

    tk.Label(
        header,
        text="Windows Defender Emergency Response System  |  Threat Level: CRITICAL",
        fg="#ff6666",
        bg="#1a0000",
        font=("Consolas", 13)
    ).pack()

    # ── DIVIDER ──
    tk.Frame(root, bg="red", height=2).pack(fill="x")

    # ── MAIN CONTENT AREA ──
    content = tk.Frame(root, bg="black")
    content.pack(expand=True, fill="both", padx=40, pady=10)

    # Left: big alert label
    left = tk.Frame(content, bg="black")
    left.pack(side="left", expand=True, fill="both")

    title = tk.Label(
        left,
        text="⛔  SYSTEM COMPROMISED  ⛔",
        fg="red",
        bg="black",
        font=("Consolas", 36, "bold")
    )
    title.pack(pady=(20, 10))

    tk.Label(
        left,
        text="Multiple threats detected. Your files are at risk.\nDo NOT shut down your computer.",
        fg="#ff4444",
        bg="black",
        font=("Consolas", 16)
    ).pack(pady=5)

    label = tk.Label(
        left,
        text="Initializing threat analysis...",
        fg="lime",
        bg="black",
        font=("Consolas", 20),
        justify="center"
    )
    label.pack(pady=30)

    # Right: scrolling log
    right = tk.Frame(content, bg="#0a0a0a", bd=1, relief="sunken", width=500)
    right.pack(side="right", fill="both", padx=(20, 0), pady=10)
    right.pack_propagate(False)

    tk.Label(
        right,
        text="── LIVE THREAT LOG ──",
        fg="#00ff99",
        bg="#0a0a0a",
        font=("Consolas", 12, "bold")
    ).pack(pady=5)

    log_label = tk.Label(
        right,
        text="",
        fg="#00cc66",
        bg="#0a0a0a",
        font=("Consolas", 11),
        justify="left",
        anchor="nw",
        wraplength=480
    )
    log_label.pack(padx=10, pady=5, fill="both", expand=True)

    # ── BOTTOM STATUS BAR ──
    tk.Frame(root, bg="red", height=2).pack(fill="x")

    bottom = tk.Frame(root, bg="#1a0000", pady=8)
    bottom.pack(fill="x")
    
    tk.Label(
        bottom,
        text="Press ESC only if you accept full responsibility for data loss",
        fg="gray",
        bg="#1a0000",
        font=("Consolas", 10)
    ).pack()

    # ── THREADS ──
    threading.Thread(target=update_text, daemon=True).start()
    threading.Thread(target=flicker_title, daemon=True).start()
    threading.Thread(target=scroll_log, daemon=True).start()
    threading.Thread(target=beep_loop, daemon=True).start()

    root.mainloop()


if __name__ == "__main__":
    main()
