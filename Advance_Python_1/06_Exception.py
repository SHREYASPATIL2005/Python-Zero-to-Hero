try :
    a = int(input("Enter a number: "))
    print(f"You entered: {a}")

except Exception as e:
    print(f"An error occurred: {e}")

'''   
except ValueError:
    print("Invalid input! Please enter a valid integer.")
    print(v)

except ZeroDivisionError:
    print("Division by zero is not allowed.")

except Exception as e:
    print(f"An unexpected error occurred: {e}")

except KeyboardInterrupt:
    print("\nProgram interrupted by user.")

except TypeError:
    print("Type error occurred. Please check your input types.")

except IndexError:
    print("Index error occurred. Please check your list or array indices.")

except FileNotFoundError:
    print("File not found. Please check the file path.")

except KeyError:
    print("Key error occurred. Please check the dictionary keys.")

except AttributeError:
    print("Attribute error occurred. Please check the object attributes.")

except ImportError:
    print("Import error occurred. Please check the module imports.")

except ModuleNotFoundError:
    print("Module not found. Please check the module name.")

except OSError:
    print("OS error occurred. Please check the operating system related issues.")

except RuntimeError:
    print("Runtime error occurred. Please check the runtime conditions.")

except MemoryError:
    print("Memory error occurred. The program ran out of memory.")

except OverflowError:
    print("Overflow error occurred. The result is too large to be represented.")

except RecursionError:
    print("Recursion error occurred. Maximum recursion depth exceeded.")
'''

print("Program continues after exception handling.")
