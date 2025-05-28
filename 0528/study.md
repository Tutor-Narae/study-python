# 상속 (Inheritance)
## 상속이란?
기존 클래스(부모 클래스, 슈퍼 클래스)의 속성과 메서드를 **새로운 클래스(자식 클래스, 서브 클래스)**가 물려 받는 것

## 목적
- 코드 재사용
- 계층 구조 구성
- 확장성 있는 구조 설계

## 문법
1. 부모 클래스 생성
2. 자식 클래스 생성하되, 클래스 이름 옆의( )에 부모 클래스 넣기
```python
class 부모클래스:
  def 부모메서드(self):
    print("Hello from Parent")

class 자식클래스(부모클래스이름):  # 상속
  pass
```
<sup>- 자식 클래스나 함수에 아직 아무 코드도 작성하지 않을 때 자리를 채우기 위해 사용하는 문법</sup> <br/>
<sup>- 파이썬에서는 들여쓰기된 블록이 반드시 있어야 하므로, 아무 동작도 하지 않을 때 `pass`를 써야 문법 오류가 나지 않음</sup><br/>
<sup>- `클래스, 함수, 조건문`등 구문 블록이 필요하지만 내용을 아직 안 채운 경우 전부 다 사용 가능</sup>

### 1. 기본 문법
```python
class Parent:
  def say_hello(self):
    print("Hello from Parent")

class Child(Parent):  # 상속
  pass

c = Child()
c.say_hello() # Hello from Parent
```

### 2. 자식 클래스에 메서드 추가
```python
class Parent:
  def greet(self):
    print("Hello from Parent")

class Child(Parent):
  def introduce(self):
    print("I'm a child")

c = Child()
c.greet()     # Hello from Parent
c.introduce() # I'm from child
```

### 3. 오버라이딩
부모 클래스에 있는 함수를 재정의 하는것
```python
class Parent:
  def greet(self):
    print("Hello from Parent")

class Child(Parent):
  def greet(self):
    print("Hello from Child")

c = Child()
c.greet()   # Hello from Parent
```

### 4. super() 사용
- `부모 클래스를 호출`하고 싶을 때 사용
- 부모 클래스의 동작을 유지하면서 자식에서 추가 행동을 하고 싶을 때 사용
```python
class Parent:
  def greet(self):
    print("Hello from Parent")

class Child(Parent):
  def greet(self):
    super().greet()
    print("Hello from Child")

c = Child()
c.greet()
# Hello from Parent
# Hello from Child
```

### 5. 생성자(Initializer) 상속 (`__init()__`)
```python
class Parent:
  def __init__(self, name):
    self.name = name

class Child(Parent):
  def __init__(self, name, age):
    super().__init__(name)  
    self.age = age

p1 = Parent("Alice")
p2 = Parent("Alice", 12) # Error!: Parent.__init__() takes 2 positional arguments but 3 were given

c = Child("Alice", 12)
print(c.name)
print(c.age)
```

### 6. 다중 상속
자식이 여러 클래스를 상속 받음<br/>
다중 상속은 `MRO(Method Resoultion Order)`가 중요! => 상속 관계가 복잡할 경우 어떤 메서드가 먼저 호출될지를 결정하는 순서<br/>

- 2개의 클래스를 상속: 2개의 클래스는 서로 다른 메서드를 가지고 있음
  ```python
  class Father:
    def speak(self):
      print("Father speaks")

  class Mother:
    def sing(self):
      print("Mother sings")

  class Child(Father, Mother): # Child -> Father -> Mother  순으로 탐색하고 있다면 호출
    pass

  c = Child()
  c.speak() # Father speaks
  c.sing()  # Mother sings
  ```
<br/>

- 2개의 클래스를 상속: 2개의 클래스에 이름이 같은 메서드가 있음
  ```python
  class Father:
    def speak(self):
      print("Father speaks")

  class Mother:
    def speak(self):
      print("Mother speaks")
    def sing(self):
      print("Mother sings")

  class Child(Father, Mother): 
    pass

  print(Child.__mro__)  # (<class 'Child'>, <class 'Father'>, <class 'Mother'>, <class 'object'>)
  c = Child()
  c.speak() # Father speaks
  ```
<br/>

- 2개의 클래스를 상속: 상속받은 부모 클래스와 동일한 메서드가 자식 클래스에도 있음
  ```python
  class Father:
    def speak(self):
      print("Father speaks")

  class Mother:
    def speak(self):
      print("Mother speaks")
    def sing(self):
      print("Mother sings")

  class Child(Father, Mother): 
    def speak(self):
      print("Child speaks")

  print(Child.__mro__)  # Method Resolution Order
  c = Child()
  c.speak() # Child speaks
  ```

## 상속 구조에서의 `isinstance()`와 `issubclass()` 메서드
| 함수                       | 의미                         | 예시 질문                    |
| ------------------------ | -------------------------- | ------------------------ |
| `isinstance(obj, Class)` | obj가 이 클래스의 `인스턴스`인가? <br/>=> `객체 검사`  | "이 `객체`가 이 클래스에서 만들어졌나요?"  |
| `issubclass(A, B)`       | A 클래스는 B 클래스의 자식 `클래스`인가? <br/> => `클래스 간 관계를 검사` | "이 클래스가 다른 클래스를 상속받았나요?" |

