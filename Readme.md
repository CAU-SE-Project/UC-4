# Clinic-System
Repository for Team C's subprogram, Find Disease

#### Requirements for Use Case 04
- **REQ-17(6pts)** : As a general/patient user, the names of all possible diseases associated with my symptoms can be found on the Disease Search page.

- **REQ-18(5pts)** : As a general/patient user, click on the name of the disease to view the definition, cause, symptoms, diagnosis, treatment, progress, precautions, and medical information of the disease

- **REQ-19(10pts)** : The system can retrieve all disease information from the database and filter only the diseases associated with the symptoms.

- **REQ-20(1pts)** : As a general/patient user, I can choose whether to receive medical treatment for the disease.

- **REQ-21(1pts)** : As a general/patient user, I can choose whether to receive treatment face-to-face or non-face-to-face.

- **REQ-22(7pts)** : As a general/patient user, I can receive recommendations of nearby hospitals based on your current location.



## Requirement
- Windows, MacOS or Linux (Ubuntu recommended)
- Python 3 (We tested in conda, but not necessary)
  - PyQt5
  - selenium
  - chromedriver


## Overview
- **Controller.py** : symptomlist에 증상을 넣고 Controller 객체 생성

- **DiseaseFinder.py** : checkDisease()함수에서 해당 symptoms과 관련된 질병 이름과 사이트 url을 tempDiseaseFinder에 반환

- **DiseaseSelector.py** : makeSelectedDiseaseInfo()함수에서 해당 질병의 자세한 정보(정의, 원인, 증상, 진단, 진료, 경과, 주의사항, 관련질환, 진료과) 를 tempDiseaseInfo에 반환

- **HospitalFinder.py** : 선택된 질병의 진료과 정보를 GET방식으로 CAUSE_UC-4 (https://reserve-gwabang.web.app/cause_project2.html) 사이트에 전달, 병원을 검색해 결과를 지도에 표시

- **DevCtrl.py** : 받아온 정보를 GUI로 화면에 출력, 사용자 입력을 Controller에 전달

- **selectedDiseaseInfo.txt** : 선택된 질병의 이름과 진료과 정보를 DB에 저장해 다음에도 사용할 수 있도록 함

## Installation
The package requires python3, selenium, and chromedriver(has to match your chrome version)
- Download the repository

```
git clone https://github.com/CAU-SE-Project/UC-4
```

### Download chromedriver
- Check your chome version and download chromedriver at (https://sites.google.com/a/chromium.org/chromedriver/home)
- Change chromedriver path in DiseaseFinder.py, DiseaseSelector.py, and HospitalFinder.py


### Download selenium and PyQt5
```
cd UC-4
pip install selenium
pip install PyQt5
```
