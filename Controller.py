import sys
from PyQt5.QtWidgets import (QWidget, QGridLayout,QPushButton, QApplication)
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
import DiseaseFinder
import DiseaseSelector
import DevCtrl
import pymysql


class Controller:
    def __init__(self, symptomlist):
        self.symptomlist = symptomlist
        DiseaseList, self.tempDiseaseFinder = self.findDisease(symptomlist)
        app = QApplication(sys.argv)
        self.windowExample = DevCtrl.Viewer(symptomlist, DiseaseList, self)
        self.windowExample.show()
        sys.exit(app.exec_())

    def findDisease(self, symptomlist):
        DiseaseList = []
        val = DiseaseFinder.DiseaseFinder(symptomlist).checkDisease()
        self.back = False  # back이 1이면 backbutton이 활성화되었다고 생각하고 그 전 단계로 돌아간다.
        if val != None:
            # create diseaseList
            DiseaseList = []  # 병명, site 주소가 저장되어 있다.
            # destory symptom's list
            del(symptomlist)
            for key in val:  # 이름만 따로 저장해서 activate("viewer, DiseaseList")
                DiseaseList.append(key)

            tempDiseaseFinder = val
            print(DiseaseList)
            return DiseaseList, tempDiseaseFinder
        else:
            # activate backbutton + prompt
            print("decrease symptoms")
            # enter symptoms()

    def selectDisease(self, selectedDisease):
        #selectedDisease = '라이 증후군(Reye syndrome)'

        url = ""
        for diseaseName in self.tempDiseaseFinder:
            if(selectedDisease == diseaseName):
                url = self.tempDiseaseFinder[diseaseName]


        tempDiseaseInfo = DiseaseSelector.DiseaseSelector(url).makeSelectedDiseaseInfo()   # 선택된 증상, 관련질환, 진료과 등등이 저장
        ###activate("viewer", selectedDiseaseInfo)
        self.windowExample2 = DevCtrl.Viewer2(selectedDisease, tempDiseaseInfo, self)
        self.windowExample2.show()

        selectedDiseaseInfo = {}  # 병명, 진료과 저장
        selectedDiseaseInfo['병명'] = selectedDisease
        for diseaseinfo in tempDiseaseInfo:
            if diseaseinfo == "진료과":     # 병명과 진료과만 따로 저장(이후에 UC-5, 6에서 이용하기 위해)
                selectedDiseaseInfo[diseaseinfo] = tempDiseaseInfo[diseaseinfo]
        
        f = open("selectedDiseaseInfo.txt", "w")
        keys = list(selectedDiseaseInfo.keys())
        for k in keys:
            f.write(str(k)+": "+selectedDiseaseInfo[k]+"\n")
        f.close()

        #print(diseaseinfo)
        print(tempDiseaseInfo)
        #print(tempDiseaseInfo.keys())
        return selectedDiseaseInfo


DiseaseList = []
symptomlist = ['머리', '건망증']
controller = Controller(symptomlist)


