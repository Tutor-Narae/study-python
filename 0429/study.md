# Module: study_module
- 파이썬 코드가 담긴 파일, 어떤 기능들을 미리 만들어 놓은 도구 상자
- 내가 만들지 않앋도 누군가가 만든 모듈을 불러와서 사용하는 것 가능

## 모듈 구조
- `Module` = `classes` + `attributies`
  ```
  datetime (모듈)
  └── datetime (클래스)
  ```

- 모듈 구조 확인: [Python 공식문서](https://docs.python.org/3/library/)

## 모듈 불러오는 법 - 저번시간 이어서
### 1. `import`: 모듈 전체 불러오기
- 묘듈의 모든 기능을 사용할 수 있으나, 모듈의 이름을 계속 반복적으로 써야함. ex) `datetime.datetime`.now()
  - 기본 사용법
  ```python
  import 모듈명
  ```

  - 예시
  ```python
  import datetime

  print(datetime.datetime.now()) # 모듈 -> 클래스 -> 메서드()
  ```

### 2. `from`: 으로 모듈에서 특정 기능(클래스, 함수, 변수)만 불러오기 
- 모듈은 여러 개의 클래스의 집합체이므로, 특정 method를 호출할 때는 어떤 클래스의 메서드를 가져올 것인지 클래스 명을 정확히 명시 해줘야 함.
- now()는 datetime 클래스의 메서드 이므로, 클래스명.메서드()로 호출해야 함.
- 모듈에서 바로 호출할 경우, **datetime.datetime object has no attribute 'strptime'** 에러가 남.

  - 기본 사용법
  ```python
  from 모듈명 import [클래스명, 함수명, 변수명]
  ```
  
  - 예시 1: 하나의 클래스명, 함수명, 변수명 만을 불러옴 
  ```python
  # 모듈에서 필요한 기능(클래스)만을 불러와서, 모듈명 없이 바로 사용 가능
  from datetime import datetime 
  print(datetime.now())
  ```

  - 예시 2: 여러개의 클래스명, 함수명, 변수명을 불러옴
  ```python
  from datetime import MINYEAR, MAXYEAR, date, datetime

  print(MINYEAR)
  print(MAXYEAR)
  print(date)
  print(datetitme)
  print(datetitme.now())
  ```

  - 예시 3: 모든 함수와 클래스 불러오기 (추천하지 않음: 메모리가 낭비되고, 코드가 더러워지고, 이름 충돌 가능성도 높아짐.)
  ```python
  from datetime import *  # datetime의 모든 함수와 변수를 불러옴.

  print( datetime.now() ) # 모든 함수와 변수를 불러왔기 때문에 datetime.datetime.now()가 아니라 datetime.now() 로 쓸 수 있음.
  ```

### 3. as: 모듈명에 별명 붙이기
- 가독성, 코드의 간결함, 충돌방지 때문에 as를 써서 별명을 붙임.
- 현재 단계에서는 거의 쓸 일 없음.

- 기본 사용법
  ```python
  import 모듈명 as 별명
  ```

- 예시
  ```python
  import datetime as dt

  print(dt.datetime.noe())
  ```
  <br/>

# Magic Mathod & Magic Attribute (`__something__`)
## Magic Method
### 정의
- 이름이 `__이름__`처럼 언더스코어 두 개(__)로 감싸져 있는 **특별한 함수(메서드)**
- 클래스를 정의할 때, 객체의 동작(생성, 출력, 연산자 사용 등)을 직접 제어할 수 있게 도와줌.

### 종류
#### 1. 객체 생성: `__init__`
- 객체를 생성할 때 호출 (생성자)
  ```python
  def __init__(self, a, b, c):
    self.a = a
    self.b = b
    self.c = c
  ```

#### 2. 문자열 출력: `__str__`
  - print()나 str()로 호출될 때 문자열로 표현
    ```python
    def __str__(self):
      return f"Person's name is {self.name}"
    ```

#### 3. 객체의 길이: `__len__`
  - len(객체) 사용할 때 동작
    ```python
    def __len__(self):
      return len(self.items)
    ```

#### 4. 연산자(+,-,== ) 사용: `__add__`, `__eq__` 등
  - 객체끼리 + 연산자 사용할 때
    ```python
    class Number:
      def __init__(self, value):
        self.value = value

      def __add__(self, other):
        return Number(self.value + other.value)

    a = Number(10)
    b = Number(20)
    result = a + b
    print(result.value)  # 출력: 30
    ```

