current_hour, current_minute = input().split()
required_time = input()
hour = int(current_hour)
minute = int(current_minute)
delta = int(required_time)
delta_hour = delta//60
delta_minute = delta%60
hour += delta_hour
minute += delta_minute
if(minute >= 60):
    hour += minute//60
    minute = minute%60
if(hour >= 24):
    hour = hour%24
print("{} {}".format(hour, minute))