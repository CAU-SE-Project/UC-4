# -*- coding: utf-8 -*-
import sys
from PyQt5.QtWidgets import (QWidget, QGridLayout,QPushButton, QApplication)
from PyQt5 import QtCore, QtWidgets
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
import HospitalFinder

class DevCtrl(QWidget):
    def __init__(self, symptomsList, diseaseList, controller):
        super().__init__()
        self.Controller = controller
        self.setWindowTitle("SEARCH DISEASE")
        self.setGeometry(300,100,1200,800)
    
        self.layout = QtWidgets.QHBoxLayout(self)
        self.scrollArea = QtWidgets.QScrollArea(self)
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.gridLayout = QtWidgets.QGridLayout(self.scrollAreaWidgetContents)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.layout.addWidget(self.scrollArea)
        
        #x축위치 y축위치, 넓이, 높이
        # label
        symptomsStr = ','.join(map(str,symptomsList))
        self.label = QLabel("선택된 증상: "+symptomsStr, self)
        self.label.move(20, 20)
        self.label.resize(500, 30)
        #self.gridLayout.addWidget(self.label, 1, 0, 1, 1)

        # button
        self.btn = QPushButton("뒤로가기", self)
        self.btn.setStyleSheet(
            "color: white;"
            "background-color: rgb(58, 134, 255);"
            "border-radius: 3px;"
        )
        self.btn.resize(90, 35)
        self.btn.move(1100, 10)

        self.btn.clicked.connect(self.btn_clicked)

        names = diseaseList

        for i, name in enumerate(names):
            button = QPushButton(self.breakName(name), self)
            button.setStyleSheet(
                "color: rgb(58, 134, 255);"
                "background-color: white;"
                "border: 2px solid rgb(58, 134, 255);"
                "border-radius: 5px;"
                "font-size: 18px;"
                "width: 200px;"
                "height: 200px;"
                "margin-top: 10px;"
                "margin-left: 10px;"
            )
            button.resize(100,100)
            button.clicked.connect(self.make_calluser(name))
            row, col = divmod(i, 4)
            self.gridLayout.addWidget(button, row+2, col, 1, 1)
           
    def breakName(self, name):
        n = 20
        list = []
        b = name.find('(')
        if(b != -1): 
            first = name[:b]
            for j in range(0, len(first), 10):
                list.append(first[j:j+10])
            name = name[b:]

        for i in range(0, len(name), n):
            list.append(name[i:i+n])
        return '\n'.join(list)
    
    def btn_clicked(self):
        self.close()

    def make_calluser(self, name):
        def calluser():
            print(name)
            self.Controller.selectDisease(name)
            #self.windowExample2 = DevCtrl2(name)
            #self.windowExample2.show()
        return calluser

class DevCtrl2(QWidget):
    def __init__(self, diseaseName, tempDiseaseInfo):
        super().__init__()
        self.setWindowTitle("DISEASE INFO")
        self.setGeometry(300,100,1200,800)

        self.layout = QtWidgets.QHBoxLayout(self)
        self.scrollArea = QtWidgets.QScrollArea(self)
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.gridLayout = QtWidgets.QGridLayout(self.scrollAreaWidgetContents)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.layout.addWidget(self.scrollArea)

        #self.gridLayout = QGridLayout()
        #self.setLayout(self.gridLayout)

        #x축위치 y축위치, 넓이, 높이
        self.button = QPushButton(self.breakName(diseaseName), self)
        self.button.setStyleSheet(
                "color: rgb(58, 134, 255);"
                "background-color: white;"
                "border: 2px solid rgb(58, 134, 255);"
                "border-radius: 5px;"
                "width: 200px;"
                "height: 200px;"
                "font-size: 18px;"
                "margin-top: 10px;"
                "margin-left: 10px;"
            )
        self.button.move(10,10)
        self.gridLayout.addWidget(self.button, 1, 1, 2, 2)

        selectedDiseaseInfo = {}  # 병명, 진료과 저장
        selectedDiseaseInfo['병명'] = diseaseName
        for diseaseinfo in tempDiseaseInfo:
            if diseaseinfo == "진료과":
                selectedDiseaseInfo[diseaseinfo] = tempDiseaseInfo[diseaseinfo]

        if("진료과" in selectedDiseaseInfo):
            self.btn = QPushButton("진료받기", self)
            self.btn.setStyleSheet(
                "color: white;"
                "background-color: rgb(58, 134, 255);"
                "border-radius: 5px;"
                "height: 30px;"
                "margin-left: 20px;"
                "margin-right: 10px;"
            )
            self.gridLayout.addWidget(self.btn, 3, 1, 1, 2)
            self.btn.clicked.connect(self.make_calluser(selectedDiseaseInfo))

        # button
        self.btn = QPushButton("뒤로가기", self)
        self.btn.setStyleSheet(
            "color: white;"
            "background-color: rgb(58, 134, 255);"
            "border-radius: 3px;"
        )
        self.btn.resize(90, 35)
        self.btn.move(1100, 10)
        self.btn.clicked.connect(self.btn_clicked)
        #self.gridLayout.addWidget(self.btn, 1, 12, 1, 1)

        findkeys = ["정의", "원인", "증상", "진단", "치료", "경과", "주의사항", "진료과", "관련질환"]
        keys = list(tempDiseaseInfo.keys())
        for k in keys:
            if(k not in findkeys): keys.remove(k)

        key = keys[0]
        self.label = QLabel(key+": "+tempDiseaseInfo[key], self)
        self.label.setWordWrap(True)
        self.label.setStyleSheet(
                    "margin-top: 20px;"
                    "margin-bottom: 20px;"
                    "margin-left: 10px;"
                )
        self.gridLayout.addWidget(self.label, 1, 3, 1, 8)

        for i in range(1,len(keys)):
            if(keys[i] in tempDiseaseInfo):
                key = keys[i]
                self.label = QLabel(key+": "+tempDiseaseInfo[key], self)
                self.label.setWordWrap(True)
                self.label.setStyleSheet(
                    "margin-bottom: 20px;"
                    "margin-left: 10px;"
                )
                self.gridLayout.addWidget(self.label, 1+i, 3, 1, 9)
                
    def breakName(self, name):
        n = 20
        list = []
        b = name.find('(')
        if(b != -1): 
            first = name[:b]
            for j in range(0, len(first), 10):
                list.append(first[j:j+10])
            name = name[b:]
            
        for i in range(0, len(name), n):
            list.append(name[i:i+n])
        return '\n'.join(list)
    
    def btn_clicked(self):
        self.close()

    def make_calluser(self, DiseaseInfo):
        def calluser():
            print(DiseaseInfo)
            self.windowExample3 = DevCtrl3(DiseaseInfo)
            self.windowExample3.show()
        return calluser

