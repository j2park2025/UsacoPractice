import sys
sys.stdin = open("billboard.in", "r")
sys.stdout = open("billboard.out", "w")

x1, y1, x2, y2 = map(int, input().split()) # [1,2,3,5]
x3, y3, x4, y4 = map(int, input().split())
x5, y5, x6, y6 = map(int, input().split())

# x3 = 6
# y3 = 0
# x4 = 10
# y4 = 4

# x5 = 2
# y5 = 1
# x6 = 8
# y6 = 3

firstb = int(x1-x2)*int(y1-y2)
seconb = int(x3-x4)*int(y3-y4)

# print(firstb, seconb)

twoblockarea = firstb + seconb

in1 = ((min(x2, x6) - max(x1, x5)))
in2 = ((min(x4, x6) - max(x3, x5)))
in3 = ((min(y2, y6) - max(y1, y5)))
in4 = ((min(y4, y6) - max(y3, y5)))

# print(in1, in2, in3, in4)
OverlapArea = (in1*in3) + (in2*in4)
# print("Overlapping Area:", OverlapArea)
print(twoblockarea - OverlapArea)

# r1 x1 y1 x2 y2 
# r2 x1 y1 x2 y2

# min(r1.x2, r2.x2) - max(r1.x1, r2.x1)
