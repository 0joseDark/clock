#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Relógio simples com Qt (PySide6)
Exibe horas, minutos e segundos.
Inclui menu e botões (Iniciar/Parar, Sair) e opção no menu para mostrar/ocultar segundos.

Compatível com: Windows 10, Ubuntu (Linux) e macOS.
Dependência: PySide6 -> pip install PySide6

Este ficheiro contém comentários passo-a-passo para explicar cada bloco.
"""

import sys
from datetime import datetime
from PySide6.QtWidgets import (QApplication, QMainWindow, QLabel, QPushButton,
                               QWidget, QVBoxLayout, QHBoxLayout, QAction)
from PySide6.QtCore import QTimer, Qt
from PySide6.QtGui import QFont


class RelogioMainWindow(QMainWindow):
    """Janela principal do relógio."""

    def __init__(self):
        super().__init__()
        # Título e tamanho inicial da janela
        self.setWindowTitle("Relógio Qt — Horas, minutos e segundos")
        self.resize(480, 220)

        # --- Estado interno ---
        # Flag que controla se mostramos segundos (True por defeito)
        self.show_seconds = True
        # Flag que indica se o temporizador está a correr
        self.running = True

        # --- Widget central e layout ---
        central = QWidget()
        self.setCentralWidget(central)
        vbox = QVBoxLayout()
        central.setLayout(vbox)

        # --- Rótulo grande para mostrar a hora ---
        # Criamos um QLabel centralizado com fonte grande
        self.time_label = QLabel()
        font = QFont()
        font.setPointSize(48)  # tamanho da fonte — pode ajustar conforme o ecrã
        font.setBold(True)
        self.time_label.setFont(font)
        self.time_label.setAlignment(Qt.AlignCenter)
        vbox.addWidget(self.time_label, stretch=1)

        # --- Botões ---
        # Criamos um layout horizontal com o botão Iniciar/Parar e Sair
        hbox = QHBoxLayout()

        self.start_stop_button = QPushButton("Parar")
        # Ligamos o clique do botão ao método toggle_running
        self.start_stop_button.clicked.connect(self.toggle_running)
        hbox.addWidget(self.start_stop_button)

        self.quit_button = QPushButton("Sair")
        self.quit_button.clicked.connect(self.close)
        hbox.addWidget(self.quit_button)

        vbox.addLayout(hbox)

        # --- Barra de menus ---
        # Criamos um menu com Ficheiro->Sair, Ver->Mostrar Segundos e Ajuda->Sobre
        self.create_menus()

        # --- Timer que atualiza a hora ---
        # O QTimer dispara a cada 1000 ms (1 s) e chama update_time
        self.timer = QTimer(self)
        self.timer.setInterval(1000)
        self.timer.timeout.connect(self.update_time)
        self.timer.start()

        # Atualiza imediatamente para evitar 1 s de espera ao abrir
        self.update_time()

    def create_menus(self):
        """Cria a barra de menus e as ações."""
        menubar = self.menuBar()

        # Ficheiro -> Sair (atalho Ctrl+Q)
        file_menu = menubar.addMenu("&Ficheiro")
        sair_action = QAction("&Sair", self)
        sair_action.setShortcut("Ctrl+Q")
        sair_action.triggered.connect(self.close)
        file_menu.addAction(sair_action)

        # Ver -> Mostrar Segundos (checável)
        view_menu = menubar.addMenu("&Ver")
        self.toggle_seconds_action = QAction("Mostrar &Segundos", self, checkable=True)
        self.toggle_seconds_action.setChecked(True)
        # Quando o utilizador alterna esta ação chamamos toggle_seconds
        self.toggle_seconds_action.triggered.connect(self.toggle_seconds)
        view_menu.addAction(self.toggle_seconds_action)

        # Ajuda -> Sobre
        help_menu = menubar.addMenu("&Ajuda")
        about_action = QAction("&Sobre", self)
        about_action.triggered.connect(self.show_about)
        help_menu.addAction(about_action)

    def update_time(self):
        """Obtém a hora atual e atualiza o rótulo.

        Este método é chamado pelo QTimer a cada segundo quando o relógio está a correr.
        """
        now = datetime.now()
        if self.show_seconds:
            text = now.strftime("%H:%M:%S")
        else:
            text = now.strftime("%H:%M")
        self.time_label.setText(text)

    def toggle_running(self):
        """Alterna entre iniciar e parar o temporizador.

        Quando parado, o temporizador deixa de chamar update_time.
        """
        if self.running:
            self.timer.stop()
            self.start_stop_button.setText("Iniciar")
            self.running = False
        else:
            self.timer.start()
            self.start_stop_button.setText("Parar")
            self.running = True
            # Atualiza imediatamente quando reiniciamos
            self.update_time()

    def toggle_seconds(self, checked):
        """Muda a flag show_seconds quando o utilizador alterna a opção no menu."""
        self.show_seconds = bool(checked)
        self.update_time()

    def show_about(self):
        """Mostra uma caixa de diálogo 'Sobre'."""
        from PySide6.QtWidgets import QMessageBox
        QMessageBox.information(self, "Sobre",
                                "Relógio Qt\nMostra horas, minutos e segundos.\nFeito com PySide6.")


if __name__ == "__main__":
    # Ponto de entrada: criamos a aplicação Qt e mostramos a janela principal
    app = QApplication(sys.argv)
    w = RelogioMainWindow()
    w.show()
    sys.exit(app.exec())
