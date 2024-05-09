import streamlit as st
from streamlit_option_menu import option_menu

from home import run_home

def main():
    st.write('## K-Means 클러스터링 앱')

    menu = ['데이터 클러스터링 하기']
    with st.sidebar :
        st.write('# 🖥️ K-Means 클러스터링 앱')
        choice = option_menu('Use only staff', menu,
                             icons=['house','bi bi-clipboard-heart','bi bi-flower3'],
                             menu_icon='bi bi-list', default_index=0,
                             styles={
        "container": {"padding": "5!important", "background-color": "#ffffff"},
        "nav-link": {"font-size": "16px", "text-align": "left", "margin":"0px", "--hover-color": "#fff"},
        "nav-link-selected": {"background-color": "#6E6E6E"}})

        st.divider()

        st.write('''
                 ## 🖥️ 제작 동기
                 실제로 K-Means 알고리즘을 사용해 본 결과 구현이 쉽고 계산 복잡도가 낮았으며, 대용량 데이터에도
                 빠르게 적용되었습니다. 이러한 부분이 기업에서 고객 정보 데이터를 가지고 클러스터링하면
                 기업 이익에 도움이 되는 방향으로 활용할 수 있다고 생각하여 앱을 제작하였습니다.''')
        
        st.divider()

        st.write('''
                 ## 🖥️ 예상 적용 분야
                 마케팅 및 고객 세분화, 문서 클러스터링, 이미지 분할 및 처리 등 
                 다양한 분야에서 적용시킬 수 있다고 생각합니다.''')

        st.divider()

        st.write('''
                 ## 🖥️ K-Means 알고리즘의 장단점
                 > 장점 : 간단하고 이해하기 쉬워 누구나 빠르게 수행 가능하며, 대용량 데이터셋에도 적용이 가능합니다. \n
                 > 단점 : 초기 중심점에 따라 결과가 달라질 수 있어 어러번 실행하여 최적화 해야하며, 클러스터의 개수를 사전에 지정해야해서 최적의 값을 찾기 어렵습니다.''')
   
    if choice == menu[0] :
        run_home()
    else :
        pass


if __name__ == '__main__' :
    main()