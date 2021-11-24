#Write a script in Python that converts British spelling of a text to the American spelling using at least two generalizable replacement patterns. “Generalizable” means applicable to more than one lexeme. For example, replacing “fireman” with “firefighter” is not generalizable, but replacing “theatre” with “theater” is. Your script should read an input text file and write an output text file. The names of the input and output files may be hard-coded in the script.


import re
import os

from datetime import *

filename = input("Please enter the name of a text file with extension (e.g., sample.txt): ")
#intended for use with british.txt

while os.path.isfile(filename) == False:
    filename = input("That file does not exist. Please enter a different filename: ")

userfile = open(filename)
file = userfile.read()
userfile.close() 

output = re.sub(r"(\w+)([iy])se\b", r"\1\2ze", file) #converts -ise and -yse endings to -ize and -yze
output = re.sub(r'(\w+)our\b', r'\1or', output, flags=re.I) #converts -our endings to -or

#both of these overgeneralize, as shown by the last 2 words in each group in the source text (hour, flour, wise, poise)

fileout = open(f'{filename[:-4]}_Americanized.txt', "w")
for line in output:
    fileout.write(line)
fileout.close()

print('Your Americanized text is: ' + output)
print(f'Your Americanized text is saved in {filename[:-4]}_Americanized.txt')