## Magic Attribute
### 정의
- 이름이 `__이름__`처럼 언더스코어 두 개(__)로 감싸져 있는 **특별한 속성(변수)**
- 객체, 클래스, 모듈이 기본적으로 가지고 있는 정보성 데이터를 제공

### 종류
#### 1. 현재 실행 중인 모듈 이름: `__name__`
- 의미: 현재 실행 중인 모듈의 이름을 나타내는 변수. 
- 용도: 모듈이 직접 실행될 때와 import될 때의 동작을 구분할 수 있음.
  - 직접 실행:  __name__ 값이 `__main__`으로 설정
  - 다른 파일에서 import해서 사용: __name__ 값은 `모듈의 이름`으로 설정

- 예시 1. 직접 출력
  ```python
  # test.py
  print(__name__) # __main__ 출력
  ```

- 예시 2. 다른 곳에서 import
  ```python
  #my_module.py
  def some_fun():
    print("some_fun() 호출")

  if __name__ == "__main__":
    print("파일 직접 실행!")
    some_fun()

  # 이 파일을 실행하면 "파일 직접 실행!, some_fun() 호출" 둘 다 출력
  ```

  ```python
  # test.py
  import mymodule

  mymodule.some_fun() 
  # 이 파일을 실행하면 "some_fun() 호출" 만 출력
  ```

#### 2. `__version__`
- 의미: 모듈의 버전을 나타내는 변수.
- 용도: 모듈의 버전 정보를 담아두고, 다른 사람이 모듈의 버전을 쉽게 확인할 수 있도록 함.

- 활용 예시:
  ```python
  # mymodule.py
  __version__ = "1.0.0"
  ```

## 클래스 VS 모듈
|구분 | 매직 메서드 사용 | 매직 변수 사용|
|----|---------------|------------|
|클래스 | 매우 자주 사용 | 자주 사용|
|모듈 | 거의 안 사용 | 자주 사용|

<br/>

# Comprehension
- 파이썬에서만 사용 가능하며, 간결하고 가독성 높은 방식으로 새로운 컬렉션을 생성하기 위한 문법
- `간단한 반복과 조건 필터링`을 짧고 명확하게 표현하려고 쓸 때 유용. 복잡한 로직이 필요한 경우에는 오히려 일반 for문이 더 가독성 높을 수 있음.
  - 가능한 조합
    - for
    - for + if
    - for + for
    - for + if + if
    - for + for + if
  - while은 ❌ 불가능!

## 문법
```python
컬렉션결과물 = [컬렉션아이템 for 요소 in 컬렉션객체 if문/for문]
```

## Comprehension을 사용할 수 있는 컬렉션 타입
- 결과 값에 어떤 괄호([], {key: value}, {}, ())를 씌우냐에 따라 리턴되는 결과 타입이 달라짐
### 1. list []
- `for문`
  ```python
  squares = [x**2 for x in range(5)]  # [0, 1, 4, 9, 16]
  ```

- `for문` + `if문`
  ```python
  even_squares = [x**2 for x in range(10) if x % 2 == 0]  # [0, 4, 16, 36, 64]
  ```

- `for문` + `for문`
  ```python
  pairs = [(x, y) for x in [1, 2] for y in ['a', 'b']]  # [(1, 'a'), (1, 'b'), (2, 'a'), (2, 'b')]
  ```

### 2. Dictionary {key: value}
- `for문`
  ```python
  dic = {k: v for k, v in [('a', 1), ('b', 2)]}  # {'a': 1, 'b': 2}
  ```

### 3. Set {}
- `for문`
  ```python
  squares = {x**2 for x in range(5)}  # {0, 1, 4, 9, 16}
  ```

### 4. Generator ()
이터레이터(iterator)의 한 종류로, 메모리를 아끼기 위해 `필요할 때` 값을 계산하는 객체<br/>
Iterator를 인자로 받는 함수에 바로 넣어서 사용 가능<br/>

- `for문`
  ```python
  (x**2 for x in range(4)) # generator object (리스트가 아님!)
  ```

- `sum()`: Iterator를 인자로 받는 함수
  ```python
  sum(x * x for x in range(5)) # 45
  ```

- `max()`: Iterator를 인자로 받는 함수
  ```python
  max(len(word) for word in ["apple", "banana", "kiwi"]) # 6
  ```

- `min()`: Iterator를 인자로 받는 함수
  ```python
    min(score for score in [0, -1, 50, 20] if score > 0) # 20
  ```

- `any()`: Iterator를 인자로 받는 함수
  ```python
  any(ch.isdigit() for ch in "abc123") # True
  ```
<br/>
