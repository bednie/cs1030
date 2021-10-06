# This program asks the user to enter their height in feet and inches, 
# then converts that input to meters, rounding to two decimal places. 
# Then the program prints the height in feet and inches as well as meters. 

# Declare variables
height_feet = ""
height_inches = ""
total_height_inches = 0
total_height_centimeters = 0
total_height_meters = 0

# Get valid feet of height from user
while not height_feet.isnumeric() or int(height_feet) < 0: 
    height_feet = input("""Enter a value for the feet of your height (Example: If you are 5'7", enter 5), \nor you may press the Enter key to exit the program: """)
    if height_feet == "":
        print("Exiting program. Bye bye.\n")
        quit() # Exit program if user presses enter, returning an empty string
    elif not height_feet.isnumeric():
        print("Invalid input. Try again.\n")
    else: 
        if height_feet.isnumeric():
            height_feet = int(height_feet)
            break
  
# Get valid inches of height from user
while not height_inches.isnumeric() or (int(height_inches) < 0) or (int(height_inches) >= 12): 
    height_inches = input("""Enter a value for the inches (whole numbers only; no fractions of inches) of your height (Example: If you are 5'7", enter 7), \nor you may press the Enter key to exit the program: """)
    if height_inches == "": 
        print("Exiting program. Bye bye.\n")
        quit() # Exit program if user presses enter, returning an empty string
    elif not height_inches.isnumeric() or (int(height_inches) < 0) or (int(height_inches) > 12):
        print("Invalid input. Try again.\n")
    elif (int(height_inches) == 12):
        print("Invalid input. Twelve inches is equal to 1 foot. Try again.\n")   
    else: 
        if height_inches.isnumeric():
            height_inches = int(height_inches)
            break    

# Calculate the total inches from the feet and inches. If the total inches is greater than or equal 96 inches (the equivalent of 8’0 or more), print a message that the person is really tall!
total_height_inches = ( height_feet * 12 ) + height_inches

if total_height_inches >= 96:
    print("Wow, you are really tall!")

# Convert inches to centimeters. There are exactly 2.54 centimeters per inch.
total_height_centimeters = total_height_inches * 2.54

# Convert the centimeters to meters, rounding to two places with the round(some variable name, 2) function.
total_height_meters = round(( total_height_centimeters / 100 ),2)

# Print the original height in feet and inches, and the equivalent in meters with messages describing each number.
print("Your height in feet and inches: " + str(height_feet) + "\'" + str(height_inches) + "\".")
print("Your height in meters: {0:.2f}m.\n".format(total_height_meters))

# Exit the program.
quit()