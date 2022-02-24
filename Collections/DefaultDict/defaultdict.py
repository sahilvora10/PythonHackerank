from collections import defaultdict
n,m = map(int,input().split())
A = []
B = []
d = defaultdict(list)
for i in range(n):
    x = input()
    d[x].append(i+1)
for i in range(m):
    y = input()
    if d[y]:
        print(*d[y])
    else:
        print(-1)