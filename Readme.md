# Clinic-System
Repository for Team C's subprogram, Find Disease

#### Requirements for Use Case 04
- **REQ-17(6pts)** : As a general/patient user, the names of all possible diseases associated with my symptoms can be found on the Disease Search page.

- **REQ-18(5pts)** : As a general/patient user, click on the name of the disease to view the definition, cause, symptoms, diagnosis, treatment, progress, precautions, and medical information of the disease

- **REQ-19(10pts)** : The system can retrieve all disease information from the database and filter only the diseases associated with the symptoms.

- **REQ-20(1pts)** : As a general/patient user, I can choose whether to receive medical treatment for the disease.

- **REQ-21(1pts)** : As a general/patient user, you can choose whether to receive treatment face-to-face or non-face-to-face.

- **REQ-22(7pts)** : As a general/patient user, can receive recommendations from nearby clinics based on your current location.



## Requirement
- Windows, MacOS or Linux (Ubuntu recommended)
- Python 3 (We tested in conda, but not necessary)
  - PyQt5
  - selenium
  - chromedriver


## Overview
추가 필요

## Installation
The package requires python3, selenium, and chromedriver(has to match your chrome version)
- Download the repository

```
git clone https://github.com/CAU-SE-Project/UC-4
```

### Download chromedriver
- Check your chome version and download at (https://sites.google.com/a/chromium.org/chromedriver/home)
- change chromedriver path in DiseaseFinder.py, DiseaseSelector.py, and HospitalFinder.py


### Download selenium and PyQt5
```
cd UC-4
pip install selenium
pip install PyQt5

```
