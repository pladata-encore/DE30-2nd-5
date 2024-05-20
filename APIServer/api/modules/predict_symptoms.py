# parameter : String (ex) "가래, 기침, 손발이 떨림"
# return : JSONArray

import os
import pickle
from sklearn.metrics.pairwise import cosine_similarity
from konlpy.tag import Kkma
import numpy as np


def predict_symptoms(input_value_raw):
    # setting environment variable 'JAVA_HOME' for konlpy
    os.environ['JAVA_HOME'] = 'C:\Program Files\Java\jdk-17'

    kkma = Kkma()

    # load 'symptoms' pickle
    with open('C:/projects/wheresurhurt/backend/api/modules/processed_data.pkl', 'rb') as f:
        data, tokenized_symptoms, tfidf_matrix, vectorizer = pickle.load(f)

    input_values = input_value_raw.split(",")

    # selected_symptoms_info 리스트 초기화: 선택된 증상 정보를 저장합니다.
    selected_symptoms_info = []

    # selected_symptoms_id_set 집합 초기화: 선택된 증상의 ID를 저장하여 중복을 방지합니다.
    selected_symptoms_id_set = set()

    # 형태소 분석을 통해 입력 값을 토큰화
    input_tokenized = [" ".join(kkma.morphs(input_value)) for input_value in input_values]

    for input_value, input_tok in zip(input_values, input_tokenized):
        for index, row in data.iterrows():
            symptom = row['symptoms']
            if symptom in input_value:
                # symptoms이 완전히 일치하는 경우에 대해 처리
                if row['symptom_ids'] not in selected_symptoms_id_set:
                    selected_symptoms_info.append((symptom, 1.0, row['symptom_ids'], row['symptom_describe']))
                    selected_symptoms_id_set.add(row['symptom_ids'])

        # 타겟 문장의 TF-IDF 벡터화
        target_vector = vectorizer.transform([input_tok])

        # 증상과 타겟 문장 간의 유사도 계산
        similarities = cosine_similarity(tfidf_matrix, target_vector)

        # 유사도를 리스트로 변환
        similarity_list = similarities.flatten()

        # 유사도 임계값 설정
        similarity_threshold = 0.35

        # 유사도 리스트를 내림차순으로 정렬된 인덱스로 변환
        sorted_indices = np.argsort(similarity_list)[::-1]

        # 유사도 기반으로 상위 10개의 증상 선택
        top_indices = similarity_list.argsort()[-10:][::-1]  # 상위 10개의 인덱스를 유사도 기준으로 내림차순 정렬
        for idx in top_indices:
            if similarity_list[idx] > similarity_threshold:  # 유사도가 0보다 큰 경우만 처리
                symptom = data.loc[idx, 'symptoms']
                if data.loc[idx, 'symptom_ids'] not in selected_symptoms_id_set:
                    selected_symptoms_info.append((symptom, similarity_list[idx], data.loc[idx, 'symptom_ids'], data.loc[idx, 'symptom_describe']))
                    selected_symptoms_id_set.add(data.loc[idx, 'symptom_ids'])

    # 최종적으로 selected_symptoms_info에는 중복되지 않은 증상 정보가 최대 10개까지 저장됩니다.
    response = []
    for i, (symptom, similarity, symptom_id, symptom_description) in enumerate(selected_symptoms_info, 1):
        response.append({
            "symptom": symptom,
            "symptom_id": symptom_id,
            "similarity": similarity,
            "symptom_description": symptom_description
        })

    # similarity 값 기준으로 내림차순 정렬
    response = sorted(response, key=lambda x: x['similarity'], reverse=True)

    if not response:
        return None

    return response
