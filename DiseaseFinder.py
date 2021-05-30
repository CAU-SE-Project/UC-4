from requests.api import head


class DiseaseFinder:
    def __init__(self, symptomsList):
        self.symptomsList = symptomsList

    def getsymptomsList(self):
        return self.symptomsList

    def checkDisease(self):
        # 크롬 브라우저를 띄우기 위해, 웹드라이버를 가져오기
        from selenium import webdriver
        from selenium.webdriver.common.keys import Keys
        from selenium.webdriver.support.ui import Select

        # 크롬 드라이버로 크롬을 실행한다.
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument('headless')
        chrome_options.add_argument('--disable-gpu')
        chrome_options.add_argument('lang=ko_KR')
        driver = webdriver.Chrome(
            r'C:\Users\es344\chromedriver', chrome_options=chrome_options)

        # 신체부위 체크
        task_list = [['머리', '?partId=B000007'], ['목', '?partId=B000008'],
                     ['가슴', '?partId=B000020'], ['배', '?partId=B000010'],
                     ['등', '?partId=B000006'], ['엉덩이', '?partId=B000013'],
                     ['팔', '?partId=B000018'], ['다리', '?partId=B000005'],
                     ['눈', '?partId=B000004'], ['귀', '?partId=B000002'],
                     ['코', '?partId=B000017'], ['입', '?partId=B000015'],
                     ['전신', '?partId=B000016'], ['피부', '?partId=B000019'],
                     ['유방', '?partId=B000014'], ['생식기', '?partId=B000011'],
                     ['골반', '?partId=B000001'], ['손', '?partId=B000012'],
                     ['발', '?partId=B000019'], ['기타', '?partId=B000003']]

        nowBody = self.getsymptomsList()[0]  # 아픈위치
        print("nowBody", nowBody)
        for i in task_list:
            for j in i:
                if i[0] == nowBody:
                    nowBody = i[1]
                    break
        print(nowBody)
        # 증상백과 페이지로 이동
        task_list_dict = {}  # 등이라면 {'관절통':'cont1_1', '굽은등', 'cont1_2'} 이런식으로 저장
        driver.get(
            'http://www.amc.seoul.kr/asan/healthinfo/symptom/symptomSubmain.do'+nowBody)

        # 검색 결과 확인
        elem2 = driver.find_element_by_class_name('searchCont')  # ul class
        ul_list = elem2.find_element_by_tag_name('ul')
        li_list = ul_list.find_elements_by_tag_name('li')

        # 검색 결과 모두 긁어서 리스트로 저장
        for li in li_list:
            key = li.text  # 병 이름
            label_tags = li.find_elements_by_tag_name('label')
            if label_tags:
                for label in label_tags:
                    link = label.get_attribute('for')  # 하이퍼링크
                    value = link
                    task_list_dict[key] = value
        # 검색 결과 확인
        elemsymptom = driver.find_element_by_class_name(
            'searchCont')  # ul class
        ul_list = elemsymptom.find_element_by_tag_name('ul')
        li_list = ul_list.find_elements_by_tag_name('li')
        # 검색 결과 모두 긁어서 리스트로 저장
        for li in li_list:
            key = li.text  # 병 이름
            label_tags = li.find_elements_by_tag_name('label')
            if label_tags:
                for label in label_tags:
                    link = label.get_attribute('for')  # 하이퍼링크
                    value = link
                    task_list_dict[key] = value

        # symptomlist와 비교
        task_dict = {}
        task_dict[self.getsymptomsList(
        )[1]] = task_list_dict[self.getsymptomsList()[1]]

        for task in task_dict.values():
            checkbox = driver.find_element_by_id(task)
            checkbox.click()

        # 검색 버튼 클릭
        search_button = driver.find_element_by_class_name('grayMdBtn2')
        search_button.click()

        # 검색 결과 확인
        elem2 = driver.find_element_by_class_name('listCont')
        strong_list = elem2.find_elements_by_tag_name('strong')
        results = {}
        diseaseList = {}

        # 검색 결과 모두 긁어서 리스트로 저장
        for strong in strong_list:
            key = strong.text  # 병 이름
            a_tags = strong.find_elements_by_tag_name('a')
            if a_tags:
                for a_tag in a_tags:
                    link = a_tag.get_attribute('href')  # 하이퍼링크
                    value = link
                    results[key] = value
        # print(results)
        return results
