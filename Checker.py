#############################################################################
# This program asks the user to enter a coordinate that corresponds to      # 
# a square on a chess board. Then the program returns the color of the      #
# square and repeats the process until the user exits the program.          #
#############################################################################

black_odd_white_even = ['a','c','e','g'] # letters following the black-odd, white-even pattern
black_even_white_odd = ['b','d','f','h'] # letters following the black-even, white-odd pattern

# Define a function to check user input for a variety of invalid input scenarios
def Check_User_Input(): 
    user_input = ""
    
    # While loop to test whether input is valid
    while len(user_input) != 2 or not user_input[0].isalpha() or not user_input[1].isnumeric() or \
        user_input[0] > "h" or int(user_input[1]) > 8 or int(user_input[1]) < 1:

        user_input = input("""\nWhat color is that square on a chess board?\n
Enter a square's coordinates to find out if it is black or white, 
or press Enter to exit.\n
Input must be one letter a-h and one number 1-8 (for example j5 or a6):""").lower()

        if user_input == "": # User can press Enter key to exit program
            print('\nExiting program. Byebye.\n')
            exit()

        # In cases of invalid input, the following print
        # messages to tell the user what was wrong with 
        # their input before exiting the program.
        elif len(user_input) != 2:
            print('You entered "' + user_input + '", which is too long or too short. Try again.')
            print('Exiting program. Byebye.\n')
            exit()

        elif user_input[0].lower() > "h":
            print('You entered "' + user_input + '". Make sure the letter is between A and H. Try again.')   
            print('Exiting program. Byebye.\n')
            exit()

        elif not user_input[0].isalpha() or not user_input[1].isnumeric():
            print('You entered "' + user_input + '", which is not the incorrect format. Try again.')
            print('Exiting program. Byebye.\n')
            exit()

        elif user_input[1].isnumeric: 
            if int(user_input[1]) > 8 or int(user_input[1]) < 1:
                print('You entered "' + user_input + '". Make sure the number is an integer between 1 and 8. Try again.') 
                print('Exiting program. Byebye.\n')
                exit()
    return user_input


def Get_Square_Color(uinput):

    # Determine if the square follows the pattern for black-even/white-odd or vice versa.
    # Depending on the pattern, determine if the number portion of the coordinate means
    # that the square is white or black.
    if uinput[0] in black_even_white_odd and (int(uinput[1]) % 2 == 0):
        print("\nThe square " + uinput + " is black.")

    elif uinput[0] in black_even_white_odd and int(uinput[1]) % 2 != 0:
        print("\nThe square " + uinput + " is white.") 

    elif uinput[0] in black_odd_white_even and int(uinput[1]) % 2 == 0:
        print("\nThe square " + uinput + " is white.")        

    elif uinput[0] in black_odd_white_even and int(uinput[1]) % 2 != 0:
        print("\nThe square " + uinput + " is black.") 

def main(): # Define main function to control program

    Get_Square_Color(Check_User_Input()) # Get square color based on validated user input
    main() # Call main function recursively until user presses Enter key to exit

main() # Call main function to run the program