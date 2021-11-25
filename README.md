# :notebook:  프로젝트 소개

- 영화 정보 기반 추천 서비스 구성 :movie_camera:

- 사용 언어 

  - python 3.9
  - Django 3.2
  - Vue.js

- 아키텍처 : Django REST API 서버 & Vue.js

- 업무 분담 내역

  - 주지환 : Front-end 구성
  - 정지윤 : Back-end 구성

- 프로젝트 포함 fixture

  - accounts : admin-admin

  - community
  -  movies



# :facepunch:  프로젝트 목표

**`Hashtag`에 기반한 영화 추천 서비스** !

커뮤니티 페이지의 기능을 잘 활용하여 사용자들의 관심 정보들을  `Hashtag`로 분류하여 관련 영화 목록들을 추천하는 서비스를 구성하기로 하였다.

- 초기 화면 기획안 (ovenapp 사용)

  - `Home`

  <img src="README.assets/image-20211125152310729.png" alt="image-20211125152310729" width="550">

  - `Search` / `Detail`

    <img src="README.assets/image-20211125152502795.png" alt="image-20211125152502795"  width="550">

  - `Login`/ `Signup`

    <img src="README.assets/image-20211125152609725.png" alt="image-20211125152609725" width="550">

  - `Community`

    <img src="README.assets/image-20211125152647870.png" alt="image-20211125152647870" width="550">



# :sweat_smile: 프로젝트수행 과정

- **URL 주소 관리** : google docs를 활용하여 URL 주소 공유

  <img src="README.assets/image-20211125153053732.png" alt="image-20211125153053732" width="550">

- **일정 관리** : 디스코드 및  Notion을 통해 일정 관리

  ​					<img src="README.assets/image-20211125153211059.png" alt="image-20211125153211059" width="300"> 									<img src="README.assets/image-20211125153330537.png" alt="image-20211125153330537" width="300">

  

- **데이터베이스 모델링 (ERD)**

<img src="README.assets/ERD.PNG" alt="ERD" width="550">



# :page_with_curl: 기능 및 화면 설명



## :house: HOME 화면 

- `Weekly Boxoffice`

  **영화진흥위원회**의 주간 박스 오피스 조회 API를 활용하여 오늘 날짜를 기준으로 한 주간 상영작들의 박스오피스 정보를 보여줍니다.

- `Top Rated Movies`

  평점이 높은 영화 10개를 추천해줍니다.

<img src="README.assets/image-20211125153906022.png" alt="image-20211125153906022" width="550">



- `Hashtag` 영화 추천

  해당 서비스의 게시판 내 가장 개수가 많은 <u>Hashtag 1, 2위</u>에 대해 제목 및 줄거리에 관련이 있는 영화 10가지를 임의로 추천해줍니다.

<img src="README.assets/image-20211125154309871.png" alt="image-20211125154309871" width="550">

​														

- `Hashtag` 배지 

  `Hashtag` 배지를 클릭하면 현재 인기 있는 `Hashtag`태그들에 대해 보여줍니다. 또한, 해당 `Hashtag` 클릭 시, `Hashtag` 1위에 관한 영화 내용이 해당 `Hashtag` 내용으로 변경되어 알려줍니다.  (`#어벤져스` 클릭 시 아래 그림과 같이 영화 내용 변경)

  <img src="README.assets/image-20211125154849523.png" alt="image-20211125154849523" width="500">

  <img src="README.assets/image-20211125155124422.png" alt="image-20211125155124422" width="550">

## :pencil: Detail 화면

`weekly Boxffice` 부분을 제외한 영화 포스터 이미지 클릭 시 영화에 대한 상세 정보를 볼 수 있습니다. 

<img src="README.assets/image-20211125155425445.png" alt="image-20211125155425445" width="550">



 

## :mag_right:  Search 기능 및 화면

- 검색창 

  상단 navbar에 검색을 할 수 있는 검색창을 만들었습니다.

<img src="README.assets/image-20211125155900278.png" alt="image-20211125155900278" width="750">

<img src="README.assets/image-20211125155912446.png" alt="image-20211125155912446" width="550">

- 검색 결과

  검색어 입력 시 영화 정보의 제목, 줄거리, 배우(영어만 가능), 장르에 대한 검색 결과를  보여줍니다.

<img src="README.assets/image-20211125160200940.png" alt="image-20211125160200940" width="550">



## :writing_hand:  Community 화면

서비스 유저들이 영화에 관해 자유롭게 의논할 수 있는 페이지 입니다.

- 전체 게시글 화면

  `v-expansion-panel` components를 사용하여 게시판 화면을 구성하였습니다. 영화 제목과 작성일자, 리뷰제목, 조회수가 출력되도록 하였으며, 해당 패널 선택 시 하단으로 해당 게시글의 디테일 내용이 조회됩니다.

  

<img src="README.assets/image-20211125160555831.png" alt="image-20211125160555831" width="550">

