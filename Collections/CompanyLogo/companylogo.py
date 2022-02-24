from collections import Counter
s = sorted(input())
c = Counter(s)
# print(c)
for key, value in c.most_common(3):
    print(key, value)