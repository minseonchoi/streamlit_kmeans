<img src="https://capsule-render.vercel.app/api?type=slice&color=F5ECCE&height=150&section=header&text=streamlit_kmeans&fontSize=30" />

#### K-Means 클러스터링 앱 개발

#### 비슷한 항목끼리 묶어서 그룹으로 지정할 수 있어, 그룹 별 특징에 따라서 여러 방면으로 활용할 수 있습니다.

[K-Means 클러스터링 앱 URL : http://ec2-43-203-246-183.ap-northeast-2.compute.amazonaws.com:8503/](http://ec2-43-203-246-183.ap-northeast-2.compute.amazonaws.com:8503/)


✏️ 작업순서
-

클러스터링 할 데이터 수집 

➡︎ 데이터 가공 및 내가 작성한 코드로 K-means로 클러스터링 잘 되는지 확인 (주피터노트북 사용)

➡︎ Streamlit 프레임워크 웹 대시보드 개발 

➡︎ AWS EC2 배포




✏️ 데이터 가공
-

데이터를 받았을 때 클러스터링하기 위한 데이터 준비

1. Nan 데이터 있으면 삭제합니다.
   - 비어 있는 데이터를 확인하고 있으면 dropna()로 삭제합니다.
   - 삭제를 하고 나면, 데이터가 어지러워질 수 있기 때문에 꼭 reset_index() 를 해줍니다.

2. 컬럼의 데이터가 문자열이면, 레이블인코딩 또는 원핫인코딩을 합니다.
    - 유니크 값의 수를 구해서 2개면 레이블인코딩 2개 이상이면 원핫인코딩 합니다.




✏️ Streamlit 웹 대시보드 개발
-

파일명으로 정리했습니다.

✉︎ APP.PY
- 사이드바를 통해서 나의 웹 대시보드의 의도를 설명을 합니다.
- 제작 동기, 예상 적용 분야, K-Means 알고리즘의 장단점을 적었습니다.
  
✉︎ HOME.PY
- 데이터를 사용자에게 받아서 해당 데이터를 클러스터링 하기 때문에, 내가 지정한 K 개수 이하의 데이터를 업로드할 수 없게 개발했습니다.
- 데이터 가공하는 과정을 사용자에게 보여줘서 사용자의 이해를 돕습니다.
- 클러스터링에 사용할 컬럼은 2개 이상이어야 하기 때문에, 컬럼을 선택할 때도 2개 미만으로 선택할 경우 클러스터링 할 수 없게 개발했습니다.
- K 개수를 1부터 10개까지 해서 구한 WCSS를 차트로 보여주고 사용자는 차트를 보고 K 값을 선택할 수 있습니다.
- 나온 결과 데이터를 사용자가 저장할 수 있습니다.




✏️ 배포
-

AWS EC2에 리눅스 프리 티어를 사용해서 배포했습니다.
- Git 설치 과정과 AWS 배포 과정 블로그 정리했습니다.
- [minseonchoi의 블로그 AWS 카테고리](https://msdev-st.tistory.com/category/AWS)
  
github Actions로 EC2 리눅스에 git pull 자동화했습니다.

현재 사용하고 있는 사용자도 새로운 버전의 화면을 볼 수 있도록 서버 실행 명령어에 --server.runOnSave true를 추가했습니다.


✏️ 사용한 프로그램
-

<a href="https://jupyter.org/"><img src="https://img.shields.io/badge/jupyter-F37626?style=flat-square&logo=jupyter&logoColor=white"/></a>

<a href="https://streamlit.io/"><img src="https://img.shields.io/badge/streamlit-FF4B4B?style=flat-square&logo=streamlit&logoColor=white"/></a>

<a href="https://code.visualstudio.com/"><img src="https://img.shields.io/badge/visualstudiocode-007ACC?style=flat-square&logo=visualstudiocode&logoColor=white"/></a>

<a href="https://aws.amazon.com/ko/console/"><img src="https://img.shields.io/badge/amazonec2-FF9900?style=flat-square&logo=amazonec2&logoColor=000000"/></a>




✏️ 사용한 언어
-

[![Top Langs](https://github-readme-stats.vercel.app/api/top-langs/?username=minseonchoi&langs_count=8)](https://github.com/minseonchoi/github-readme-stats)
