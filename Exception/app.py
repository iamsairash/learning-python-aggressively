# try:
#     age = int(input("Age: "))
# except ValueError:
#     print("the age is invalid")
# finally:
#     print("The finally block")
# print("program continues.")


##############

try:
    age = int(input("Age: "))
    xfactor = 10 / age
except (ValueError, ZeroDivisionError):
    print("Invalid age")


######################

try:
    with open("abc.txt") as file:
        print("file opened. ")
        ### the file get opened and close automatically, with normal syntax we have to close the file in finally block
except ValueError:
    pass
