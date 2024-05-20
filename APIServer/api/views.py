from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .serializers import UserSymptomsSerializer, RequestDiseaseSerializer
from .modules.predict_symptoms import predict_symptoms
from .modules.predict_diseases import predict_diseases
from .modules.retrieve_disease import retrieve_disease


# Create your views here.
@api_view(['POST'])
def symptom(request):
    if request.method == 'POST':
        userSymptomsSerializer = UserSymptomsSerializer(data=request.data)
        if(userSymptomsSerializer.is_valid()):
            input_symptoms = userSymptomsSerializer.data['input_symptoms']

            predictedSymptomsJSONArray = predict_symptoms(input_symptoms)
            predictedSymptomsList = []
            for predictedSymptomJSON in predictedSymptomsJSONArray:
                predictedSymptomsList.append(predictedSymptomJSON['symptom'])

            resultJSONArray = predict_diseases(predictedSymptomsList)
            result = {'predicted_diseases': resultJSONArray}

            return Response(result, status=200)
        return Response(userSymptomsSerializer.errors, status=status.HTTP_400_BAD_REQUEST)
"""
POST 요청
{
    "input_symptoms" : "고열, 메스꺼움, 복통"
}

POST 반환
{
    "predicted_diseases": "[{'질병': '진행성 위암(Advanced gastric cancer)', '일치하는 증상 수': 3, '평균 유사도': 0.9636171460151672, '증상별 유사도': [0.9322993159294128, 0.9919241070747375, 0.9666280150413513]}, {'질병': '급성 A형 간염(Acute hepatitis A)', '일치하는 증상 수': 3, '평균 유사도': 0.9632888237635294, '증상별 유사도': [0.9320560693740845, 0.9955141544342041, 0.9622962474822998]}, {'질병': '자가면역용혈질환(Autoimmune hemolytic disease)', '일치하는 증상 수': 3, '평균 유사도': 0.961867113908132, '증상별 유사도': [0.9327969551086426, 0.9927545189857483, 0.9600498676300049]}, {'질병': '화농성 간농양(Pyogenic liver abscess)', '일치하는 증상 수': 3, '평균 유사도': 0.9605428576469421, '증상별 유사도': [0.928540050983429, 0.9936819672584534, 0.9594065546989441]}, {'질병': '단장 증후군(Short Bowel Syndrome)', '일치하는 증상 수': 3, '평균 유사도': 0.9600605765978495, '증상별 유사도': [0.9281111359596252, 0.9939674735069275, 0.9581031203269958]}]"
}
"""


@api_view(['POST'])
def disease(request):
    if request.method == 'POST':
        requestDiseaseSerializer = RequestDiseaseSerializer(data=request.data)
        if (requestDiseaseSerializer.is_valid()):
            request_disease = requestDiseaseSerializer.data['request_disease']

            disease_info = retrieve_disease(request_disease)
            disease_info = disease_info[0]
            result = {'disease_id': disease_info['disease_id'],
                      'disease_name': disease_info['disease_name'],
                      'disease_link': disease_info['disease_link'],
                      'disease_img': disease_info['disease_img'],
                      'symptoms': disease_info['symptoms'],
                      'symptom_ids': disease_info['symptom_ids'],
                      'related_diseases': disease_info['related_diseases'],
                      'related_disease_ids': disease_info['related_disease_ids'],
                      'department': disease_info['department'],
                      'synonyms': disease_info['synonyms'],
                      'detailed_symptoms': disease_info['detailed_symptoms'],
                      'disease_course': disease_info['disease_course'],
                      'disease_specific_diet': disease_info['disease_specific_diet'],
                      'diet_therapy': disease_info['diet_therapy'],
                      'recommended_food': disease_info['recommended_food'],
                      'caution_food': disease_info['caution_food'],
                      'other_notes': disease_info['other_notes']
                      }

            return Response(result, status=200)
        return Response(requestDiseaseSerializer.errors, status=status.HTTP_400_BAD_REQUEST)


