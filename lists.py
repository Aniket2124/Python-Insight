myUniqueList = []
myLeftovers = []


def add(addValue):
    isExist = addValue in myUniqueList
    if isExist:
        myLeftovers.append(addValue)
        return False
    else:
        myUniqueList.append(addValue)
        return True


print("initial myUniqueList list - ", myUniqueList)
print("initial myLeftovers list - ", myLeftovers)

print("is value 4 added in myUniqueList? - ", add(4))

print("is value 5 added in myUniqueList? - ", add(5))


print("is value 4 added in myUniqueList? - ", add(4))


print("is value 6 added in myUniqueList? - ", add(6))


print("is value 7 added in myUniqueList? - ", add(7))

print("is value 'patil' added in myUniqueList? - ", add('Patil'))


print("is value 'patil' added in myUniqueList? - ", add('Patil'))

print("is value 'Aniket' added in myUniqueList? - ", add('Aniket'))


print("is value 'True' added in myUniqueList? - ", add(True))

print("is value False added in myUniqueList? - ", add(False))

print("is value True added in myUniqueList? - ", add(True))

print("Final myUniqueList list - ", myUniqueList)
print("Final myLeftovers list - ", myLeftovers)
