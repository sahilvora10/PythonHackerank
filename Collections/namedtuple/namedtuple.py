from collections import namedtuple
N, Student = int(input()) , namedtuple('Student',input().split())
S = [int(Student(*input().split()).MARKS)  for i in range(N)]
print("{0:.2f}".format(sum(S)/N))

# from collections import namedtuple
# N = int(input())
# col_name = list(input().split())
# Student = namedtuple('Student',col_name)
# s = 0
# for i in range(N):
#     f1,f2,f3,f4 = input().split()
#     x = Student(f1,f2,f3,f4)
#     s += int(x.MARKS)
# print("{0:.2f}".format(s/N))