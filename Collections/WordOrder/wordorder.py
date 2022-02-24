from collections import OrderedDict
o = OrderedDict()
for i in range(int(input())):
    s = input()
    o[s] = o.get(s,0) + 1
print(len(o))
print(*o.values())

# from collections import OrderedDict
# o = OrderedDict()
# for i in range(int(input())):
#     s = input()
#     if o.get(s):
#         o[s] += 1
#     else:
#         o[s] = 1
# print(len(o))
# print(*o.values())