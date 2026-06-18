def goodDay(name, ending):
    print("Good day, " + name + "!")
    print(ending)
    return "done"

goodDay("Alice", "Thank you!")  # Function call with argument
goodDay("Bob", "Thanks!")  # Function call with argument


a = goodDay("Harry", "Thank you!")  # Function call with argument
print(a)  # Print the return value of the function call

