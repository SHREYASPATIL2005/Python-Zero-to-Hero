a = int(input("Enter your age: "))

#IF ELIF ELSE LADDER 

if(a>=18):
    print("You can drive ( You are above the age of consent )")

elif(a<0):
    print("You are entering an invalid age")

elif(a==0):
    print("You are a newborn baby, you cannot drive")

else:
    print("You cannot drive ( You are below the age of consent )")


print("End of the program")