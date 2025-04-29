def print_diamond(n):
 if n % 2 == 1:
  for i in range(1, n+1, 2):
    print(" " * ((n - i) // 2) + "*" * i)
  for i in range(n-2, 0, -2):
    print(" " * ((n - i) // 2) + "*" * i)
 else:
    print("홀수를 입력하세요.")

n = int(input())
print_diamond(n)