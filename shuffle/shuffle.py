from inspect import _void
import sys

sys.stdin = open("shuffle.in", "r") 
sys.stdout = open("shuffle.out", "w")

x = int(input())
y = list(map(int, input().split()))
z = list(map(int, input().split()))

# x = 5

# y = [1, 3, 4, 5, 2]
# z = [1234567, 2222222, 3333333, 4444444, 5555555]

# y.reverse()
# print(y)


o = []

for j in range(3):
    o = [0]*x
    for i in range(len(y)):
        o[i] = z[y[i]-1]
    z = o

for l in range(len(o)):
    print(o[l])
    
        # print(i)
        # a = z.pop(0)
        # print(a)
        # # y[i] z[y[i]]
        # b = z[y[i]-1]
        # o.insert(i, b)
        # print(o)
        # for k in range(len(z)): #0, 1, 2, 3...
        #     if k > i:
        #         z.append(z[k])
        #     elif k < i:
        #         z.insert()


        # z[i], z[y[i]-1] = z[y[i]-1], z[i]
        # print(z)
        #-2, -1, -1

    # x = number of cows
    # y = shuffle order of cows
    # z = the order of cows after three shuffles

'''
5
1 3 4 5 2
1234567 2222222 3333333 4444444 5555555

1. change 2 and 5
1234567 5555555 3333333 4444444 2222222

2. change 4 and 5
1234567 5555555 4444444 3333333 2222222

3. change 4 and 3
1234567 5555555 3333333 4444444 2222222

4. change 2 and 3
1234567 3333333 5555555 4444444 2222222

5. change 1 and 1
1234567 3333333 5555555 4444444 2222222????

1234567 5555555 2222222 3333333 4444444
1234567 5555555 2222222 3333333 4444444
1234567 2222222 5555555 3333333 4444444
1234567 2222222 3333333 5555555 4444444
1234567 2222222 3333333 4444444 5555555
1234567 5555555 3333333 4444444 2222222

1  2  3  4  5
1  3  4  5  2
a1 a2 a3 a4 a5

1234567 5555555 2222222 3333333 4444444
1234567 2222222 3333333 4444444 5555555
1       2       3       4       5
to a1   to a5   to a2   to a3   to a4

z[i-1]

13452
1번을 1번에 + 3번을 2번에 + 4번을 3번에 + 5번을 4번에 + 2번을 5번에

----
10
5 4 8 9 1 6 3 2 7 10
2641421 9202362 1490027 1368690 5520059 2897763 6513926 7180540 2383426 8089172


5520059 6513926 1368690 1490027 2641421 2897763 9202362 2383426 7180540 8089172
1490027 2641421 6513926 1368690 5520059 7180540 2383426 9202362 2897763 8089172
'''