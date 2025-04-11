print("------------------------------------ Exceptions Handler ---------------------------------------------------")

# Exceptions = an event that occurs during the execution of a program that disrupts the normal flow of instructions.
#               a process that deals with these exceptions and prevents the program from crashing.
#               Exceptions are caught by the try-except block.(1.try, 2.except, 3.finally)
#               (ZeroDivisionError, ValueError, TypeError, FileNotFoundError, etc.)

def divide(x, y):
    try:
        result = x / y
    except ZeroDivisionError:
        print("You can't divide by zero Idiot!")
    except ValueError:
        print("Please enter a valid number!")
    else:
        print("Result is: ", result)
    finally:
        print("Finally block is executed!") 

divide(10, 0)
#divide(10, 'a')
divide(10, 2)
divide(10, 5)

print()
print("______________________________Except Exception ____________________________________")
# Except Exception

def divide(x, y):
    try:
        result = x / y
    except Exception as e:     # Exception class is the base class for all exceptions. And it considered as bad practice.
        print("Exception occurred: ", e)  
    else:
        print("Result is: ", result)
    finally:    # finally block is always executed whether exception is raised or not.And it is used to release resources.
                # And using to close opened files, databases connection, etc.
        print("Finally block is executed")


divide(10, 0)
divide(10, 'a')
divide(10, 2)
divide(10, 5)













print()
print("-----------------------------------------------------------------------------------------------------------")