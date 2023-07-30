from inspect import _void
import sys

sys.stdin = open("lostcow.in", "r") 
sys.stdout = open("lostcow.out", "w")

x, y = list(map(int, input().split()))

# #x+1, x-2, x+4, x-8, x+16

# x = 7
# y = 5
abso = abs(y-x)*9

l = []
a = 0.5
c = x
t = 0

for n in range(abso):  
    if n%2==0:
        a = a*2
        l.append(a)
    elif n%2!=0:
        a = a*2
        l.append(-a)

for k in range(len(l)):
    c = x
    c += l[k]
    t += abs(l[k])*2
    # print(c, t)
    if x>y:
        if c<y or c==y:
            t -= abs(l[k])*2
            t += abs(x-y)
            break
    elif x<y:
        if c>y or c==y:
            t -= abs(l[k])*2
            t += abs(x-y)
            break
    
    # if abs(l[k])<b:
    #     t += abs(l[k]-b)
    #     break
    # elif c==b:
    #     break
    #c += l[k]#adding the traveling (c = final destination location)
    # t += abs(l[k])*2 #total traveling distance

print(int(t)) 

# 0 1 2 3 4 5 6 7
# 2 3 5 6 7 9

# for k in range(len(l)):
#     print(l[k], abs(b-j), j)
#     if abs(b-j)>l[k]:
#         c += (abs(b-j)-l[k])
#         for u in range(len(l)):
#             c += (abs(l[k]))*2
#             print(c)
#         break

# print(c)


# for j in range (len(l)):
#     for i in range (l[j]):
#         if l[j]<0:
#             j -= 1
#             c += 1
#         elif l[j]>0:
#             j += 1
#             c += 1
#         if j == b:
#             break

# add = 0

# for k in range(len(l)):
#     if (abs(l[k])<abs(j)) and (abs(l[k+2])>abs(j)):
#         for u in range(k):
#             add += abs(l[u])
#         for o in range():
#             if abs(l[k])==abs(j):
#                 break
#             abs(l[k]) + 1
#             add += 1

# print(add)

