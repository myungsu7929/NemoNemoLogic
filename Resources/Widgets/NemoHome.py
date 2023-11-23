import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from functools import partial

#widget_number 0
class NemoHome(QWidget):
    ChildComponents = []

    def __init__(self, main):
        super().__init__()
        self.main = main
        self.go_make_button = QPushButton("문제 만들기")
        self.go_solve_button = QPushButton("문제 풀기")
        
        NemoHome.ChildComponents.append(self.go_make_button)
        NemoHome.ChildComponents.append(self.go_solve_button)
        self.apply_childs()
        self.set_geometries()
        self.set_button_event()
        
    
    def apply_childs(self):
        for comp in NemoHome.ChildComponents:
            comp.setParent(self)

    def set_geometries(self):
        self.go_make_button.setGeometry(30,30, 180,100)
        self.go_solve_button.setGeometry(30,160, 180, 100)
        self.setGeometry(0,0,240,300)

    def set_button_event(self):
        self.go_make_button.clicked.connect(partial(self.main.goto, 1))
        self.go_solve_button.clicked.connect(partial(self.main.goto, 2))



