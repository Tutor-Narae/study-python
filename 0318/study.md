
# Collection Type: study_collection_type
- 여러 개의 데이터를 저장할 수 있는  컬렉션 자료형

| 자료형	| 특징	| 예시 | 
|--------|-------|-------|
| [List (리스트)](#list)	| 변경 가능(Mutable), 순서 유지	| ["apple", "banana", "cherry"]| 
|[Tuple (튜플)](#tuple)	|변경 불가능(Immutable), 순서 유지	|("apple", "banana", "cherry")|
|[Set (세트)](#set)	|중복 허용 X, 순서 없음	|{"apple", "banana", "cherry"}|
|[Dictionary (딕셔너리)](#dictionary)|	키-값(Key-Value) 쌍 저장	|{"name": "John", "age": 25}|

## List
- 여러 개의 데이터를 순서대로 저장 가능. 
- 값을 추가, 삭제, 변경 가능. 
- 중복 가능
- [] 사용

```python
# list
fruits1 = ["apple", "banana", "cherry", “apple”] # = 기준으로 왼쪽의 값을 오른쪽에 할당
print( fruits1 )    # ['apple', 'banana', 'cherry']
print(fruits1[0] ) # apple

# list() constructor
fruits2 = list(("apple", "banana", "cherry", “apple”)) # note the double round-brackets

# List length
print( len(fruits1) ) #4

# Access Items
print( fruits1[0] ) # apple
print( fruits1[-2] ) # cherry: 뒤에서부터 순서 셈.

# Range of Indexes
print(fruits[1:3])  # “banana”, "cherry": 1번째 포지션부터 (3-1)까지 출력
print(fruits[:3])    # “apple”, “banana”, “cherry”
print(fruits[1:])    # “banana”, “cherry”, “apple”
print(fruits[-3:-1]) # “banana”, “cherry”

# Check if Item exists
If “apple” in fruits1:
print("Yes, 'apple' is in the fruits list")

# Change item value
fruits1[1] = “lemon”
print( fruits1)

# Change a range of item values
fruits[1:3] = [“kiwi”, “mango”]
print( fruits1) 

# Insert items at the specified index
fruits1.insert(2, “watermelon”)

# Append items
fruits1.append(lemon)
print( fruits1 )

# Extend list: to append elements from another list
fruits1.extend(fruits2)
print( fruits1 )

# Remove specified item: If there are more than one item with the specified value, the remove() method removes the first occurrence
fruits1.remove(“banana”)

# Remove specified index
fruits1.pop(1)

# Sort list items
fruits1.sorted(fruits1)
```
### Differences Between `pop()` and `remove()`
| Method  | Removes by | Returns Removed Value | Affects Indices? |
|---------|------------|----------------------|------------------|
| `remove(value)` | Value | ❌ No | ✅ Yes, shifts elements left |
| `pop(index)` | Index  | ✅ Yes | ✅ Yes, shifts elements left |

결론:
- 특정 위치에서 요소를 제거할 때는 pop(index)
- 특정 값을 찾아서 삭제할 때는 remove(value)
- 제거된 값을 사용해야 하면 pop()을 사용

## Tuple
- 여러 개의 데이터를 순서대로 저장 가능. 
- 값을 추가, 삭제, 변경 불가능. 
- 중복 가능
- () 사용

## Set
- 여러 개의 데이터를 순서 없이 저장
- 값을 추가, 삭제, 변경 가능
- 중복 불가능
- {} 사용

## Dictionary
- 여러 개의 데이터를 순서 없이 key: value로 저장
- 값을 추가, 삭제, 변경 가능
- 중복 가능
- {} 사용

```python
# 딕셔너리 생성
student = {"name": "Alice", "age": 25, "grade": "A"}

# 특정 키 삭제
del student["age"]
print(student)  # {'name': 'Alice', 'grade': 'A'}

# 전체 딕셔너리 삭제
del student
# print(student)  # NameError: name 'student' is not defined

```
<br/>

# Conditional Statements: study_conditional_statements
## Comparison Operators (복습)
| Operator | Description                   | Example     |
|----------|-------------------------------|------------|
| `==`     | Equals                        | `a == b`   |
| `!=`     | Not Equals                    | `a != b`   |
| `<`      | Less than                     | `a < b`    |
| `<=`     | Less than or equal to         | `a <= b`   |
| `>`      | Greater than                  | `a > b`    |
| `>=`     | Greater than or equal to      | `a >= b`   |

## and
- 두개의 조건 다 만족할 때:
  ```python
  a = 200
  b = 33
  c = 500
  if a > b and c > a:
    print("Both conditions are True")
  ```

## or
- 둘 중 하나의 조건을 만족할 때:
  ```python
  a = 200
  b = 33
  c = 500
  if a > b or a > c:
    print("At least one of the conditions is True")
  ```

## not
- 조건이 아닐 때:
  ```python
  a = 33
  b = 200
  if not a > b:
    print("a is NOT greater than b")
  ```

## Nested If
- 여러개의 조건을 중첩해서 쓰고 싶을 때:
  ```python
  x = 41

  if x > 10:
    print("Above ten,")
    if x > 20:
      print("and also above 20!")
    else:
      print("but not above 20.")
  ```
