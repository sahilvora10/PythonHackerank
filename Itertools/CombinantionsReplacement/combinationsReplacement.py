from itertools import combinations_with_replacement

A = list(input().split())
S = A[0]
k = int(A[1])
C = list(combinations_with_replacement(sorted(S),k))
print('\n'.join(''.join(x) for x in C))
