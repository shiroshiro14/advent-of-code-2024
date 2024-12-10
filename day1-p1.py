f = open("day1.txt", "r")
s = f.read()[:-1]
lines = s.split('\n')
left = []
right = []
result = 0
for l in lines:
    temp = l.split('  ')
    #print(temp)
    left.append(int(temp[0]))
    right.append(int(temp[1]))

left.sort()
right.sort()
print(left)
print(right)
for l, r in zip(left, right):
   result += abs(l-r)

print(result)
