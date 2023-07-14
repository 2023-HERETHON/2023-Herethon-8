## 🏥2023 여기톤 team 8 "WELLNEVE"🏥


2023 여기톤의 주제 중 하나인 "여성을 위한" 서비스, 여성 병원 전문 서비스를 제작했습니다
<br/> (서비스명)은 사용자가 원하는 조건의 여성병원을 필터링해 지도상에서 검색이 가능합니다. 
지인 소개와 인터넷 검색에 의존한 블확실한 여성병원 찾기가 아닌 똑똑하고, 효율적으로 여성병원 정보를 제공합니다.
<br/>
더불어 내 몸이 보내는 작은 여성 질환 신호라도 <br/>
언제나 의료 전문가에게 물어볼 수 있는 "1:1 전문가 QnA를 제공합니다.


### ✨ 기능
**(서비스명)**가 제공하는 기능은 다음과 같습니다.
1. 지역, 여성 전문의 여부, 휴무여부에 따른 필터링 검색
2. 검색한 병원에 대한 유저들의 생생한 리뷰
3. 원하는 병원에 대한 예약 서비스
4. 사소한 증상도 물어볼 수 있는 전문가 QnA 서비스

<br>
<hr>
<br>

## ✨ 팀원 소개

<table border="" cellspacing="0" cellpadding="0" width="100%">
    <tr width="100%">
        <td align="center"><a href= "https://github.com/jihyxxg">김지형</a></td>
        <td align="center"><a href= "https://github.com/won0324">권희원</a></td>
        <td  align="center"><a href= "https://github.com/OHseugyeon">오승연</a></td>
        <td  align="center"><a href= "https://github.com/7beunseo">김은서</a></td>
        <td  align="center"><a href= "https://github.com/LGAIN">이가인</a></td>
        <td  align="center"><a href= "https://github.com/newoceanwave">이서현</a></td>
    </tr>
    <tr width="100%">
         <td  align="center"><img src = "https://ifh.cc/g/J8FJYy.jpg" width="80px"/></td>
        <td  align="center"><img src = "https://ifh.cc/g/Vo4n9y.png" width="100px" /></td>
        <td  align="center"><img src = "" width="80%"/></td>
        <td  align="center"><img src = "https://ifh.cc/g/3pJqOT.jpg" width="80px"/></td>
        <td  align="center"><img src = "https://ifh.cc/g/KHNqkk.png" width="80%"/></td>
        <td  align="center"><img src = "https://ifh.cc/g/ydn0yw.png" width="80px"/></td>
    </tr>
    <tr width="100%">
      <td  align="center"><p>기획디자인</p></td>
      <td  align="center"><p>프론트엔드</p></td>
      <td  align="center"><p>프론트엔드</p></td>
     <td  align="center">백엔드</td>
      <td  align="center">백엔드</td>
      <td  align="center">백엔드</td>
   </tr>
        <tr width="100%">
      <td  align="center"><p>웹디자인, 브랜딩, 발표</p></td>
      <td  align="center"><p>프론트엔드</p></td>
      <td  align="center"><p>프론트엔드</p></td>
     <td  align="center">지도, 예약, 리뷰 작성, 마이페이지</td>
      <td  align="center">마이페이지</td>
      <td  align="center">q&a 작성, q&a 디테일</td>
   </tr>
</table>

### 개발 기간

- 2023.07.11 ~ 2023.07.15

<br/>



## ✨ 기술 스택

- 기획디자인 : 피그마
- 프론트엔드 : HTML, CSS, JavaScript, Kakao map API
- 백엔드 : python, django
- ETC : git

</br>

## ✨ 라이브러리

```
 "@reduxjs/toolkit": "^1.8.5",
    "@testing-library/jest-dom": "^5.16.5",
    "@testing-library/react": "^13.3.0",
    "@testing-library/user-event": "^13.5.0",
    "axios": "^0.27.2",
    "gulp-sass": "5.1.0",
    "react": "^18.2.0",
    "react-dom": "^18.2.0",
    "react-ga": "^3.3.1",
    "react-icons": "^4.4.0",
    "react-redux": "^8.0.2",
    "react-router-dom": "^6.3.0",
    "react-scripts": "^4.0.0",
    "redux": "^4.2.0",
    "redux-persist": "^6.0.0",
    "redux-thunk": "^2.4.1",
    "sass": "^1.54.9",
    "styled-components": "^5.3.5",
    "util": "^0.12.4",
    "web-vitals": "^2.1.4"

asgiref              3.4.1
distlib              0.3.6
Django               3.2.20
django-debug-toolbar 3.2.4
filelock             3.4.1
importlib-metadata   4.8.3
importlib-resources  5.4.0
Pillow               8.4.0
pip                  10.0.1
platformdirs         2.4.0
pytz                 2023.3
setuptools           39.0.1
sqlparse             0.4.4
typing-extensions    4.1.1
virtualenv           20.17.1
zipp                 3.6.0
```

## ✨ 프로젝트 구조

<img width="80%" src="https://ifh.cc/g/1Xnr9M.png"/>


### ✨ 폴더 구조

```
📂 2023-Herethon-8
└─ smarthospital
 ├─ smarthospital
 │  ├─ __init__.py
 │  ├─ asgi.py
 │  ├─ settings.py
 │  ├─ urls.py
 │  └─ wsgi.py
 ├─ qnas/
 │  ├─ static
 │  │  ├─ css/
 │  │  │  ├─ index.css
 │  │  │  ├─ mypage1.css
 │  │  │  ├─ mypage2.css
 │  │  │  ├─ mypage3.css
 │  │  │  ├─ mypage4.css
 │  │  │  ├─ mypage5.css
 │  │  ├─ media/
 │  │  │  ├─ back2.png
 │  │  │  ├─ doctor.png
 │  │  │  ├─ search.png
 │  │  │  ├─ submit.png
 │  ├─ templates/
 │  │  ├─ mypage5.html
 │  │  ├─ question_detail.html
 │  │  ├─ question_list.html
 │  │  ├─ question_write.html
 │  │  ├─ review_create.html
 │  ├─ __init__.py
 │  ├─ admin.py
 │  ├─ apps.py
 │  ├─ apps.py
 │  ├─ models.py
 │  ├─ forms.py
 │  ├─ tests.py
 │  └─ views.py
 ├─ hospitalapp/
 │  ├─ templates/
 │  │  ├─ index.html
 │  │  │  ├─ hospital/
 │  │  │  │  ├─ hspital_detai.html
 │  │  │  │  ├─ hospital_review.html
 │  │  │  ├─ accounts/
 │  │  │  │  ├─ login.html
 │  │  │  │  ├─ signup_doctor.html
 │  │  │  │  ├─ signup.html
 │  ├─ __init__.py
 │  ├─ admin.py
 │  ├─ apps.py
 │  ├─ models.py
 │  ├─ forms.py
 │  ├─ urls.py
 │  ├─ tests.py
 │  └─ views.py
 ├─ accounts/
 │  ├─ __init__.py
 │  ├─ admin.py
 │  ├─ apps.py
 │  ├─ apps.py
 │  ├─ models.py
 │  ├─ forms.py
 │  ├─ tests.py
 │  └─ views.py
 ├─ users/
 │  ├─ __init__.py
 │  ├─ admin.py
 │  ├─ apps.py
 │  ├─ apps.py
 │  ├─ models.py
 │  ├─ tests.py
 │  └─ views.py
 └─ manage.py

```


