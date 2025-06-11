# orders
- 문제: `data/orders.csv` 파일에는 쇼핑몰 주문 정보가 저장되어 있는데, 이 파일을 읽어 다음과 같은 결과를 출력하는 프로그램을 작성
- 요구 사항:
    - 고객별 총 주문 금액 출력
    - 제품별 판매 개수 출력
    - 제품별 총 수익 출력 (수익 = 수량 × 가격), 수익 높은 순으로 정렬
    - 단, price 값이 잘못된 경우 해당 줄은 건너뛰고 오류 메시지를 출력


- 디렉토리 구조:
  ```
  shopping_system/
  ├── main.py
  ├── data/
  │   └── orders.csv
  ├── models/
  │   └── order.py
  ├── services/
  │   └── order_service.py
  └── views/
      └── report_view.py
  ```

- 출력 예시:
  ```yaml
  에러 발생: could not convert string to float: 'invalid_price' → 해당 줄은 건너뜁니다.

  🧾 고객별 총 주문 금액:
  - Alice: $96.0
  - Bob: $45.0
  - Dave: $76.5

  📦 제품별 총 판매량:
  - Mouse: 5개
  - Keyboard: 2개

  💰 제품별 총 수익 (내림차순):
  - Mouse: $127.5
  - Keyboard: $90.0
  ```

- 힌트:
  <details>
  <summary>힌트없이 문제 풀어보고 모르겠는 경우 열어보기 </summary>

  1. CSV 파일을 읽을 때는 csv 모듈을 사용
  
  ```python
  import csv

  with open('data/orders.csv', newline='', encoding='utf-8') as f:
    reader = csv.DictReader(f)
    for row in reader:
      print(row)

  ```

  2. 각 셀 값은 문자열(str)이므로 int(), float()를 사용하여 
  
  
  3. `views/report_view.py` 파일에 함수를 만들어서,
보기 좋은 형식으로 출력만 담당

  - 예시 코드: 
  ```python
  # views/report_view.py

  def print_total_per_customer(totals):
    print("🧾 고객별 총 주문 금액:")
    for name, total in totals.items():
      print(f" - {name}: ${total:.1f}")
  ```

  - `main.py`에서 사용하는 법
  ```python
  from views.report_view import print_total_per_customer

  print_total_per_customer(customer_totals)
  ```
  </details>

- csv 파일: [orders.csv](./orders.csv)
