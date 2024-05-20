## 크롤링
### 출처
(입력 데이터 형식 및 Positive/Negative에 따른 한국어 증상 기반 질병 예측 모델)의 논문
[아산병원 식이요법](https://www.amc.seoul.kr/asan/healthinfo/mealtherapy/mealTherapyList.do)
### 데이터 출처 근거 
  - 다양한 질병 데이터를 찾았으나 크롤링이 안됨
  - 전문성 있는 한양대 레퍼런스인 [입력 데이터 형식 및 Positive/Negative에 따른 한국어 증상 기반 질병 예측 모델] 논문을 참고
  - 논문에 제시된 크롤링 경로인 아산병원에서 크롤링 수행 후 모델링 학습
### 정보 수집
![](https://velog.velcdn.com/images/kimheesu98/post/bb1589d7-6a88-42b1-b81b-b6ef28751257/image.png)
  - 질병ID,질병명,증상,식이요법 등 필요한 데이터 수집
### 3가지로 나눈 csv
  - _질병 기본정보 diseases_240510.csv_
```
import requests
from bs4 import BeautifulSoup
import csv

# CSV 파일에 저장할 헤더
header = ['disease_id', 'disease_name', 'disease_link', 'disease_img', 'symptoms', 'symptom_ids', 'related_diseases', 'related_disease_ids', 'department', 'synonyms']

# CSV 파일 열기
with open('diseases_240510.csv', 'w', newline='', encoding='utf-8') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(header)

    # 질병 종류별 순환
    disease_kind_ids = ['C000001', 'C000002', 'C000003', 'C000004', 'C000005', 
                        'C000006', 'C000007', 'C000008', 'C000009', 'C000010', 
                        'C000011', 'C000012', 'C000013', 'C000014', 'C000015', 
                        'C000016', 'C000017', 'C000018', 'C000019', 'C000020']
    for kind_id in disease_kind_ids:  # 질병 종류는 C000001부터 C000020까지 순환
        print(kind_id, " 시작")
        url = f'https://www.amc.seoul.kr/asan/healthinfo/disease/diseaseList.do?pageIndex=1&partId=&diseaseKindId={kind_id}&searchKeyword=%EA%B0%90%EC%97%BC%EC%84%B1%EC%A7%88%ED%99%98'
        response = requests.get(url)
        soup = BeautifulSoup(response.text, 'html.parser')

        # 페이지 순환
        for i in range(1, 11):  # pageIndex는 1부터 10까지 순환
            url = f'https://www.amc.seoul.kr/asan/healthinfo/disease/diseaseList.do?pageIndex={i}&partId=&diseaseKindId={kind_id}&searchKeyword=%EA%B0%90%EC%97%BC%EC%84%B1%EC%A7%88%ED%99%98'
            response = requests.get(url)
            soup = BeautifulSoup(response.text, 'html.parser')

            # 질병 목록 추출
            # disease_list = soup.select('.listCont .contBox')
            disease_list = soup.select('#listForm > div > div > ul > li')

            # 각 질병에 대한 정보 추출 및 CSV에 추가
            for disease in disease_list:
                disease_name_elem = disease.select_one('.contTitle a')
                disease_name = disease.select_one('.contTitle a').text.strip()
                disease_link = disease_name_elem['href']
                disease_id = disease_link.split('=')[-1] 
                disease_img = disease.select_one('.imgBox img')['src']

                # 증상 및 관련질환 추출
                symptoms_elem = disease.select_one('dt:contains("증상") + dd')
                if symptoms_elem:
                    symptoms = ', '.join([a.text.strip() for a in symptoms_elem.select('a')])
                    symptom_ids = [a['href'].split('=')[-1] for a in symptoms_elem.select('a')]
                else:
                    symptoms = ''
                    symptom_ids = ''
                
                related_diseases_elem = disease.select_one('dt:contains("관련질환") + dd')
                if related_diseases_elem:
                    related_diseases = ', '.join([a.text.strip() for a in related_diseases_elem.select('a')])
                    related_disease_ids = [a['href'].split('=')[-1] for a in related_diseases_elem.select('a')] if related_diseases_elem else ''
                else:
                    related_diseases = ''
                    related_disease_ids = ''

                # 진료과 및 동의어 추출
                department_elem = disease.select_one('dt:contains("진료과") + dd')
                department = department_elem.text.strip() if department_elem and department_elem.text.strip() else None
                synonyms_elem = disease.select_one('dt:contains("동의어") + dd')
                synonyms = synonyms_elem.text.strip() if synonyms_elem else ''

                # CSV 파일에 추가
                writer.writerow([disease_id, disease_name, "https://www.amc.seoul.kr" + disease_link, "https://www.amc.seoul.kr" + disease_img, symptoms, ','.join(symptom_ids), related_diseases, ','.join(related_disease_ids), department, synonyms])
        print(kind_id, " 끝")

print("CSV 파일이 성공적으로 생성되었습니다.")

```
  - _질병 증상 정보 diseases_txt240513.csv_
```
import requests
from bs4 import BeautifulSoup
import csv
# CSV 파일에 저장할 헤더
header = ['disease_id', 'disease_name', 'disease_link', 'disease_img', 'symptoms', 'symptom_ids', 'related_diseases', 'related_disease_ids', 'department', 'synonyms', 'detailed_symptoms', 'disease_course']
# CSV 파일 열기
with open('diseases_txt_240513.csv', 'w', newline='', encoding='utf-8') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(header)
    # 질병 종류별 순환
    disease_kind_ids = ['C000001', 'C000002', 'C000003', 'C000004', 'C000005',
                        'C000006', 'C000007', 'C000008', 'C000009', 'C000010',
                        'C000011', 'C000012', 'C000013', 'C000014', 'C000015',
                        'C000016', 'C000017', 'C000018', 'C000019', 'C000020']
    for kind_id in disease_kind_ids:  # 질병 종류는 C000001부터 C000020까지 순환
        print(kind_id, " 시작")
        url = f'https://www.amc.seoul.kr/asan/healthinfo/disease/diseaseList.do?pageIndex=1&partId=&diseaseKindId={kind_id}&searchKeyword=%EA%B0%90%EC%97%BC%EC%84%B1%EC%A7%88%ED%99%98'
        response = requests.get(url)
        soup = BeautifulSoup(response.text, 'html.parser')
        # 페이지 순환
        for i in range(1, 11):  # pageIndex는 1부터 10까지 순환
            url = f'https://www.amc.seoul.kr/asan/healthinfo/disease/diseaseList.do?pageIndex={i}&partId=&diseaseKindId={kind_id}&searchKeyword=%EA%B0%90%EC%97%BC%EC%84%B1%EC%A7%88%ED%99%98'
            response = requests.get(url)
            soup = BeautifulSoup(response.text, 'html.parser')
            # 질병 목록 추출
            disease_list = soup.select('#listForm > div > div > ul > li')
            for disease in disease_list:
                disease_link_elem = disease.select_one('.contTitle a')
                disease_name = disease_link_elem.text.strip()
                disease_link = disease_link_elem['href']
                disease_id = disease_link.split('=')[-1]
                disease_img = disease.select_one('.imgBox img')['src']
                # 질병 상세 페이지 요청
                detailed_response = requests.get("https://www.amc.seoul.kr" + disease_link)
                detailed_soup = BeautifulSoup(detailed_response.text, 'html.parser')
                # 상세 증상과 경과 텍스트 추출
                # detailed_symptoms = detailed_soup.select_one('dt:contains("증상") + dd').text.strip() if detailed_soup.select_one('dt:contains("증상") + dd') else ''
                # disease_course = detailed_soup.select_one('dt:contains("경과") + dd').text.strip() if detailed_soup.select_one('dt:contains("경과") + dd') else ''
                temp = detailed_soup.select_one('#content > div.healthinfoWrap.clearfix > div.regionReviewLeft > div.contDescription')
                detailed_symptoms = temp.select_one('dt:contains("증상") + dd').text.strip()
                disease_course = temp.select_one('dt:contains("경과") + dd').text.strip()
                # 기존 정보와 함께 저장
                writer.writerow([disease_id, disease_name, "https://www.amc.seoul.kr" + disease_link, "https://www.amc.seoul.kr" + disease_img, symptoms, ','.join(symptom_ids), related_diseases, ','.join(related_disease_ids), department, synonyms, detailed_symptoms, disease_course])
        print(kind_id, " 끝")
```
  - _질병 식이요법 disease_diet.csv_
```
import requests
from bs4 import BeautifulSoup
import csv

# 결과를 담을 빈 리스트 생성
data = []

# 페이지 인덱스를 변경하며 각 페이지의 URL에 접근하여 데이터 추출
for page_index in range(1, 12):  # 예시로 10 페이지까지만 순회
    url = f"https://www.amc.seoul.kr/asan/healthinfo/mealtherapy/mealTherapyList.do?pageIndex={page_index}&searchCondition=&searchKeyword=&mtId="
    response = requests.get(url).text
    soup = BeautifulSoup(response, "html.parser")

    # 질병명과 링크 가져오기
    for disease in soup.find_all("dt"):
        disease_name_tag = disease.find("a", class_="txtellipsis")
        if disease_name_tag:
            disease_name = disease_name_tag.text.strip()
            disease_link = "https://www.amc.seoul.kr" + disease_name_tag["href"]

            # 상세 페이지의 HTML 가져오기
            disease_response = requests.get(disease_link).text
            disease_soup = BeautifulSoup(disease_response, "html.parser")

            # contentId 가져오기
            content_id_tag = disease_soup.find("a", href=lambda href: href and "contentId=" in href)
            if content_id_tag:
                content_id = content_id_tag["href"].split("=")[-1].split('.')[0]
                content_id = int(content_id)  # 문자열로 변환 후 소수점을 제거하고 정수형으로 변환
            else:
                content_id = ""

            # 관련 질환과 동의어 가져오기
            related_conditions_tag = disease_soup.find("div", class_="contBox")
            related_conditions_text = ""
            synonyms_text = ""
            if related_conditions_tag:
                related_conditions_tag = related_conditions_tag.find_all("dd")
                if len(related_conditions_tag) >= 2:
                    related_conditions_text = related_conditions_tag[0].text.strip()
                    synonyms_text = related_conditions_tag[1].text.strip()
                elif len(related_conditions_tag) == 1:
                    related_conditions_text = related_conditions_tag[0].text.strip()

            # 본문 내용 가져오기
            diet_therapy_tag = disease_soup.find("dl", class_="descDl")
            if diet_therapy_tag:
                # 각 항목을 딕셔너리로 저장
                diet_therapy_dict = {}
                for item in diet_therapy_tag.find_all(["dt", "dd"]):
                    if item.name == "dt":
                        current_key = item.text.strip()
                    elif item.name == "dd" and current_key:
                        diet_therapy_dict[current_key] = item.text.strip()

                # 결과를 리스트에 추가
                data.append([disease_name, related_conditions_text, synonyms_text,
                             diet_therapy_dict.get("식사요법의 실제", ""),
                             diet_therapy_dict.get("권장 식품", ""),
                             diet_therapy_dict.get("주의 식품", ""),
                             diet_therapy_dict.get("그 외 주의사항", ""),
                             content_id])

# CSV 파일에 결과 저장
with open("disease_data.csv", "w", encoding="utf-8-sig", newline="") as csvfile:
    writer = csv.writer(csvfile)

    # 칼럼 헤더 작성 (영어로 변경)
    headers = ["disease_specific_diet","disease_name", "synonyms", "diet_therapy", "recommended_food", "caution_food", "other_notes", "disease_id"]
    writer.writerow(headers)

    # 각 행 작성
    for row in data:
        writer.writerow(row)

print("Data has been saved to 'disease_diet.csv'")
```
- 데이터 병합  
