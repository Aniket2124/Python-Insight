
score = []


def fun_record():
    for i in range(5):
        currentscore = int(input("Enter thescore "+str(i+1)+": "))
        # str(i) : this prints index value from 0
        # str(i+1): this prints index value from 1
        score.append(currentscore)

    print(score)


fun_record()

# File I/O
'''
file = open("filename", "r")  # "r","w","a","r+"->read & write

file.close()
'''
vacationspots = ["London", "paris", "New York", "Brazil", "Iceland"]
vacationfile = open("Vacationplaces", "w")

for spots in vacationspots:
    vacationfile.write(spots + " \n")
vacationfile.close()
vacationfile = open("Vacationplaces", "r")
firstline = vacationfile.readline()
print(firstline)
for line in vacationfile:
    print(line, end="")
#thewholefile = vacationfile.read()
# print(thewholefile)
vacationfile.close()
finalspot = "Thailand\n"
vacationfile = open("Vacationplaces", "a")
vacationfile.write(finalspot)
vacationfile.close()
vacationfile = open("Vacationplaces", "r")
for line in vacationfile:
    print(line, end="")
vacationfile.close()
with open("Vacationplaces", "r") as vacationfile:
    for line in vacationfile:
        print(line)
