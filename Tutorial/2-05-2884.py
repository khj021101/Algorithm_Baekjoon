#Datetime 라이브러리로 날먹하려 했으나 import 시간 때문에 시간초과됨
hour_input, minute_input = input().split()
hour, minute = int(hour_input), int(minute_input)
mod_hour, mod_minute = 0, 0
#hour 와 minute을 직접 바꾸면 조건문을 통과한 뒤 바뀐 변수 때문에 이후 조건문에 다시 걸릴 수 있음
if(minute >= 45):
    mod_hour = hour
    mod_minute = minute - 45
else:
    if(hour == 0):
        mod_hour = 23
        mod_minute = 60 - (45 - minute)
    else:
        mod_hour = hour - 1
        mod_minute = 60 - (45 - minute)
print("{} {}".format(mod_hour, mod_minute))