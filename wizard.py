# I never meant to make you daughter cry,
# I apologize a million times.....
from PIL import Image
from colorama import Fore, Style
import pyfiglet

word_wizard = "The Word-Wizard"
my_github = 'https://github.com/bfrisbyh92   ----------   Brendan Frisby'

# Use pyfiglet to convert the text to ASCII art
word_wizard_art = pyfiglet.figlet_format(word_wizard)
# Use colorama to add color to the ASCII art
colored_word_wizard = Fore.BLUE + word_wizard_art + Style.RESET_ALL
# Print the colored ASCII art
print(colored_word_wizard)

# Use the "small" font in pyfiglet for Github
banner = pyfiglet.figlet_format(my_github, font="small")
# print(banner)
# print(my_github)

# Open an image file
image = Image.open("YourBoyDarth.png")

# Convert the image to grayscale
image = image.convert("L")

# Resize the image to fit the terminal window
width, height = image.size
aspect_ratio = height / width
new_width = 80
new_height = int(aspect_ratio * new_width)
image = image.resize((new_width, new_height))

# Convert the image to ASCII art
chars = " .,-:;i+hHM$* "
for y in range(new_height):
    for x in range(new_width):
        pixel = image.getpixel((x, y))
        index = int(pixel / 255 * (len(chars) - 1))
        print(chars[index], end="")
    print()

# Open the wordlist file and store the contents in a variable
with open(input("Enter the location of the wordlist: "), "r") as f:
    words = f.readlines()

# Ask the user if they want to capitalize a specific index
capitalize = input("Do you want to capitalize a specific index? (y/n) ")

# If the user wants to capitalize a specific index, ask them which index
if capitalize.lower() == "y":
    index = int(input("Which index do you want to capitalize? "))

# Ask the user what characters they want to append to the end of each word
ImsorRYmRsJacKsON = input("Enter the first character to append: ")
iaMIamIaMFooOoOooReALlLLL = input("Enter the second character to append: ")

# Open a new file to write the modified wordlist
with open("modified_wordlist.txt", "w") as f:
    # Iterate over the words in the wordlist
    for word in words:
        # Strip the newline character from the word
        word = word.strip()
        
        # If the user wants to capitalize a specific index, capitalize it
        if capitalize.lower() == "y" and index < len(word):
            word = word[:index] + word[index].upper() + word[index+1:]
        
        # Write the modified word to the file
        f.write(word + ImsorRYmRsJacKsON + iaMIamIaMFooOoOooReALlLLL + "\n")


the_author = "BHF 1992"
the_author_art = pyfiglet.figlet_format(the_author, font='small')
colored_the_author = Fore.RED + the_author_art + Style.RESET_ALL
print(colored_the_author)




