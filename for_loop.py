
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

# range(start, stop, steps)


# printing Odd Numbers
Numbers = []
for num in range(1, 10, 2):

    Numbers.append(num)
    print(num)
print(Numbers)
