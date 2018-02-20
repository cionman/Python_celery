import time

import tasks

result = tasks.add.delay(3, 9) # 여기는 비동기
print('여기는 바로 찍히나?')
print('결과 : ' , result.get()) # 여기는 동기 
print('여기는???')
time.sleep(15)

print('결과 15초 후 : ', result.get())