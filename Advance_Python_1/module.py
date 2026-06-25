def myFunc():
    print("Hello from myFunc in module.py")


myFunc()  # Call the function to see the output
print(__name__)  # This will print the name of the module, which is "__main__" if run directly


if __name__ == "__main__":
    print("This code is running directly from module.py")
    myFunc()  # Call the function to see the output
    print(__name__)  # This will print the name of the module, which is "__main__" if run directly