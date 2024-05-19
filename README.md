# 증상 기반 질병 예측 프로젝트 - 어디아파?

<br />

**사용언어** <br />
<p align="center">  <img src="https://github.com/pladata-encore/DE30-3-personal_book_recommendation/assets/161932948/ef3a4384-7c35-45a3-a114-21f23830c499" align="center" width="32%">  <img src="https://velog.velcdn.com/images/devysy55/post/df11f6c5-2a12-40b0-80e2-6ab9baf2cbfb/image.png" align="center" width="32%">  <img src="https://velog.velcdn.com/images/devysy55/post/9b1d770b-25bc-47f0-8041-df988e35c44f/image.png" align="center" width="12%">  </p>



**사용 라이브러리**
   - `sklearn`,`konlpy`, `gensim`
   - `pandas`, `numpy`, `csv`, `json`, `pickle`
   - `matplotlib`, `os`
   
**작업 툴**
   - `Jupyter Lab`
   - `VScode`
   
#  Members 
| 윤소영 | 김희수 | 김민승 |  이선경|
|---|---|---|---|
| <img src='https://velog.velcdn.com/images/devysy55/post/3216254e-5711-4ed8-9edb-42c660ab0a7f/image.gif' width=150px></img> |  <img src='https://velog.velcdn.com/images/devysy55/post/a4f8ca44-9a19-4d2b-85db-a9718b7e7bc9/image.gif' width=150px></img> | <img src='https://velog.velcdn.com/images/devysy55/post/2c90da31-4818-4978-9fb1-c57309a21414/image.gif' width=150px></img> |<img src='https://velog.velcdn.com/images/devysy55/post/b257a753-97cf-4483-9a81-a8ffba96d3e6/image.gif' width=150px></img> |
# 프로젝트 개요
<img src='https://velog.velcdn.com/images/devysy55/post/ceb0e670-8865-47d8-816d-99d480032e13/image.png' width=500px></img>

## 🏣 프로젝트 소개
질병 별 증상정보를 수집하여 수집된 데이터를 기반으로 자연어로 된 증상정보에서 증상을 추출하고 질병을 예측합니다. 예측된 질병 중 사용자가 원하는 질병의 정보를 제공합니다.
### 서비스 시연
<img src='https://velog.velcdn.com/images/devysy55/post/e197b2b8-458d-4872-8c1b-209e0f90088c/image.png' width=600px></img>

앱 영상 gif로 첨부

