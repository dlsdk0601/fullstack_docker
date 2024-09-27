# docker 설치
```shell
sudo apt-get install curl
curl -fsSL https://get.docker.com/ | sudo sh
```
> 사실 이 명령보다 상황에 따라 docker install ubuntu 검색해서 공식문서 보는게 이득

<br />

# root 에게 docker 권한 부여
```shell
sudo usermod -aG docker ${USER}
```
> 권한 주고 접속을 끊고 다시 재접속 하는게 속편함 (sudo 를 붙이지 않기 위해 사용)

<br />

# docker IMAGE ID 만 표시가기
```shell
docker image ls -q
```

<br />

# docker IMAGE 제거
```shell
docker rmi <IMAGE-ID>

docker image rm <IMAGE-ID>
```

<br />

# docker Container 생성
```shell
docker create <IMAGE 이름>
```
> 이미지를 먼저 pull 받아야 한다.
> --name <이름> 으로 하면 컨테이너에 이름을 지정 가능

<br />

# docker Container 확인
```shell
docker ps
```
> 옵션이 없다면 실행중인 컨테이너만 보인다. 전부 보려면 -a 를 붙여야한다.

<br />

# docker Container 삭제
```shell
docker rm <CONTAINER-ID>
```

<br />

# docker Container 실행
```shell
docker start <CONTAINER-NAME>
```

<br />

