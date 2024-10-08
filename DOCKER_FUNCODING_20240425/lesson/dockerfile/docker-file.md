## 빌드
```shell
docker build <option> <Dockerfile 경로>
```

<br />

-t, --tag: 이미지 이름 설정

<br />

-f: Dockerfile 의 파일명 (파일 이름이 Dockerfile 이면 굳이 안해도 된다.)

<br />

### ex)
```shell
docker build --tag my-web .
```

<br />

## 실행
```shell
docker run <option> <이미지이름>
```

<br />

-d: detach 모드로 백그라운드로 돌리고 싶을 때 추가. (default 가 attach 모드임)

-p: 컨테이너의 port 설정 (-p 9999:80 이면 localhost:9999 접속시 컨테이너의 80 포트로 연결)

--rm: 컨테이너 stop 할 경우, 컨테이너 삭제 

--name: 컨테이너 이름 설정

-it: i 와 t 옵션은 다른데 거의 같이 쓴다. 터미널을 붙이는 옵션

### ex)
> docker run -d -p 9999:80 --name apacheweb my-web

<br />

## 로그 출력
> docker logs <컨테이너_이름_or_ID>

