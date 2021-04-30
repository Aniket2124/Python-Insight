'''
Word = "Viraj"
Letters = []
for w in Word:
   # if w == "a":
   #     print("Funny letter")
    Letters.append(w)
    print(w)
    print(Letters)


participants = ["Aniket", "Viraj", "Abhi", "Avi", "Kiran", "Sourabh"]
position = 1

for currentIndex in range(len(participants)):
    print(currentIndex)
    if participants[currentIndex] == "Kiran":
        print("break")
        break

    print("Not break")

print(currentIndex+1)

for number in range(10):
    if number % 3 == 0:
        print(number)
        continue
    print("Number Divisible by 3")
    print(number)
    print("not divisible by 3")
'''
'''
# 1. Write a Python program to find those numbers
# which are divisible by 7 and multiple of 5, between 1500 and 2700 (both included).
num = []
for numbers in range(1500, 2700):
    if numbers % 7 == 0 and numbers % 5 == 0:
        num.append(numbers)

print(num)

# Write a Python program to construct the following pattern, using a nested for loop.
'''
'''
*
* *
* * *
* * * *
* * * * *
* * * *
* * *
* *
*

'''
'''
star = 5
for i in range(star):
    for j in range(i):
        print('*', end="")
    print('')
for i in range(star, 0, -1):
    for j in range(i):
        print('*', end="")
    print('')
'''
n = input("enter a number\n")
if int(n) % 2 == 1:
    print("Weird")
else:
    if int(n) >= 2 and int(n) <= 5:
        print("Not Weird")
    elif int(n) >= 6 and int(n) <= 20:
        print("Weird")
    elif int(n) > 20:
        print("Not Wired")

    # 9767382913 baban salvi

a = 6564424525
b = 323252462
print(a+b)
print(a-b)
print(a*b)
# print(int(a/b))
# print(float(a/b))
