# Dictionary
dict_song = {"Title": "Ik Mulakhat", "Album": "Dream Girl",
             "Artist": "Altamash Faridi", "Uploaded": "Zee Company",
             "Music": "Meet Bros", "Movie": "Dream Girl"}


def fun_dict(key_par, value_par):

    for dict_key, dict_value in dict_song.items():
        print(dict_key + " : " + dict_value)

        if(dict_key == key_par and dict_value == value_par):
            print(True)
            break
    else:
        print(False)


key_input = input("Enter Key Parameter: ")
val_input = input("Enter value Parameter: ")
fun_dict(key_input, val_input)
