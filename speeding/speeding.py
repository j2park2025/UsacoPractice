from inspect import _void
import sys

sys.stdin = open("speeding.in", "r") 
sys.stdout = open("speeding.out", "w")

N, M = list(map(int, input().split()))

Nl = [] #N length
Ns = [] #N Speed Limit

Ml = [] #M Length (Bessie's Driven Length)
Ms = [] #M Speed (Bessie's Driven Speed)

len, spli= list(map(int, input().split()))
Nl.append(len)
Ns.append(spli)

for i in range(1, N):
    len, spli= list(map(int, input().split()))
    Nl.append(len+Nl[i-1])
    Ns.append(spli) # speed limit ex) [10, 30, 50, 90, 100]

Blen, Bspli= list(map(int, input().split()))
Ml.append(Blen)
Ms.append(Bspli) # Bessie's actual speed ex) [20, ]

for j in range(1, M):
    Blen, Bspli= list(map(int, input().split()))
    Ml.append(Blen+Ml[j-1])
    Ms.append(Bspli)

# print("Ns: ", Ns) #s = speed
# print("Nl: ", Nl) #l = length
# print("Ms: ", Ms)
# print("Ml: ", Ml)

record = []
nind = 0
mind = 0
for inf in range(1, 101):
    if inf > Nl[nind]:
        nind += 1 
    if inf > Ml[mind]:
        mind += 1
    if inf <= Nl[nind] and inf <= Ml[mind]:
        if (Ms[mind]-Ns[nind])>=0:
            record.append(Ms[mind]-Ns[nind])
        # speed comparison 


# if the inf is less than or equal to some kind of length, then check if the speedlimit of that particular zone is over/less than Bessie's actual speed.
# check to see Bessie's speed within her own length range
# if the inf is greater than the length range at the current ind #, then +1 to ind and test the whole thing again.

# the problem is if the number is negative then you shoudn't add it to the list

# for inf in range(100):
#     if inf<=Nl[ind]:
#         if inf<=Ml[ind]:
#             if (Ms[ind]-Ns[ind])>=0:
#                 record.append(Ms[ind]-Ns[ind])
#                 print(record)
#         else:
#             if (Ms[ind+1]-Ns[ind])>=0:
#                 record.append(Ms[ind+1]-Ns[ind])
#                 print(Ms[ind+1], "_______", Ns[ind])
#                 print(record)
#             elif (Ms[ind]-Ns[ind+1])>=0:
#                 record.append(Ms[ind+1]-Ns[ind])
#     else:
#         ind += 1

# print(record)

if record == []:
    print("0")
else:
    record.sort()
    record.reverse()   
    print(record[0])

# for inf in range(100):
#     if (inf<=Nl[ind]) and (inf<=Ml[ind]):
#         speedlimit = Ns[ind]
#         bessiespeed = Ms[ind]
#         print("the km is ", speedlimit)
#         if speedlimit<bessiespeed:
#             record.append(bessiespeed-speedlimit)
#     elif (inf<=Nl[ind]) and (inf>Ml[ind]):
#         speedlimit = Ns[ind]
#         bessiespeed = Ms[ind-1]
#         print(speedlimit )
#         if speedlimit<bessiespeed:
#             record.append(bessiespeed-speedlimit)
#     if inf>Nl[ind]:
#         ind += 1
#         if (inf<=Nl[ind]) and (inf<=Ml[ind]):
#             speedlimit = Ns[ind]
#             bessiespeed = Ms[ind]
#             print("less than ", speedlimit)
#             if speedlimit<bessiespeed:
#                 record.append(bessiespeed-speedlimit)
#         elif (inf<=Nl[ind]) and (inf>Ml[ind]):
#             speedlimit = Ns[ind]
#             bessiespeed = Ms[ind-1]
#             if speedlimit<bessiespeed:
#                 record.append(bessiespeed-speedlimit)

# 1. N and M are different in numbers
# but it deons' tmatter?