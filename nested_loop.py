
def playing_cards(row__para, column_para):
    column_divider_number = column_para*2 - 1
    column_divider_string = ""
    for cd in range(column_divider_number):
        column_divider_string = column_divider_string + "-"

    print(column_divider_string)

    for row in range(row__para*2-1):
        if row % 2 == 0:

            for column in range(1, column_para*2):
                if column % 2 == 1:
                    if column != column_para*2-1:
                        print(" ", end="")

                    else:
                        print(" ")

                else:
                    print("|", end="")

        else:
            print(column_divider_string)


max_row = 19
max_column = 82

row_val = int(input("Enter row value: "))
column_val = int(input("Enter column value: "))
if row_val > max_row or column_val > max_column:
    print(False)
else:
    playing_cards(row_val, column_val)
    print(True)
