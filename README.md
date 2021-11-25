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

    그동안의 프로젝트들을 합치면 쉽게 완성될 것이라 생각했었는데 실제로 

  







1. M대N관계 :dizzy_face:

   

   

2. 또 Movie detail 화면...  :woman_facepalming:   포스터 이미지를 보여주는 부분에서 이전에 배웠던 것들이 혼합되면서 static 디렉토리를 설정해야 하는 것인지 강아지 이미지 불러왔던 것 처럼 하면 될 것 같은데, 허둥지둥하다가 profile에서 userid를 받아오는 부분과 유사하게, movie에 담겨온 poster_path를 받아 img src속성에 넣어 출력하였습니다.

   - `movies/detail.html`

     ```javascript
     {% block script %}
     <script>
       {% comment %} const imgSrc = document.querySelector() {% endcomment %}
       const post = document.querySelector('#post')
       const path = post.dataset.posterpath   
       console.log(path)
       const ImgTag = document.querySelector('img')
       ImgTag.setAttribute('src', path)   
       
     </script>
     {% endblock script %}
     ```

3. recommend 부분에서 random하게 10개를 보낼 것인데, `어떻게 random하게` 할 것인지...

   처음에 당연히  `lodash`만 생각하고 있었는데, `pair`님의 python의 random모듈을 사용하자는 의견에 그런방법도 있구나! 했는데, `movie.objects.all()`은 list가 아니라 random.sample이 안 되었습니다... 각자 방법을 찾는 중 저는 전체 movie 데이터를 list로 형변환 하는 방법을 생각했는데, `pair`분께서 aggregate를 사용하는 방법을 말씀하셔서, 연습겸 해당 방법을 통해 random하게 10개를 추출하였습니다.

   ```python
   @login_required
   @require_safe
   def recommended(request):    
       if request.user.is_authenticated:
           recommendMovies = set()
           # 전체 영화 목록에서 random 10개 추출
           while True:
               if len(recommendMovies) == 10:
                   break
               max_id = Movie.objects.all().aggregate(max_id=Max('id'))["max_id"]
               pk = random.randint(1, max_id)
               recommendMovies.add(Movie.objects.get(pk=pk))
           context = {
               'recommendMovies': recommendMovies
   
           }
           # movies = list(Movie.objects.all())        
           # recommendMovies = random.sample(movies, 10)        
          
           return render(request, 'movies/recommended.html', context)s
   ```

   

