# Conditional Statements: study_conditional_statements
## 조건문: match/case
- 기본 문법
  ```python
  n = 0

  match n:
    case 0:
      print("Zero")
    case 1 | 2 | 3:
      print("Small number")
    case 4 | 5 | 6 | 7 | 8 | 9:
      print("Big number")
    case _: # default
      print("Other number")
  ```

- 튜플
  ```python
  point = (2, 3)

  match point:
    case (0, 0):
      print("원점입니다.")
    case (x, 0):
      print(f"x축 위의 점입니다: x={x}")
    case (0, y):
      print(f"y축 위의 점입니다: y={y}")
    case (x, y):
      print(f"일반적인 점입니다: ({x}, {y})")
  ```

- 리스트
  ```python
  data = []
  match data:
    case []:
      print("빈 리스트입니다.")
    case [x]:
      print(f"리스트에 하나의 요소가 있습니다: {x}")
    case [x, y]:
      print(f"두 개의 요소가 있습니다: {x}, {y}")
    case [x, y, *rest]:
      print(f"최소 두 개의 요소가 있고 나머지가 존재합니다: {x}, {y}, {rest}")
  ```

- 딕셔너리
  ```python
  person = {"name": "Alice", "age": 17}

  match person:
    case {"name": name, "age": age}:
      print(f"이름: {name}, 나이: {age}")
    case {"name": name}:
      print(f"이름: {name}, 나이 없음")
    case {"age": age}:
      print(f"이름 없음, 나이: {age}")
    case _:
      print("이름과 나이를 알 수 없음")
  ```
<br/>

## if vs match/case
| **구분** | **if/elif/else** |	**match/case** |
|-----|--------------|------------|
| Python 버전	|`모든 버전`에서 사용 가능|	Python `3.10 이상`|
| 비교 방식	|범위, 복합 조건 가능	|값과 패턴 매칭 중심|
| 가독성|	긴 조건문이 있을 경우 다소 복잡	|같은 유형의 값 비교 시 가독성 좋음|
| 유연성	|`숫자, 문자열, 논리 연산 등 다양한 조건 비교` 가능	|`특정 값과 패턴`에 적합|
| 언제 사용 | 범위 비교, 조건문 긴 경우 | 비교할 값이 고정된 경우, 튜풀/리스트 등 복합 데이터 처리|
<br/>

# Loop Statements: study_loop_statements
## for
반복 가능한 객체(list, tuple, string 등등)에서 특정한 행위를 반복

- 기본 문법
  ```python
  for 변수 in 리스트(또는 튜플, 문자열):
    수행할_문장1
    수행할_문장2

  ######################################
  test_list = [1,2,3]

  for item in test_list:
    print(item)
  ```

- 예제 
  ```python
  # list
  fruits = ["apple", "banana", "cherry"]
  for x in fruits:
    print(x)
  
  a = [(1,2), (3,4), (5,6)]
  for (first, second) in a:
    print(f"{first} + {second} = {first + second}")

  # string
  for x in "hello":
    print(x)

  # range
  for x in range(6):
    print(x) # 0부터 6이전까지

  for x in range(2, 6):
    print(x) # 2부터 6이전까지
  ```

### Nested Loops
  ```python
  adj = ["red", "big", "tasty"]
  fruits = ["apple", "banana", "cherry"]

  for x in adj:
    for y in fruits:
      print(x, y)
  ```
