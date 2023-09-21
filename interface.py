import sys,os,string
from PyQt5 import QtWidgets,QtCore,QtGui
from PyQt5.QtWidgets import QApplication, QMainWindow, QLineEdit
from game import Game

class Interface(QMainWindow):
    def __init__(self):
        super(Interface, self).__init__()
        self.setGeometry(200,100,1100,600)
        self.setWindowTitle("Guess The Word!")
        self.initUI()
        self.current_answer = ""
        self.current_guess = ""
        self.current_game = Game(5)

# Initial Interface. With all labels and buttons defined first
    def initUI(self):
    
    # 【1】 Title and Result section
        self.label_title = QtWidgets.QLabel(self)
        self.label_title.setText("Click the Button and Start A Game!")
        self.label_title.move(50,10)
        self.label_title.setAlignment(QtCore.Qt.AlignCenter)
        self.label_title.setStyleSheet("border:1px solid black")
        self.label_title.resize(250,40)

        self.label_show_result = QtWidgets.QLabel(self)
        self.label_show_result.setStyleSheet("color:red;font-size:28pt;")
        self.label_show_result.resize(600,40)
        self.label_show_result.move(350,10)

    # 【2】 Start Button Section (start 5/6 or show answer)
        self.button_start5 = QtWidgets.QPushButton(self)
        self.button_start5.setText("5-letter word game")
        self.button_start5.resize(150,30)
        self.button_start5.move(50,60)
        self.button_start5.setStyleSheet("background-color:yellow;")
        self.button_start5.clicked.connect(lambda:self.StartGame(5))

        self.button_start6 = QtWidgets.QPushButton(self)
        self.button_start6.setText("6-letter word game")
        self.button_start6.resize(150,30)
        self.button_start6.move(220,60)
        self.button_start6.setStyleSheet("background-color:yellow;")
        self.button_start6.clicked.connect(lambda:self.StartGame(6))

        self.button_answer = QtWidgets.QPushButton(self)
        self.button_answer.setText("Show Answer")
        self.button_answer.resize(100,30)
        self.button_answer.move(400,60)
        self.button_answer.setStyleSheet("background-color:green;color:white;")
        self.button_answer.clicked.connect(lambda:self.ShowAnswer())

    # 【3】 User Guesses Section (6 rows of guess label and user input)
        #guess sections of six trys
        #'Guess X' labels are visible
        #Guess results labels are created, but left blank first
        
        # Guess 1
        self.label_try1 = QtWidgets.QLabel(self)
        self.label_try1.setText("Guess 1:")
        self.label_try1.setStyleSheet("font-size:18pt;")
        self.label_try1.resize(100,50)
        self.label_try1.move(50,150)

        self.label_guess1_letter1 = QtWidgets.QLabel(self)
        self.label_guess1_letter1.resize(35,50)
        self.label_guess1_letter1.move(180,150)

        self.label_guess1_letter2 = QtWidgets.QLabel(self)
        self.label_guess1_letter2.resize(35,50)
        self.label_guess1_letter2.move(220,150)

        self.label_guess1_letter3 = QtWidgets.QLabel(self)
        self.label_guess1_letter3.resize(35,50)
        self.label_guess1_letter3.move(260,150)

        self.label_guess1_letter4 = QtWidgets.QLabel(self)
        self.label_guess1_letter4.resize(35,50)
        self.label_guess1_letter4.move(300,150)

        self.label_guess1_letter5 = QtWidgets.QLabel(self)
        self.label_guess1_letter5.resize(35,50)
        self.label_guess1_letter5.move(340,150)

        self.label_guess1_letter6 = QtWidgets.QLabel(self)
        self.label_guess1_letter6.resize(35,50)
        self.label_guess1_letter6.move(380,150)

        # Guess 2
        self.label_try2 = QtWidgets.QLabel(self)
        self.label_try2.setText("Guess 2:")
        self.label_try2.setStyleSheet("font-size:18pt;")
        self.label_try2.resize(100,50)
        self.label_try2.move(50,180)

        self.label_guess2_letter1 = QtWidgets.QLabel(self)
        self.label_guess2_letter1.resize(35,50)
        self.label_guess2_letter1.move(180,180)

        self.label_guess2_letter2 = QtWidgets.QLabel(self)
        self.label_guess2_letter2.resize(35,50)
        self.label_guess2_letter2.move(220,180)

        self.label_guess2_letter3 = QtWidgets.QLabel(self)
        self.label_guess2_letter3.resize(35,50)
        self.label_guess2_letter3.move(260,180)

        self.label_guess2_letter4 = QtWidgets.QLabel(self)
        self.label_guess2_letter4.resize(35,50)
        self.label_guess2_letter4.move(300,180)

        self.label_guess2_letter5 = QtWidgets.QLabel(self)
        self.label_guess2_letter5.resize(35,50)
        self.label_guess2_letter5.move(340,180)

        self.label_guess2_letter6 = QtWidgets.QLabel(self)
        self.label_guess2_letter6.resize(35,50)
        self.label_guess2_letter6.move(380,180)


        # Guess 3
        self.label_try3 = QtWidgets.QLabel(self)
        self.label_try3.setText("Guess 3:")
        self.label_try3.setStyleSheet("font-size:18pt;")
        self.label_try3.resize(100,50)
        self.label_try3.move(50,210)

        self.label_guess3_letter1 = QtWidgets.QLabel(self)
        self.label_guess3_letter1.resize(35,50)
        self.label_guess3_letter1.move(180,210)

        self.label_guess3_letter2 = QtWidgets.QLabel(self)
        self.label_guess3_letter2.resize(35,50)
        self.label_guess3_letter2.move(220,210)

        self.label_guess3_letter3 = QtWidgets.QLabel(self)
        self.label_guess3_letter3.resize(35,50)
        self.label_guess3_letter3.move(260,210)

        self.label_guess3_letter4 = QtWidgets.QLabel(self)
        self.label_guess3_letter4.resize(35,50)
        self.label_guess3_letter4.move(300,210)

        self.label_guess3_letter5 = QtWidgets.QLabel(self)
        self.label_guess3_letter5.resize(35,50)
        self.label_guess3_letter5.move(340,210)

        self.label_guess3_letter6 = QtWidgets.QLabel(self)
        self.label_guess3_letter6.resize(35,50)
        self.label_guess3_letter6.move(380,210)

        # Guess 4
        self.label_try4 = QtWidgets.QLabel(self)
        self.label_try4.setText("Guess 4:")
        self.label_try4.setStyleSheet("font-size:18pt;")
        self.label_try4.resize(100,50)
        self.label_try4.move(50,240)

        self.label_guess4_letter1 = QtWidgets.QLabel(self)
        self.label_guess4_letter1.resize(35,50)
        self.label_guess4_letter1.move(180,240)

        self.label_guess4_letter2 = QtWidgets.QLabel(self)
        self.label_guess4_letter2.resize(35,50)
        self.label_guess4_letter2.move(220,240)

        self.label_guess4_letter3 = QtWidgets.QLabel(self)
        self.label_guess4_letter3.resize(35,50)
        self.label_guess4_letter3.move(260,240)

        self.label_guess4_letter4 = QtWidgets.QLabel(self)
        self.label_guess4_letter4.resize(35,50)
        self.label_guess4_letter4.move(300,240)

        self.label_guess4_letter5 = QtWidgets.QLabel(self)
        self.label_guess4_letter5.resize(35,50)
        self.label_guess4_letter5.move(340,240)

        self.label_guess4_letter6 = QtWidgets.QLabel(self)
        self.label_guess4_letter6.resize(35,50)
        self.label_guess4_letter6.move(380,240)


        # Guess 5
        self.label_try5 = QtWidgets.QLabel(self)
        self.label_try5.setText("Guess 5:")
        self.label_try5.setStyleSheet("font-size:18pt;")
        self.label_try5.resize(100,50)
        self.label_try5.move(50,270)

        self.label_guess5_letter1 = QtWidgets.QLabel(self)
        self.label_guess5_letter1.resize(35,50)
        self.label_guess5_letter1.move(180,270)

        self.label_guess5_letter2 = QtWidgets.QLabel(self)
        self.label_guess5_letter2.resize(35,50)
        self.label_guess5_letter2.move(220,270)

        self.label_guess5_letter3 = QtWidgets.QLabel(self)
        self.label_guess5_letter3.resize(35,50)
        self.label_guess5_letter3.move(260,270)

        self.label_guess5_letter4 = QtWidgets.QLabel(self)
        self.label_guess5_letter4.resize(35,50)
        self.label_guess5_letter4.move(300,270)

        self.label_guess5_letter5 = QtWidgets.QLabel(self)
        self.label_guess5_letter5.resize(35,50)
        self.label_guess5_letter5.move(340,270)
        
        self.label_guess5_letter6 = QtWidgets.QLabel(self)
        self.label_guess5_letter6.resize(35,50)
        self.label_guess5_letter6.move(380,270)


        # Guess 6
        self.label_try6 = QtWidgets.QLabel(self)
        self.label_try6.setText("Guess 6:")
        self.label_try6.setStyleSheet("font-size:18pt;")
        self.label_try6.resize(100,50)
        self.label_try6.move(50,300)

        self.label_guess6_letter1 = QtWidgets.QLabel(self)
        self.label_guess6_letter1.resize(35,50)
        self.label_guess6_letter1.move(180,300)

        self.label_guess6_letter2 = QtWidgets.QLabel(self)
        self.label_guess6_letter2.resize(35,50)
        self.label_guess6_letter2.move(220,300)

        self.label_guess6_letter3 = QtWidgets.QLabel(self)
        self.label_guess6_letter3.resize(35,50)
        self.label_guess6_letter3.move(260,300)

        self.label_guess6_letter4 = QtWidgets.QLabel(self)
        self.label_guess6_letter4.resize(35,50)
        self.label_guess6_letter4.move(300,300)

        self.label_guess6_letter5 = QtWidgets.QLabel(self)
        self.label_guess6_letter5.resize(35,50)
        self.label_guess6_letter5.move(340,300)

        self.label_guess6_letter6 = QtWidgets.QLabel(self)
        self.label_guess6_letter6.resize(35,50)
        self.label_guess6_letter6.move(380,300)

        # two dictionary, of six labels and six guess results  
        self.labels = {"self.label_try1":self.label_try1,"self.label_try2":self.label_try2,"self.label_try3":self.label_try3,"self.label_try4":self.label_try4,"self.label_try5":self.label_try5,"self.label_try6":self.label_try6}
        self.results = {"self.label_guess1_letter1":self.label_guess1_letter1,"self.label_guess1_letter2":self.label_guess1_letter2,"self.label_guess1_letter3":self.label_guess1_letter3,"self.label_guess1_letter4":self.label_guess1_letter4,"self.label_guess1_letter5":self.label_guess1_letter5,"self.label_guess1_letter6":self.label_guess1_letter6,\
                        "self.label_guess2_letter1":self.label_guess2_letter1,"self.label_guess2_letter2":self.label_guess2_letter2,"self.label_guess2_letter3":self.label_guess2_letter3,"self.label_guess2_letter4":self.label_guess2_letter4,"self.label_guess2_letter5":self.label_guess2_letter5,"self.label_guess2_letter6":self.label_guess2_letter6,\
                        "self.label_guess3_letter1":self.label_guess3_letter1,"self.label_guess3_letter2":self.label_guess3_letter2,"self.label_guess3_letter3":self.label_guess3_letter3,"self.label_guess3_letter4":self.label_guess3_letter4,"self.label_guess3_letter5":self.label_guess3_letter5,"self.label_guess3_letter6":self.label_guess3_letter6,\
                        "self.label_guess4_letter1":self.label_guess4_letter1,"self.label_guess4_letter2":self.label_guess4_letter2,"self.label_guess4_letter3":self.label_guess4_letter3,"self.label_guess4_letter4":self.label_guess4_letter4,"self.label_guess4_letter5":self.label_guess4_letter5,"self.label_guess4_letter6":self.label_guess4_letter6,\
                        "self.label_guess5_letter1":self.label_guess5_letter1,"self.label_guess5_letter2":self.label_guess5_letter2,"self.label_guess5_letter3":self.label_guess5_letter3,"self.label_guess5_letter4":self.label_guess5_letter4,"self.label_guess5_letter5":self.label_guess5_letter5,"self.label_guess5_letter6":self.label_guess5_letter6,\
                        "self.label_guess6_letter1":self.label_guess6_letter1,"self.label_guess6_letter2":self.label_guess6_letter2,"self.label_guess6_letter3":self.label_guess6_letter3,"self.label_guess6_letter4":self.label_guess6_letter4,"self.label_guess6_letter5":self.label_guess6_letter5,"self.label_guess6_letter6":self.label_guess6_letter6}

    # 【4】 Keyboard Section
        self.button_letterA = QtWidgets.QPushButton(self)
        self.button_letterA.setText("A")
        self.button_letterA.setStyleSheet("background-color:black;color:white;font-size:18pt;")
        self.button_letterA.resize(35,35)
        self.button_letterA.move(50,400)
        #self.button_letterA.clicked.connect(self.key_clicked)

        self.button_letterB = QtWidgets.QPushButton(self)
        self.button_letterB.setText("B")
        self.button_letterB.setStyleSheet("background-color:black;color:white;font-size:18pt;")
        self.button_letterB.resize(35,35)
        self.button_letterB.move(100,400)
        #self.button_letterB.clicked.connect(self.key_clicked)

        self.button_letterC = QtWidgets.QPushButton(self)
        self.button_letterC.setText("C")
        self.button_letterC.setStyleSheet("background-color:black;color:white;font-size:18pt;")
        self.button_letterC.resize(35,35)
        self.button_letterC.move(150,400)
        #self.button_letterC.clicked.connect(self.key_clicked)

        self.button_letterD = QtWidgets.QPushButton(self)
        self.button_letterD.setText("D")
        self.button_letterD.setStyleSheet("background-color:black;color:white;font-size:18pt;")
        self.button_letterD.resize(35,35)
        self.button_letterD.move(200,400)
        #self.button_letterD.clicked.connect(self.key_clicked)

        self.button_letterE = QtWidgets.QPushButton(self)
        self.button_letterE.setText("E")
        self.button_letterE.setStyleSheet("background-color:black;color:white;font-size:18pt;")
        self.button_letterE.resize(35,35)
        self.button_letterE.move(250,400)
        #self.button_letterE.clicked.connect(self.key_clicked)

        self.button_letterF = QtWidgets.QPushButton(self)
        self.button_letterF.setText("F")
        self.button_letterF.setStyleSheet("background-color:black;color:white;font-size:18pt;")
        self.button_letterF.resize(35,35)
        self.button_letterF.move(300,400)
        #self.button_letterF.clicked.connect(self.key_clicked)

        self.button_letterG = QtWidgets.QPushButton(self)
        self.button_letterG.setText("G")
        self.button_letterG.setStyleSheet("background-color:black;color:white;font-size:18pt;")
        self.button_letterG.resize(35,35)
        self.button_letterG.move(350,400)
        #self.button_letterG.clicked.connect(self.key_clicked)

        self.button_letterH = QtWidgets.QPushButton(self)
        self.button_letterH.setText("H")
        self.button_letterH.setStyleSheet("background-color:black;color:white;font-size:18pt;")
        self.button_letterH.resize(35,35)
        self.button_letterH.move(400,400)
        #self.button_letterH.clicked.connect(self.key_clicked)

        self.button_letterI = QtWidgets.QPushButton(self)
        self.button_letterI.setText("I")
        self.button_letterI.setStyleSheet("background-color:black;color:white;font-size:18pt;")
        self.button_letterI.resize(35,35)
        self.button_letterI.move(450,400)
        #self.button_letterI.clicked.connect(self.key_clicked)

        self.button_letterJ = QtWidgets.QPushButton(self)
        self.button_letterJ.setText("J")
        self.button_letterJ.setStyleSheet("background-color:black;color:white;font-size:18pt;")
        self.button_letterJ.resize(35,35)
        self.button_letterJ.move(500,400)
        #self.button_letterJ.clicked.connect(self.key_clicked)

        self.button_letterK = QtWidgets.QPushButton(self)
        self.button_letterK.setText("K")
        self.button_letterK.setStyleSheet("background-color:black;color:white;font-size:18pt;")
        self.button_letterK.resize(35,35)
        self.button_letterK.move(82,450)
        #self.button_letterK.clicked.connect(self.key_clicked)

        self.button_letterL = QtWidgets.QPushButton(self)
        self.button_letterL.setText("L")
        self.button_letterL.setStyleSheet("background-color:black;color:white;font-size:18pt;")
        self.button_letterL.resize(35,35)
        self.button_letterL.move(132,450)
        #self.button_letterL.clicked.connect(self.key_clicked)

        self.button_letterM = QtWidgets.QPushButton(self)
        self.button_letterM.setText("M")
        self.button_letterM.setStyleSheet("background-color:black;color:white;font-size:18pt;")
        self.button_letterM.resize(35,35)
        self.button_letterM.move(182,450)
        #self.button_letterM.clicked.connect(self.key_clicked)

        self.button_letterN = QtWidgets.QPushButton(self)
        self.button_letterN.setText("N")
        self.button_letterN.setStyleSheet("background-color:black;color:white;font-size:18pt;")
        self.button_letterN.resize(35,35)
        self.button_letterN.move(232,450)
        #self.button_letterN.clicked.connect(self.key_clicked)

        self.button_letterO = QtWidgets.QPushButton(self)
        self.button_letterO.setText("O")
        self.button_letterO.setStyleSheet("background-color:black;color:white;font-size:18pt;")
        self.button_letterO.resize(35,35)
        self.button_letterO.move(282,450)
        #self.button_letterO.clicked.connect(self.key_clicked)

        self.button_letterP = QtWidgets.QPushButton(self)
        self.button_letterP.setText("P")
        self.button_letterP.setStyleSheet("background-color:black;color:white;font-size:18pt;")
        self.button_letterP.resize(35,35)
        self.button_letterP.move(332,450)
        #self.button_letterP.clicked.connect(self.key_clicked)

        self.button_letterQ = QtWidgets.QPushButton(self)
        self.button_letterQ.setText("Q")
        self.button_letterQ.setStyleSheet("background-color:black;color:white;font-size:18pt;")
        self.button_letterQ.resize(35,35)
        self.button_letterQ.move(382,450)
        #self.button_letterQ.clicked.connect(self.key_clicked)

        self.button_letterR = QtWidgets.QPushButton(self)
        self.button_letterR.setText("R")
        self.button_letterR.setStyleSheet("background-color:black;color:white;font-size:18pt;")
        self.button_letterR.resize(35,35)
        self.button_letterR.move(432,450)
        #self.button_letterR.clicked.connect(self.key_clicked)

        self.button_letterS = QtWidgets.QPushButton(self)
        self.button_letterS.setText("S")
        self.button_letterS.setStyleSheet("background-color:black;color:white;font-size:18pt;")
        self.button_letterS.resize(35,35)
        self.button_letterS.move(482,450)
        #self.button_letterS.clicked.connect(self.key_clicked)

        self.button_letterT = QtWidgets.QPushButton(self)
        self.button_letterT.setText("T")
        self.button_letterT.setStyleSheet("background-color:black;color:white;font-size:18pt;")
        self.button_letterT.resize(35,35)
        self.button_letterT.move(132,500)
        #self.button_letterT.clicked.connect(self.key_clicked)

        self.button_letterU = QtWidgets.QPushButton(self)
        self.button_letterU.setText("U")
        self.button_letterU.setStyleSheet("background-color:black;color:white;font-size:18pt;")
        self.button_letterU.resize(35,35)
        self.button_letterU.move(182,500)
        #self.button_letterU.clicked.connect(self.key_clicked)

        self.button_letterV = QtWidgets.QPushButton(self)
        self.button_letterV.setText("V")
        self.button_letterV.setStyleSheet("background-color:black;color:white;font-size:18pt;")
        self.button_letterV.resize(35,35)
        self.button_letterV.move(232,500)
        #self.button_letterV.clicked.connect(self.key_clicked)

        self.button_letterW = QtWidgets.QPushButton(self)
        self.button_letterW.setText("W")
        self.button_letterW.setStyleSheet("background-color:black;color:white;font-size:18pt;")
        self.button_letterW.resize(35,35)
        self.button_letterW.move(282,500)
        #self.button_letterW.clicked.connect(self.key_clicked)

        self.button_letterX = QtWidgets.QPushButton(self)
        self.button_letterX.setText("X")
        self.button_letterX.setStyleSheet("background-color:black;color:white;font-size:18pt;")
        self.button_letterX.resize(35,35)
        self.button_letterX.move(332,500)
        #self.button_letterX.clicked.connect(self.key_clicked)

        self.button_letterY = QtWidgets.QPushButton(self)
        self.button_letterY.setText("Y")
        self.button_letterY.setStyleSheet("background-color:black;color:white;font-size:18pt;")
        self.button_letterY.resize(35,35)
        self.button_letterY.move(382,500)
        #self.button_letterY.clicked.connect(self.key_clicked)

        self.button_letterZ = QtWidgets.QPushButton(self)
        self.button_letterZ.setText("Z")
        self.button_letterZ.setStyleSheet("background-color:black;color:white;font-size:18pt;")
        self.button_letterZ.resize(35,35)
        self.button_letterZ.move(432,500)
        #self.button_letterZ.clicked.connect(self.key_clicked)
    
        #set a dictionary of buttons in keyboard section
        self.button_letters_dict = {"self.button_letterA":self.button_letterA,\
                               "self.button_letterB":self.button_letterB,\
                               "self.button_letterC":self.button_letterC,\
                               "self.button_letterD":self.button_letterD,\
                               "self.button_letterE":self.button_letterE,\
                               "self.button_letterF":self.button_letterF,\
                               "self.button_letterG":self.button_letterG,\
                               "self.button_letterH":self.button_letterH,\
                               "self.button_letterI":self.button_letterI,\
                               "self.button_letterJ":self.button_letterJ,\
                               "self.button_letterK":self.button_letterK,\
                               "self.button_letterL":self.button_letterL,\
                               "self.button_letterM":self.button_letterM,\
                               "self.button_letterN":self.button_letterN,\
                               "self.button_letterO":self.button_letterO,\
                               "self.button_letterP":self.button_letterP,\
                               "self.button_letterQ":self.button_letterQ,\
                               "self.button_letterR":self.button_letterR,\
                               "self.button_letterS":self.button_letterS,\
                               "self.button_letterT":self.button_letterT,\
                               "self.button_letterU":self.button_letterU,\
                               "self.button_letterV":self.button_letterV,\
                               "self.button_letterW":self.button_letterW,\
                               "self.button_letterX":self.button_letterX,\
                               "self.button_letterY":self.button_letterY,\
                               "self.button_letterZ":self.button_letterZ}

    # 【5】 Hint Section
        self.label_hint1 = QtWidgets.QLabel(self)
        self.label_hint1.setText("Green: RIGHT letter, RIGHT position")
        self.label_hint1.move(600,100)
        self.label_hint1.resize(350,40)
        self.label_hint1.setStyleSheet("font-size: 18pt;color:green;border:1px solid green;")
        
        self.label_hint2 = QtWidgets.QLabel(self)
        self.label_hint2.setText("Orange: RIGHT letter, WRONG position")
        self.label_hint2.move(600,150)
        self.label_hint2.setStyleSheet("font-size:18pt;color:orange;border:1px solid orange;")
        self.label_hint2.resize(350,40)

        self.label_hint3 = QtWidgets.QLabel(self)
        self.label_hint3.setText("Gray: WRONG letter, WRONG position")
        self.label_hint3.move(600,200)
        self.label_hint3.setStyleSheet("border:1px solid gray;color:gray;font-size:18pt;")
        self.label_hint3.resize(350,40)

        self.label_hint4 = QtWidgets.QLabel(self)
        #self.label_hint4.setText("Gray: WRONG letter, WRONG position")
        self.label_hint4.move(600,250)
        self.label_hint4.setStyleSheet("color:red;font-size:18pt;")
        self.label_hint4.resize(350,40)


