class MyCar:

  def __init__(self, maker, year):
    self.maker = maker
    self.year = year
  
  def move():
    print("Move")

mycar = MyCar("Hyundai",2024)
print(mycar.maker)
print(mycar.year)

mycar.move()