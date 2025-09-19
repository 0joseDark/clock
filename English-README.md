# What the program includes

* Qt interface (PySide6) compatible with **Windows 10, Ubuntu, and macOS**.
* Displays **hours, minutes, and seconds** in a large `QLabel`.
* **Buttons**: `Start/Stop` (toggle) and `Exit`.
* **Menu**: `File → Exit`, `View → Show Seconds` (checkable), and `Help → About`.
* Updates via `QTimer` every 1000 ms (1 second).
* Step-by-step commented code inside the file (in English) — see the file in the editor.

# How to run (quick)

1. Install the dependency:

   * `pip install PySide6`
2. Run:

   * `python clock_qt.py`  (or `python3 clock_qt.py` depending on your system)

# Step-by-step explanation (summary)

1. **Imports and setup** — imports `QApplication`, `QMainWindow`, `QLabel`, `QPushButton`, `QTimer`, etc., and `datetime` to get the system time.
2. **Main class (`ClockMainWindow`)** — inherits from `QMainWindow` and sets up:

   * `time_label`: the widget that shows the time (large font, centered).
   * `Start/Stop` and `Exit` buttons in a horizontal layout.
   * `create_menus()` builds the menu bar with actions (includes Ctrl+Q shortcut to exit).
3. **Timer (`QTimer`)** — fires every second, calls `update_time()` which formats `datetime.now()` into `HH:MM:SS` (or `HH:MM` if seconds are hidden).
4. **Start/Stop control** — the button toggles the timer state; when stopped, the timer no longer calls `update_time`.
5. **Show/Hide Seconds** — checkable option in the menu that toggles the `show_seconds` flag and forces an update.
6. **About** — simple `QMessageBox` with application info.

# Quick customization tips

* Change font size: in the file, adjust `font.setPointSize(48)` to another value.
* Switch between 24h/12h format: modify `strftime(\"%H:%M:%S\")` to use `%I` and add ` %p` for AM/PM.
* Add an analog clock: create a custom `QWidget` and draw with `QPainter`.
* Styling: use `setStyleSheet()` on the `QLabel`/buttons to change the look.

# Packaging for each OS

* **Windows**: `pyinstaller --onefile --windowed clock_qt.py` (you can add an icon).
* **macOS**: `py2app` or `pyinstaller` with proper flags (`--windowed`).
* **Linux**: create a `.deb`/snap/flatpak package as needed; you can also use `pyinstaller` for a binary.
