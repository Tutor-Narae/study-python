# 예외처리
- 코드를 짜다 보면 **예상치 못한 이유로 오류를 발생**시키는 경우에 사용

## 사용 이유
- 프로그램이 중간에 멈추지 않게 하기 위해서
- 사용자에게 친절하게 오류 메시지를 보여주기 위해서
- 오류가 발생해도 다음 코드를 계속 실행하게 하기 위해서

## 어떤 상황에서 if/else보다 예외 처리가 더 적절할까?
어떤 상황에서는 `if/else로 처리`가 가능할 수도 있는데, 그 때도 예외처리를 해야하는걸까?

- `if/else`가 더 좋은 경우
```python
num = int(input("숫자를 입력하세요: "))

if num != 0:
  print(10 / num)
else:
  print("0으로 나눌 수 없어요.")
```

- `예외처리`가 더 좋은 경우
  - 예측하지 못한 문제가 생길 수 있을 때
  - 외부 자원(파일, 네트워크, 사용자 입력 등)을 다룰 때
  - 복잡한 입력이나 시스템 자원을 다룰 때
```python
try:
  with open("data.txt", "r") as f:
    content = f.read()
    print(content)
except FileNotFoundError:
  print("파일을 찾을 수 없어요.")
```

| 상황                 | if/else 사용 | 예외처리 사용 |
| ------------------ | ---------- | ------- |
| 예상 가능한 입력 검사       | ✅          | ❌       |
| 사용자가 입력한 값이 잘못된 경우 | ✅          | ❌ / ✅   |
| 파일이 없거나 열 수 없을 때   | ❌          | ✅       |
| 0으로 나누는 경우         | ✅ or ✅     | ✅       |
| API 호출, 네트워크 오류 등  | ❌          | ✅       |

## 문법
### 기본 문법
```python
try:
  # 에러 발생 가능성 있는 코드
except ZeroDivisionError:
  # 보다 구체적인 예외를 먼저!
```

### try-except
- 예외가 발생했을 때 `except` 실행
```python
try:
  x = 10 / 0
except ZeroDivisionError:
  print("0으로 나눌 수 없습니다.")
```

### try-except-except
- try에서 예외가 발생하면, 위에서부터 except 블록을 차례대로 검사
- 가장 먼저 일치하는 except 블록 하나만 실행
- 그 아래의 except들은 무시되고, try-except 블록을 벗어나게 됨.

```python
try:
  num = int(input("숫자를 입력하세요: "))
  print(10 / num)
except ZeroDivisionError:
  print("0으로 나눌 수는 없어요!")
except ValueError:
  print("숫자가 아닌 값을 입력했어요.")
except Exception: # Exception은 가장 최상위 에러
  print("기타 예외 발생")
```

### try-except-else
- 예외가 없을 경우 `else` 실행
- 실습코드:
  - 숫자 입력 → 0이면 ZeroDivisionError
  - 문자 입력 → ValueError
  - 정상 숫자 입력 → else 실행
```python
try:
  num = int(input("10으로 나눌 숫자를 입력하세요: "))
  result = 10 / num
except ZeroDivisionError:
  print("0으로 나눌 수 없어요.")
except ValueError:
  print("숫자가 아닌 값을 입력했어요.")
else:
  print("나눗셈 결과는:", result)
```

### try-except-finally
- 무조건 실행되는 정리 코드. 예외 발생 여부와 관계없이 `finally` 실행 ex. 파일 닫기, 종료 등 자원 정리
- 실습코드:
  - 파일이 있으면 읽고 출력
  - 없으면 에러 메시지
  - 마지막에 무조건 "작업 종료!" 출력
```python
try:
  file = open("example.txt", "r")
  content = file.read()
  print(content)
except FileNotFoundError:
  print("파일이 없어요.")
finally:
  print("작업 종료! (파일 열기 시도했음)")
```

### try-except-else-finally
- 예외 발생 없으면 else 실행한 후 `finally` 실행
- 실습코드:
  - 숫자 입력 후 → 결과 출력 또는 에러 메시지
  - 마지막엔 항상 "프로그램이 종료되었습니다." 출력됨
