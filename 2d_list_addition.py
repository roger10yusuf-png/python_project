list_one = [[1,2],
            [3,4]]

list_two = [[5,6],
            [7,8]]

list_three = [[0,0],
              [0,0]]
            
for i in range(2):
    for j in range(2):
        list_three[i][j] = list_one[i][j] + list_two[i][j]

print(list_three)