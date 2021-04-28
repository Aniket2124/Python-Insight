# Tic Tac Toe Game
def drawfield(field):
    for row in range(5):    # 0 1 2 3 4
        if row % 2 == 0:  # print lines
            practicalRow = int(row / 2)
            for column in range(5):
                if column % 2 == 0:  # 0 2 4
                    practicalColumn = int(column / 2)  # 0 1 2
                    if column != 4:
                        print(field[practicalColumn][practicalRow], end="")
                    else:
                        print(field[practicalColumn][practicalRow])
                else:
                    print("|", end="")

        else:
            print("-----")


player = 1
currentfield = [[" ", " ", " "], [" ", " ", " "], [" ", " ", " "]]
drawfield(currentfield)
while(True):  # True == True
    print("Player Turn: ", player)
    move_row = int(input("Enter a Row: "))
    move_column = int(input("Enter a Column: "))
    if player == 1:  # make move for layer 1
        if currentfield[move_column][move_row] == " ":
            currentfield[move_column][move_row] = "X"
            player = 2
    else:
        if currentfield[move_column][move_row] == " ":
            currentfield[move_column][move_row] = "O"
            player = 1
    drawfield(currentfield)
