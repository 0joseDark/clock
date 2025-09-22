#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Simple Clock with Qt (PySide6)
Displays hours, minutes, and seconds.
Includes menu and buttons (Start/Stop, Exit) and an option in the menu to show/hide seconds.

Compatible with: Windows 10, Ubuntu (Linux) and macOS.
Dependency: PySide6 -> pip install PySide6

This file contains step-by-step comments explaining each block.
"""

import sys
from datetime import datetime
from PySide6.QtWidgets import (QApplication, QMainWindow, QLabel, QPushButton,
                               QWidget, QVBoxLayout, QHBoxLayout)
from PySide6.QtGui import QAction
from PySide6.QtCore import QTimer, Qt
from PySide6.QtGui import QFont


class ClockMainWindow(QMainWindow):
    """Main window of the clock."""

    def __init__(self):
        super().__init__()
        # Window title and initial size
        self.setWindowTitle("Clock Qt — Hours, minutes and seconds")
        self.resize(480, 220)

        # --- Estado interno ---
        # Flag to control whether to show seconds (True by default)
        self.show_seconds = True
        # Flag indicating whether the timer is running
        self.running = True

        # --- Central widget and layout ---
        central = QWidget()
        self.setCentralWidget(central)
        vbox = QVBoxLayout()
        central.setLayout(vbox)

        # --- Large label to display the time ---
        # We create a centered QLabel with a large font
        self.time_label = QLabel()
        font = QFont()
        font.setPointSize(48)  # font size — can be adjusted according to the screen
        font.setBold(True)
        self.time_label.setFont(font)
        self.time_label.setAlignment(Qt.AlignCenter)
        vbox.addWidget(self.time_label, stretch=1)

        # --- Buttons ---
        # We create a horizontal layout with Start/Stop and Exit buttons
        hbox = QHBoxLayout()

        self.start_stop_button = QPushButton("stop")
        # We connect the button click to the toggle_running method
        self.start_stop_button.clicked.connect(self.toggle_running)
        hbox.addWidget(self.start_stop_button)

        self.quit_button = QPushButton("Exit")
        self.quit_button.clicked.connect(self.close)
        hbox.addWidget(self.quit_button)

        vbox.addLayout(hbox)

        # --- Menu bar ---
        # We create a menu with File->Exit, View->Show Seconds and Help->About
        self.create_menus()

        # --- Timer that updates the time ---
        # The QTimer triggers every 1000 ms (1 s) and calls update_time
        self.timer = QTimer(self)
        self.timer.setInterval(1000)
        self.timer.timeout.connect(self.update_time)
        self.timer.start()

        # Updates immediately to avoid a 1 s delay when opening
        self.update_time()

    def create_menus(self):
        """Creates the menu bar and actions."""
        menubar = self.menuBar()

        # File -> Exit (atalho Ctrl+Q)
        file_menu = menubar.addMenu("&File")
        sair_action = QAction("&Exit", self)
        sair_action.setShortcut("Ctrl+Q")
        sair_action.triggered.connect(self.close)
        file_menu.addAction(sair_action)

        # View -> Show Seconds (checável)
        view_menu = menubar.addMenu("&View")
        self.toggle_seconds_action = QAction("Show &Seconds", self, checkable=True)
        self.toggle_seconds_action.setChecked(True)
        # When the user toggles this action we call toggle_seconds
        self.toggle_seconds_action.triggered.connect(self.toggle_seconds)
        view_menu.addAction(self.toggle_seconds_action)

        # Help -> About
        help_menu = menubar.addMenu("&Help")
        about_action = QAction("&About", self)
        about_action.triggered.connect(self.show_about)
        help_menu.addAction(about_action)

    def update_time(self):
        """Gets the current time and updates the label.

        This method is called by the QTimer every second when the clock is running.
        """
        now = datetime.now()
        if self.show_seconds:
            text = now.strftime("%H:%M:%S")
        else:
            text = now.strftime("%H:%M")
        self.time_label.setText(text)

    def toggle_running(self):
        """Toggles between starting and stopping the timer.

        When stopped, the timer no longer calls update_time.
        """
        if self.running:
            self.timer.stop()
            self.start_stop_button.setText("Start")
            self.running = False
        else:
            self.timer.start()
            self.start_stop_button.setText("stop")
            self.running = True
            # Updates immediately when restarted
            self.update_time()

    def toggle_seconds(self, checked):
        """Changes the show_seconds flag when the user toggles the option in the menu."""
        self.show_seconds = bool(checked)
        self.update_time()

    def show_about(self):
        """Mostra uma caixa de diálogo 'About'."""
        from PySide6.QtWidgets import QMessageBox
        QMessageBox.information(self, "About",
                                "Qt Clock\nDisplays hours, minutes and seconds. \nMade with PySide6.")


if __name__ == "__main__":
    # Entry point: create the Qt application and show the main window
    app = QApplication(sys.argv)
    w = ClockMainWindow()
    w.show()
    sys.exit(app.exec())
