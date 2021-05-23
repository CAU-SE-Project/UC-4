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
        driver = webdriver.Chrome(r'C:\Users\es344\chromedriver')

        # 신체부위 체크
        task_list = [['머리', '?partId=B000007'], [
            '목', '?partId=B000008'], ['가슴', '?partId=B000020']]
        nowBody = '머리'
        BodyStr = None
        for i in task_list:
            for j in i:
                if i[0] == nowBody:
                    nowBody = i[1]
                    break

        # 증상백과 페이지로 이동
        driver.get(
            'http://www.amc.seoul.kr/asan/healthinfo/symptom/symptomSubmain.do'+nowBody)

        task_list_dict = {'간성뇌증': 'cont1_1', '강박증': 'cont1_2', '건망증': 'cont1_3', '고산병': 'cont1_4',
                          '광대뼈 위치 이상': 'cont1_5', '기민상태': 'cont1_6', '기억장애': 'cont1_7', '깨어나면 기억하지 못함': 'cont1_8',
                          '납작한 코': 'cont1_9', '축 쳐진 귀': 'cont1_10', '낮 시간대의 졸음': 'cont1_11', '낮은 지능': 'cont1_12',
                          '낮은 학업 성취': 'cont1_13', '내분비계이상': 'cont1_14', '놀란표정': 'cont1_15', '놀람반사의 약화': 'cont1_16',
                          '뇌부종': 'cont1_17', '뇌압상승증상': 'cont1_18', '뇌염증상': 'cont1_19', '뇌출혈': 'cont1_20',
                          '달모양의 둥근 얼굴': 'cont1_21', '두부 외상': 'cont1_22', '두통': 'cont1_23', '두피 건조': 'cont1_24',
                          '두피 열상': 'cont1_25', '만성 부비동염': 'cont1_26', '머리모양 변형': 'cont1_27', '모발 탈색': 'cont1_28',
                          '모발이 가늘어짐': 'cont1_29', '모발이 거침': 'cont1_30', '무균성 뇌막염': 'cont1_31', '무의식': 'cont1_32',
                          '박동성 통증': 'cont1_33', '방향감각 상실': 'cont1_34', '볼, 눈주위 움푹 꺼짐': 'cont1_35', '볼이 처짐': 'cont1_36',
                          '비웃는 듯한 표정': 'cont1_37', '삐뚤어진 눈, 코, 입': 'cont1_38', '수막자극증상': 'cont1_39', '실인증': 'cont1_40',
                          '실행증': 'cont1_41', '안면 변형': 'cont1_42', '안면마비': 'cont1_42', '안면부 출혈': 'cont1_44', '안면통': 'cont1_45',
                          '안면홍조': 'cont1_46', '어지러움': 'cont1_47', '언어장애': 'cont1_48', ' 얼굴 중심선이 안맞음': 'cont1_49',
                          '얼굴 한쪽의 반점': 'cont1_50', '얼굴모양변화': 'cont1_51', '얼굴부종': 'cont1_52', '얼굴에 땀이 남': 'cont1_53',
                          '얼굴에 털이 자람': 'cont1_54', '얼굴의 나비모양 홍반': 'cont1_55', '얼굴이 밋밋함': 'cont1_56', '얼굴이 화끈거림': 'cont1_57',
                          '얼굴형태의 이상': 'cont1_58', '운동 실어증': 'cont1_59', '원형, 타원형의 탈모': 'cont1_60',
                          '의식 변화': 'cont1_61', '의식 저하': 'cont1_62', '이마가 넓어짐': 'cont1_63', '이마의 주름': 'cont1_64',
                          '이중턱': 'cont1_65', '인지장애': 'cont1_66', '졸림': 'cont1_67', '지남력 장애': 'cont1_68', '짓누르는 느낌': 'cont1_69',
                          '치매': 'cont1_70', '코 옆과 입꼬리 주름': 'cont1_71', '콧등이 넓어짐': 'cont1_72', '턱끝이 커보임': 'cont1_73',
                          '턱의 통증': 'cont1_74', '편두통': 'cont1_75', '하악전돌': 'cont1_76', '학습장애': 'cont1_77', '혼돈': 'cont1_78', '혼수': 'cont1_79'}

        # symptomlist와 비교
        task_dict = {}
        for i in self.getsymptomsList():
            for j in task_list_dict:
                if i == j:
                    task_dict[i] = task_list_dict[j]

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
