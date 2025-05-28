# hw1.py
- 문제: 속성을 추가하는 자식 클래스 만들기
- 요구사항:  
  - `Vehicle` 클래스와 `Car` 클래스를 생성
  - `Vehicle` 클래스는 `brand` 속성을 가짐  
  - `Car` 클래스는 `Vehicle`클래스를 상속받고, `model` 속성도 추가로 가짐  
  - `Car`에서 `info()` 메서드를 만들어 전체 정보 출력  

- 호출 예시
  ```python
  c = Car("현대", "아반떼")
  c.info()
  ```

- 출력 예시
  ```
  현대 - 아반떼
  ```
<br/>

### hw2.py
- 문제: 메서드 오버라이딩 연습하기  
- 요구사항:  
  - `Bird` 클래스는 `fly()` 메서드를 가지고 있고, '새가 납니다'를 출력  
  - `Penguin` 클래스는 `Bird`를 상속하고, `fly()`를 오버라이드해서 '펭귄은 날 수 없습니다' 출력  

- 호출 예시
  ```python
  p = Penguin()
  p.fly()
  ```

- 출력 예시
  ```
  펭귄은 날 수 없습니다
  ```
<br/>

# hw3.py
- 문제: 다형성과 super() 사용하기  
- 요구사항:  
  - `Person` 클래스는 `__init__()`에서 name을 받아 저장하고 `speak()`메소드를 가짐  
  - `Student` 클래스는 `Person`을 상속하고 `school` 속성을 추가로 받아 저장함  
  - `Student.speak()`에서 super()를 사용해 부모 메서드 호출 후, 학교 정보도 출력  

- 호출 예시
  ```python
  s = Student("민수", "중앙고")
  s.speak()
  ```

- 출력 예시
  ```
  안녕하세요, 제 이름은 민수입니다.
  저는 중앙고 학생입니다.
  ```
<br/>

# hw4.py
- 문제: 다형성과 반복문 사용하기  
- 요구사항:  
  - `Shape` 클래스를 만들고 `draw()`는 아무 작업도 하지 않음  
  - `Circle`과 `Square`는 `Shape`를 상속하고 각자 다른 `draw()` 구현  
  - 반복문으로 다양한 도형들을 draw() 하게 만들기  

- 호출 예시
  ```python
  shapes = [Circle(), Square(), Circle()]
  for s in shapes:
    s.draw()
  ```

- 출력 예시
  ```
  원을 그립니다
  정사각형을 그립니다
  원을 그립니다
  ```
<br/>

# hw5.py
- 문제: isinstance()를 이용한 분기 처리  

- 요구사항:  
  - `Book`과 `Movie` 클래스 생성하되, 안의 내용물은 없음.
  - 리스트에서 반복문을 통해서 각 인스턴스가 어떤 클래스인지 확인하고, 타입에 따라 다른 문장 출력  

- 호출 예시
  ```python
  [Book(), Movie(), Book()]
  ```

- 출력 예시
  ```
  책입니다
  영화입니다
  책입니다
  ```

- 힌트:
  <details>
  <summary>힌트없이 문제 풀어보고 모르겠는 경우 열어보기 </summary>
  1. 각 인스턴스가 어떤 클래스인지 확인하는 법: isinstance()  <br/>
  </details>
<br/>

## hw6.py
- 문제: 다중 상속
- 요구사항:
  - `Flyable`과 `Swimmable` 클래스를 정의하고 각자 fly()와 swim() 메서드 작성
  - `Duck` 클래스는 두 클래스를 모두 상속받아 fly()와 swim()을 호출 가능하게 함

- 호출 예시:
  ```python
  duck = Duck()
  duck.fly()
  duck.swim()
  ```

- 출력 예시:
  ```
  나는 날 수 있어요!
  나는 수영할 수 있어요!
  ```
<br/>

