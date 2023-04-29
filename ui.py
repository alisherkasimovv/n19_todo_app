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
    
    def render_all(self):
        data = self.db.get_all_tasks()
        for row in data:
            self.grid.addWidget()