"""
POST 요청
{
    "request_disease" : "허혈성 심질환(Ischemic heart disease)"
}

POST 반환
{
    "disease_id":30275.0,
    "disease_name":"허혈성 심질환(Ischemic heart disease)",
    "disease_link":"https:\/\/www.amc.seoul.kr\/asan\/healthinfo\/disease\/diseaseDetail.do?contentId=30275",
    "disease_img":"https:\/\/www.amc.seoul.kr\/asan\/file\/imageView.do?fileId=F000000004114",
    "symptoms":"방사통, 호흡곤란, 가슴 통증",
    "symptom_ids":"SS000768,SS000908,SS000862",
    "related_diseases":"심근병증, 불안정형 협심증, 오래된 심근경색증, 급성 심근경색증, 흉통, 전도 장애, 부정맥, 협심증",
    "related_disease_ids":"30320,32135,32118,32111,30290,30292,30298,32179",
    "department":"심장내과, \r\n\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t심장병원",
    "synonyms":"허혈성심장병,허혈성심장질환",
    "detailed_symptoms":null,
    "disease_course":null,
    "disease_specific_diet":"허혈성심장질환식",
    "diet_therapy":"1. 밥은 현미, 보리 등을 섞은 잡곡밥이 좋으며 기호에 따라 적정량 혼식합니다. 단, 입맛에 맞지 않을 경우 무리하게 잡곡밥을 고집하지 말고 쌀밥을 섭취합니다.\r\n2. 고기, 두부, 생선 등의 단백질 반찬도 골고루 섭취하되 고기는 기름기와 껍질을 제거한 살코기로 섭취합니다.\r\n3. 채소찬은 제철 채소를 이용하여 싱겁게 조리하되 장아찌, 김치 등의 염장식품은 지양합니다.\r\n4. 간식은 정규 식사 사이에 제철 과일과 우유로 섭취합니다.\r\n5. 전체적인 조리 방법은 지방 섭취를 줄이기 위해 튀기거나 부치는 대신 굽기, 찜, 삶는 방법을 주로 선택하나 맛을 내기 위해 적당량의 식물성기름(참기름, 들기름 등)은 사용합니다.\r\n6. 저염식 적응을 위해 조리 시 미리 염분을 넣는 것보다 무염 조리 후 따로 분량의 저염 소스를 곁들이는 것이 더욱 효과적입니다.\r\n7. 콜레스테롤이 높은 식품은 월 2~3회로 줄여서 섭취합니다.",
    "recommended_food":"신선한 채소를 비롯한 잡곡, 저지방 어육류, 생선, 두부 그리고 제철 과일과 우유 등 균형잡힌 식사",
    "caution_food":"고지방 어육류 : 갈비, 삼겹살, 육류의 껍질과 기름, 장어, 햄류\r\n고콜레스테롤 식품 : 내장류, 새우, 오징어, 계란노른자\r\n기름진 음식 : 탕류, 중국음식, 튀김류, 전류\r\n염장 식품 - 김치류, 젓갈류, 장아찌류, 건어물 및 자반 생선류\r\n가공식품 - 햄류, 통조림류, 라면\r\n국, 찌개 국물류",
    "other_notes":"오메가-3 지방산은 에이코사펜타엔산(EPA), 도코사헥사엔산(DHA) 등으로 주로 생선기름에 많이 포함되어 있습니다.\r\n생선을 많이 먹는 알래스카 원주민에서 심혈관계 질환의 사망률이 낮은 것이 관찰되었고 이후 오메가-3의 효능에 대한 많은 연구들에서 오메가-3가 심혈관계 사망률을 낮춘다는 결과를 보고하였습니다. 오메가-3는 혈소판 응집과 염증반응을 감소시키고, 혈중 중성지방의 농도를 감소시키고, 심박수와 혈압을 강하시켜 심혈관계 질환으로 인한 사망을 감소시키는 것으로 생각되고 있습니다."
}
"""