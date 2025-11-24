# import streamlit as st
# import joblib
# from model import load_model, predict
# import pandas as pd

# # 페이지 설정
# st.set_page_config(
#     page_title="소득 예측 서비스",
#     page_icon="💰",
#     layout="wide"
# )

# # 타이틀
# st.title("💰 연간 소득 예측 서비스")
# st.markdown("---")
# st.write("개인 정보를 입력하면 연간 소득이 $50K를 초과할 확률을 예측합니다.")

# # 모델 로드 (캐싱)
# @st.cache_resource
# def get_model():
#     try:
#         return load_model("model.pkl")
#     except Exception as e:
#         st.error(f"모델 로드 실패: {e}")
#         return None

# model = get_model()

# st.markdown("---")

# # 입력 폼
# with st.form("prediction_form"):
#     st.header("📝 개인 정보 입력")
    
#     # 3개 컬럼으로 나누기
#     col1, col2, col3 = st.columns(3)
    
#     with col1:
#         st.subheader("기본 정보")
#         age = st.number_input("나이 (Age)", min_value=17, max_value=90, value=38, step=1)
        
#         workclass = st.selectbox(
#             "근무 형태 (Workclass)",
#             options=[0, 1, 2, 3, 4, 5, 6, 7],
#             format_func=lambda x: [
#                 "Private", "Self-emp-not-inc", "Self-emp-inc", 
#                 "Federal-gov", "Local-gov", "State-gov", 
#                 "Without-pay", "Never-worked"
#             ][x]
#         )
        
#         fnlwgt = st.number_input(
#             "인구 가중치 (Final Weight)", 
#             min_value=0, 
#             max_value=1500000, 
#             value=200000,
#             step=1000
#         )
        
#         education = st.selectbox(
#             "최종 학력 (Education)",
#             options=[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15],
#             format_func=lambda x: [
#                 "Preschool", "1st-4th", "5th-6th", "7th-8th", "9th",
#                 "10th", "11th", "12th", "HS-grad", "Some-college",
#                 "Assoc-voc", "Assoc-acdm", "Bachelors", "Masters",
#                 "Prof-school", "Doctorate"
#             ][x]
#         )
        
#         education_num = st.number_input(
#             "교육 연수 (Education Number)", 
#             min_value=1, 
#             max_value=16, 
#             value=10,
#             step=1
#         )
    
#     with col2:
#         st.subheader("가족 및 직업")
#         marital_status = st.selectbox(
#             "결혼 상태 (Marital Status)",
#             options=[0, 1, 2, 3, 4, 5, 6],
#             format_func=lambda x: [
#                 "Married-civ-spouse", "Divorced", "Never-married",
#                 "Separated", "Widowed", "Married-spouse-absent",
#                 "Married-AF-spouse"
#             ][x]
#         )
        
#         occupation = st.selectbox(
#             "직업 (Occupation)",
#             options=[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14],
#             format_func=lambda x: [
#                 "Tech-support", "Craft-repair", "Other-service",
#                 "Sales", "Exec-managerial", "Prof-specialty",
#                 "Handlers-cleaners", "Machine-op-inspct", "Adm-clerical",
#                 "Farming-fishing", "Transport-moving", "Priv-house-serv",
#                 "Protective-serv", "Armed-Forces", "Unknown"
#             ][x]
#         )
        
#         relationship = st.selectbox(
#             "가족 관계 (Relationship)",
#             options=[0, 1, 2, 3, 4, 5],
#             format_func=lambda x: [
#                 "Wife", "Own-child", "Husband", "Not-in-family",
#                 "Other-relative", "Unmarried"
#             ][x]
#         )
        
#         race = st.selectbox(
#             "인종 (Race)",
#             options=[0, 1, 2, 3, 4],
#             format_func=lambda x: [
#                 "White", "Asian-Pac-Islander", "Amer-Indian-Eskimo",
#                 "Other", "Black"
#             ][x]
#         )
        
#         sex = st.selectbox(
#             "성별 (Sex)",
#             options=[0, 1],
#             format_func=lambda x: ["Female", "Male"][x]
#         )
    
#     with col3:
#         st.subheader("경제 정보")
#         capital_gain = st.number_input(
#             "자본 이득 (Capital Gain)", 
#             min_value=0, 
#             max_value=100000, 
#             value=0,
#             step=100
#         )
        
#         capital_loss = st.number_input(
#             "자본 손실 (Capital Loss)", 
#             min_value=0, 
#             max_value=5000, 
#             value=0,
#             step=50
#         )
        
