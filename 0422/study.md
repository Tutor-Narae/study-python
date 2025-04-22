# Module: study_module
- 파이썬 코드가 담긴 파일, 어떤 기능들을 미리 만들어 놓은 도구 상자
- 내가 만들지 않앋도 누군가가 만든 모듈을 불러와서 사용하는 것 가능

## 모듈 - 저번시간 이어서

### datetime
#### 주요 메서드
- datetime.now(): 현재 날짜 객체 생성
  ```python
  import datetime
  now = datetime.datetime.now() # 현재 날짜/시간 객체 생성

  # now는 객체이기 때문에 여러가지 정보를 담고 있음. method 호출, properties 출력 등 가능.
  print(now.year)    # 연도
  print(now.month)   # 월
  print(now.day)     # 일
  print(now.hour)    # 시
  print(now.minute)  # 분
  print(now.second)  # 초
  ```

- datetime.date(): 날짜만 갖고 오기
  ```python
  import datetime

  now = datetime.datetime.now() # 현재 날짜/시간 객체 생성
  print( now.date() )  # 날짜만 출력
  ```
- datetime.time(): 시간만 갖고 오기
  ```python
  import datetime

  now = datetime.datetime.now() # 현재 날짜/시간 객체 생성
  print( now.time() )  # 시간만 출력
  ```

- datetime(2025, 4, 22, 15, 8): 원하는 날짜 객체 생성
  ```python
    import datetime

    customised_date = datetime.datetime(2025, 4, 22, 15, 8) # 원하는 날짜/시간 객체 생성
    print( customised_date )
  ```

#### 날짜 포맷팅 
- datetime.strftime(): 날짜 -> 문자열 (String format time -> format time to string)
  ```python
  import datetime

  now = datetime.datetime.now() # 현재 날짜/시간 객체 생성
  print( now.strftime("%Y-%m-%d %H:%M:%S") )  # 문자열로 변환
  ```

- datetime.strptime(): 문자열 -> 날짜 (String parse time)
  ```python
  import datetime
  text = "2025-04-22"
  dt = datetime.datetime.strptime(text, "%Y-%m-%d") # 날짜 객체로 변환

  print( dt )
  ```

- 포맷 코드 ([공식문서](https://docs.python.org/3/library/datetime.html#strftime-and-strptime-format-codes)): 파이썬 공식 문서에 *strftime() format codes follow the C standard* 라고 명시되어 있듯이, C언어에서 쓰이던 strftime표준을 그대로 따름

  - 📅 날짜 관련

    | 코드 | 의미 | 예시 |
    |-----|-----|------|
    | `%Y` | 연도 (4자리) | 2025 |
    | `%y` | 연도 (2자리) | 25 |
    | `%m` | 월 (숫자, 2자리) | 04 |
    | `%B` <sup>1)</sup> | 월 이름 (전체) | April |
    | `%b` | 월 이름 (축약) | Apr |
    | `%d` | 일 (2자리) | 22 |

    <sup>1) **B**: "Full month name"을 나타내는 내부적인 약속. 영어의 약자는 아니고, C언어에서 쓰이던 strftime표준을 그대로 따라온 포맷 코드</sup> <br/>

  - 🕒 시간 관련

    | 코드 | 의미 | 예시 |
    |-----|-----|------|
    | `%H` | 시 (24시간제, 2자리) | 15 |
    | `%I` <sup>1)</sup> | 시 (12시간제, 2자리) | 03 |
    | `%M` | 분 (2자리) | 08 |
    | `%S` | 초 (2자리) | 59 |
    | `%p` <sup>1)</sup> | AM/PM 표시 | AM, PM |

    <sup>1) 영어의 약자는 아니고, C언어에서 쓰이던 strftime표준을 그대로 따라온 포맷 코드</sup> <br/>

  - 📆 요일 관련

    | 코드 | 의미 | 예시 |
    |-----|-----|-----|
    | %A <sup>1)</sup> | 요일 이름 (전체) | Tuesday |
    | %a | 요일 이름 (축약) | Tue |
    | %w | 요일 숫자 (0~6, 일요일=0) | 2 (화요일) |

    <sup>1) 영어의 약자는 아니고, C언어에서 쓰이던 strftime표준을 그대로 따라온 포맷 코드</sup> <br/>

  - 🗓️ 기타

    | 코드 | 의미 | 예시 |
    |-----|-----|-----|
    | %j | 올해의 몇 번째 날인가 | 112 |
    | %U | 연중 몇 번째 주 (일요일 시작) | 16 |
    | %W | 연중 몇 번째 주 (월요일 시작) | 17 |

#### 자주쓰는 포맷 예시

| 형태 | 포맷 문자열 | 예시 결과 | 
|-----|-----|-----|
| YYYY-MM-DD | `%Y-%m-%d` | 2025-04-22 |
| DD/MM/YYYY | `%d/%m/%Y` | 22/04/2025 |
| Month DD, YYYY | `%B %d, %Y` | April 22, 2025 |
| HH:MM:SS (24시) | `%H:%M:%S` | 15:08:59 |
| HH:MM AM/PM | `%I:%M %p` | 03:08 PM |
| 요일+날짜 전체 | `%A, %d %B %Y` | Tuesday, 22 April 2025 |

### time
- `Return the current time in seconds since the Epoch`: Epoch(1970년 1월 1일 00:00:00 UTC (유닉스 시간 기준점)) 기준으로 **얼마나 초가 지났는지를 반환** 하는 함수 (return: float)
- `Fractions of a second may be present if the system clock provides them`: 컴퓨터 시계가 초보다 더 정밀한 시간을 제공하면, 그 정밀도까지 반환
- time 모듈은 `간단한 타이머, 지연` 등에 많이 사용. 복잡한 날짜 계산, 시간대 처리 등은 datetime 모듈 사용

