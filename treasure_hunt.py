import random
treasurehunt_line = [["_","_","_","_"],["_","_","_","_"],["_","_","_","_"],["_","_","_","_"]]
def show_map():
    for i in range(4):
        for j in range(4):
            print(treasurehunt_line [i][j],end=" ")
        print()
show_map() 

treasure_x = random.randint(0,3)
treasure_y = random.randint(0,3)
while True:
    guess_treasure_x = int(input("which row?"))
    guess_treasure_y = int(input("which column?"))
    if treasure_x == guess_treasure_x and treasure_y == guess_treasure_y:
        print("\n you have found the treasure \n")
        break
    if guess_treasure_x < treasure_x:
        print("\n go down \n")
    elif guess_treasure_x > treasure_x:
        print("\n go up \n")
    if guess_treasure_y < treasure_y:
         print("\n move to the right \n")
    elif guess_treasure_y > treasure_y:
        print("\n move to the left \n")
    if guess_treasure_x > 3 or guess_treasure_x < 0 or guess_treasure_y > 3 or guess_treasure_y < 0:
        print("\n the row or the column of the number is incorrect. please pick a number between 0 and 3 \n")
    treasurehunt_line[guess_treasure_x][guess_treasure_y] = "X"
    show_map()