#         hours_per_week = st.number_input(
#             "주당 근무 시간 (Hours per Week)", 
#             min_value=1, 
#             max_value=100, 
#             value=40,
#             step=1
#         )
        
#         native_country = st.selectbox(
#             "출신 국가 (Native Country)",
#             options=[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 
#                      15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 
#                      27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40],
#             format_func=lambda x: [
#                 "United-States", "Cambodia", "England", "Puerto-Rico",
#                 "Canada", "Germany", "Outlying-US", "India", "Japan",
#                 "Greece", "South", "China", "Cuba", "Iran", "Honduras",
#                 "Philippines", "Italy", "Poland", "Jamaica", "Vietnam",
#                 "Mexico", "Portugal", "Ireland", "France", "Dominican-Republic",
#                 "Laos", "Ecuador", "Taiwan", "Haiti", "Columbia", "Hungary",
#                 "Guatemala", "Nicaragua", "Scotland", "Thailand", "Yugoslavia",
#                 "El-Salvador", "Trinidad&Tobago", "Peru", "Hong", "Holland-Netherlands"
#             ][x] if x < 41 else "Other"
#         )
    
#     st.markdown("---")
    
#     # 제출 버튼
#     submitted = st.form_submit_button("🔍 소득 예측하기", type="primary", use_container_width=True)

# # 예측 수행
# if submitted:
#     if model is None:
#         st.error("⚠️ 모델이 로드되지 않았습니다. model.pkl 파일을 확인해주세요.")
#     else:
#         # 입력 데이터 준비 (id 제외)
#         input_data = {
#             'age': age,
#             'workclass': workclass,
#             'fnlwgt': fnlwgt,
#             'education': education,
#             'education.num': education_num,
#             'marital.status': marital_status,
#             'occupation': occupation,
#             'relationship': relationship,
#             'race': race,
#             'sex': sex,
#             'capital.gain': capital_gain,
#             'capital.loss': capital_loss,
#             'hours.per.week': hours_per_week,
#             'native.country': native_country
#         }
        
#         try:
#             # 예측
#             with st.spinner("예측 중..."):
#                 prediction, probability = predict(model, input_data)
            
#             st.markdown("---")
#             st.header("📊 예측 결과")
            
#             # 결과 표시
#             col1, col2, col3 = st.columns(3)
            
#             with col1:
#                 st.metric(
#                     label="예측 소득 구간",
#                     value="≤$50K" if prediction == 0 else ">$50K",
#                     delta="낮은 소득" if prediction == 0 else "높은 소득"
#                 )
            
#             with col2:
#                 st.metric(
#                     label="≤$50K 확률",
#                     value=f"{probability[0]:.2%}"
#                 )
            
#             with col3:
#                 st.metric(
#                     label=">$50K 확률",
#                     value=f"{probability[1]:.2%}"
#                 )
            
#             # 프로그레스 바
#             st.subheader("소득 구간별 확률")
#             st.progress(float(probability[1]), text=f">$50K 확률: {probability[1]:.2%}")
            
#             # 상세 정보
#             with st.expander("📋 입력 데이터 확인"):
#                 df_display = pd.DataFrame([input_data])
#                 st.dataframe(df_display, use_container_width=True)
            
#             # 해석
#             if probability[1] > 0.7:
#                 st.success("✅ 연간 소득이 $50,000를 초과할 가능성이 **매우 높습니다**!")
#             elif probability[1] > 0.5:
#                 st.info("📌 연간 소득이 $50,000를 초과할 가능성이 **높습니다**.")
#             else:
#                 st.warning("⚠️ 연간 소득이 $50,000 이하일 가능성이 **높습니다**.")
                
#         except Exception as e:
#             st.error(f"❌ 예측 중 오류가 발생했습니다: {e}")

# # 사이드바
# with st.sidebar:
#     st.header("ℹ️ 사용 안내")
#     st.markdown("""
#     ### 데이터 입력 방법
#     1. **기본 정보**: 나이, 근무 형태, 학력 등
#     2. **가족 및 직업**: 결혼 상태, 직업, 관계 등
#     3. **경제 정보**: 자본 이득/손실, 근무 시간 등
    
#     ### 예측 결과
#     - **≤$50K**: 연간 소득 5만 달러 이하
#     - **>$50K**: 연간 소득 5만 달러 초과
    
#     ### 주의사항
#     - 모든 값을 정확히 입력해주세요
#     - 예측 결과는 참고용입니다
#     """)
    
#     st.markdown("---")
#     st.caption("🤖 Powered by Machine Learning")

