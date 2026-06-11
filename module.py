import pyjokes

print("Here's a joke for you:")
# print("Loading joke...")   # Ctrl + / to comment out this line
# This print a random joke from the pyjokes library
joke = pyjokes.get_joke()
print(joke)

"""In this code, we import the pyjokes library and use it to get a random joke. The line that prints "Loading joke..." is commented out, so it won't be executed.
You can uncomment it if you want to see that message before the joke is printed.
To run this code, make sure you have the pyjokes library installed. You can install it using pip:
pip install pyjokes"""