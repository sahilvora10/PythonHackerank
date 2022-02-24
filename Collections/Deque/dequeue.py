from collections import deque
d = deque()
# for i in range(int(input())):
#     s = list(input().split())
#     if(s[0] == 'append'):
#         d.append(int(s[1]))
#     elif(s[0] == 'appendleft'):
#         d.appendleft(int(s[1]))
#     elif(s[0]=='pop'):
#         d.pop()
#     else:
#         d.popleft()
# print(*d)
for i in range(int(input())):
    cmd,*args = input().split()
    getattr(d,cmd)(*args)
print(*d)