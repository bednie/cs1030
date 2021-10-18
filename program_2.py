sum_of_integers = 0 
number_of_integers = 0 
average_of_integers = 0
list_of_integers = [1,2,3,4,5,6,7,8,9,10]

# get filename from user

# check that file exists 
    #user_file.exists()

# if it files exists, open the file in read mode. elif ask again. else press enter to exit.


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

