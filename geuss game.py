#creating the user defined execption for lower
class greater(Exception):

    pass

#creating the user defined execption for higher
class lower(Exception):

    pass

#seting a permenent number to geussing
guessing_number = 120

#creating the loop for get the value then process to raise error or break the loop when the ans is guessed.
while True:

    guessed_number = int(input())

#process to raise error or break
    try:

        if guessed_number==guessing_number:

            print("WHOOYEEE!!! You guessed it!")

            break

        elif guessed_number<=guessing_number:

            raise lower

        else:

            raise greater

#when the value is greater
    except greater:

        print("OOPS!  It is greater than the number that you guessed ")
#when the value is lower
    except lower:

        print("OHOH! It is lower than the number that you guessed ")
#A simple quoat for each and every try
    # finally:
    #
    #     print('''"TRY UNTIL YOU GOT IT"''')
