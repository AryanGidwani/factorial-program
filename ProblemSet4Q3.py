# Aryan Gidwani
# November 12, 2021
# ICS3UO - A
# The purpose of this program is to calculate the factorial of any positive
# integer that the user inputs. For instance, 4! should output 24, because
# 4 * 3 *2 * 1 equals 24.

name = input("Hello! What is your name? ")
# asks the user for their name
print("Hello " + name + "! Enter in a positive integer of your choice, and the program will " + "\n" + "find the factorial of that integer. When you see the exclamation mark, that is " + "\n" + "simply just the algebraical character for factorial." + "\n")
# introductory message

flag = True
# holds a boolean value in the variable "flag"

# creates a variable sign that holds a quotation mark
while flag:
    try:
        number = input("Type quit once you want the program to stop. Enter a positive integer. Any " + "\n" + "negative integer inputted will be turned into positive, and any decimal number " + "\n" + "inputted will be rounded: ")
        # asks the user to choose a number
        sign = ""
        # holds an empty pair of quotes which will hold the multiplication sign
        if number == "quit":
            print("Thank you for using this program!")
            # concluding message
            break
            # stops the loop from running
        number = float(number)
        # casts the number to a float
        number = round(abs(number))
        # changes it to the absolute value of the number and rounds it
        fixedNumber = number
        # fixedNumber stores the value of what number was originally

        for counter in range(number - 1, 0 , -1):
            number = number * counter
            # finds the value of the factorial of the number
            if counter != 1:
                sign = sign + str(counter) + "*"
                # prints the multiplication signs
            else:
                sign = sign + str(counter)
                # prints the final number without the multiplication sign if
                # counter is equal to one

        print("Thus, " + str(number) + " is the answer to " + str(fixedNumber) + "*" + str(sign) + ", or " + str(fixedNumber) + "!. The exclamation mark is the symbol " + "\n" + "for factorial." + "\n")
        # outputs it to the user

    except :
        print("Input a valid value please!" + "\n")
        # informs the user that they have inputted an invalid value
         
         


     
        


      
