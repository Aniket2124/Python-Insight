'''
word = " Hello"

Letters = []
for w in word:
    print(w)
    if w == "e":
        print("what a funny letter")
    Letters.append(w)
print(Letters)


Numbers = [1, 2, 3, 4, 5]
for n in Numbers:
    if n % 2 == 0:
        print(n)
'''
# range(start, stop, steps)
'''


# printing Odd Numbers
Numbers = []
for num in range(1, 10, 2):

    Numbers.append(num)
    print(num)
print(Numbers)
'''


def digit(start, n):
    Numbers = []
    for num in range(1, n+1):
        if num % 3 == 0 and num % 5 == 0:
            Numbers.append("FizzBuzz")
        elif num % 3 == 0:
            Numbers.append("Fizz")
        elif num % 5 == 0:
            Numbers.append("Buzz")
        else:
            Numbers.append(str(num))

    return Numbers


verify = digit(1, 100)
print(verify)
