# import sys

# t = int(input())
# cows = list(map(int, input().split()))

t = 6 #int(input())
nm = [] #[number of cows, max moving distance]
go = [] #["given order"]
patchH = 0
patchG = 0
mark = False
finarr = []
for i in range(t):
    N, K= 5, 2#list(map(int, input().split()))
    cows = "GHHGG"#input()
    finarr = [] #purpose?
    for n in range(N):
        finarr.append('.')
    for a in range (N): # number of cows 만큼 반복  N = 5 01234
        # if a + K >= len(cows): #if it's the end
        #     finarr[len(cows)] = go[a]

        cows[a] == 'H' 'G'
        if patchH > a:
            continue 
        else:
            if a+K >= N: #if the max travel distance + current location is >= the number of cow locations available,
                finarr[a+K-1] = cows[a] # go one step back and place it there
                print("if a+K >= N", finarr)
                print("a, K = ", a, K)
                #a = for's value starting from 0
            else:
                finarr[a+K] = cows[a] # orselse just place it in the space
                print("else", finarr)
                print("a, K = ", a, K)
                #K = maximum traveling distance of the cows
                #N = the numer of cows

    print(finarr)
