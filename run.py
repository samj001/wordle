import os,sys,json,math,operator,random
from game import Game
from interface import Interface
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication

def main():

    
    app = QApplication(sys.argv)
    win = Interface()
    win.show()
    sys.exit(app.exec_())

    
    

if __name__ == '__main__':
    main()