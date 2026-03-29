# Python-fake-virus

<img width="1919" height="1079" alt="image" src="https://github.com/user-attachments/assets/19185f45-57fd-4f7f-ad88-d197df7e6845" />

This is a Python script that enters full screen and displays a fake security alert — purely for entertainment and educational purposes.

--------------------

# Disclaimer

> Information and code provided on this repository are for educational and entertainment purposes only. The creator bears absolutely no responsibility for any direct or indirect damage, harm, or loss caused by the misuse of this software. By downloading, running, or distributing this script, you accept full legal and moral responsibility for your own actions. The creator is not liable in any way, legally or otherwise, for any consequences arising from the use or misuse of this code. Use at your own risk.

--------------------

# How to Use

1. Download the repository as a ZIP file
2. Unzip the folder
3. Install [Python](https://www.python.org/downloads/) on your computer
4. Run `main.py` using Python (e.g. double-click or run `python main.py` in terminal)

--------------------

# How to Close the App

Since the app respawns when closed normally, follow these steps to fully shut it down:

**Option 1 — Task Manager (Recommended):**
1. Press **Ctrl + Shift + Esc** to open Task Manager
2. Click **"More details"** if you're in the simple view
3. Go to the **Details** tab
4. Find every `python.exe` entry in the list
5. Right-click each one and select **End Task**
6. Repeat until no `python.exe` entries remain

**Option 2 — Command Prompt (Fastest):**
1. Press **Win + R** to open the Run dialog
2. Type `cmd` and press Enter
3. In the Command Prompt window, type the following and press Enter:
```
taskkill /f /im python.exe /t
```
4. This instantly kills the app and all related processes

**Option 3 — If nothing opens:**
1. Press **Ctrl + Alt + Delete**
2. Click **Task Manager**
3. Go to the **Details** tab
4. Kill all `python.exe` processes

--------------------