## hw7.py
- 문제: isinstance() 함수 활용
- 요구사항:
  - `Fruit` 클래스를 생성하고 `Apple`, `Banana` 클래스는 이를 상속받음
  - 리스트에 다양한 객체를 넣고 Fruit 인스턴스만 출력하기

- 호출 예시:
  ```python
  items = [Apple(), Banana(), "hello", 123]
  ```

- 출력 예시:
  ```
  나는 사과입니다.
  나는 바나나입니다.
  ```
<br/>

## hw8.py
- 문제: issubclass() 활용
- 요구사항:
  - `Animal` 클래스와 그 하위 클래스 `Cat`, `Dog` 정의
  - Animal의 하위 클래스인지 여부를 issubclass()로 확인하는 코드 작성

- 호출 예시:
  ```python
  print(issubclass(Cat, Animal))
  print(issubclass(Dog, Animal))
  print(issubclass(int, Animal))
  ```

- 출력 예시:
  ```
  True
  True
  False
  ```
<br/>

## hw9.py
- 문제: 오버라이딩된 메서드에서 super() 사용하기
- 요구사항:
  - `Employee` 클래스를 만들고 greet() 메서드 정의
  - `Manager` 클래스는 Employee를 상속받고, greet()을 오버라이딩하되 super()로 부모 greet() 호출

- 호출 예시:
  ```python
  m = Manager("Lee")
  m.greet()
  ```

- 출력 예시:
  ```
  안녕하세요. 저는 직원입니다.
  제 이름은 Lee이고, 저는 매니저입니다.
  ```
<br/>

# hw10.py
- 문제: 상속 클래스에서 조건문과 반복문 활용

- 요구사항: 
  - Appliance(가전제품)라는 부모 클래스를 생성
    - `__init__()`에 name, power 속성을 갖음
  - `WashingMachine`이라는 자식 클래스를 생성
    - modes라는 리스트 속성 및 세탁 모드 속성을 갖음
    - start() 메서드를 만들고 다음 조건에 따라 동작:
      - power가 True가 아니라면 "전원이 꺼져 있습니다." 출력
      - 그렇지 않다면 modes 리스트를 반복문으로 돌면서 각 모드를 출력

- 호출 예시:
  ```python
  washer1 = WashingMachine("삼성 세탁기", True, ["헹굼", "세탁", "탈수"])
  washer1.start()

  washer2 = WashingMachine("삼성 세탁기", False, ["헹굼", "세탁", "탈수"])
  washer2.start()
  ```

- 출력 예시:
  ```
  '삼성 세탁기' 작동 시작!
  [모드] 헹굼
  [모드] 세탁
  [모드] 탈수

  전원이 꺼져 있습니다.
  ```
<br/>

# hw11
- 문제: 패키징과 상속을 활용한 교통수단 클래스 만들기

- 요구사항: 
  - `transport`라는 패키지를 생성
  - `vehicle.py`에는 `Vehicle`이라는 부모 클래스를 생성
    - `__init__(self, brand)` 메서드로 브랜드를 초기화
    - `describe(self)` 메서드로 `"이 차량은 {brand} 브랜드입니다."` 를 출력
  - `car.py`에는 `Car`라는 자식 클래스 생성
    - `Vehicle`을 상속 받음.
    - 추가로 `__init__(self, brand, model)`을 정의. `super()`를 사용해서 부모 초기화 포함.
    - `describe()` 메서드를 오버라이딩해서 `"이 차량은 {brand}의 {model} 모델입니다."` 라고 출력
    - `drive()` 메서드를 추가해서 `"출발합니다!"` 를 출력
  - `main.py`에서는 `Car` 클래스를 불러옴.

- 실행 예시
  ```python
  car = Car("Hyundai", "Avante")
  car.describe()
  car.drive()
  ```

- 출력 예시
  ```
  이 차량은 Hyundai의 Avante 모델입니다.
  출발합니다!
  ```