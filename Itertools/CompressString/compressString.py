from itertools import groupby
S = input()
C = groupby(S)
C = [(len(list(g)),int(k)) for k,g in C]
print(*C)
