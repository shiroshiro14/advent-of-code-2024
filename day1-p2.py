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

for l in left:
    temp = right.count(l)
    result += l * temp

print(result)

