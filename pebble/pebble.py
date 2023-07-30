import sys

sys.stdin = open("pebble.in", "r")
sys.stdout = open("pebble.out", "w")
k = 0
n = list(map(int, input().split()))[0]

# print(n)
l = []
for p in range(n):
    l.append(k)
    k+=1

k = 0
counter = []
for p in range(n):
    counter.append(k)

answer = 0

for i in range (n):
    a1, b1, g1 = map(int, input().split())

    a1-=1
    b1-=1
    g1-=1

    l[a1], l[b1] = l[b1], l[a1] #switch a1 and b1
    counter[l[g1]] +=1

print(max(counter))

    # print("ans = ", ans)
    # for i in range(1, len(ans)): #1~len[g1]
    # if ans[0] == ans[i]:
    #     k+=1
    #     print("in the for:", k)

# if k>(len(ans)-k):
#     final = k
#     print(k)
# else:
#     final = len(ans)-k

# print("final:", final)
# final = [i for i in ans if ans[0]==ans[i]]
# print("final = ", final)
# print(len(final))

'''
1 2 3
2 1 3
2 3 1
1 3 2
'''