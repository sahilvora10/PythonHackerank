from itertools import combinations

A = list(input().split())
S = A[0]
k = int(A[1])
for i in range(1,k+1):
    C = list(combinations(sorted(S),i))
    print('\n'.join(''.join(x) for x in C))