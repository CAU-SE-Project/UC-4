# Search-Disease
Repository for Team C's subprogram, Search Disease

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

- **HospitalFinder.py** : 선택된 질병의 진료과 정보를 GET방식으로 CAUSE_UC-5 (https://reserve-gwabang.web.app/cause_project2.html) 사이트에 전달, 병원을 검색해 결과를 지도에 표시(UC-5의 일부 구현)

- **DevCtrl.py** : 받아온 정보를 GUI로 화면에 출력, 사용자 입력을 Controller에 전달

- **selectedDiseaseInfo.txt** : 선택된 질병의 이름과 진료과 정보를 DB에 저장해 다음에도 사용할 수 있도록 함


## Demo
You can see demonstration of the project below
- UC4_screen_recording.mp4

- screenshot example
![image](https://user-images.githubusercontent.com/48945057/120111730-0c506e00-c1ae-11eb-8861-1300d1cc691f.png)


## Installation
The package requires python3, selenium, and chromedriver(has to match your chrome version)
- Download the repository

```
git clone https://github.com/CAU-SE-Project/UC-4-Search-Disease
```

### Download chromedriver
- Check your chome version and download chromedriver at (https://sites.google.com/a/chromium.org/chromedriver/home)
- Change chromedriver path in DiseaseFinder.py, DiseaseSelector.py, and HospitalFinder.py


### Download selenium and PyQt5
```
cd UC-4-Search-Disease
pip install selenium
pip install PyQt5
```

### Run Demo
```
cd UC-4-Search-Disease
python controller.py
```
