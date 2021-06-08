제목(H: '# '_띄어쓰기 필수)

내용(입력)

코드 인라인(``를 사용하여 문장 안에서 짧은 코드 표시)

코드 블럭(``````를 사용하여 코드 블럭 생성하여 넓은 영역에서 코드 작성, 이후 우측하단에서 언어 선택 가능)

목록(-,+,*)

강조(Ctrl+B, 별*두개)

표(|제목1|제목2|제목3|)

| ㅁ   | ㄴ   | ㄴ   |
| ---- | ---- | ---- |
| ㄹ   | ㄹ   | ㄹ   |
|      |      |      |
|      |      |      |

수식은($$)

:smiley: 콜론: 사용하여 이모지 입력 가능



# Unix CLI Command(H1)

터미널 명령어

ls, cd, mkdir, touch, mv, rm 

## 터미널 실행하기(H2)

윈도우는 git bash로 터미널 프로그램 실행. 맥은 터미널 구동.



## 명령어 정리

### 폴더 이동(H3)



### 폴더(생성, 삭제)



### 파일(생성, 이동, 삭제)



## git

버전 표기법

| 1.    | 3.    | 1     |
| ----- | ----- | ----- |
| Major | Minor | Patch |



touch .gitignore 생성하여 무시하려는 폴더, 파일 지정(폴더명엔 끝에 슬래시/ 붙일 것) -> 이후 git add .gitignore로 추가



git init (home 폴더는 tracking하면 안 됨. rm -r .git으로 취소.) :'.git' 파일을 생성하여 그 안에 관련 기능을 저장.

git config --global user.name ('kjh')

git config --global user.email ('jihoon5537@gmail.com')



git add (file 또는 .)

git restore --staged (file) :unstaged 상태로 만들기.

git commit -m 'message'



&& :한번에 두 가지 명령 수행하도록

ex) `git add . && commit -m 'message'` 

`-h` 사용하여 사용할 수 있는 명령어 확인 가능(도움말)



git status

git log

git log --oneline :짧게 표현(git log --pretty=oneline도 가능)



git restore (file)

git checkout (master 또는 version :일부만 쳐도 됨. 되도록이면 이전 버전은 참고만 하고 돌아간 상태에서 새로 작업하지 않도록.) - head가 이동함.



open (file) :윈도우는 start



파이참 등에서도 git 기능을 지원(터미널을 사용하지 않고도 쓸 수 있음.)



git commit --amend 이용하여 이전 커밋에 수정된 파일을 편입하거나, 커밋 설명을 수정할 수 있다. (새로운 커밋으로 저장하지 않고.)

`git add .` `git commit --amend` 를 사용하여 수정된 파일 편입

세부 내용을 수정할 때는 `git commit --amend` 에서 vim처럼 i, :wq 등을 사용.





## Project ToDo List

1. 프로젝트 폴더(디렉토리) 생성
2. `.gitignore` 와 `README.md` 파일을 생성.
   1. `.gitignore` 에는 git의 파일 관리에서 무시할 내용을,
   2. `README.md` 에는 프로젝트의 소개 및 정리 내용을 담는다.

3. `git init` 실행
4. **주의**
   1. `.git/` 폴더와 `.gitignore` 파일, `README.md` 파일이 같은 위치에 존재하는지 확인.
5. 커밋 실행 `git commit -m 'message'`



## vim (file) :터미널에서 파일 수정.

i 눌러서 INSERT 모드로 변경하여 일반편집.

esc로 탈출

shift ;(:)로 명령 모드

w 입력하여 저장(write)

q 입력하여 파일 종료(quit)

wq로 저장하고 종료

q!로 강제종료(저장하지 않아도 종료 가능)



## brnach

git branch :브랜치 확인

git branch (이름): 브랜치 추가

git switch (이름): 브랜치 변경(해당 브랜치로 헤드 이동) = git checkout (이름)과 유사한 기능. 

=> 새로 생성한 브랜치에 add . / commit 

git log --oneline --graph 를 사용하여 브랜치의 구성 현황을 시각적으로 확인할 수 있음



## 개별 branch를 master에 병합

