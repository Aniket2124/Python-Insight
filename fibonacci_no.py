def fun_fibonacci_series(fibonacci_num_limit):
    if fibonacci_num_limit < 0:
        print("Incorrect no")
    elif fibonacci_num_limit == 0:
        print(0)

    elif fibonacci_num_limit == 1:
        print("0,1")
    else:
        fibonacci_series_str = "0, 1"
        fibonacci_num = 0
        fibonacci_num_last = 1
        for i in range(1, fibonacci_num_limit-1):
            if fibonacci_num_last < fibonacci_num_limit:
                temp_fibonacci_num = fibonacci_num + fibonacci_num_last
                fibonacci_num = fibonacci_num_last
                fibonacci_num_last = temp_fibonacci_num
                fibonacci_series_str = fibonacci_series_str + \
                    ", " + str(fibonacci_num_last)
            '''
            fibonacci_series_str = fibonacci_series_str + \
                ","+str(fibonacci_num_last)
            fibonacci_num = int(fibonacci_num) + int(fibonacci_num_last)
            print(fibonacci_num)
            fibonacci_num_last = int(fibonacci_num_last) + int(fibonacci_num)
            fibonacci_series_str = fibonacci_series_str + \
                ","+str(fibonacci_num)
            '''

        print(fibonacci_series_str)


fibonacci_series_limit_input = int(
    input("Please enter fibonacci series limit : "))
fun_fibonacci_series(fibonacci_series_limit_input)
# 0,1,1,2,3,5,8,13,21

# 01

# new fibonacci program


def fib(n):    # write Fibonacci series up to n
    a, b = 0, 1
    while a < n:
        print(a, end=' ')
        a, b = b, a+b
    print()


def fib2(n):   # return Fibonacci series up to n
    result = []
    a, b = 0, 1
    while a < n:
        result.append(a)
        a, b = b, a+b
    return result
