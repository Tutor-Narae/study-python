# integer = [1, 2, 3, 4]
nums = input("숫자 리스트:")
target = input("찾고 싶은 정수:")

nums = list(map(int, nums.split()))

if target in nums:
 print(target, "은 리integer스트에 포함되어 있습니다.")
 