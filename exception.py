def compare(a=None, b=None, c=None):
    try:
        value = False
        a = int(a)
        b = int(b)
        c = int(c)
        print("Values")
        if a == b or b == c or c == a:
            value = True

    except ValueError:
        print("ValueError: Only numbers are allowed")
    except TypeError:
        print("TypeError: Please enter only numbers")
    except Exception:
        print(Exception)
        print("Exception: only numbers are allowed")
    finally:
        print("values", a, b, c)
        return value


# intergers
print("Result", compare(7, 5, 6))
print("\n")
# strings
print(compare("7", "5", "6"))
print("\n")
# alphabets
print(compare("a", "b", "c"))
print("\n")
# bool
print(compare(True))
print("\n")
# 3 bool
print(compare(True, True, False))
print("\n")

# 2 bool 1 str
print(compare(True, "a", False))
print("\n")

# str bool
print(compare("2", "5", True))
print("\n")

# str
print(compare("2", "2", "2"))
print("\n")

# empty str
print(compare("-5", ""))
print("\n")

print(compare("", "", ""))
print("\n")

# float
print(compare("1.5", "5", "5.8"))
print("\n")

# strings
print(compare("Aniket"))
print("\n")
