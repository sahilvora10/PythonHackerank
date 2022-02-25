from itertools import product
def Sq(n):
    return int(n)**2
K, M = map(int,input().split())
l = []
for i in range(K):
    l.append(list(map(Sq,input().split()))[1:])
# print(l)
p = list(product(*l))
c = 0
for i in p:
    s = sum(i)
    c = max(c,s%M)
print(c)
