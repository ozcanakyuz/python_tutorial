import time
import datetime

print('Please type your text after 3 seconds..')

print('3')
time.sleep(1)
print('2')
time.sleep(1)
print('1')
time.sleep(1)
print('GO!')
time.sleep(0.2)
before = datetime.datetime.now()

text = input("Type Here : ")
after = datetime.datetime.now()

speed = after - before
seconds = round(speed.total_seconds(),2)
letter_per_second = round(len(text) / seconds, 1)

print(f'You typed in : {format(seconds)} second')
print(f'Your speed is: {letter_per_second} letters per second')