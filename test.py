# Open the wordlist file and store the contents in a variable
with open(input("Enter the location of the wordlist: "), "r") as f:
    words = f.readlines()

# Ask the user if they want to capitalize a specific index
capitalize = input("Do you want to capitalize a specific index? (y/n) ")

# If the user wants to capitalize a specific index, ask them which index
if capitalize.lower() == "y":
    index = int(input("Which index do you want to capitalize? "))

# Open a new file to write the modified wordlist
with open("modified_wordlist.txt", "w") as f:
    # Iterate over the words in the wordlist
    for word in words:
        # Strip the newline character from the word
        word = word.strip()
        
        # If the user wants to capitalize a specific index, capitalize it
        if capitalize.lower() == "y":
            word = word[:index] + word[index].upper() + word[index+1:]
        
        # Iterate over all combinations of the characters "1!" and "1#"
        for c1 in ["1!", "1#"]:
            for c2 in ["1!", "1#"]:
                # Write the modified word to the file
                f.write(word + c1 + c2 + "\n")
w