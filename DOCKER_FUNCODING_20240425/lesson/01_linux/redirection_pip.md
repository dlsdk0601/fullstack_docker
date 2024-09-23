
* Standard Stream (표준 입출력)
```shell
command 로 실행되는 프로세스는 3가지 스트림을 가진다 
- 표준 입력 스트림(Standard Input Stream): stdin
- 표준 출력 스트림(Standard Output Stream): stdout
- 오류 출력 스트림(Standard Error Stream): stderr

- 모든 스트림은 일반적인 plain text 로 console 에 출력되게 되어있음
```
<br />

* Redirection (리다이렉션)
```shell
- 표준 스트림 흐름을 바꿔줄 수 있다.
- <, > 을 사용함
- 주로 명령어 표준 출력을 화면이 아닌 파일에 쓸 때 사용

- ex)
- ls > files.txt
- ls 로 출력 되는 표준 출력 스트림의 방향을 files.txt 로 바꿔줌
```

<br />

* 파이프
```shell
- | 는 두 프로세스 사시에서 한 프로세스의 출력 스트림을 또다른 프로세스의 입력 스트림으로 사용할때 사용
```

* grep
```shell
- 검색 할때 사용
```