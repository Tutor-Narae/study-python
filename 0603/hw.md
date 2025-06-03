
# average_score_1
- 문제: 사용자 입력을 받아 파일에서 숫자 평균 계산하기
- 요구사항:
  - 사용자로부터 파일 이름을 입력받아 한 줄씩 숫자를 읽고 평균을 계산
  - 파일이 없으면 "파일이 존재하지 않습니다." 출력
  - 숫자가 아닌 값이 한 줄이라도 있으면 "숫자가 아닌 값이 포함되어 있습니다." 출력
  - 정상 작동 시 평균을 출력
  - finally 블록에서 항상 "파일 닫힘" 출력

- 입력 예시 (파일 내용): numbers.txt
```
10  
20  
thirty  
40
```

- 실행 예시
```
파일 이름을 입력하세요: numbers.txt  
숫자가 아닌 값이 포함되어 있습니다.  
파일 닫힘
```
<br/>

# library_system
책 등록 및 대여 기록을 관리하는 **미니 도서관 시스템** 구현

## 요구사항
- `Book` 클래스와 `Library` 클래스를 생성  
- `Book` 클래스는 `title`, `author`, `available` 속성을 가짐 (`available`: 대여 가능 여부)  
- `Library` 클래스는 다음 기능을 가짐:
  - 책을 추가 (`add_book`)
  - 책을 대여 (`borrow_book`)
  - 전체 책 목록 출력 (`list_books`)
  - 파일에서 책 불러오기 (`load_books`)
  - 책 목록을 파일로 저장하기 (`save_books`)
- `file input/output`, `if`, `for`, `class`, `function`, `try-except`, `package`, `module` 을 모두 사용할 것
- 예외 처리:  
  - 파일이 없을 경우 새로 시작하도록 안내  
  - 중복 등록된 책은 등록 불가  
  - 존재하지 않는 책은 대여 불가

## 출력 예시

```python
from services.library import Library

lib = Library()
lib.load_books("data/book_data.txt")
lib.add_book("모모", "미하엘 엔데")
lib.borrow_book("모모")
lib.list_books()
lib.save_books("data/book_data.txt")
```

### 실행 결과
```
책 'Welcome to Python World!'가 등록되었습니다.
책 'Welcome to Python World!'를 대여했습니다.
[대여 중] Welcome to Python World! - Guido van Rossum
```

## 디렉토리 구조 예시

```
library_system/
├── main.py
├── models/
│   └── book.py
├── services/
│   └── library.py
└── data/
    └── book_data.txt
```

## 예시 데이터 파일: `data/book_data.txt`
```
해리포터,J.K.롤링,True
1984,조지 오웰,False
```
<br/>

# average_score_2
- 문제: 사용자로부터 파일 이름을 입력받고, 해당 파일에 있는 이름-점수 쌍을 읽어 평균 점수 계산하기
- 요구사항:
  - 파일에는 각 줄마다 "이름,점수" 형태의 데이터가 들어 있음
  - 점수가 숫자가 아닐 경우 "잘못된 점수 형식이 있습니다." 출력
  - 파일이 없으면 "파일이 존재하지 않습니다." 출력
  - 모든 데이터가 정상일 경우 이름별 점수를 출력하고 전체 평균 출력
  - finally에서는 "파일 처리 종료" 출력

- 입력 예시 (파일 내용: scores.txt)
  ```
  Alice,85  
  Bob,90  
  Charlie,not_a_number  
  David,70
  ```

- 실행 예시
  ```
  파일 이름을 입력하세요: scores.txt  
  잘못된 점수 형식이 있습니다.  
  파일 처리 종료
  ```

  ```
  파일 이름을 입력하세요: scores.txt  
  Alice: 85.0  
  Bob: 90.0  
  David: 70.0  
  전체 평균: 81.67  
  파일 처리 종료
  ```