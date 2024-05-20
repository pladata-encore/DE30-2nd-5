# parameter : List of String (ex) ['가래', '기침', '손발이 떨림']
# return : String of JSONArray

import pickle
from gensim.models import Word2Vec
import numpy as np


def predict_diseases(input_symptoms):
    # load ML model
    model = Word2Vec.load("C:/projects/wheresurhurt/backend/api/modules/test_240517_final.model")
    # load 'diseases' pickle
    with open('C:/projects/wheresurhurt/backend/api/modules/disease_list.pkl', 'rb') as f:
        diseases = pickle.load(f)

    # 각 증상에 대해 가장 유사한 질병과 그 유사도 찾기
    symptom_to_diseases_similarity = {}
    for symptom in input_symptoms:
        try:
            similar_words = model.wv.most_similar(symptom, topn=300)
            symptom_to_diseases_similarity[symptom] = [(word, similarity) for word, similarity in similar_words if
                                                       word in diseases]
        except KeyError:
            pass

    # 질병별로 증상과의 유사도 및 일치하는 증상 수 저장
    disease_similarity_info = {}
    for symptom, diseases_similarities in symptom_to_diseases_similarity.items():
        for disease, similarity in diseases_similarities:
            if disease in disease_similarity_info:
                disease_similarity_info[disease]['count'] += 1
                disease_similarity_info[disease]['similarities'].append(similarity)
            else:
                disease_similarity_info[disease] = {'count': 1, 'similarities': [similarity]}

    # 증상이 2개 이상 일치하는 질병 필터링 및 평균 유사도 계산
    if len(symptom_to_diseases_similarity.keys()) == 1:
        filtered_diseases = [(disease, info['count'], np.mean(info['similarities']), info['similarities'])
                             for disease, info in disease_similarity_info.items() if info['count'] >= 1]
    else:
        filtered_diseases = [(disease, info['count'], np.mean(info['similarities']), info['similarities'])
                             for disease, info in disease_similarity_info.items() if info['count'] >= 2]

    # 증상 일치 수 및 평균 유사도에 따라 정렬
    filtered_diseases.sort(key=lambda x: (x[1], x[2]), reverse=True)

    # 상위 5개 출력
    top_diseases = filtered_diseases[:5]

    result = [{"질병": disease, "일치하는 증상 수": count, "평균 유사도": avg_similarity, "증상별 유사도": similarities}
              for disease, count, avg_similarity, similarities in top_diseases]

    return str(result)
