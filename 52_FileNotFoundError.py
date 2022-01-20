# try / except / finally
# try:
#     print(5/0)
# except ZeroDivisionError:
#     print("You can't divide by zero!")
# finally:
#     print("This will always run!")

try:
    file = open("folder/my_file.txt")
    try:
        s = file.readlines()
        for i in s:
            print(i, end="")
    finally:
        file.close()
except FileNotFoundError:
    print("The file was not found!")
except:
    print("Something else went wrong!")

# with
try:
    with open("folder/my_file.txt") as file:
        s = file.readlines()
        for i in s:
            print(i, end="")
except FileNotFoundError:
    print("The file was not found!")
except:
    print("Something else went wrong!")
finally:
    print("file is closed", file.closed)