집 관련 토이 프로젝트

참고 사이트
당근마켓, 오늘의 집, 네이버 쇼핑몰, 직방


## FRONT : Vue

## BACKEND : Django

```
DATABASE : MYSQL, MongoDB, REIDS

version

python : 3.8
vue : 2.6.14

아직 mongodb가 익숙치 않아 docker 기반이 아닌 local로 테스트중.

```


```
실행 방법
docker-compose up -d
```


> DB 관련은 backend -> models 참고

# TODO

테스트 코드
return response status code & error exception



- [ ] 환경설정
    - [x] Docker
    - [ ] logging
    - [ ] prod, dev
    - [ ] return status code
    - [ ] test code
    - [ ] k8s
    - [ ] load balace
    - [ ] monitor

- [ ] AUTH (JWT)
    - [ ] NestJS 예정

- [ ] 회원가입
    - [ ] NestJS 예정

- [ ] 내정보
    - [ ] 내 정보 조회
    - [ ] 내 정보 수정
    - [ ] 장바구니
    - [ ] 즐겨찾기
    - [ ] 

- [ ] 쇼핑(Product)
    - [x] 상품 목록 
    - [x] 상품 상세 정보
    - [x] 상품 정보 수정
    - [x] 상품 삭제
    - [ ] 페이지 기능
    - [ ] 장바구니 추가
    - [ ] 바로 구매

- [ ] 배송
    - [ ] 출발 - 도착지 거리 계산
    - [ ] 

- [ ] 부동산
    - [ ] 아파트
    - [ ] 오피스텔
    - [ ] 원룸
    - [ ] 사무실
    - [ ] 기타

- [ ] 인테리어
    - [ ] 가정
    - [ ] 원룸
    - [ ] 사무실

- [ ] 이사
    - [ ] 가정
    - [ ] 원룸
    - [ ] 사무실

- [ ] 청소
    - [ ] 가정
    - [ ] 원룸
    - [ ] 사무실

- [ ] 커뮤니티(story)
    - [x] 게시판 등록
    - [x] 조회수 기능
    - [ ] 이미지 추가
    - [x] 댓글 기능
    - [ ] 좋아요 등 기타 감정 표현
    - [ ] 대댓글
    - [ ] 댓글 삭제
        - [ ] 삭제된 댓글입니다

- [ ] 리뷰
    - [ ] 리뷰 작성
    - [ ] 리뷰 수정
    - [ ] 리뷰 삭제