# Methods
    def StartGame(self,length):

    # Clear former guesses first

        # Clear hint sections
        self.label_show_result.setText("")
        self.label_hint4.setText("")
        
        # Clear guess section
        for i in range(6):
            for k in range(6):
                label_name = f"self.label_guess{i+1}_letter{k+1}"
                self.results[label_name].setText("")
        
        # Clear keyboard section
        for i in range(26):
            letter_list = list(string.ascii_uppercase)
            target_label = f"self.button_letter{letter_list[i]}"
            self.button_letters_dict[target_label].setStyleSheet(f"color:white;background-color:black;font-size:18pt;")

        
    # Create a new Game Instance 
        
        new_game = Game(length)
        
        self.current_game = new_game
        self.current_answer = new_game.answer

        self.label_hint = QtWidgets.QLabel(self)
        self.label_hint.setText(f"Input your guess, and press enter:")
        self.label_hint.setStyleSheet("font-size:15pt;color:black;")
        self.label_hint.resize(300,50)
        self.label_hint.move(50,110)

        self.textbox1 = QLineEdit(self)
        self.textbox1.setPlaceholderText(f"Word of {length} letters. No repeating letter.")
        self.textbox1.move(300,120)
        self.textbox1.resize(250,30)
        self.label_hint.show()
        self.textbox1.show()

        self.textbox1.returnPressed.connect(lambda:self.ProcessInput())



    def ProcessInput(self):

        if self.current_game.end == True:
            self.textbox1.setEnabled(False)
            self.label_show_result.setText("Click button to restart or Exit")

        
        else:
            self.current_guess = self.textbox1.text()
            self.textbox1.clear()

            user_guess = self.current_guess

            self.label_hint4.setText("")
            guess_result,letter_result = self.current_game.HandleInput(user_guess)

            if guess_result == "NotLegitWord":
                self.current_game.chances += 1
                self.label_hint4.setText("Not a legit word! Try Again!")
                
            
            elif guess_result == "NotRightLength":
                self.label_hint4.setText("Not right length! Try Again!")
                

            else:
                self.ShowGuessResult(user_guess,letter_result,6-self.current_game.chances)
                self.ChangeBoxColor(user_guess,letter_result,18)

                if guess_result == "RightGuess":
                    self.label_show_result.setText("You Win!!!!!Click button to restart or Exit")                
                    for i in range(6):
                        for k in range(6):
                            label_name = f"self.label_guess{i+1}_letter{k+1}"
                            self.results[label_name].setText("")

       

    def ShowAnswer(self):
        if self.current_answer == "":
            self.label_show_result.setText(f"Game not start yet! Click button to start or exit")
        else:
            self.label_show_result.setText(f"Right answer: {self.current_answer}. Click button to restart or Exit")
        self.current_game.end = True
    
    def ChangeLabelText(self,label,text):
        return label.setText(text)

    
    def ChangeBoxColor(self,user_guess,letter_result,targe_size):
        letter_color = []

        for i in range(len(user_guess)):
            if letter_result[i] == "W":
                letter_color.append("grey")
            if letter_result[i] == "R":
                letter_color.append("green")
            if letter_result[i] == "P":
                letter_color.append("orange")

        for i in range(len(letter_result)):
            if letter_result[i] != "green":
                target_label = "self.button_letter"+user_guess[i].upper()
                self.button_letters_dict[target_label].setStyleSheet(f"color:white;background-color:{letter_color[i]};font-size:{targe_size}pt;")


    
    def ShowGuessResult(self,user_guess,letter_result,guess_time):
        letter_color = []

        for i in range(len(user_guess)):
            if letter_result[i] == "W":
                letter_color.append("grey")
            if letter_result[i] == "R":
                letter_color.append("green")
            if letter_result[i] == "P":
                letter_color.append("orange")
        
        if len(user_guess) == 5:
            for i in range(5):
                label_name = f"self.label_guess{guess_time}_letter{i+1}"
                self.ChangeLabelText(self.results[label_name],user_guess[i])
    
                style_string = f"font-size:18pt;color:{letter_color[i]}"
                self.results[label_name].setStyleSheet(style_string)
        
        if len(user_guess) == 6:
            for i in range(6):
                label_name = f"self.label_guess{guess_time}_letter{i+1}"
                self.ChangeLabelText(self.results[label_name],user_guess[i])
                #self.results[label_name].setText[user_guess[i]]
                style_string = f"font-size:18pt;color:{letter_color[i]}"
                self.results[label_name].setStyleSheet(style_string)
        







