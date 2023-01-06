import argparse

# Create the argument parser
parser = argparse.ArgumentParser()

# Add the optional "file_path" argument
parser.add_argument("file_path", nargs="?", help="The path of the password list")

# Parse the arguments
args = parser.parse_args()

# Check if the "file_path" argument was provided
if args.file_path:
    # Use the file path provided as an argument
    file_path = args.file_path
else:
    # Prompt the user for the file path
    file_path = input("Enter the path of the password list: ")

# Open the password list file
with open(file_path, "r") as f:
    # Read the contents of the file into a list of lines
    lines = f.readlines()

# Ask the user if they want to uppercase the first letter of each word
uppercase_first_letter = input("Do you want to uppercase the first letter of each word? (y/n) ")

# Ask the user which characters they want to add to the end of each word
characters_to_add = input("Enter the characters to add to the end of each word (e.g. '1! 2@ 6*'): ")

# Split the characters to add into a list
characters_to_add = characters_to_add.split()

# Open a new file to write the modified password list to
with open("modified_list.txt", "w") as f:
    # Iterate over each line in the list
    for line in lines:
        # Split the line into words
        words = line.split()
        # Iterate over each word in the line
        for word in words:
            # Modify the word based on the user's choices
            if uppercase_first_letter == "y":
                modified_word = word[0].upper() + word[1:]
            else:
                modified_word = word
            for character in characters_to_add:
                modified_word += character
            # Write the modified word to the output file
            f.write(modified_word + " \n")
       
