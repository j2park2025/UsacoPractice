import sys

n = int(input())
cows = list(map(int, input().split()))

# sys.stdin = open("cowcollege.in", "r") 
# sys.stdout = open("cowcollege.out", "w")

# n = int(input())
# cows = list(map(int, input().split()))
# for i in range(n):
#     c = list(map(int, input().split()))
#     cows.append(c)

cows.sort()
pos = 0
# rows, cols = (n, 3)
# arr = [[0]*cols]*rows
# print(arr)
d = [[0] * (3) for a in range(n)]
# print(d)
for i in range(n):
    pos = cows[i]*(n-i)
    # print(pos)
    d[i][0] = pos
    d[i][1] = cows[i] # the tuition fee
    d[i][2] = (n-i) # number of cows attending
    # full[i][i][i].insert(pos, cows[i], (n-i))
    # print(full)
d.sort()
for f in range(len(d)-1, -1, -1):
    if d[f][0] != d[f-1][0]:
        answer = f
        break
# print(d)
print(d[answer][0], d[answer][1])

