list1 = [
    [11, 13],
    [15, 17],
    [19, 21]
]

list2 = [
    [1, 2],
    [3, 4],
    [5, 6]
]

list3 = [
    [0, 0],
    [0, 0],
    [0, 0]
]


for i in range(3):
    for j in range(2):
        list3[i][j] = list1[i][j] - list2[i][j]

print(list3)