```python
try:
  num = int(input("나눌 숫자 입력: "))
  result = 10 / num
except ZeroDivisionError:
  print("0으로 나눌 수 없어요.")
except ValueError:
  print("숫자가 아닌 값을 입력했어요.")
else:
  print("결과는:", result)
finally:
  print("프로그램이 종료되었습니다.")
```

## 다양한 예외 유형별 예시
| 예외 이름               | 언제 발생              | 예시 코드                   |
| ------------------- | ---------------------- | ----------------------- |
| `ZeroDivisionError` | 0으로 나눌 때               | `10 / 0`                |
| `ValueError`        | 정수로 바꿀 수 없는 값을 입력받았을 때 | `int("hello")`          |
| `IndexError`        | 리스트 인덱스를 잘못 접근했을 때     | `my_list[10]`           |
| `TypeError`         | 타입이 안 맞는 연산을 했을 때      | `3 + "hello"`           |
| `FileNotFoundError` | 없는 파일을 열려고 할 때         | `open("없는파일.txt", "r")` |
| `Exception` | 모든 예외에서 사용 가능     | - |

### ZeroDivisionError
- 상황
```python
# 예시: 0으로 나누기
print("10을 0으로 나눕니다.")
print(10 / 0)  # ZeroDivisionError
```

- 예외 처리 적용
```python
try:
  num = int(input("숫자를 입력하세요: "))
  print(10 / num)
except ZeroDivisionError:
  print("0으로 나눌 수 없습니다.")
```

### ValueError
- 상황
```python
# 예시: 문자열을 정수로 변환
num = int("hello")  # ValueError
```

- 예외 처리 적용
```python
try:
  user_input = input("정수를 입력하세요: ")
  num = int(user_input)
  print("입력한 정수:", num)
except ValueError:
  print("정수가 아닌 값을 입력했어요.")
```

### IndexError
- 상황
```python
# 예시: 리스트의 없는 인덱스에 접근
my_list = [1, 2, 3]
print(my_list[10])  # IndexError
```

- 예외 처리 적용
```python
try:
  my_list = ["사과", "바나나", "포도"]
  index = int(input("0~2 중 하나를 입력하세요: "))
  print("선택한 과일:", my_list[index])
except IndexError:
  print("존재하지 않는 인덱스입니다.")
except ValueError:
  print("숫자를 입력해야 합니다.")
```

### TypeError
- 상황
```python
# 예시: 타입이 안 맞는 연산
result = 3 + "hello"  # TypeError
```

- 예외 처리 적용
```python
try:
  a = 3
  b = "hello"
  print(a + b)
except TypeError:
  print("정수와 문자열은 더할 수 없습니다.")
```

### FileNotFoundError
- 상황
```python
# 예시: 존재하지 않는 파일 열기
with open("없는파일.txt", "r") as f:
  content = f.read()  # FileNotFoundError
```

- 예외 처리 적용
```python
try:
  filename = input("열 파일 이름을 입력하세요: ")
  with open(filename, "r") as f:
    print(f.read())
except FileNotFoundError:
  print("파일을 찾을 수 없습니다.")
```

### Exception
- Exception은 모든 예외의 부모 클래스이므로 모든 에러를 다 잡을 수 있음
- Exception이 먼저 있다면 그 블록에서 끝나버림 => 보다 구체적인 예외를 항상 위에 작성!

| 예외 발생        | `except` 순서                         | 실행 결과                      |
| ------------ | ----------------------------------- | -------------------------- |
| `ValueError` | 1. `Exception` <br> 2. `ValueError` | `Exception` 블록 실행됨 ❌ (주의!) |
| `ValueError` | 1. `ValueError` <br> 2. `Exception` | `ValueError` 블록 실행됨 ✅      |

```python
try:
  value = int(input("숫자를 입력하세요: "))
  print(10 / value)
except Exception as e:
  print("예외 발생:", e)
```

# 파일 입출력
외부 파일에 데이터를 저장하거나, 저장된 데이터를 읽어오는 작업

