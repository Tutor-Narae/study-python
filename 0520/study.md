# README.md 파일 작성 방법

## 제목
```
# 제목1
## 제목2 
### 제목 3
```

## 링크
```
[링크제목1](#링크선택1)
[링크제목2](#링크선택2)
```

## 글씨
```html
<b>볼드</b>
**볼드**
<i>이태릭</i>
***이태릭 + 볼드***
`하이라이트`
```

## 띄어쓰기
```
<br/>
```

## 블럭
\``` <br/>
\```

- ex
```sh
project/
│
├── game.py       # 메인 실행 로직
├── cave.py       # Cave 클래스
├── character.py  # Enemy, Friend 클래스
└── item.py       # Item 클래스
```

# Git branch 생성하는 법
## 1. 현재 브랜치 확인
```sh
git branch 
```

## 2. 브랜치 생성
```sh
git branch 'stage1'
```

## 3. 생성된 브랜치(state1)를 Github(원격저장소)에 올리기
```sh
git branch -set--uptram origin 'stage1'
```

## 4. 생성된 브랜치(stage1)으로 이동
```sh
git switch 'stage1'
```

## 5. 코드 수정
수정하고 싶은 코드 작성

## 6. 현재 변경사항 추가 & 커밋
```sh
git add .
git commit -m "Completed stage 1: cave game setup with characters and items"
git push
```
