filename = input("파일 이름을 입력하세요:")

numbers = []
try:
  with open("0603/" + filename, "r") as file:
    lines = file.readlines()

    for line in lines:
      number = int(line.strip())
      numbers.append(number)

except FileNotFoundError:
  print("파일이 존재하지 않습니다.")

except ValueError:
  print("숫자가 아닌 값이 포함되어 있습니다.")

else:
  pass

finally:
  print("파일 닫힘")
