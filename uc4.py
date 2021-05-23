import sys
from PyQt5.QtWidgets import (QWidget, QGridLayout,QPushButton, QApplication)
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *

class MyWindow(QWidget):
    def __init__(self, symptomsList):
        super().__init__()
        self.setWindowTitle("SEARCH DISEASE")
        self.setGeometry(300,300,600,400)

        #x축위치 y축위치, 넓이, 높이
        # label
        symptomsStr = ','.join(map(str,symptomsList))
        self.label = QLabel("선택된 증상: "+symptomsStr, self)
        self.label.move(10, 10)
        self.label.resize(500, 30)

        # button
        self.btn = QPushButton("뒤로가기", self)
        self.btn.setStyleSheet(
            "color: white;"
            "background-color: rgb(58, 134, 255);"
            "border-radius: 20px;"
        )
        self.btn.move(500, 10)

        self.btn.resize(80, 30)
        self.btn.clicked.connect(self.btn_clicked)

        grid = QGridLayout()
        self.setLayout(grid)

        names = ['상기도 감염', '인플루엔자', '신종플루', '폐렴', '감기',
                 '급성 호흡기 증후군', '코로나', '과제', '하기', '시러어어ㅓㅓ어어']

        for i, name in enumerate(names):
            button = QPushButton(self.breakName(name), self)
            button.setStyleSheet(
                "color: rgb(58, 134, 255);"
                "background-color: white;"
                "border: 2px solid rgb(58, 134, 255);"
                "border-radius: 5px;"
                "width: 100px;"
                "height: 100px;"
            )
            button.resize(100,100)
            button.clicked.connect(self.make_calluser(name))
            row, col = divmod(i, 5)
            grid.addWidget(button, row, col, 1, 1)
           
    def breakName(self, name):
        if(len(name)>6):
            name = name[:6]+'\n'+name[6:]
        return name
    
    def btn_clicked(self):
        self.close()

    def make_calluser(self, name):
        def calluser():
            print(name)
            self.windowExample2 = MyWindow2(name)
            self.windowExample2.show()
        return calluser

class MyWindow2(QWidget):
    def __init__(self, diseaseName):
        super().__init__()
        self.setWindowTitle("DISEASE INFO")
        self.setGeometry(300,300,600,400)

        #x축위치 y축위치, 넓이, 높이
        self.button = QPushButton(diseaseName, self)
        self.button.setStyleSheet(
                "color: rgb(58, 134, 255);"
                "background-color: white;"
                "border: 2px solid rgb(58, 134, 255);"
                "border-radius: 5px;"
                "width: 100px;"
                "height: 100px;"
            )
        self.button.move(10,10)
        # label
        self.label = QLabel("질병이름: "+diseaseName, self)
        self.label.move(150, 10)
        self.label.resize(400, 30)

        # button
        self.btn = QPushButton("뒤로가기", self)
        self.btn.setStyleSheet(
            "color: white;"
            "background-color: rgb(58, 134, 255);"
            "border-radius: 20px;"
        )
        self.btn.move(500, 10)
        self.btn.resize(80, 30)
        self.btn.clicked.connect(self.btn_clicked)

        # label
        self.label = QLabel("증상: "+"코로나바이러스감염증(코로나19)은 새롭게 발견된 코로나바이러스로 인해 발생하는 감염 질환입니다.코로나19에 감염되면 대부분 경증에서 중증 수준의 증상을 보이며 특별한 치료 없이도 질환으로부터 회복합니다.", self)
        self.label.setWordWrap(True)
        self.label.move(150, 50)
        self.label.resize(400, 100)

    
    def btn_clicked(self):
        self.close()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    windowExample = MyWindow(["두통","피곤함","졸림"])
    #windowExample2 = MyWindow2("코로나")
    windowExample.show()
    #windowExample2.show()
    sys.exit(app.exec_())