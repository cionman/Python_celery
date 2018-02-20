import time

import tasks

result = tasks.add.delay(3, 9)
print('여기는 바로 찍히나?')
print('결과 : ' , result.get())

time.sleep(15)

print('결과 15초 후 : ', result.get())