## 💻 프로젝트 구조
![](https://velog.velcdn.com/images/devysy55/post/ec2abad6-0ce8-4e9c-95ea-dd4987c8d42d/image.png)


## ⭐ 프로젝트 목표

- 한국어 자연어 처리 및 문장 유사도 분석 능력 향상
- 증상 기반 질병 예측 모델 제작

## 📖 프로젝트 기획

- 피그마를 활용한 브레인스토밍 및 기초 플로우 기획
![](https://velog.velcdn.com/images/devysy55/post/e940260c-42d4-4c88-a77e-5df0e5befeb6/image.png)
<br>
- 구글 공유문서를 활용한 데이터 기획
<img src='https://velog.velcdn.com/images/devysy55/post/6ace71b5-bc5f-4058-9911-4e576ef9913a/image.png' width=500px></img>


 
***
# 데이터 수집
 
## ✨수집 기준
 
희수가 작성한 부분 넣기

## 🧬질병 기본 정보 및 디테일 정보
### 질병 기본 정보
#### 윤소영
<img src='https://velog.velcdn.com/images/devysy55/post/d8b442d1-f41d-48fb-9712-a9e5fa99fdbb/image.png' width=500px>

- 아산병원 질환백과의 질환별 질한 리스트에서 "증상", "관련질환", "진료과", "동의어"를 크롤링하였습니다.
- 질병별 제공 정보의 종류가 유동적이라는 문제가 있었습니다. 이를 해결하기 위해 CSS 선택자를 복합 선택자로 구성하여 구체적인 조건을 주어 크롤링하였습니다. ex) `symptoms_elem = disease.select_one('dt:contains("증상") + dd')`



### 디테일 정보 
#### 이선경

## 🩺증상정보 
#### 윤소영
- 미리 수집한 증상 기본 정보 파일 속 증상id 데이터를 활용하여 수집
<img src='https://velog.velcdn.com/images/devysy55/post/598738fb-ceae-48a4-a17d-36b57006ae3c/image.png' width=300px>

## 🍉식사요법 정보
#### 김희수


## 🌟파일 병합
### 이선경

---
# 모델링
![](https://velog.velcdn.com/images/devysy55/post/69ac48c7-a07c-401b-b588-20b2df025a8f/image.png)


1. 증상추출 모델
- 모델 선정 이유
- Input & Output
- 모델 설명

2. 질병예측모델(Word2Vec Model)
- 모델 선정 이유
- Input & Output
- 모델 설명

## 1. 증상추출 모델

### 모델 선정 이유
- 자연어로 입력 받은 증상설명에서 증상명을 추출하는 것을 목표로 모델을 제작하였습니다.
- 아산병원 증상백과에서 증상, 증상설명 쌍으로 된 정보를 크롤링하여 데이터를 준비하였습니다.
- 증상추출 과정에서 2가지 어려움이 있었습니다.
  - 증상 표현의 다양성 - 데이터 부족
  - 한국어 자연어 처리 자료 부족 및 복잡성
- 이를 해결하기 위해 역번역(back translation) 데이터를 증강하였고 형태소 분석과 벡터화를 진행하였습니다.
  - 형태소 분석: KoNLPy의 Kkma 형태소 분석기를 활용하여 증상 설명을 형태소 단위로 분석하고 토큰화하였습니다.(Kkma 선정 이유에 대해서는 블로그에 따로 정리하였습니다.)
  - TF-IDF 벡터화: 단어의 중요도를 반영하는 가중치를 계산하여, 각 문서에서의 단어의 중요성을 수치화하였습니다.
- 위 작업을 통해 생성된 TF-IDF matrix을 활용하여 사용자가 입력한 증상설명에서 유사도가 높은 증상명을 추출합니다.

### Input & Output
#### Input
- 증상설명 데이터

#### Output
- 유사도가 임계치보다 높은 증상명 상위 10개
- 임계치는 테스트 후 0.35로 결정
![](https://velog.velcdn.com/images/devysy55/post/f9cab2d4-b569-4dc8-9ac6-ac5289065d37/image.png)




### 모델 설명
- 모델의 작동 방식은 다음과 같습니다.
  1. 증상설명을 문장형으로 입력받습니다. 복수의 증상설명 입력시 ","으로 구분합니다.  
  2. 입력받은 증상설명과 TF-IDF matrix로 구성된 증상의 유사도를 구합니다.
  3. 유사도가 임계치보다 높은 증상을 유사도 높은 순서로 정렬 후 상위 5개를 알려줍니다.

## 2. 질병예측모델(Word2Vec Model)

### 모델 선정 이유
- 증상정보로 질병 예측 시 데이터 부족의 어려움이 있었습니다.
- 이러한 문제를 해결하기 위해, 우리는 데이터의 양을 증가시키고 모델 학습에 적합한 형태의 데이터셋을 생성하기로 결정했습니다. 
- 이 과정에서 다양한 모델의 효율성과 정확성을 비교하여  Word2Vec 모델을 선택하였습니다.
  - Word2Vec은 단어 간의 관계를 벡터 공간에 표현함으로써, 단어들 사이의 의미적 유사성을 학습할 수 있게 해 줍니다. 
  - 이는 매우 부족한 데이터를 활용함에 있어 데이터 증강을 효율적으로 할 수 있었고 질병과 증상 사이의 관계를 모델링하는 데 있어 매우 유용하였습니다.
  - 참고 논문: 김민정, 조인휘 "입력 데이터 형식 및 Positive/Negative에 따른 한국어 증상 기반 질병 예측 모델"

### Input & Output
#### Input
- 모델 학습을 위해, 질병과 증상의 쌍으로 데이터셋이 필요하였고 데이터 증강이 필요하였습니다. 이를 위해 2가지 작업을 하였습니다.
  - 질병 증상 추가 추출
    - 아산병원 질환백과는 아래 이미지와 같이 2가지 형태로증상 정보를 제공합니다  ![](https://velog.velcdn.com/images/devysy55/post/75d21821-0bd5-4820-89fb-f10f6bec8841/image.png)
    - 글로 된 증상정보에서 미리 준비된 증상 데이터의 증상명이 있는 경우, 증상을 추가로 추출하여 증상 데이터를 증가 시켰습니다.

  - 다양한 형태의 데이터 배치로 데이터 확장 
    - 참고 논문 속 내용을 바탕으로 데이터를 아래 이미지와 같이 2가지 형태로 배치하여 데이터를 확장하였습니다.
    ![](https://velog.velcdn.com/images/devysy55/post/a49b5031-e860-4576-a971-bad79d4833b9/image.png)

    - ex) 인플루엔자(Influenza), 오한, 열, 설사, 근육통, 구토, 목의 통증, 두통, 인플루엔자(Influenza), 오한, 인플루엔자(Influenza), 열, 인플루엔자(Influenza), 설사, 인플루엔자(Influenza), 근육통 ...

#### Output
- 모델의 출력은 특정 증상을 입력했을 때 해당 증상과 관련된 가능한 질병들을 예측하는 것입니다. 
- 증상은 리스트 형태로 입력할 수 있으며 입력된 증상별 유사도를 계산하여 평균이 높은 5개의 질병이 추출됩니다.
  - 추가적으로 일치하는 증상 수, 평균 유사도, 증상별 유사도가 제공됩니다. 
- ex) 구토, 가래 입력 시 결과 
![](https://velog.velcdn.com/images/devysy55/post/8441b098-14b9-4f33-98db-0f2c631a3054/image.png)


#### 모델 설명
- 모델의 작동 방식은 다음과 같습니다.
  1. 증상을 리스트 형태로 입력받습니다.
  2. 입력받은 증상과 질병별 유사도를 구합니다.
  3. 평균 유사도가 높은 질병을 유사도 높은 순서로 정렬 후 상위 5개를 알려줍니다.
  
  
# App
![](https://velog.velcdn.com/images/devysy55/post/892d6cfe-451f-477b-9b72-8d84b1453e2f/image.png)
