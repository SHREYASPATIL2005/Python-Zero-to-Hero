words = {
    "madd" : "Help",
    "kursi" : "Chair",
    "billi" : "Cat",
}

word = input("Enter the word you want to translate: ")
print(words.get(word, "We don't have this word in our dictionary")) # This line retrieves the translation of the input word from the 'words' dictionary using the get() method. If the word is not found in the dictionary, it returns the default message "We don't have this word in our dictionary".