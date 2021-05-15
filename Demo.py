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

'''
'''
Q.Write a Python program to count the number of even and odd numbers from a series of numbers. Go to the editor
Sample numbers : numbers = (1, 2, 3, 4, 5, 6, 7, 8, 9) 
Expected Output :
Number of even numbers : 5
Number of odd numbers : 4
'''

even_no = []
odd_no = []
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
for number in numbers:
    if number % 2 == 0:

        even_no.append(number)
    else:
        odd_no.append(number)

print("Number of even numbers :", len(even_no))
print("Number of odd numbers :", len(odd_no))


'''
Write a Python program that prints each item and its corresponding type from the following list.
Sample List : datalist = [1452, 11.23, 1+2j, True, 'w3resource', (0, -1), [5, 12], {"class":'V', "section":'A'}]

'''

datalist = [1452, 11.23, 1+2j, True, 'w3resource', (0, -1), [5, 12],
            {"class": 'V', "section": 'A'}]
for item in datalist:
    print("Type of", item, "is", type(item))
'''
Write a Python program that prints all the numbers from 0 to 6 except 3 and 6.
Note : Use 'continue' statement.
Expected Output : 0 1 2 4 5
'''
#num = [0, 1, 2, 3, 4, 5, 6]
for i in range(6):
    if(i == 3 or i == 6):
        continue
    print(i)

print("\n")
'''
 Write a Python program to get the Fibonacci series between 0 to 50. 
Note : The Fibonacci Sequence is the series of numbers :
0, 1, 1, 2, 3, 5, 8, 13, 21, ....
Every next number is found by adding up the two numbers before it.
Expected Output : 1 1 2 3 5 8 13 21 34
'''
fibancciNo1 = 0
fibancciNo2 = 1
fibancciArray = []
fibancciArray.append(fibancciNo1)
fibancciArray.append(fibancciNo2)
for num in range(8):
    fibancciNo3 = fibancciNo1+fibancciNo2
    fibancciArray.append(fibancciNo3)
    fibancciNo1 = fibancciNo2
    fibancciNo2 = fibancciNo3

print(fibancciArray)
