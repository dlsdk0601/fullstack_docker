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

# docker run
```shell
docker run <CONTAINER-NAME>
-i => 컨테이너 입력(STDIN) 을 열어놓는 옵션
-t => 가상 터미널 (tty) 을 할당하는 옵션, 주로 -it 로 -i 와 -t 를 합께 사용 
--name => 컨테이너 이름 설정 옵션
-d => 컨테이너를 백그라운드에서 실행
--rm => 컨테이너 종료시 컨테이너를 자동으로 삭제하는 옵션
-p => 호스트와 컨테이너 포트를 연결 하는 옵션
-v => 호스트와 컨테이너 디렉토리를 연결하는 옵션
```
> 옵션을 넣어서 image 를 pull 받아서 바로 container 를 만들어서 실행 시킨다.  

<br />

# docker Container 종료
```shell
docker stop <CONTAINER-NAME>
```
> 컨테이너를 삭제 시키진 않는다.

<br />

# docker Container 종료
```shell
docker stop <CONTAINER-NAME>
```
> 컨테이너를 삭제 시키진 않는다.