# UI 변경 버전 - 1

# import streamlit as st
# import pandas as pd
# from model import load_model, predict

# # 페이지 기본 설정
# st.set_page_config(
#     page_title="소득 예측 서비스",
#     page_icon="💰",
#     layout="wide"
# )

# #  CSS
# st.markdown("""
#     <style>
#         .stForm {
#             max-height: 650px; 
#             overflow: visible !important;
#             padding-bottom: 10px !important;
#         }
#         .block-container {
#             padding-top: 1rem;
#             padding-bottom: 1rem;
#         }
#         .stForm label {
#             font-size: 0.90rem;
#             margin-bottom: 0.2rem;
#         }
#     </style>
# """, unsafe_allow_html=True)


# st.title("💰 연간 소득 예측 서비스")
# st.caption("왼쪽에 입력하고 오른쪽에서 예측 결과가 표시됩니다.")
# st.markdown("---")


# # ===========================
# # 모델 로드
# # ===========================
# @st.cache_resource
# def get_model():
#     return load_model("model.pkl")

# model = get_model()


# # ===========================
# # 좌/우 레이아웃
# # ===========================
# left, right = st.columns([0.8, 1.2])


# # ===========================
# # LEFT: 입력 FORM
# # ===========================
# with left:
#     st.subheader("📝 입력 정보")

#     form = st.form("prediction_form")  # ★ form 객체 선언

#     form.markdown("### 기본 정보")
#     age = form.number_input("나이 (Age)", 17, 90, 38)

#     workclass = form.selectbox(
#         "근무 형태 (Workclass)",
#         options=list(range(8)),
#         format_func=lambda x: [
#             "Private", "Self-emp-not-inc", "Self-emp-inc",
#             "Federal-gov", "Local-gov", "State-gov",
#             "Without-pay", "Never-worked"
#         ][x]
#     )

#     fnlwgt = form.number_input("인구 가중치 (Final Weight)", 0, 1500000, 200000, 1000)

#     education = form.selectbox(
#         "최종 학력 (Education)",
#         options=list(range(16)),
#         format_func=lambda x: [
#             "Preschool", "1st-4th", "5th-6th", "7th-8th", "9th",
#             "10th", "11th", "12th", "HS-grad", "Some-college",
#             "Assoc-voc", "Assoc-acdm", "Bachelors", "Masters",
#             "Prof-school", "Doctorate"
#         ][x]
#     )

#     education_num = form.number_input("교육 연수 (Education-num)", 1, 16, 10)


#     form.markdown("### 가족 및 직업 정보")
#     marital_status = form.selectbox(
#         "결혼 상태 (Marital Status)",
#         options=list(range(7)),
#         format_func=lambda x: [
#             "Married-civ-spouse", "Divorced", "Never-married",
#             "Separated", "Widowed", "Married-spouse-absent",
#             "Married-AF-spouse"
#         ][x]
#     )

#     occupation = form.selectbox(
#         "직업 (Occupation)",
#         options=list(range(15)),
#         format_func=lambda x: [
#             "Tech-support", "Craft-repair", "Other-service",
#             "Sales", "Exec-managerial", "Prof-specialty",
#             "Handlers-cleaners", "Machine-op-inspct", "Adm-clerical",
#             "Farming-fishing", "Transport-moving", "Priv-house-serv",
#             "Protective-serv", "Armed-Forces", "Unknown"
#         ][x]
#     )

#     relationship = form.selectbox(
#         "가족 관계 (Relationship)",
#         options=list(range(6)),
#         format_func=lambda x: [
#             "Wife", "Own-child", "Husband",
#             "Not-in-family", "Other-relative", "Unmarried"
#         ][x]
#     )

#     race = form.selectbox(
#         "인종 (Race)",
#         options=list(range(5)),
#         format_func=lambda x: [
#             "White", "Asian-Pac-Islander", "Amer-Indian-Eskimo",
#             "Other", "Black"
#         ][x]
#     )

#     sex = form.selectbox(
#         "성별 (Sex)",
#         options=[0, 1],
#         format_func=lambda x: ["Female", "Male"][x]
#     )


#     form.markdown("### 경제 정보")
#     capital_gain = form.number_input("자본 이득 (Capital Gain)", 0, 100000, 0, 100)
#     capital_loss = form.number_input("자본 손실 (Capital Loss)", 0, 5000, 0, 50)
#     hours_per_week = form.number_input("주당 근무 시간", 1, 100, 40)

