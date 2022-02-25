import itertools

N = int(input())
l = list(input().split(' '))
k = int(input())

r = [i for i in range(1,N+1)]
r = list(itertools.combinations(r,k))
indices = [i+1 for i, x in enumerate(l) if x == 'a']
c = 0
for t in r:
    if any(i in t for i in indices):
        c += 1
print(c/len(r))