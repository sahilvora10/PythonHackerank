from itertools import permutations

A = list(input().split())
S = A[0]
k = int(A[1])
C = list(permutations(sorted(S),k))
print('\n'.join(''.join(x) for x in C))