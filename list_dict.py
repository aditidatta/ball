a = [[4,5,[6,7]], [1,2]] # 2 lists inside a list
b = [1,2,3,4]
a.append(b)
# a = [[4,5,[6,7]], [1,2], [1,2,3,4]]
print(a[1][0])
print(a[0][2][1])

h = []

# h -> []
# h -> [[1,2,3,4,5,6,7,8,9,10],[2,4,6,8,10,12,14,16,18,20], [3,6,9,...,30]]

for i in range(1,4):
    h.append([])
    for j in range(1,11):
        h[i-1].append( i * j)
print(h)

#[[1,2,3,4,5,6,7,8,9,10], [2,4,6,8,10, ........], [.........]]
