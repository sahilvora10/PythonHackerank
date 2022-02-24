from collections import deque
for i in range(int(input())):
    n = int(input())
    d = deque(map(int,input().split()))
    # print(d)
    m = max(d[0],d[-1])
    while len(d) > 0:
        # print(d)
        if d[0]>=d[-1] and m>=d[0]:
            m = d.popleft()
            # print(m)
        elif d[-1]>d[0] and m>=d[-1]:
            m = d.pop()
            # print(m)
        else:
            break
    if(len(d)==0):
        print('Yes')
    else:
        print('No')
