def main():    
    try:
        a = int(input("Enter a number: "))
        print(f"You entered: {a}")
        return

    except Exception as e:
        print(f"An error occurred: {e}")
        return

    finally:
        print("Hey I am inside finally block. I will always execute regardless of whether an exception occurred or not.")



main()