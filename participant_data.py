# Participant Data
participantNumber = 5
participantData = []
registeredparticipants = 0
outputfile = open("participantData.txt", "w")

while(registeredparticipants < participantNumber):
    tempPartData = []  # name, country of origin,age
    name = input("Enter your Name: ")
    tempPartData.append(name)
    country = input("Enter your Country: ")
    tempPartData.append(country)
    age = int(input("Enter your Age: "))
    tempPartData.append(age)
    print(tempPartData)
    participantData.append(tempPartData)
    print(participantData)
    registeredparticipants += 1

for participant in participantData:
    for data in participant:
        outputfile.write(str(data))
        outputfile.write(" ")
    outputfile.write("\n")

outputfile.close()

inputfile = open("participantData.txt", "r")

inputlist = []
for line in inputfile:
    tempparticipant = line.strip().split()
    # .strip will print a sring "Aniket,India,21"
    # .split will print a element in list ["Aniket","India","21"]
    inputlist.append(tempparticipant)
    # print(inputlist)

age = {}    # to save data
print(inputlist)
for part in inputlist:
    # to find whether age is already exits or not
    tempage = int(part[-1])
    if tempage in age:
        age[tempage] += 1
    else:
        age[tempage] = 1
print(age)
countries = {}
print(inputlist)
for part in inputlist:
    tempcountry = part[1]
    if tempcountry in countries:
        countries[tempcountry] += 1
    else:
        countries[tempcountry] = 1
print("Countries that attended:", countries)

oldest = 0
youngest = 100
mostoccuringage = 0
counter = 0
for tempage in age:
    if tempage > oldest:
        oldest = tempage

    if tempage < youngest:
        youngest = tempage
    if age[tempage] >= counter:
        counter = age[tempage]
        mostoccuringage = tempage
print("Most Oldest Age is:", oldest)
print("Most Youngest Age is:", youngest)
print("Most occuring Age is:", mostoccuringage,
      "With", counter, "Participants")
inputfile.close()
