import typing
from PyQt6 import QtCore
from PyQt6.QtWidgets import *
from sys import exit

from PyQt6.QtWidgets import QWidget
from db import Database


class MainWindow (QWidget):
    def __init__(self) -> None:
        super().__init__()
        self.db = Database()

        self.grid = QVBoxLayout()
        self.render_all()
        self.setLayout(self.grid)
    
    def render_all(self):
        data = self.db.get_all_tasks()

        for row in data:
            check = QCheckBox()
            check.clicked.connect(self.make_done)
            check.setText(str(row[0]) + ". " + row[1])
            if row[4] == 1:
                check.setChecked(True)
                check.setStyleSheet("text-decoration:line-through;")
                check.setCheckable(False)
            self.grid.addWidget(check)
            
            
    
    def make_done(self):
        sender = self.sender()

        self.db.make_done(int(sender.text().split(".")[0]))
        sender.setStyleSheet("text-decoration:line-through;")
        sender.setCheckable(False)