#     native_country = form.selectbox(
#         "출신 국가",
#         options=list(range(41)),
#         format_func=lambda x: [
#             "United-States", "Cambodia", "England", "Puerto-Rico", "Canada",
#             "Germany", "Outlying-US", "India", "Japan", "Greece", "South",
#             "China", "Cuba", "Iran", "Honduras", "Philippines", "Italy",
#             "Poland", "Jamaica", "Vietnam", "Mexico", "Portugal", "Ireland",
#             "France", "Dominican-Republic", "Laos", "Ecuador", "Taiwan",
#             "Haiti", "Columbia", "Hungary", "Guatemala", "Nicaragua",
#             "Scotland", "Thailand", "Yugoslavia", "El-Salvador",
#             "Trinidad&Tobago", "Peru", "Hong", "Holland-Netherlands"
#         ][x] if x < 41 else "Other"
#     )

#     form.markdown("----")

#     # ★ submit 버튼 — 반드시 form 안에 있어야 함
#     submitted = form.form_submit_button("예측하기", use_container_width=True)



# # ===========================
# # RIGHT: 예측 결과
# # ===========================
# with right:
#     st.subheader("📊 예측 결과")

#     if not submitted:
#         st.info("왼쪽에서 정보를 입력하고 '예측하기' 버튼을 눌러주세요.")
#     else:
#         # 입력 데이터 dict 구성
#         input_data = {
#             'age': age, 'workclass': workclass, 'fnlwgt': fnlwgt,
#             'education': education, 'education.num': education_num,
#             'marital.status': marital_status, 'occupation': occupation,
#             'relationship': relationship, 'race': race, 'sex': sex,
#             'capital.gain': capital_gain, 'capital.loss': capital_loss,
#             'hours.per.week': hours_per_week, 'native.country': native_country
#         }

#         with st.spinner("예측 중..."):
#             prediction, probability = predict(model, input_data)

#         st.metric("예측 소득 구간",
#                   "≤ $50K" if prediction == 0 else "> $50K")

#         st.metric(">$50K 확률",
#                   f"{probability[1]:.2%}")

#         st.progress(probability[1])

#         st.markdown("---")
#         st.markdown("#### 입력 정보")
#         st.dataframe(pd.DataFrame([input_data]))

# UI 변경 버전 - 2

import streamlit as st
import pandas as pd
from model import load_model, predict

# ============================
# 페이지 설정
# ============================
st.set_page_config(
    page_title="소득 예측 서비스 (Step UI)",
    page_icon="💰",
    layout="wide"
)

st.title("💬 단계별 소득 예측 서비스")
st.caption("아래 단계를 순서대로 진행해 소득 예측을 완료하세요.")
st.markdown("---")

# ============================
# 모델 로드
# ============================
@st.cache_resource
def get_model():
    return load_model("model.pkl")

model = get_model()


# ============================
# Session State 초기화
# ============================
if "step" not in st.session_state:
    st.session_state.step = 1

if "data" not in st.session_state:
    st.session_state.data = {}


# ============================
# Step 이동 함수
# ============================
def go_next():
    st.session_state.step += 1

def go_back():
    st.session_state.step -= 1


# =========================================================
# STEP 1 — 기본 정보
# =========================================================
if st.session_state.step == 1:
    st.header("📘 STEP 1 — 기본 정보 입력")

    age = st.number_input("나이 (Age)", 17, 90, 38)
    workclass = st.selectbox(
        "근무 형태 (Workclass)",
        options=list(range(8)),
        format_func=lambda x: [
            "Private", "Self-emp-not-inc", "Self-emp-inc",
            "Federal-gov", "Local-gov", "State-gov",
            "Without-pay", "Never-worked"
        ][x]
    )
    fnlwgt = st.number_input("인구 가중치 (Final Weight)", 0, 1500000, 200000, 1000)
    education = st.selectbox(
        "최종 학력 (Education)",
        options=list(range(16)),
        format_func=lambda x: [
            "Preschool", "1st-4th", "5th-6th", "7th-8th", "9th",
            "10th", "11th", "12th", "HS-grad", "Some-college",
            "Assoc-voc", "Assoc-acdm", "Bachelors", "Masters",
            "Prof-school", "Doctorate"
        ][x]
    )
    education_num = st.number_input("교육 연수 (Education-num)", 1, 16, 10)

    if st.button("다음 단계 ➡️", use_container_width=True):
        st.session_state.data.update({
            "age": age,
            "workclass": workclass,
            "fnlwgt": fnlwgt,
            "education": education,
            "education.num": education_num
        })
        go_next()


