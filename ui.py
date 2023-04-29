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

        self.grid = QGridLayout()
        self.render_all()
        self.setLayout(self.grid)
    
    def render_all(self):
        data = self.db.get_all_tasks()

        c = [(x, 0, 1) for x in range(len(data))]

        for row, c in zip(data, c):
            check = QCheckBox()
            check.setText(str(row[0]))
            check.clicked.connect(self.make_done)
            if row[4]:
                check.setChecked(True)
                if row[3] == 0:
                    task.setStyleSheet("font-weight: 700;text-decoration:line-through;")
                else:
                    task.setStyleSheet("color: #333; font-size: 10px;text-decoration:line-through;")
            self.grid.addWidget(check, c[0], c[1])

            task = QLabel(str(row[1]))
            if row[3] == 0:
                task.setStyleSheet("font-weight: 700;")
            else:
                task.setStyleSheet("color: #333; font-size: 10px")

            self.grid.addWidget(task, c[0], c[2])
            
    
    def make_done(self, id):
        sender = self.sender()
        print(sender.text())

        self.db.make_done(int(sender.text()))
        self.grid = QGridLayout()
        self.render_all()
