from datetime import datetime

t = int(input())

for t_itr in range(t):
    t1 = input()

    t2 = input()
    frmt = "%a %d %b %Y %H:%M:%S %z"
    T1 = datetime.strptime(t1,frmt)
    T2 = datetime.strptime(t2,frmt)
    print(int(abs(T1-T2).total_seconds()))
