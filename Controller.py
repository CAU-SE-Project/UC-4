import DiseaseFinder
import DiseaseSelector

DiseaseList = []
symptomlist = ['기민상태']
tempDiseaseFinder = DiseaseFinder.DiseaseFinder(symptomlist).checkDisease()
for key in tempDiseaseFinder:
    DiseaseList.append(key)
print(DiseaseList)

selectedDisease = '라이 증후군(Reye syndrome)'
url = ""

for diseaseName in tempDiseaseFinder:
    if selectedDisease == diseaseName:
        url = tempDiseaseFinder[diseaseName]
tempDiseaseInfo = DiseaseSelector.DiseaseSelector(
    url).makeSelectedDiseaseInfo()
selectedDiseaseInfo = {}  # 병명, 진료과 저장
selectedDiseaseInfo['병명'] = selectedDisease
for diseaseinfo in tempDiseaseInfo:
    if diseaseinfo == "진료과":
        selectedDiseaseInfo[diseaseinfo] = tempDiseaseInfo[diseaseinfo]
# print(selectedDiseaseInfo)