- 예제 1: isinstance(인스턴스, 클래스) <br/>
```python
class Animal:
  pass

class Dog(Animal):
  pass

d = Dog()
print(isinstance(d, Dog))     # ✅ True
print(isinstance(d, Animal))  # ✅ True (상속받았기 때문에)
print(isinstance(d, object))  # ✅ True (모든 클래스는 object 상속)
print(isinstance(d, str))     # ❌ False
```

- 예제 2: issubclass(클래스1, 클래스2)
```python
class Animal:
  pass

class Dog(Animal):
  pass

print(issubclass(Dog, Animal))   # ✅ True
print(issubclass(Dog, object))   # ✅ True
print(issubclass(Animal, Dog))   # ❌ False
print(issubclass(str, object))   # ✅ True (모든 클래스는 object의 자식)

```

# 다형성 (Polymorphism)
## 다형성이란?
하나의 메서드가 다양한 동작을 하는 것. 즉, 같은 이름의 메서드를 호출하더라도 어떤 객체에서 호출되느냐에 따라 다르게 작동하는 것을 의미.<br/>

## 목적
- 유연성: 다양한 객체를 같은 방식으로 다를 수 있음.
- 확장성: 새로운 클래스를 추가해도 기존 코드를 변경할 필요가 거으 ㅣ없음
- 재사용성 & 유지보수 향상: 공통 인터페이스 덕분에 중복을 줄이고 유지보수가 쉬움.

## 문법
```python
class Animal:
  def speak(self):
    print("동물이 소리를 냅니다")

class Dog(Animal):
  def speak(self):
    print("멍멍!")

class Cat(Animal):
  def speak(self):
    print("야옹~")

class Bird(Animal):
  def speak(self):
    print("짹짹!")
```

# `상속`과 `다형성`의 관계
상속과 다형성은 객체 지향 프로그래밍(OOP)의 핵심 개념이며, 서로 긴밀하게 연결되어 있음.<br/>
상속은 다형성을 가능하게 만드는 기반<br/>
=> **공통된 부분은 하나로 묶고 다른 부분만을 정의하기 위해서 반드시 필요한 개념**<br/>

| 개념  | 역할                                    | 핵심 단어 |
| --- | --------------------------------------- |--------|
| 상속  | 코드 재사용, 구조 설계, `공통` 인터페이스 제공  | `통일된 틀` |
| 다형성 | 자식 클래스마다 동작을 `다르게` 정의하여 유연하고 확장 가능한 코드 구현 | `오버라이딩` |
<br/>

# Package
- 패키지는 모듈을 폴더 형태로 묶은 것. 모듈은 .py 하나를 모듈이라고 함. Function/Method, Variables < Class < Module < Package
- 패키지를 사용하면 여러 개의 관련된 모듈들을 그룹화 할 수 있음.
- 패키지 폴더 안에는 반드시 `__init__.py` 파일이 있어야 하며, 이 파일은 빈 파일이어도 괜찮고, 패키지를 초기화하는 코드가 들어 있을 수도 있음.

## 패키지 생성 방법
1. 클래스를 각각 .py파일로 분리
2. 성격이 비슷한 클래스끼리 묶고 패키지(폴더)를 생성
3. 폴더를 패키지라고 인식시키기 위해, 폴더 내붸 `__init__.py` 파일 생성
4. 호출 경로 맞추기

## 패키지 경로 맞추기
- 패키지를 from을 써서 가져오기 위해서는 경로를 어느 경로에 있는지를 알려줘야 함.
- 경로의 기준점은 실행되는 파일 기준. ex. main.py에서 코드가 실행된다면 main.py가 있는 경로가 root경로로 기준이 됨.
- 코드가 실행되는 경로를 기준 위치로 잡는 것을 `상대경로`라고 함.
- 패키지 안의 패키지 안의 패키지를 계속 따라간다면 `.`으로 연결 할 수 있음 ex. `package1.package2.package3`

| 상황                    | 추천 import 방식                           |
| --------------------- | -------------------------------------- |
| 모듈이 **패키지 내부에 있는 경우** | ✅ `from .animal import Animal` (상대 경로) |
| 루트에서 직접 import할 때     | ✅ `from animals.animal import Animal`  |
| 모듈을 **직접 실행할 경우만**    | `from animal import Animal` (단, 불안정)   |


## 예제: Animal
예제: Animal 클래스, Dog 클래스, 실행부를 각각 다른 파일로 분리하고 animal이라는 패키지 생성<br/>

- 패키지 구조
  ```
  my_project/
  ├── animals/
  │   ├── __init__.py
  │   ├── animal.py
  │   └── dog.py
  └── main.py
  ```

- `animals/__init__.py`
  ```python
  # 비워둬도 상관 없음.
  ```
- `animals/animal.py`
```python
class Animal:
  def __init__(self, name):
    self.name = name

  def speak(self):
    print(f"{self.name} is making a sound.")
```

- `animals/dog.py`
```python
from .animal import Animal

class Dog(Animal):
  def speak(self):
    print(f"멍멍! 나는 {self.name}야")
```

- `main.py`
```python
from animals.dog import Dog

dog = Dog("초코")
dog.speak()
```