​	

- 게시글 디테일 화면

  선택한 영화에 맞는 `Poster Image` 가 출력되며 작성된 게시글의 내용과 하단에는 `Comments`를 추가할 수 있는 기능이 있어 게시글에 대해 댓글을 작성할 수 있습니다. 

  

  <img src="README.assets/image-20211125161417360.png" alt="image-20211125161417360" width="650">

  

- 게시글 작성 화면

  전체 게시글 화면 상단의 <u>연필 아이콘</u> 클릭 시 글을 작성할 수 있는 창이 뜹니다.  영화 제목과 게시글 제목, 별점, 내용을 작성 후 저장을 누르면 게시글이 등록됩니다. 영화 선택 부분은 검색어에 맞게 필터링되어 결과를 보여줍니다. 

  

  <img src="README.assets/image-20211125161713593.png" alt="image-20211125161713593" width="650">

  <img src="README.assets/image-20211125161637822.png" alt="image-20211125161637822" width="650">

  

  >** Hashtag 수집 규칙
  >
  >- 게시글 작성 시 `Hashtag`를 입력하면 서버의 `Hashtag` 테이블에 등록됩니다.
  >-  하나의 글에 다량으로 동일한 Hashtag 작성하는 악성 사용자를 막기 위해 하나의 게시글에서 발생하는 중복되는 `Hashtag`의 개수는 하나만 count하였습니다.
  >- 게시글 Delete 및 Update 시에도 관련 hashtag 내용들도 함께 update됩니다.



## :lock_with_ink_pen: Login / Signup 화면

Login 화면 하단 Signup 링크를 통해 Signup 화면으로 이동 할 수 있습니다.

<img src="README.assets/image-20211125162505501.png" alt="image-20211125162505501" width="450">		<img src="README.assets/image-20211125162533073.png" alt="image-20211125162533073" width="450">





## :heavy_check_mark: 느낀점 및 어려웠던 부분

- 정지윤 

  - 그동안 수업 시간에 했던 프로젝트들이 다 내것이 아니었다는 것을 뼈저리게 깨닫게 되었습니다. :sweat:  

    그동안의 프로젝트들을 합치면 쉽게 완성될 것이라 생각했었는데 실제로 원하는 부분을 modify하며 진행하다보니 잘 안 되는 것 투성이였습니다. 

    특히 `serializer` !!  뭔가 넣기만 하면 자동으로 짠하고 되어서 쉬울 것 같았는데, 잘 안 되서 처음 작성했던 부분인 `movies` 관련 부분은 대부분 리스트 형태로 수작업 하여 `JsonResponse`로 데이터를 전송하였습니다. 

    추후 `community`부분을 serializer로 작성하며 이럴 때 serializer를 쓰면 편리하구나를 깨달았습니다. :smiley: 

  - bootstrap외에도 다양한 module들을 사용하며 module의 편리함과 어려움에 대해 동시에 느꼈습니다... 홈화면의 영화를 멋지게 보여주는 부분을 구성하며, `vue-slick`을 사용하였는데 친절한 설명과 함께 다양한 option들을 통해 쉽게 영화 리스트를 넘어가는 모양을 만들었지만, 해당 영화 이미지를 선택 시 디테일 화면의 위치가 이상하게 고정되어 하루동안 원인을 분석하였습니다. 

    수업시간에 배운 개발자 툴들이 유용하게 사용되어 `vue-slick`의 `transform` 속성으로 내부 카드 이미지 컴포넌트의 위치가 고정되었음을 알게되었습니다. 하지만 transform 속성을 무력화시키면 영화 리스트를 움직이게 만들 수 없어서, 상단에 안 보이는 곳에 사용하지 않을 vue-slick 하나를 생성하여 transform 속성을 none으로 설정하여 문제를 해결하였습니다. :smile: 

  - 아무거나 가져다 사용하면 그게 다 내것이 아니고 더 큰 탈이 난다는 것을 깨달았습니다. :dizzy_face:  

    인터넷을 통해 이미 많은 소스들이 있기에 멋져보이는 소스를 가져다 사용하면 쉽게 화면 구성이 완성 될 줄 알았는데,,, 오히려 기본 component들이 자유도가 높아 설정하는데는 더 쉬웠던 것 같습니다. 잘 모르는 소스를 가져다 사용하면 프로젝트 전체에 영향을 끼칠 수도 있기에 !!! (다른 파일의 style 속성이 전체로 설정되어있으면서 `#app`에 대해 건들이는 부분이 있어서 화면 구성이 갑자기 변경되어서 당황한 적이있었습니다.  :woman_facepalming: ) 

  - 인증부분에 대해 잘 모르고 프로젝트를 진행한 것 같아 아쉬움이 남습니다. 그저 Login 수업 시간에 배운 부분을 복사 붙여넣기 한 것 같습니다. 인증에 대해 제대로 이해해야겠다고 깨달았습니다. 

  

  

  

  







