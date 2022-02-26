M,D,Y = map(int,input().split())
import calendar
day = calendar.weekday(Y, M, D)
print(calendar.day_name[day].upper())
