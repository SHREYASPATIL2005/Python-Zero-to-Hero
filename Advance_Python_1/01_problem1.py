try:
    with open("1.txt", "r") as f:
        print(f.read())
except Exception as e:
    print(f"An error occurred while reading 1.txt: {e}")

try:
    with open("Advance_Python_1/2.txt", "r") as f:
        print(f.read())
except Exception as e:
    print(f"An error occurred while reading 2.txt: {e}")

try:
    with open("3.txt", "r") as f:
        print(f.read())
except Exception as e:
    print(f"An error occurred while reading 3.txt: {e}")

    
