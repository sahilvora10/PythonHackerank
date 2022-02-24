from collections import Counter
X = int(input())
Y = list(map(int,input().split()))
N = int(input())
# print(X,Y,N)
c = Counter(Y)
# print(c)
sum = 0
for i in range(N):
    s,xi = map(int,input().split())
    if c[s]:
        sum += xi
        c[s] -= 1
print(sum)