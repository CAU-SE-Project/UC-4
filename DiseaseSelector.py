from requests.api import head


class DiseaseSelector:
    def __init__(self, url):
        self.url = url

    def getUrl(self):
        return self.url

    def makeSelectedDiseaseInfo(self):
        # 크롬 브라우저를 띄우기 위해, 웹드라이버를 가져오기
        from selenium import webdriver
        from selenium.webdriver.common.keys import Keys
        from selenium.webdriver.support.ui import Select
        # 크롬 드라이
        # 버로 크롬을 실행한다.
        driver = webdriver.Chrome(r'C:\Users\es344\chromedriver')

        # 질환백과 페이지로 이동
        driver.get(self.getUrl())
        elemdt = driver.find_elements_by_tag_name('dt')
        elemdd = driver.find_elements_by_tag_name('dd')
        resultsdt = []
        resultsdd = []
        resultdic = {}
        # 검색 결과 모두 긁어서 리스트로 저장
        for eledt in elemdt:
            resultsdt.append(eledt.text)
        for eledd in elemdd:
            resultsdd.append(eledd.text)
        index = 0
        while index < len(resultsdt):
            resultdic[resultsdt[index]] = resultsdd[index]
            # print(resultdic)
            index += 1
        # print(resultdic)
        return resultdic
