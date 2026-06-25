with (
open("file1.txt", "r") as file1,
      open("file2.txt", "r") as file2,
      open("file3.txt", "r") as file3
):
    # Read the contents of each file
    content1 = file1.read()
    content2 = file2.read()
    content3 = file3.read()

    # Print the contents of each file
    print("Contents of file1.txt:")
    print(content1)
    print("\nContents of file2.txt:")
    print(content2)
    print("\nContents of file3.txt:")
    print(content3)