class DevCtrl3(QWidget):
    def __init__(self, DiseaseInfo):
        super().__init__()
        self.setWindowTitle("GET TREATMENT")
        self.setGeometry(400,200,300,180)
        
        self.label = QLabel("병명: "+DiseaseInfo["병명"], self)
        self.label.setWordWrap(True)
        self.label.move(20, 20)
        self.label.resize(260, 30)

        self.label = QLabel("진료과: "+DiseaseInfo["진료과"], self)
        self.label.setWordWrap(True)
        self.label.move(20, 60)
        self.label.resize(260, 30)

        self.btn = QPushButton("대면", self)
        self.btn.setStyleSheet(
            "color: white;"
            "background-color: rgb(58, 134, 255);"
            "border-radius: 3px;"
        )
        self.btn.move(50, 110)
        self.btn.resize(80, 30)
        self.btn.clicked.connect(self.make_calluser(DiseaseInfo, "offline"))

        self.btn2 = QPushButton("비대면", self)
        self.btn2.setStyleSheet(
            "color: white;"
            "background-color: rgb(58, 134, 255);"
            "border-radius: 3px;"
        )
        self.btn2.move(180, 110)
        self.btn2.resize(80, 30)
        self.btn2.clicked.connect(self.make_calluser(DiseaseInfo, "online"))
    
    def make_calluser(self, DiseaseInfo, type):
        def calluser():
            print(DiseaseInfo, type)
            if(type == "offline"):
                HospitalFinder.HospitalFinder(DiseaseInfo).FindHospital()
            self.close()
        return calluser

