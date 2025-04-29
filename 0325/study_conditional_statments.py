person ={"name": "Alice"}

match person:
  case {"name": name, "age": age}: 
    print(f"name is {name}, and age is {age}")
  case {"name": name}: 
    print(f"name is {name}")
  case {"age": age}: 
    print(f"age is {age}")
  case _:
    print()




# - 문제: 사용자가 입력한 숫자에 따라 다른 메시지를 출력
#   - 1이면 → "하나"
#   - 2이면 → "둘"
#   - 3이면 → "셋"
#   - 그 외의 경우 → "알 수 없는 숫자"




# - 문제: 리스트의 길이에 따라 다른 메시지를 반환하는 "함수"를 작성
#   - 빈 리스트 → "리스트가 비어 있습니다."
#   - 하나의 요소가 있는 경우 → "하나의 요소가 있습니다."
#   - 두 개의 요소가 있는 경우 → "두 개의 요소가 있습니다."
#   - 그 외의 경우 → "여러 개의 요소가 있습니다."

# check_list_length([])
# check_list_length([1])
# check_list_length([1,2])
# check_list_length([1,2,5,6,7])


# - 딕셔너리를 입력받아 특정 키(name, age)가 존재하는지 확인하는 함수
#     - {"name": "Alice", "age": 25} → "이름: Alice, 나이: 25"
#     - {"name": "Bob"} → "이름: Bob, 나이는 없음"
#     - {"age": 30} → "이름 없음, 나이: 30"
#     - 기타 → "이름과 나이를 알 수 없음"

# is_exist( {"name": "Alice"} )
# print(is_exist( {"name": "Alice", "age": 25} ))
# print(is_exist( {"name": "Bob"} ))
# print(is_exist( {"weight": 70} ))