<details>
  <summary>UTC 시간</summary>

- UTC: Coordinated Universal Time
- 국제적으로 사용하는 조율 된 시간 대 (세계 어디서든 동일한 시간 기준으로 사용 가능)
- 표준 시간대 -> 시간대 계산의 기준점
- UTC+0 은 영국(Greenwich)
  - 영국 왕 찰스 2세가 런던의 그리니치에 왕립 천문대를 세움.
  - 이곳에서 정확한 별의 위치, 시각 계산, 향해용 시간 측정등을 연구함 (영국이 해양 강국이자 과학 선진국 이었음)
  - 19세기 후반은 대영제국의 전성기. 과학 기술, 향해, 철도, 산업에서 영국이 표준을 만들던 시기 -> 영국의 영향력이 강했음.
  - 이후 전 세계 향해자들이 시간을 맞출 기준점으로 사용 

- 왜 한국은 +9이고, 시드니는 +10일까?
  - 하루는 24시간, 지구는 360도 => 1시간에 15도(=260/24) 이동
  - 그리니치 기준점을 기준으로 15도 간격으로 24개의 시간 대로 나뉘어져 있음.
  - 그리니치 기준점(자🐭오🐴선, meridian)으로 오른쪽으로 갈 수록 + 왼쪽으로 갈수록 - 됨.
  - 한국(서울)은 동경 135도 => 즉, 135/15 = 9.xxx 이므로 UTC+9 임.

    &nbsp;&nbsp;← 서쪽(느림)&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;기준선(UTC+0)&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;동쪽(빠름) →

    | UTC-5 | UTC-1 | UTC+0 | UTC+3 | UTC+9 | UTC+10 |
    |-------|-------|-------|-------|-------|---------|
    | 뉴욕  | 리스본 | `런던`   | 이스탄불 | 서울   | `시드니`    |

</details>
<br/>

<details>
  <summary>1970년 1월 1일 00:00:00 이 기준인 이유</summary>

  - CPU는 심장이 뛰듯 tick을 발생시키는데 이를 기준으로 시스템이 돌아감.
  - 그래서 컴퓨터가 사람의 시간을 측정하는 방법은 특정 시점을 기준으로 그때부터 발생 된 틱의 수를 세는 방식.
  - Unix 시스템 개발 시점	1960년대 부터 존재. 1970년부터 본격적인 개발·보급 시작됨 -> 유닉스 개발자 중 한명이 기준점을 정함.
  - Epoch Time은 "1970-01-01 00:00:00 UTC"로, 유닉스 시스템이 내부적으로 시간을 계산할 때 기준으로 삼은 시작점
  - 대부분의 
  - 이 기준점 이전 날짜는 음수 값으로 표시
  <br/>
  <br/>

    - `운영체제 별 기준 시간`

    | 구분 | 기준 시각 | 비고 |
    |-----|---------|----|
    | Unix/Linux/macOS/Android | 1970-01-01 00:00:00 UTC |  유닉스 시간 기준 |
    | Windows 내부 (FILETIME) | 1601-01-01 00:00:00 UTC | 변환 필요 |
    | 대부분의 프로그래밍 언어 | 1970-01-01 UTC | 통일돼 있음 |

    - `운영체제 비교`

    | 운영체제 | 유닉스 계열인가? | 설명 |
    |-----|---------|----|
    | Unix |  원조 | 1969년, AT&T 벨 연구소에서 개발|
    | Linux | 유닉스 클론 | 유닉스를 참고해서 1991년 리누스 토르발스가 만든 오픈소스 OS|
    | macOS | 유닉스 기반 | 실제로 유닉스 인증 받은 OS (Darwin 기반)|
    | Windows | 유닉스 계열 아님 | 독자적인 NT 커널 기반으로 설계됨|
</details>

#### 주요 메서드
- `time.time()`: 현재 시간을 Epoch (1970.01.01 00:00:00 UTC) 기준으로 지난 초 단위 숫자(float)로 반환
  ```python
  import time
  print(time.time())  # 예: 1713764562.4712017
  ```

- `time.ctime([초])`: 타임스탬프를 보기 좋은 문자열로 변환
  ```python
  import time

  print(time.ctime())              # 현재 시간: 'Mon Apr 22 18:32:42 2025'
  print(time.ctime(0))            # Epoch 기준: 'Thu Jan  1 09:00:00 1970' (KST)
  ```

- `time.sleep(초)`: 몇 초간 정지/지연
  ```python
  import time
    
  print("3초 대기 중...")
  time.sleep(3)
  print("끝!")
  ```

- `time.localtime()` / `time.gettime()`: 현재 시간을 객체로 변환
  ```python
  import time

  now = time.localtime()
  print(now.tm_year, now.tm_mon, now.tm_mday)
  ```

- `time.strftime([문자열])`: '시간 객체 -> 문자열'로 변환
  ```python
  import time

  now_obj = time.localtime()  # 현재 지역 시간
  formatted = time.strftime("%Y/%m/%d", now_obj)
  print(f"지금 시각: {formatted}")
  ```

- `time.strptime([문자열], [포맷])`: '문자열 -> 시간 객체'로 변환
  ```python
  import time

  t = time.strptime("2025-04-22", "%Y-%m-%d")
  print(t.tm_year)  # 2025
  ```

## 모듈 구조
- `Module` = `classes` + `attributies`
  ```
  datetime (모듈)
  └── datetime (클래스)
  ```
