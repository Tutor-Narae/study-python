# import math

# print(math.sqrt(4))
# print(math.pow(4, 2))
# print(math.log10(abs(-1000)))
# print(math.pi * 4)

# import random

# print(random.random())
# print(random.randint(1, 10))
# print(random.choice(["A", "B", "C", "D"]))


# import datetime

# now = datetime.datetime.now()
# print(now)
# print(now.date())
# print(now.time())
# print(now.hour)

# import os

# print( os.getcwd() )
# print( os.listdir())

import time

# print("5초 후에 인사할게요!")
# time.sleep(5)
# print("안녕하세요!")

start = time.time()

for i in range(1, 10001):
  continue

end = time.time()

print(f"걸린시간: {end - start}")