# =========================================================
# STEP 2 — 가족 및 직업 정보
# =========================================================
elif st.session_state.step == 2:
    st.header("📗 STEP 2 — 가족 및 직업 정보")

    marital_status = st.selectbox(
        "결혼 상태 (Marital Status)",
        options=list(range(7)),
        format_func=lambda x: [
            "Married-civ-spouse", "Divorced", "Never-married",
            "Separated", "Widowed", "Married-spouse-absent",
            "Married-AF-spouse"
        ][x]
    )

    occupation = st.selectbox(
        "직업 (Occupation)",
        options=list(range(15)),
        format_func=lambda x: [
            "Tech-support", "Craft-repair", "Other-service",
            "Sales", "Exec-managerial", "Prof-specialty",
            "Handlers-cleaners", "Machine-op-inspct", "Adm-clerical",
            "Farming-fishing", "Transport-moving", "Priv-house-serv",
            "Protective-serv", "Armed-Forces", "Unknown"
        ][x]
    )

    relationship = st.selectbox(
        "가족 관계 (Relationship)",
        options=list(range(6)),
        format_func=lambda x: [
            "Wife", "Own-child", "Husband",
            "Not-in-family", "Other-relative", "Unmarried"
        ][x]
    )

    race = st.selectbox(
        "인종 (Race)",
        options=list(range(5)),
        format_func=lambda x: [
            "White", "Asian-Pac-Islander", "Amer-Indian-Eskimo",
            "Other", "Black"
        ][x]
    )

    sex = st.selectbox(
        "성별 (Sex)",
        options=[0, 1],
        format_func=lambda x: ["Female", "Male"][x]
    )

    col1, col2 = st.columns(2)

    if col1.button("⬅️ 이전 단계", use_container_width=True):
        go_back()

    if col2.button("다음 단계 ➡️", use_container_width=True):
        st.session_state.data.update({
            "marital.status": marital_status,
            "occupation": occupation,
            "relationship": relationship,
            "race": race,
            "sex": sex
        })
        go_next()


# =========================================================
# STEP 3 — 경제 정보
# =========================================================
elif st.session_state.step == 3:
    st.header("📙 STEP 3 — 경제 정보 입력")

    capital_gain = st.number_input("자본 이득 (Capital Gain)", 0, 100000, 0, 100)
    capital_loss = st.number_input("자본 손실 (Capital Loss)", 0, 5000, 0, 50)
    hours_per_week = st.number_input("주당 근무 시간", 1, 100, 40)

    native_country = st.selectbox(
        "출신 국가",
        options=list(range(41)),
        format_func=lambda x: [
            "United-States", "Cambodia", "England", "Puerto-Rico",
            "Canada", "Germany", "Outlying-US", "India", "Japan",
            "Greece", "South", "China", "Cuba", "Iran", "Honduras",
            "Philippines", "Italy", "Poland", "Jamaica", "Vietnam",
            "Mexico", "Portugal", "Ireland", "France", "Dominican-Republic",
            "Laos", "Ecuador", "Taiwan", "Haiti", "Columbia", "Hungary",
            "Guatemala", "Nicaragua", "Scotland", "Thailand", "Yugoslavia",
            "El-Salvador", "Trinidad&Tobago", "Peru", "Hong",
            "Holland-Netherlands"
        ][x] if x < 41 else "Other"
    )

    col1, col2 = st.columns(2)

    if col1.button("⬅️ 이전 단계", use_container_width=True):
        go_back()

    if col2.button("예측하기 🚀", use_container_width=True):
        st.session_state.data.update({
            "capital.gain": capital_gain,
            "capital.loss": capital_loss,
            "hours.per.week": hours_per_week,
            "native.country": native_country
        })
        go_next()


# =========================================================
# STEP 4 — 예측 결과
# =========================================================
elif st.session_state.step == 4:
    st.header("📊 STEP 4 — 예측 결과")

    input_df = pd.DataFrame([st.session_state.data])

    with st.spinner("예측 중..."):
        prediction, prob = predict(model, st.session_state.data)

    st.metric("예측 소득 구간", "≤ $50K" if prediction == 0 else "> $50K")
    st.metric(">$50K 확률", f"{prob[1]:.2%}")

    st.progress(prob[1])

    st.markdown("---")
    st.subheader("📋 입력 데이터 확인")
    st.dataframe(input_df, use_container_width=True)

    if st.button("🔄 처음으로 돌아가기", use_container_width=True):
        st.session_state.step = 1
        st.session_state.data = {}
