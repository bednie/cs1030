from os.path import exists

sum_of_integers = 0 
number_of_integers = 0 
average_of_integers = 0
list_of_integers = []

# get filename from user
user_filename = input(
"""
Enter the filename of your file
(file must be in same directory as program), 
or press Enter to open 'LotsOfNumbers.txt':  
"""
)

# check that file exists, and open file
if exists(user_filename):
    # TODO create file object with user_filename
    print(user_filename + ' exists')

elif user_filename == "" and exists('LotsOfNumbers.txt'):
    print('LotsOfNumbers.txt exists')
    # TODO create file object with LotsOfNumbers.txt 

else:
    print('File not found. Please run the program again.')

# read file content into variables    

file = open(user_filename, 'r')
for line in file:
    list_of_integers.append(int(file.read()))

# calculate sum, average, and count of integers in file
number_of_integers = len(list_of_integers)
sum_of_integers = sum(list_of_integers)
average_of_integers = sum_of_integers / number_of_integers

# output file to 'Program2.out'
with open('Program2.out', 'w') as f:
    f.write('Sum of integers in file: ' + str(sum_of_integers) + '\n')
    f.write('Average of integers in file: ' + str(average_of_integers) + '\n')
    f.write('Count of integers in file: ' + str(number_of_integers) + '\n')
    f.close()