git switch master

git merge (이름)

=> commit이 다 끝난 상태여야 함. 실행하면 개별 브랜치의 위치로 마스터가 이동함.

git branch -d (이름) :을 사용하여 용도가 끝난 개별 브랜치를 삭제.



git switch -c (이름) :해당 브랜치를 생성한 뒤 이동.



merge 할때 두 브랜치가 서로 충돌(중복 영역 수정)이 없으면 문제없이 두 브랜치의 수정사항이 모두 반영됨.

충돌이 있을 경우 자동병합이 실패. 충돌한 파일에는 양 브랜치의 코드가 모두 기입되고 문법에 맞지 않는 단순 텍스트로 충돌한 부분을 표시해줌. 직접 파일을 열어서 해당 코드를 수정. 그 상태로 `add . && commit -m 'message'` 를 사용하면 두 브랜치가 병합된 커밋이 새로 생성되어 master가 위치하게 됨. 이후 merge 이용하여 병합 후, 개별 브랜치 삭제.


## + 

md에 이미지 첨부할 때 -설정에서 {filename}.assets 경로로 이미지 복사, 상대적 위치 사용 체크 확인



## Github

1. 리모트 리포 생성

   github - create a new repository

2. local :arrow_right: remote 이름 지정

   `git remote add (이름.origin) (주소)` 

3. 업로드(백업)

   `git push (이름) (브랜치.master)` 




git remote -v 를 사용하여 현재 버전과 (이름)을 확인할 수 있음. (* 클론을 사용하여 다운받으면 기본값이 origin으로 설정되어 있음.)

git remote remove (이름) 으로 등록한 주소 삭제.



git clone (주소)를 사용해 업로드된 깃허브의 프로젝트를 현재 디렉토리에 다운로드할 수 있음.



## 루틴

커밋은 의미가 있는 순간에(버전 바뀔 때마다) 하고, 푸시는 낮은 빈도로 해도 괜찮음. 푸시하면 그간 이루어졌던 각 커밋이 모두 반영됨.



## 협업

혼자 자리를 바꾸면서 일할 때.

다른 컴퓨터에서 프로젝트를 작업 후, 커밋-푸시

기존 컴퓨터는 `git pull (이름) (브랜치.master)` 사용하여 작업내용을 다운로드할 수 있음.

- 자리에 앉을 때는 pull
- 작업이 끝나고 일어날 때 push



실제 github를 중심으로 협업할 때.

`git clone (주소) (바꿀폴더명)` 으로 다른 이름으로 폴더 생성

push와 pull을 활용해 작업상황의 싱크가 맞는지 확인.

git switch -c (브랜치명)으로 개별 브랜치 생성

- 이때 브랜치명은 feature/login(기능/로그인), patch/index(패치/인덱스) 등으로 설정.

작업 후 커밋 - `git push (이름) (해당 브랜치명!=master)` 으로 push

github에 해당 브랜치가 생성.



push한 작업자가 github 프로젝트에서 'Compare & pull(=merge) request' 를 눌러 팀에게 작업 병합 요청. :arrow_right: 내용 작성(마크다운) :arrow_right: reviewers(검토자), assignees(결정권자) 등 지정

conversation 탭에서 팀원들의 코멘트/close(반려)

commits 탭에서 코드의 특정 라인에 직접 코멘트

검토 후 confirm하여 master로 merge

(* 병합은 한번에 두 개까지. 세개 이상 동시작업 불가능하므로 두개씩 순차적으로 진행.)

- 겹치는 사항이 없을 때는 아무 문제없이 merge가능하지만, 중복되는 사항이 있을 때에는 'Can't merge automatically' :arrow_right: resolve complete 사용하여 중복 사항을 확인하여 수정 :arrow_right: 'Mark as resolve' :arrow_right: 'Commit merge' :arrow_right: ​최종 병합 확인.



`git switch master`  - `git pull origin master` 하여 병합된 프로젝트로 최신화. `git branch -d (브랜치명)` 으로 기존 브랜치 삭제. `git branch -c (브랜치명)` 로 새로운 브랜치 생성하여 다음 작업 수행.



