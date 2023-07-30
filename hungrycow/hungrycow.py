#input: 
# (number of rows below, days to calculate)
# (given at day #, how many given)

import sys

# sys.stdin = open("hungrycow.in", "r") 
# sys.stdout = open("hungrycow.out", "w")

ins = []
totaleaten = 0
N, T = list(map(int, input().split()))
# print(N, T)
for a in range (N):
    di, bi = list(map(int, input().split()))
    ins.append((di, bi))
    # print (di, bi)
ins.append((T+1, 0))
# print(ins)
# print(len(ins))
#ins[i+1][0]-ins[i][0] = next day - current day ()
left = 0
for i in range (len(ins)):
    if ins[i][1] > 0:
        totaleaten += min((ins[i+1][0]-ins[i][0]), ins[i][1] + left)
        left = max((ins[i][1]+left) - (ins[i+1][0]-ins[i][0]), 0)
    else:
        continue

print(totaleaten)

'''
the amount of hay left after doing {totaleaten += (ins[i+1][0]-ins[i][0])} this should be accumulated and counted for each of the next and after rounds
#1~T days
for n in range (len(inter)/2):
     if T inter[2*n] inter[(2*n)+1]:
     w
inter = [1, 6, 10, 13, 20, 24]
T = 10
day 1 3 3 0
day 5 5 2 3
day 7 1 4 0
day 11 0

day 1 2 (2)
day 5 6 7 8 9 10 11 12 13 14 (10)

day 1 6 (4) 2
day 5 10 (1) 11
day 6 0

--> (2)+(1)=3

day 1, 2, 3, 4 (6 left), 5 , 6 (6+3left), 7, 8, 9, 10, 11 (end of 7), 12, 13, 14 (end of 3 in the middle), 15, 16, 17, 18, 19, 20 (end)
'''
