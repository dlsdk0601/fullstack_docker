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

