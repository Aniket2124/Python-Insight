def fun_loop_task(start, n):
    Numbers = []
    primeNumber = []

    for num in range(1, n+1):

        for i in range(2, num):
            if (num % i) == 0:
                break
        else:
            primeNumber.append(num)

        if num in primeNumber:
            Numbers.append("Prime")
        elif num % 3 == 0 and num % 5 == 0:
            Numbers.append("FizzBuzz")
        elif num % 3 == 0:
            Numbers.append("Fizz")
        elif num % 5 == 0:
            Numbers.append("Buzz")

        else:
            Numbers.append(str(num))
    return Numbers


print(fun_loop_task(1, 100))
