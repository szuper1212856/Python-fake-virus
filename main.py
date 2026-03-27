
import tkinter as tk
import random
import time
import threading

messages = [
    "Scanning system files...",
    "Checking boot sector...",
    "Suspicious activity detected...",
    "Decrypting registry...",
    "Unauthorized access attempt blocked...",
    "Downloading security patch...",
    "WARNING: Unknown executable detected",
    "Analyzing network traffic...",
    "Virus signature match found...",
    "Isolating infected files..."
    "Attempting to remove malicious files..."
    "Attempt failed, retrying soon..."
]

def update_text(label):
    while True:
        msg = random.choice(messages)
        percent = random.randint(1, 99)
        label.config(text=f"{msg}\n\nSystem Scan Progress: {percent}%")
        time.sleep(random.uniform(0.5, 2))


def main():
    root = tk.Tk()
    root.title("System Security Scan")

    # fullscreen
    root.attributes("-fullscreen", True)
    root.configure(bg="black")

    frame = tk.Frame(root, bg="black")
    frame.pack(expand=True)

    title = tk.Label(
        frame,
        text="CRITICAL SECURITY ALERT",
        fg="red",
        bg="black",
        font=("Consolas", 40, "bold")
    )
    title.pack(pady=40)

    label = tk.Label(
        frame,
        text="Initializing scan...",
        fg="lime",
        bg="black",
        font=("Consolas", 24)
    )
    label.pack(pady=20)

    exit_msg = tk.Label(
        frame,
        text="Remove this manually by pressing esc. and holding down the windows button and pressing R then typing shell:startup and removing the only file there.",
        fg="gray",
        bg="black",
        font=("Consolas", 14)
    )
    exit_msg.pack(pady=20)

    root.bind("<Escape>", lambda e: root.destroy())

    thread = threading.Thread(target=update_text, args=(label,), daemon=True)
    thread.start()

    root.mainloop()


if __name__ == "__main__":
    main()