if __name__ == '__main__':
    app = QApplication(sys.argv)
    names = ['상기도 감염', '인플루엔자', '신종플루', '폐렴', '감기',
             '급성 호흡기 증후군', '코로나', '과제', '하기', '시러어어ㅓㅓ어어']
    temp = {'증상': '신상아 괴사성 장염 초기에 증상이 경미할 때는 소화 불량과 증상이 비슷할 수 있습니다. 초기의 주요 증상은 복부 팽만과 이전에 섭취한 우유가 위에 그대로 남아 있는 것입니다. 그 외에 아기의 배가 부르고, 아기가 잘 빨지 않으며, 늘어지면서 잠혈변(눈에 보이지 않는 혈변)이 보입니다. 이러한 증상은 서서히 시작되며, 미숙아나 신생아의 경우 증상이 미약하여 잘 발견되지 않는 경우가 많습니다.상아 괴사성 장염 초기에 증상이 경미할 때는 소화 불량과 증상이 비슷할 수 있습니다. 초기의 주요 증상은 복부 팽만과 이전에 섭취한 우유가 위에 그대로 남아 있는 것입니다. 그 외에 아기의 배가 부르고, 아기가 잘 빨지 않으며, 늘어지면서 잠혈변(눈에 보이지 않는 혈변)이 보입니다. 이러한 증상은 서서히 시작되며, 미숙아나 신생아의 경우 증상이 미약하여 잘 발견되지 않는 경우가 많습니다.위에 그대로 남아 있는 것입니다. 그 외에 아기의 배가 부르고, 아기가 잘 빨지 않으며, 늘어지면서 잠혈변(눈에 보이지 않는 혈변)이 보입니다. 이러한 증상은 서서히 시작되며, 미숙아나 신생아의 경우 증상이 미약하여 잘 발견되지 않는 경우가 많습니다.위에 그대로 남아 있는 것입니다. 그 외에 아기의 배가 부르고, 아기가 잘 빨지 않으며, 늘어지면서 잠혈변(눈에 보이지 않는 혈변)이 보입니다. 이러한 증상은 서서히 시작되며, 미숙아나 신생아의 경우 증상이 미약하여 잘 발견되지 않는 경우가 많습니다.\n  증상이 심해지면 무호흡 증, 서맥, 저체온, 기민 상태, 신경과민, 담즙 섞인 구토, 피 섞인 구토, 복부 팽만, 혈변과 심한 설사, 위 팽만 등의 증상이 나타날 수 있습니다. 이러한 정상이 점점 더 심해질 수 있습니다. 아기가 잘 먹지 않습니다.  또한 저혈압, 저체온, 창백, 호흡 곤란 등 패혈증과 비슷한 증상이 나타날 수 있습니다. 복막염, 장 천공, 쇼크 및 사망까지 이를 수도 있습니다.', '관련질환': '신생아 답즙정체증, 신생아 호흡곤란증후군', '진료과': '산부인과, 신생아과, 소아외과', '동의어': 'Neonatal Necrotizing Enterocolitis,신생아 괴사성 소장결장염,태아 및 신생아의 괴사성 소장결장염', '정의': '신생아 괴사성 장염은 신생아의 소장이나 대장에 생기는 괴사 성 장염입니다. 여러 가지 원인에 의해 발생할 수 있는 신생아 중증 질환의 하나입니다. 장 점막의 괴사가 다양한 정도로 일어나는 것이 특징입니다. 치료하더라도 사망률이 20%에 이르는 무서운 질병입니다.\n ', '원인': '신생아 괴사성 장염은 주로 미숙아에게 발생합니다. 그 원인은 명확하게 밝혀지지 않았습니다. 1,500g 미만 신생아의 발생 빈도는 5% 내외로, 미숙아 자체가 가장 큰 위험 요인입니다. 그 외에도 고농도 우유, 저산소증, 너무 빠른 영양법, 적혈구 증가증, 감염증 등 다양한 위험 요인이 장 점막의 손상, 이차적 세균 감염, 장의 괴사를 일으키는 데 작용합니다. 만삭아의 경우는 심장 질환이나 저산소증이 있을 때 발생할 수 있습니다.', ' 진단': '신생아 괴사성 장염은 병력, 증상, 진찰 등을 종합해서 진단할 수 있습니다. 조기에 진단하고 적극적으로 치료하면 병의 진행을 막을 수 있으므로, 병을 의심하여 찾아내는 것이 중요합니다. 주로 복부 X-ray 사진만으로 진단할 수 있으며, 필요에 따라 복부 초음파 소견이 도움이 될 수 있습니다. 단순 복부 촬영상 이상 소견이 보이며, 장벽 내 공기가 진단에 가장 중요합니다. 간문맥 내 공기가 보이거나 복강 내 공기가 보이면 장 천공을 의미합니다.', '치료': '신생아 괴사성 장염 환아에게는 장기간 금식에 따라 정맥 주사로 인공적 영양 공급을 행해야 합니다. 그러나 이와 같은 정맥 영양법에 의한 합병증으로 패혈증, 혈전증 및 간경변으로 진행 하는 담즙 정체성 황달 등이 생길 수 있습니다.', '경과': '신생아 괴사성 장염을 내과적으로 치료했을 때, 진단 시 장벽 내 공기가 있었던 환자의 20%는 치료에 실패합니다. 이러한 환자 중 9~25%가 사망합니다. 약 10%의 환자는 괴사된 부위에 협착이 생길 수 있습니다. 장의 괴사가 심했던 경우는 생존하더라도 단장 증후군(short bowel syndrome)이 발생하여 영양에 어려움을 겪을 수 있습니다.', '주의사항': '신생아 괴사성 장염은 사망 을 초래할 수 있는 중증 신생아 질환입니다. 따라서 확진된 환자뿐 아니라 의심되는 환자도 집중 치료를 시작해야 합니다. 입을 통한 영양 공급을 일시 중단하고, 혈관을 통한 수액 공급, 전해질 공급, 영양 공급 등을 시 행합니다. 혈액, 대변 및 척수액 배양 검사 시행 후 전신적 항생제로 치료해야 합니다. 장이 천공된 증거가 있으면 괴사된 장을 외과적으로 절제합니다.', '초보엄마가 알아야 할 신생아 응급상황': '이병섭'}

    #windowExample = DevCtrl(["두통","피곤함","졸림"], names)
    windowExample2 = DevCtrl2("코로나", temp)
    #windowExample.show()
    windowExample2.show()
    sys.exit(app.exec_())