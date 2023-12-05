<h1> NemoNemo Logic

## 주제 설명

저희는 부산대학교 전기공학과 파이썬데이터사이언스 수업을 수강중인 팀 p2p의 김성목, 황원제, 김명수 입니다. 저희 팀은 모두 퍼즐게임을 좋아한다는 공통점이 있어 네모네모로직 이라는 게임을 GUI형태로 개발하는 것을 목표로 하여 프로젝트를 진행하였습니다. 

## 프로젝트 특징
저희팀은 게임에 필요한 로직들을 비슷한 프로젝트들에서 가져오지 않았습니다. 수업시간에 배운 오픈소스 리라이브러리를 적극 활용하여 팀원들끼리 직접 모든 로직을 구현한 점이 저희팀의 가장 큰 특징입니다.

또한 단순히 라이브러리에서 지원하는 기능을 조합하기만 한것이 아니라 라이브러리 에서 제공하는 클래스들을 wrapping하여 목적에 맞게 커스텀한 점도 또하나의 특징이라고 생각합니다.


## 사용법 설명
### 필수 패키지
pyqt5==5.15.10  
opencv-python==1.26.2    
pillow==4.8.1.78  
numpy==10.1.0    
###


1.  이 리포지토리를 클론한다. 
~~~ bash 
git clone https://github.com/myungsu7929/NemoNemoLogic
~~~

2. 클론한 폴더로 이동한다.
~~~ bash
cd ./NemoNemoLogic
~~~

3. 필요한 패키지 및 라이브러리를 설치한다.
~~~ bash
pip install -r requirements.txt
~~~

4. NemoApp.py 파일을 실행시킨다.
~~~ bash
python ./NemoApp.py
~~~

### 문제를 만들 때
1. "문제 만들기" 버튼을 클릭한다.
2. 문제 사이즈를 설정한다.
3. 그림판에 그림을 그리거나 "이미지 업로드하기" 버튼을 클릭해 원하는 이미지를 업로드 한다.  
4. "도트로 변환" 버튼을 클릭해 그림판 이미지를 도트 이미지로 변환한다.
5. "문제 저장하기 버튼을 클릭해 원하는 위치에 example.nemo 파일을 만든다.  

#### 단축키  
    C:  펜과 지우개 모드를 변경
    X:  그림판 초기화 하기
    마우스 스크롤: 펜과 지우개 굵기 조절 

### 문제를 풀때
1. "문제 불러오기" 버튼을 클릭한다. 
2. 저장해 두었던 nemo파일을 선택한다.
3. 주어진 힌트에 맞게 문제를 풀고 "정답 확인하기" 버튼을 클릭한다.

## 코드에 관한 설명
프로그램에 관한 설명

프로그램은 PyQt5 라이브러리를 기반으로하여 개발되었으며, 주요 구조는 다음과 같습니다:
### NemoApp.py (메인 어플리케이션)
PyQt5의 QStackedWidget 클래스를 상속하여 다양한 화면을 스택으로 관리합니다.
NemoHome, NemoDraw, NemoSolve와 같은 각각의 화면을 위젯으로 가지고 있습니다.

### 각 화면을 담당하는 위젯 클래스들
NemoHome: 홈 화면, 문제 만들기 또는 풀기로 이동하는 역할을 합니다.  
NemoDraw: 그림 그리기 화면, 이미지 업로드 및 도트로 변환하여 문제 생성하는 기능을 제공합니다.  
NemoSolve: 문제 풀이 화면, 문제를 불러오고 정답 확인하는 등의 기능을 수행합니다.

### 문제 생성 및 풀이 로직
NemoCanvas: PyQt5의 QGraphicsView를 상속하여 도트로 그림을 그리는 화면을 담당합니다.
Problem: 주어진 그림을 기반으로 네모네모로직 문제를 동적으로 생성합니다.
SolvingBoard: 문제 풀이 화면에서 각 네모네모에 대한 토글 버튼을 제공하고, 사용자의 풀이상태를 numpy array형태로 변환합니다.

### utils.py
이미지를 QPixmap으로 변환하는 np2pixmap, 숫자 힌트 계산 및 변환 등의 유틸리티 함수가 포함되어 있습니다.
환영 화면 및 토글 버튼 (NemoWelcome, NemoToggleButton)

### 기타
NemoWelcome: 정답 제출 후 나타나는 환영 화면입니다.  
NemoToggleButton: 네모네모를 토글하는 기능을 제공하는 토글 버튼 클래스입니다.


저희 프로그램은 다양한 클래스가 다형성을 묶여 있어 기능을 추가할때 쉽고 빠르게 작업할 수 있습니다.

