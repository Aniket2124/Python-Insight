# Note taking Program
import os
path = 'C:/Users/VIRAJ/Desktop/Aniket/PythonLearning/Python-Insight'

filename = input("Please enter a file name:")

if os.path.isfile("./" + filename):
    print("looking for file...{}".format(filename))

    print("found it")
    file_found = input(
        "You entered file exists, what do you do with file:\n\n Read, Delete OR Startover, Append, Replace \n")
    if file_found == "read":
        note = open("./" + filename, "r")
        file_found = open("./" + filename, "r")
        print(note.read())

        # Delete Part
    elif file_found == "delete":
        text = input(
            "Do you want to Delete a file Or Startover with writing a file: \n")
        os.path.isfile("./" + filename)
        os.remove("./" + filename)
        print("File Deleted Successfully...")

    # Startover Part
    elif file_found == "startover":

        file_found = open("./" + filename, "r+")
        file_found.truncate(0)
        # truncate() delete all data from file without deleting file & assign to zero
        text = input("Startover Writing data to the File: \n")
        file_found = open("./" + filename, "w")
        file_found.write(text + "\n")

        # Append Part
    elif file_found == "append":
        text = input("Enter what do you want to append to file: \n")
        file_found = open("./" + filename, "a")  # Append data to file
        file_found.write(text + "\n")

        # Replace part
    elif file_found == "replace":
        line_num = int(input(
            "What do you want to Replace: \nThe line number you want to update\n "))
        text = input("Please enter your Text:\n ")
        with open("./" + filename, "r") as read_file:
            line = read_file.readlines()
        with open("./" + filename, "w") as write_file:
            for idx, line in enumerate(line):

                if idx == line_num - 1:
                    print("Line num {} has been replaced!".format(line_num))
                    write_file.write(text + "\n")
                else:
                    print("Writing \"{}\"".format(line))
                    write_file.write(line)

# File is not exist this part will ask for creation of new file
else:
    print("Sorry file not found")
    file_not_found = input("Do you want to create a new file\n\n Yes, No \n")
    if file_not_found == "yes":
        file_not_found = input("Please enter a file name:")
        with open(file_not_found, "w")as write_file:
            write_file.write(file_not_found + "\n")

        print("You created file successfully...")
    else:
        print("Thank You...")
