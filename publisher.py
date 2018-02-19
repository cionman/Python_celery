import tasks

result = tasks.add.delay(3, 9)

print('결과 : ' , result.get())
