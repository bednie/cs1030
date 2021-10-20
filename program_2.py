from os.path import exists

sum_of_integers = 0
number_of_integers = 0 
average_of_integers = 0
list_of_integers = []

# get filename from user
user_filename = input("""
Enter the filename of your file
(file must be in same directory as program), 
or press Enter to open the default file 'LotsOfNumbers.txt':  
""")

# check that file exists, and open file
if exists(user_filename):
    pass

elif user_filename == "" and exists('LotsOfNumbers.txt'):
    user_filename = 'LotsOfNumbers.txt'

else:
    print("""
File not found. Make sure the file is in the same 
folder as this program and run the program again.
""")

# read file content into list of integers
file = open(user_filename, 'r')
for line in file:
    list_of_integers.append(int(line.strip()))
file.close()    

# calculate sum, average, and count of integers in file
number_of_integers = len(list_of_integers)
sum_of_integers = sum(list_of_integers)
average_of_integers = sum_of_integers / number_of_integers

# output file to 'Program2.out'
with open('Program2.out', 'w') as f:
    f.write('Name of file: ' + user_filename + '\n')
    f.write('Sum of integers in file: ' + str(sum_of_integers) + '\n')
    f.write('Average of integers in file: ' + str(average_of_integers) + '\n')
    f.write('Count of integers in file: ' + str(number_of_integers) + '\n')
    f.close()