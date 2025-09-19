# O que inclui o programa

* Interface Qt (PySide6) compatível com **Windows 10, Ubuntu e macOS**.
* Mostra **horas, minutos e segundos** num `QLabel` grande.
* **Botões**: `Iniciar/Parar` (toggle) e `Sair`.
* **Menu**: `Ficheiro → Sair`, `Ver → Mostrar Segundos` (checável) e `Ajuda → Sobre`.
* Atualização por `QTimer` a cada 1000 ms (1 segundo).
* Código comentado passo a passo dentro do ficheiro (em português) — ver o ficheiro no editor.

# Como executar (rápido)

1. Instale a dependência:

   * `pip install PySide6`
2. Execute:

   * `python relógio_qt.py`  (ou `python3 relógio_qt.py` conforme o seu sistema)

# Explicação passo a passo (resumo)

1. **Importações e configuração** — importa `QApplication`, `QMainWindow`, `QLabel`, `QPushButton`, `QTimer`, etc., e `datetime` para obter a hora do sistema.
2. **Classe principal (`RelogioMainWindow`)** — herda de `QMainWindow` e configura:

   * `time_label`: o widget que mostra a hora (fonte grande, alinhado ao centro).
   * Botões `Iniciar/Parar` e `Sair` num layout horizontal.
   * `create_menus()` constrói a barra de menus com ações (inclui atalho Ctrl+Q para sair).
3. **Timer (`QTimer`)** — disparado a cada segundo, chama `update_time()` que formata `datetime.now()` para `HH:MM:SS` (ou `HH:MM` se decidir ocultar segundos).
4. **Controlo Start/Stop** — o botão alterna o estado do timer; quando parado o timer não chama `update_time`.
5. **Mostrar/Ocultar Segundos** — opção checável no menu que altera a flag `show_seconds` e força atualização.
6. **Sobre** — simples `QMessageBox` com informações da aplicação.

# Dicas rápidas de personalização

* Alterar o tamanho da fonte: no ficheiro mude `font.setPointSize(48)` para outro valor.
* Mudar formato 24h/12h: modifique `strftime("%H:%M:%S")` para usar `%I` e acrescentar ` %p` para AM/PM.
* Adicionar um mostrador analógico: pode criar um `QWidget` personalizado e desenhar com `QPainter`.
* Estética: usar `setStyleSheet()` no `QLabel`/botões para mudar aparência.

# Empacotar para cada OS

* **Windows**: `pyinstaller --onefile --windowed relógio_qt.py` (pode acrescentar ícone).
* **macOS**: `py2app` ou `pyinstaller` com flags adequadas (`--windowed`).
* **Linux**: criar pacote `.deb`/snap/flatpak conforme necessidade; pode usar `pyinstaller` para binário.