## 파일열기: open()
```python
f = open("파일이름", "모드")
f = open("0603/test.txt", "r")
```
- **파일 이름**: 읽거나 쓸 파일 경로와 이름
  - 파이썬 스크립트를 실행하는 위치(폴더)를 기준으로 찾음.
  - 경로:
    - 상대 경로(Relative Path): 현재 작업 디렉터리를 기준으로 파일 위치를 지정
    - 절대 경로(Absolute Path): 컴퓨터 내 파일의 전체 경로를 지정
- **모드**: 파일을 어떻게 열지 지정 => 하나씩 다 실행해보기
  - "r" : 읽기 모드 (기본값) — 파일이 존재해야 함
  - "w" : 쓰기 모드 — 파일이 없으면 새로 만들고, 있으면 내용 덮어씀
  - "a" : 추가 모드 — 파일이 없으면 새로 만들고, 있으면 뒤에 덧붙임
  - "x" : 새 파일 생성 모드 (파일이 있으면 에러)
  - "b" : 바이너리 모드 (예: 이미지, 동영상) — 모드와 함께 "rb", "wb" 같이 사용

## 파일 읽기
- read(): 파일 전체 내용을 문자열로 읽기
  ```python
  # 1. 가능하지만 권장하지 않는 방식
  f = open("0603/test.txt", "r")
  content = f.read()
  print(content)
  f.close()  # ← 꼭 닫아줘야 함, 파일이 계속 열려있게 되어 리소스 누수가 생길 수 있음.

  # 2. 권장방식
  # with 구문은 파일 사용이 끝나면 자동으로 정리해줘서 안전
  with open("0603/test.txt", "r") as f: # as 변수
    content = f.read()
    print(content)
    # 파일이 자동으로 닫힘
  ```
  <sup>*`with` 문을 쓰면 파일 자동으로 닫히므로 close()호출 안해도 됨.</sup>

- readline(): 한 줄씩 읽기
  ```python
  with open("0603/test.txt", "r") as f:
    line = f.readline()
    print(line)
  ```

- readlines(): 모든 줄을 리스트로 읽기
  ```python
  with open("0603/test.txt", "r") as f:
    lines = f.readlines()
    for line in lines:
      print(line.strip())
  ```

## 파일 쓰기
```python
with open("0603/test.txt", "w") as f:
  f.write("Hello, World!")
  f.write("Python practice!")
```
- 쓰기 모드: w <- 기존 내용 지워지고 새로 씀
- 추가 모드: a <- 기존 내용 뒤에 덧붙임

## 파일 닫기
```python
f = open("test.txt", "r")
data = f.read()
f.close()
```

## 파일 예외처리
```python
try:
  with open("없는파일.txt", "r") as f:
    content = f.read()
except FileNotFoundError:
  print("파일이 존재하지 않습니다.")
```

## 어떤 파일 확장자를 사용할 수 있을까?
| 파일 종류                | 열 수 있나요?                | 주의사항                                     |
| -------------------- | ----------------------- | ---------------------------------------- |
| `.txt`               | ✅ 가능                    | 텍스트 그대로 읽음 (`"r"` 모드)                    |
| `.csv`               | ✅ 가능                    | 쉼표로 구분된 데이터 → `csv` 모듈과 함께 사용하면 편리       |
| `.json`              | ✅ 가능                    | `json` 모듈을 이용해 딕셔너리처럼 다룸                 |
| `.py`                | ✅ 가능                    | 일반 텍스트니까 읽기 가능                           |
| `.html`              | ✅ 가능                    | 마찬가지로 텍스트 파일이므로 읽기 가능                    |
| `.jpg`, `.png` 등 이미지 | ✅ 가능                    | 텍스트로 읽으면 깨짐 → **바이너리 모드(`"rb"`) 사용해야 함** |
| `.pdf`               | ⛔ 단순 `open()`으로는 읽기 어려움 | 특수한 라이브러리(`PyPDF2`, `pdfplumber` 등) 필요   |
| `.docx`              | ⛔ 직접 읽기 어려움             | `python-docx` 라이브러리 필요                   |
| `.xlsx`              | ⛔ 직접 못 읽음               | `openpyxl`이나 `pandas` 사용 필요              |
