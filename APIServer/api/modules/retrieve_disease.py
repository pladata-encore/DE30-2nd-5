# parameter : String (ex) '허혈성 심질환(Ischemic heart disease)'
# return : JSONArray (#object : 1)
"""
[
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
]
"""
import pandas as pd
import json


def retrieve_disease(disease_name):
    # 저장된 피클 파일 불러오기
    loaded_df = pd.read_pickle('C:/projects/wheresurhurt/backend/api/modules/disease_data.pkl')
    filtered_df = loaded_df[loaded_df['disease_name'] == disease_name]
    json_string = filtered_df.to_json(orient='records', force_ascii=False)
    result_json = json.loads(json_string)

    return result_json
