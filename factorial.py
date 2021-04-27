def fun_fact():
    num = int(input("Enterthr Factorial no: "))
    factorial = 1
    if num < 0:
        print("Negative No & No Factorial")
    elif num == 0:
        print("Factorial of 0 is 1")
    else:
        for i in range(1, num + 1):
            factorial = factorial * i
    print("The factorial of", num, "is", factorial)


fun_fact()
