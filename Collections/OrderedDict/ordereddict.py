from collections import OrderedDict
o = OrderedDict()
for i in range(int(input())):
    x,space,y = input().rpartition(" ")
    o[x] = o.get(x,0) + int(y)
for key, value in o.items():
    print(key, value)

# from collections import OrderedDict
# o = OrderedDict()
# for i in range(int(input())):
#     l = list(input().split())
#     x = " ".join(l[:-1])
#     y = int(l[-1])
#     o[x] = o.get(x,0) + y
# for key, value in o.items():
#     print(key, value)