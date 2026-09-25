STYLE = """

QWidget {
    background-color: #0b0f14;
    color: #f3f5f7;

    font-family:
        "Segoe UI",
        Arial,
        sans-serif;

    font-size: 14px;
}

QLabel {
    background-color: transparent;
}


/* ========================================================
   AUTENTICAÇÃO
======================================================== */

QFrame#authCard {
    background-color: #111720;

    border: 1px solid #202936;

    border-radius: 14px;
}

QLabel#authTitle {
    color: #f8fafc;

    font-size: 28px;

    font-weight: 700;

    padding: 2px 0px;
}

QLabel#authSubtitle {
    color: #94a3b8;

    font-size: 13px;

    padding: 0px 4px 6px 4px;
}

QLabel#fieldLabel {
    color: #cbd5e1;

    font-size: 13px;

    font-weight: 600;

    padding: 2px 0px 0px 0px;
}


/* ========================================================
   INPUT
======================================================== */

QLineEdit {
    background-color: #0d131b;

    color: #f5f7fa;

    border: 1px solid #263140;

    border-radius: 8px;

    padding: 11px 12px;

    min-height: 20px;

    selection-background-color: #7257ff;
}

QLineEdit:hover {
    border: 1px solid #344255;
}

QLineEdit:focus {
    border: 1px solid #7257ff;

    background-color: #101722;
}

QLineEdit::placeholder {
    color: #5f6b7a;
}


/* ========================================================
   BOTÃO PRINCIPAL
======================================================== */

QPushButton#primaryButton {
    background-color: #7257ff;

    color: white;

    border: none;

    border-radius: 8px;

    padding: 11px 16px;

    font-weight: 600;
}

QPushButton#primaryButton:hover {
    background-color: #826cff;
}

QPushButton#primaryButton:pressed {
    background-color: #6248e8;
}

QPushButton#primaryButton:disabled {
    background-color: #3d3566;

    color: #aaa4c7;
}


/* ========================================================
   LINK
======================================================== */

QPushButton#linkButton {
    background-color: transparent;

    color: #8f9bad;

    border: none;

    padding: 8px;
}

QPushButton#linkButton:hover {
    color: #b9c2ce;
}


/* ========================================================
   SIDEBAR
======================================================== */

QFrame#sidebar {
    background-color: #0e141c;

    border-right: 1px solid #202936;
}

QLabel#sidebarLogo {
    color: white;

    font-size: 21px;

    font-weight: 700;
}


/* ========================================================
   MENU
======================================================== */

QPushButton#navButton,
QPushButton#navButtonActive {
    text-align: left;

    border: none;

    border-radius: 7px;

    padding: 11px 12px;

    font-size: 14px;
}

QPushButton#navButton {
    background-color: transparent;

    color: #8491a3;
}

QPushButton#navButton:hover {
    background-color: #151d28;

    color: white;
}

QPushButton#navButtonActive {
    background-color: #1b2330;

    color: white;

    font-weight: 600;
}


/* ========================================================
   LOGOUT
======================================================== */

QPushButton#logoutButton {
    background-color: transparent;

    color: #7f8b9a;

    border: none;

    text-align: left;

    padding: 10px;
}

QPushButton#logoutButton:hover {
    color: #f3f5f7;
}


/* ========================================================
   DASHBOARD
======================================================== */

QLabel#pageTitle {
    color: white;

    font-size: 28px;

    font-weight: 700;
}

QLabel#pageSubtitle {
    color: #8390a1;

    font-size: 14px;
}

QLabel#sectionTitle {
    color: #f5f7fa;

    font-size: 16px;

    font-weight: 600;
}


/* ========================================================
   CARDS
======================================================== */

QFrame#statCard,
QFrame#contentCard {
    background-color: #111720;

    border: 1px solid #202936;

    border-radius: 10px;
}

QLabel#statTitle {
    color: #8793a4;

    font-size: 13px;
}

QLabel#statValue {
    color: white;

    font-size: 26px;

    font-weight: 700;
}


/* ========================================================
   TABELAS
======================================================== */

QTableWidget {
    background-color: #0e141c;

    alternate-background-color: #101720;

    border: 1px solid #202936;

    border-radius: 7px;

    gridline-color: #1c2531;

    selection-background-color: #252f3d;

    selection-color: white;
}

QTableWidget::item {
    padding: 8px;
}

QHeaderView::section {
    background-color: #141b24;

    color: #919dab;

    border: none;

    border-bottom: 1px solid #202936;

    padding: 10px;

    font-weight: 600;
}

"""

STYLE += """
QPushButton { background: #1c2534; border: 1px solid #303d51; border-radius: 7px; padding: 9px 12px; color: #dee5f0; }
QPushButton:hover { background: #29354a; }
QPushButton:disabled { color: #66738a; }
QComboBox, QSpinBox { background: #111720; border: 1px solid #303d51; border-radius: 6px; padding: 8px; min-height: 22px; }
QComboBox QAbstractItemView { background: #182132; selection-background-color: #7257ff; }
QCheckBox { spacing: 8px; color: #b7c2d4; background: transparent; }
QCheckBox::indicator { width: 16px; height: 16px; border: 1px solid #61708a; border-radius: 4px; background: #141c29; }
QCheckBox::indicator:checked { background: #927aff; border: 2px solid #d0c5ff; }
QStatusBar { color: #aab8cd; background: #0e141c; padding: 5px 12px; border-top: 1px solid #202936; }
QTableWidget::item:selected { background: #302c50; }
QPushButton:focus { border: 1px solid #ad99ff; }
"""
