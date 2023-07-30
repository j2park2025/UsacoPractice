import sys

sys.stdin = open("mixmilk.in", "r") #mixmilk.in
sys.stdout = open("mixmilk.out", "w")

c1, m1 = list(map(int, input().split()))
c2, m2 = list(map(int, input().split()))
c3, m3 = list(map(int, input().split()))

for i in range (33):
    m2 += m1 
    if m2>c2:
        m1 = (m2-c2)
        m2 = c2
    elif m2<=c2:
        m1 = 0
    m3 += m2 
    if m3>c3:
        m2 = (m3-c3)
        m3 = c3
    elif m3<=c3:
        m2 = 0
    m1 += m3
    if m1>c1:
        m3 = (m1-c1)
        m1 = c1
    elif m1<=c1:
        m3 = 0

m2 += m1 
if m2>c2:
    m1 = (m2-c2)
    m2 = c2
elif m2<=c2:
        m1 = 0

print(m1)
print(m2)
print(m3)

# lost = [m1, m2, m3]

# for i in range (100):
#    lost[0] += m1 
#     if m2>11:
#         m1 = (m2-11)#+m1
#         m2 = 11
#     elif m2<=11:
#         m1 = 0