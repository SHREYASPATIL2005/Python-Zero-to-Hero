import os

directory = input("Enter directory path (press Enter for current directory):  ").strip()

if directory:
	contents = os.listdir(directory)
else:
	contents = os.listdir()

for item in contents:
	print(item)
# This code prompts the user to enter a directory path. If the user presses Enter without typing anything, it lists the contents of the current directory. Otherwise, it lists the contents of the specified directory. The os.listdir() function is used to get the list of files and directories in the specified path.
