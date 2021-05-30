import DiseaseFinder
import DiseaseSelector

# enter symptoms() 함수를 이용해서 받아오지만, 일부분만 구현했기 때문에 symptomlist에 특정 값을 넣어놓았다.
symptomlist = ['등', '관절통']
val = DiseaseFinder.DiseaseFinder(symptomlist).checkDisease()
back = 0  # back이 1이면 backbutton이 활성화되었다고 생각하고 그 전 단계로 돌아간다.
if val != None:
    # create diseaseList
    DiseaseList = []  # 병명, site 주소가 저장되어 있다.
    # destory symptom's list
    del(symptomlist)
    for key in val:  # 이름만 따로 저장해서 activate("viewer, DiseaseList")
        DiseaseList.append(key)

    ###activate("viewer", d)
    print(DiseaseList)

    # if back==1:
    # activate backbutton + prompt
    # enter symptoms()

    # enter selectedDisease()
    selectedDisease = '간염(Hepatitis)'
    url = url = val[selectedDisease]

    val = DiseaseSelector.DiseaseSelector(
        url).makeSelectedDiseaseInfo()  # 선택된 증상, 관련질환, 진료과 등등이 저장
    del(DiseaseList)
    selectedDiseaseInfo = {}  # 병명, 진료과 저장
    selectedDiseaseInfo['병명'] = selectedDisease
    for diseaseinfo in val:
        if diseaseinfo == "진료과":  # 병명과 진료과만 따로 저장(이후에 UC-5, 6에서 이용하기 위해)
            selectedDiseaseInfo[diseaseinfo] = val[diseaseinfo]
    ###activate("viewer", selectedDiseaseInfo)
    print("selecteDiseaseInfo", selectedDiseaseInfo)
    # if back==1:
    # activate backbutton + prompt
    # enter selectedDisease()

else:
    # activate backbutton + prompt
    print("decrease symptoms")
    # enter symptoms()
