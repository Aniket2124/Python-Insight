def isTwoValuesEqual(first_par, second_par, third_par):
    if(first_par == second_par or second_par == third_par or first_par == third_par):
        return True
    return False


print(isTwoValuesEqual(7, int("5"), 6))
