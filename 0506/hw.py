class Student:
  def __init__(self, name, score):
    self.name = name
    self.score = int(score)
  
students = []
for student in range(3):
  name_and_score = input("학생 이름과 점수를 입력하세요(이름 점수):")
  name, score = name_and_score.split(" ")
  student = Student(name, score)
  students.append(student)

average = sum(student.score for student in students) / len(students)
print(f"평균 점수: {average:.1f}")