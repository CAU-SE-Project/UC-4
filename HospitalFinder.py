from requests.api import head


class HospitalFinder:
    def __init__(self, selectedDiseaseInfo):
        self.selectedDiseaseInfo = selectedDiseaseInfo

    def getDiseaseInfo(self):
        return self.selectedDiseaseInfo

    def FindHospital(self):
        # 크롬 브라우저를 띄우기 위해, 웹드라이버를 가져오기
        from selenium import webdriver
        from selenium.webdriver.common.keys import Keys
        from selenium.webdriver.support.ui import Select

        # 크롬 드라이버로 크롬을 실행한다.
        driver = webdriver.Chrome(r'C:\Users\user\CAUSE-project\chromedriver_win32\chromedriver.exe')

        # 증상백과 페이지로 이동
        hospitals = self.selectedDiseaseInfo["진료과"].split(',')
        print(hospitals)
        nowBody = hospitals[0]
        driver.get(
            'https://reserve-gwabang.web.app/cause_project2.html?'+nowBody)