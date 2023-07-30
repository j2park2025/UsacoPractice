import sys

# t = int(input())
# cows = list(map(int, input().split()))

# sys.stdin = open("feeding.in", "r") 
# sys.stdout = open("feeding.out", "w")

t = int(input())
c = [] #con
d = [] #given order
for i in range(t):
    c = list(map(int, input().split()))
    d = list(map(str, input().split()))
    lis = []
    for n in range(len(d[0])):
        lis.append('.')

    # a[0:2] + "7" + a[3:]
    for k in range(c[0]): #when t=0, c = [5, 0] k = 0, 1, 2, 3, 4
        if(c[1]+k)>=c[0]:# when k = 1 and t = 0 --> 0>=5 
            mark = True
            for j in range (max(k-c[1],0), k):
                if (lis[k-j]== d[0][k]): # t=0, k=2 01 lis[2-0, 2-1] ||| k = 3, t = 1, j = 012 lis[1+3-0]
                    mark = False
                    break
                        # print(lis[c[1]+k-j], c[1]+k-j, k, j)
                else: 
                    mark = True  
             
            if mark == False:
                continue
            else:
                if lis[len(lis)-1]==".":
                    lis[len(lis)-1] = d[0][k]
                # print("inserted H in the last space")  
                elif lis[len(lis)-1]!=".":
                    for j in range(len(lis)-1, -1, -1):
                        if lis[j]==".": 
                            lis[j] = d[0][k] # if theres none
                            break
                        elif lis[j] == d[0][k]: #if there is already
                            break
            
            # continue
        elif(c[1]+k)<c[0]: # yes 0<5
            
            mark = True
            for j in range(max(k-c[1],0), k):#t = 0, k = 1 lis[0-1+0] current location +- j cl = lis[k]
                if (lis[c[1]+k-j]== d[0][k]): # 3+0, 1, 2, 3 ,4 - (0, 1, 2, 3 ,4 minus the max traveling distance ~ 0, 1, 2, 3 ,4) t=0, k=2 01 lis[2-0, 2-1] ||| k = 3, t = 1, j = 012 lis[1+3-0]
                    mark = False
                    # print(lis[c[1]+k-j], c[1]+k-j, k, j)
                else: 
                    mark = True
                    # break 
            if mark == False:
                # print("mrk is Flase so it is continued")
                continue
            #+=(-k, -k+1, -k+2)
            #if all of result above was continue, then continue \ if not, move onto the 조건 bleow
            if mark == True: #lis[c[1]-k]!= d[0][k]: 
                lis[c[1]+k] = d[0][k] #lis[0] = d[0][0]
            # print(lis)
            #-----------added------------#
        # lis[0:(c[1]-1)] + d[0][k] + lis[c[1]:]
        # print(lis)
        # lis[j][k+c[(k*2)+1]]
    print(len(lis)-lis.count("."))
    print("".join(lis))
    # lis.append(c+d)
'''
0
01
1
23
2*2, 2*2+1
45
3*2, 3*2+1
67
'''
# lis = []
# for n in range(len(d)):
#     lis.append('.'*len(d[n]))



# j = 0
# for k in range(10^5):
#     j + ((10^5)-k)

#farthest placement

'''
Farmer John has N
 (1≤N≤105
) cows, the breed of each being either a Guernsey or a Holstein. They have lined up horizontally with the cows occupying positions labeled from 1…N
.
Since all the cows are hungry, FJ decides to plant grassy patches on some of the positions 1…N
. Guernseys and Holsteins prefer different types of grass, so if Farmer John decides to plant grass at some location, he must choose to planting either Guernsey-preferred grass or Holstein-preferred grass --- he cannot plant both at the same location. Each patch of grass planted can feed an unlimited number of cows of the appropriate breed.

Each cow is willing to move a maximum of K
 (0≤K≤N−1
) positions to reach a patch. Find the minimum number of patches needed to feed all the cows. Also, print a configuration of patches that uses the minimum amount of patches needed to feed the cows. Any configuration that satisfies the above conditions will be considered correct.

INPUT FORMAT (input arrives from the terminal / stdin):
Each input contains T
 test cases, each describing an arrangement of cows. The first line of input contains T
 (1≤T≤10
). Each of the T
 test cases follow.
Each test case starts with a line containing N
 and K
. The next line will contain a string of length N
, where each character denotes the breed of the i
th cow (G meaning Guernsey and H meaning Holstein).

OUTPUT FORMAT (print output to the terminal / stdout):
For each of the T
 test cases, please write two lines of output. For the first line, print the minimum number of patches needed to feed the cows. For the second line, print a string of length N
 that describes a configuration that feeds all the cows with the minimum number of patches. The i
th character, describing the i
th position, should be a '.' if there is no patch, a 'G' if there is a patch that feeds Guernseys, and a 'H' if it feeds Holsteins. Any valid configuration will be accepted.
SAMPLE INPUT:
6
5 0
GHHGG
5 1
GHHGG
5 2
GHHGG
5 3
GHHGG
5 4
GHHGG
2 1
GH
SAMPLE OUTPUT:
5
GHHGG
3
.GH.G
2
..GH.
2
...GH
2
...HG
2
HG
Note that for some test cases, there are multiple acceptable configurations that manage to feed all cows while using the minimum number of patches. For example, in the fourth test case, another acceptable answer would be:

.GH..
This corresponds to placing a patch feeding Guernseys on the 2nd position and a patch feeding Holsteins on the third position. This uses the optimal number of patches and ensures that all cows are within 3 positions of a patch they prefer.

SCORING:
Inputs 2 through 4 have N≤10
.
Inputs 5 through 8 have N≤40
.
Inputs 9 through 12 have N≤105
.
Problem credits: Mythreya Dharani

LINK:
http://www.usaco.org/index.php?page=viewproblem2&cpid=1252
'''