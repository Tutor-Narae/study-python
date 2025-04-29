list = [1,2,3,4]

list2= [(1,2), (3,4)]
for item in list2:
  print(item)

str1 = "hello"
for item in str1:
  print(item)

for item in range(6):
  print(item)

for item in range(2,5):
  print(item)

adj = ["red", "big", "tasty"]
fruits = ["apple", "banana", "cherry"]

for item1 in adj:
  for fruit in fruits:
    print(item1, fruit)



#  1부터 100까지 짝수만 출력하는 프로그램을 작성


for num in range(1, 101):
  if( num % 2 == 0 ):
    print(num)


# 5부터 1까지 거꾸로 출력
for num in range(0,5):
  print(5-num)