names = input("학생 이름:").split(",")
scores = list(map(int, input("학생 점수:").split(",")))
 
def print_results():
 average = sum(scores) / len(scores)

 for name, score in zip(names, scores):
  if score >= average:
    result = "합격"
  else:
    result = "불합격"
  
  print(f"{name}: {score}점 -> {result}")

print_results()