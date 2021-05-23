import sys
from PyQt5.QtWidgets import (QWidget, QGridLayout,QPushButton, QApplication)
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
import DiseaseFinder
import DiseaseSelector
import DevCtrl

class Controller:
    def __init__(self, symptomlist):
        self.symptomlist = symptomlist
        DiseaseList, self.tempDiseaseFinder = self.findDisease(symptomlist)
        app = QApplication(sys.argv)
        self.windowExample = DevCtrl.DevCtrl(symptomlist, DiseaseList, self)
        self.windowExample.show()
        sys.exit(app.exec_())

    def findDisease(self, symptomlist):
        DiseaseList = []
        tempDiseaseFinder = DiseaseFinder.DiseaseFinder(symptomlist).checkDisease() #disease name과 url을 가짐
        for key in tempDiseaseFinder:
            DiseaseList.append(key)
        print(DiseaseList)
        return DiseaseList, tempDiseaseFinder

    def selectDisease(self, selectedDisease):
        #selectedDisease = '라이 증후군(Reye syndrome)'
        url = ""
        for diseaseName in self.tempDiseaseFinder:
            if(selectedDisease == diseaseName):
                url = self.tempDiseaseFinder[diseaseName]

        tempDiseaseInfo = DiseaseSelector.DiseaseSelector(url).makeSelectedDiseaseInfo()
        self.windowExample2 = DevCtrl.DevCtrl2(selectedDisease, tempDiseaseInfo)
        self.windowExample2.show()

        selectedDiseaseInfo = {}  # 병명, 진료과 저장
        selectedDiseaseInfo['병명'] = selectedDisease
        for diseaseinfo in tempDiseaseInfo:
            if diseaseinfo == "진료과":
                selectedDiseaseInfo[diseaseinfo] = tempDiseaseInfo[diseaseinfo]
        
        f = open("selectedDiseaseInfo.txt", "w")
        keys = list(selectedDiseaseInfo.keys())
        for k in keys:
            f.write(str(k)+": "+selectedDiseaseInfo[k]+"\n")
        f.close()

        #print(diseaseinfo)
        print(tempDiseaseInfo)
        print(tempDiseaseInfo.keys())
        return selectedDiseaseInfo


DiseaseList = []
symptomlist = ['두통']
controller = Controller(symptomlist)


