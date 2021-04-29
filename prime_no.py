num = int(input("Enter a to see is Prime or Not: "))
prime_no = []
non_prime_no = []

if num > 1:

    for i in range(2, num):
        if num % i == 0:
            print("Not a Prime No: ", num)
            non_prime_no.append(num)
            break
    else:
        print("Prime Number", num)
        prime_no.append(num)
print("Prime No:", prime_no)
print("Non Prime No:", non_prime_no)
