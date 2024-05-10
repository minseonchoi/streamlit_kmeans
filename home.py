import streamlit as st
import pandas as pd
import numpy as np

from sklearn.preprocessing import LabelEncoder, OneHotEncoder
from sklearn.compose import ColumnTransformer
from sklearn.cluster import KMeans

# 리눅스 한글 폰트 설정
import platform
import matplotlib.pyplot as plt
from matplotlib import font_manager, rc
plt.rcParams['axes.unicode_minus'] = False
if platform.system() == 'Linux':
    rc('font', family='NanumGothic')


def run_home() :
    st.write('')

    st.write('''
             #### 비슷한 유형의 데이터끼리 묶어주며,
             #### 클러스터링 된 데이터를 다운받을 수 있는 앱입니다.''')
    
    st.write('')
    st.write('')

    # 1. csv 파일 업로드
    st.write('##### ✏️ 클러스터링이 필요한 파일을 업로드 합니다.')
    file = st.file_uploader('csv파일 업로드(ONLY CSV)', type=['csv'])

    if file is not None :
        
        # 1-1. 판다스의 데이터프레임으로 읽는다.
        df = pd.read_csv(file, index_col=1)

        # 1-2. 10개 미만의 파일을 올리면, 에러 처리하자
        if df.shape[0] < 10 :
            st.error('데이터의 갯수는 10개 이상이어야 합니다.')
            return

        # 1-3. 유저한테 데이터프레임 보여준다.
        else :
            st.write('업로드 파일')
            st.dataframe(df)
        
        # 2. nan 데이터 있으면, 삭제하자.
        print( df.isna().sum() )

        st.write('')
        st.write('')

        st.write('##### ✏️ 각 항목별 비어있는 데이터의 갯수 입니다.')

        st.dataframe( df.isna().sum() )

        df.dropna(inplace=True)

        # dropna 하면 reset_index 를 해줘야 한다
        df.reset_index(inplace=True)

        st.info('비어있는 데이터가 있으면 해당 데이터는 삭제합니다.')

        # 3. 유저한테 컬럼을 선택 할 수 있도록 하자.
        print( df.columns )

        st.write('')
        st.write('')

        st.write('##### ✏️ 클러스터링에 사용 할 항목을 선택합니다.')

        selected_columns = st.multiselect('X로 사용 할 컬럼을 선택하세요.', df.columns)

        X = df[ selected_columns ]

        if selected_columns == [] :
            pass
        else :
            st.dataframe( X )

        # 밑에 있는 것을 하려면 유저가 2개 이상 선택을 해야한다
        if len(selected_columns) >= 2 : 
            
            X_new = pd.DataFrame()

            print(X_new)

            # 4. 해당 컬럼의 데이터가 문자열이면, 숫자로 바꿔주자.

            for  column  in X.columns :
                
                print( X[column].dtype )

                # 컬럼의 데이터가 문자열이면, 레이블인코딩 또는 원핫인코딩 해야한다.
                if X[column].dtype == object :
                    if X[column].nunique() >= 3 :
                        # 원핫인코딩
                        column_names = sorted( X[column].unique() )
                        # 비어있는 데이터프레임에 컬럼 추가
                        X_new[column_names] = pd.get_dummies( X[column].to_frame() )
                        
                    else :
                        # 레이블인코딩
                        encoder = LabelEncoder()
                        X_new[column]= encoder.fit_transform( X[column] )

                else :
                    # 숫자 데이터 처리
                    X_new[column] = X[column]
                
            # X_new 변수가 숫자로만 되어있는 데이터프레임.
            # 4-1. 유저한테 보여주자.

            X_new.reset_index(inplace=True, drop=True)

            st.write('### ⬇︎⬇︎⬇︎')
            st.write('###### 원하는 항목의 데이터를 가공하여 클러스터링에 실제 사용 할 데이터입니다.')
            st.dataframe(X_new)

            # 5. K의 갯수를 1개부터 10개까지 해서 wcss를 구한다.
            wcss = []
            for k in np.arange(1, 10+1) :
                kmeans = KMeans(n_clusters=k, random_state=5)
                kmeans.fit(X_new)
                wcss.append(kmeans.inertia_)
                
            st.write('')
            st.write('')

            st.write('''
                     ##### ✏️ wcss를 구해서, 
                     ##### 1개부터 10개까지의 그룹으로 나누어 엘보우메소드 차트로 보여드렸습니다.
                     ''')    

            # 6. elobw method 를 이용해서. 차트로 보여준다.
            fig1 = plt.figure()
            x = np.arange(1, 10+1)
            plt.plot(x, wcss)
            plt.title('엘보우 메소드')
            plt.xlabel('클러스터의 갯수')
            plt.ylabel('WCSS')
            st.pyplot(fig1)

            st.write('''
                     #####  ✏️ 차트를 유의해서 봐야 하는 부분
                     > 엘보우 포인트 : 특정 지점에서 WCSS 값의 감소 폭이 줄어들게 되는 지점입니다. \n
                     > 이 지점 이후로는 WCSS 값의 감소 폭이 크지 않아 클러스터의 개수를 더 늘리는 것이
                     효과적이지 않다고 판단할 수 있습니다.  \n
                     > 하여, 엘보우 포인트 지점이 최적의 클러스터 개수로 간주됩니다.   
                        ''')
                
            st.write('')
            st.write('')

            # 7. 유저가 k의 갯수를 정한다.
            st.write('#####  ✏️ 클러스터의 개수는 몇 개로 설정하시겠습니까?')
            k = st.slider('차트를 보고 몇개의 그룹으로 나눌 것인지 설정하세요.', min_value=1, max_value=10)

            # 8. KMeans 수행해서 그룹정보를 가져온다.
            kmeans = KMeans(n_clusters= k, random_state= 5)
            y_pred = kmeans.fit_predict(X_new)
            
            # 9. 원래 있던 df 에 Group 이라는컬럼을 만들어준다.
            df['Group'] = y_pred

            # 저장 안함.
            ## 10. 결과를 파일로 저장한다.
            ## df.to_csv('result.csv')

            st.write('')
            st.write('')

            # 11. 유저한테 보여준다.
            st.write('##### ✏️ 클러스터링 결과 데이터 입니다.')

            st.dataframe(df)

            st.write('###### 크러스터링된 전체 데이터를 저장 할 수 있습니다.')
            # 파일 다운로드 버튼 만들기
            if st.download_button(
                label="클러스터링 데이터 다운로드",
                data=df.to_csv(index=False),
                file_name='clusters.csv',
                mime='text/csv',
                use_container_width=True):
                st.success('✔️ 파일이 다운로드 되었습니다!')

            # 12. 유저가 그룹을 선택하면, 해당 그룹의 정보를 보여준다.
            st.write('##### ✏️ 원하는 그룹을 선택하시면 해당 그룹만 출력됩니다.')
            choice = st.selectbox('그룹을 선택하세요', np.arange(0, k))

            st.dataframe(df.loc[ df['Group'] == choice , ])

            # 그룹별 통계치를 보여주자
            st.write('###### 선택한 그룹의 통계치를 확인하고 싶으면 체크박스의 내용을 확인하세요.')
            if st.checkbox('그룹 별 통계치'):
                st.dataframe(df.loc[ df['Group'] == choice , ].describe())

            # 유저가 분리된 그룹으로 된 파일로 다운 받을 수 있게 만든다.
            st.write('###### 원하는 그룹의 데이터만 저장할 수 있습니다.')
            df_choice= df.loc[ df['Group'] == choice , ].reset_index()
            if st.download_button(
                label="그룹별 클러스터링 데이터 다운로드",
                data=df_choice.to_csv(index=False),
                file_name='clusters_group.csv',
                mime='text/csv',
                use_container_width=True):
                st.success('✔️ 파일이 다운로드 되었습니다!')

        elif len(selected_columns) <= 1 :
            st.write('컬럼을 2개 이상 선택해 주세요.')
    else : 
        pass
