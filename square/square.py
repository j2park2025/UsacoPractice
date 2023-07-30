import sys
sys.stdin = open("square.in", "r")
sys.stdout = open("square.out", "w")

x1, y1, x2, y2 = map(int, input().split()) 
x3, y3, x4, y4 = map(int, input().split())

lit = []
lit.append(x1)
lit.append(x2)
lit.append(x3)
lit.append(x4)

lit.sort()
side = lit[3]-lit[0]

print(side*side)