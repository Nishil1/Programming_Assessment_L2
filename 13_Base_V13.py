import math
import pandas
import re


# Function containing instructions
def instructions():
    print("\n" + "=" * 50)
    print("Welcome to the Shape Area and Perimeter Calculator          ")
    print("=" * 50)
    print(
        "\nThis program allows you to calculate the area and perimeter (or circumference) of various shapes,"
        " including:")
    print(" - Circles")
    print(" - Squares")
    print(" - Rectangles")
    print(" - Triangles")
    print("\nSimply follow the prompts to input the necessary dimensions for your chosen shape,")
    print("and the program will provide the calculated results.")
    print("\nYou can perform multiple calculations in one session, and a summary of all your calculations")
    print("will be displayed at the end.")
    print("\nType 'xxx' at any 'Enter shape' question to exit the program.")
    print("\nNote: Area is displayed in Square Units (SU) and Perimeter in Units (U).")
    print("=" * 50 + "\n")


# choice checker to obtain valid responses from the user
def choice_checker(question, valid_responses, error_message):
    while True:
        response = input(question).lower()

        # Iterating through items in valid responses
        for var_item in valid_responses:

            # checking if the user input is valid
            if response == var_item or response == var_item[0]:
                # returning if it is
                return var_item
        # output error if input is invalid
        print(error_message)


# Number checker to obtain valid integer and float responses from the user
def num_check(question, num_type=float, exit_code=None):
    # fixed error message
    error = "Please enter an integer that is more than 0"

    # loop to obtain valid inputs
    while True:
        response = input(question)

        # is exit code is entered, quit
        if response == exit_code:
            return response

        try:

            # obtain valid integers/floats
            response = num_type(response)

            # returns response if int/float is > than 0
            if response > 0:
                return response
            else:
                # output error if 0 or less
                print(error)

        # error if input is not an integer / float as specified by parameter
        except ValueError:
            print(error)


# function to calculate area / circumference of circle
def circle(var_radius):
    area = round(math.pi * var_radius * var_radius, 2)
    perimeter = round(2 * math.pi * var_radius, 2)
    return f"| Area: {area} SU, Perimeter: {perimeter} U"


# function to calculate area / perimeter of squares and rectangles
def square_rectangle(var_length, var_width):
    area = round(var_length * var_width, 2)
    perimeter = round(2 * var_length + 2 * var_width, 2)
    return f"| Area: {area} SU, Perimeter: {perimeter} U"


# calculated area / perimeter using herons law or base and height
def triangle(base=None, height=None, first_side=None, second_side=None, third_side=None):
    perimeter = "N/A"

    # if herons law can be used, calculate area and perimeter
    if first_side is not None and second_side is not None and third_side is not None:
        s = (first_side + second_side + third_side) / 2
        area = f"{round(math.sqrt((s * (s - first_side) * (s - second_side) * (s - third_side))), 2)}"
        perimeter = f"{round(first_side + second_side + third_side, 2)}"

    # if base and height given, calculate area
    elif base is not None and height is not None:
        area = f"{round(0.5 * base * height, 2)}"

    # returns area and perimeter
    return f"| Area: {area} SU, Perimeter: {perimeter}{' U' if perimeter != 'N/A' else ''}"


# Main Routine

# Welcome Message
print("***** Welcome to Area / Perimeter Calculator *****")
print()

# Invalid characters for file name
invalid_characters = re.compile(r'[^A-Za-z0-9_]')

# Get name to be reference while executing write to file making sure it's not blank
# and has appropriate characters(only letters, numbers and underscores of max 50 character length)
while True:
    user_program_name = input("File Name: ").lower()
    if user_program_name.strip() == "" or len(user_program_name) > 50 or invalid_characters.search(user_program_name):
        print("File name cannot be blank, greater than 50 characters and cannot include "
              "anything other than letters, numbers and underscores(No spaces)")
    else:
        break

# yes no list and fixed error message
yes_no_list = ['yes', 'no']
yes_no_error_message = "Please enter yes or no"

# Shape list with xxx exit code
shape_selection_list = ['circle', 'square', 'rectangle', 'triangle', 'xxx']

# Ask if user wants instructions
show_instructions = choice_checker("Would you like to see Instructions? ", yes_no_list, yes_no_error_message)

# if they do, print it
if show_instructions == "yes":
    instructions()

# Obtain number of calculations user needs or infinite mode
number_of_calculations = num_check("Enter the number of calculations(<enter> for infinite mode): ",
                                   num_type=int, exit_code='')

# let the user know they have entered infinite mode
if number_of_calculations == "":
    print()
    print("*** You have entered Infinite Mode ***")
    print()

# variable to track # of calculations done by the user
calculations_done = 0

# Set up lists for dataframe outputting
shapes_list = []
given_information_list = []
results_list = []

# Main while loop to get shapes, integer values and display results
while number_of_calculations == "" or calculations_done < number_of_calculations:

    # let user know what question they are on
    if number_of_calculations != "":
        # as calculations done only get added as the loop is finished, it will be 1 behind
        # so need to increase it by 1
        print()
        print(f"***** Question {calculations_done + 1} of {number_of_calculations} *****")

    select_shape = choice_checker('Enter Shape("xxx" to quit): ', shape_selection_list,
                                  'Please select circle, square, rectangle or triangle')

    # if exit code is entered, exit from the program
    if select_shape == 'xxx' or select_shape == 'x':
        break

    # Let user know which shape they picked
    print()
    print(f'-- You picked {select_shape} --')
    print()

    # Decide which shape is selected
    # ask questions to get numerical information about the shape
    # Output the results

    # So results and given information aren't undefined
    results = ""
    given_information = ""

    if select_shape == "circle":
        radius = num_check("Radius: ")
        given_information = f"Radius: {str(radius)}"
        results = circle(radius)

    elif select_shape == "square":
        length = num_check("Length: ")
        given_information = f"Length: {length}"
        results = square_rectangle(length, length)

    elif select_shape == "rectangle":
        length = num_check("Length: ")
        width = num_check("Width: ")
        given_information = f"Length: {str(length)}, Width: {str(width)}"
        results = square_rectangle(length, width)

    elif select_shape == "triangle":

        # given information and results only changes if something is given

        given_information = "-- No information given --"
        results = "No results available"

        # Ask  user for length of 3 sides
        have_side_lengths = choice_checker("Do you have the lengths of the 3 sides: ",
                                           yes_no_list, yes_no_error_message)

        # if they have 3 sides, return the area and perimeter
        if have_side_lengths == "yes" or have_side_lengths == "y":
            var_first_side = num_check("Side 1/Base: ")
            var_second_side = num_check("Side 2: ")
            var_third_side = num_check("Side 3: ")
            given_information = (f"Side 1: {var_first_side},"
                                 f"Side 2: {var_second_side}, Side 3: {var_third_side}")

            # Check for impossible Triangle
            if (var_first_side + var_second_side < var_third_side or var_first_side + var_third_side < var_second_side
                    or var_second_side + var_third_side < var_first_side):
                print("Impossible Triangle")
                continue

            # Calculate area / perimeter
            results = triangle(None, None, var_first_side, var_second_side, var_third_side)

            # ask questions for base and height if 3 sides isn't given
        else:
            var_base = num_check("Base/Side 1: ")
            var_height = num_check("Height: ")
            given_information = f"Base: {var_base}, Height: {var_height}"
            results = triangle(var_base, var_height, None, None, None)

    # output results
    print()
    print("***** Results *****")
    print(results)
    print()

    # Append shape, given information and results to the dataframe dictionary
    shapes_list.append(select_shape)
    given_information_list.append(given_information)
    results_list.append(results)

    # increase calculations by 1
    calculations_done += 1

# only run if calculations done is more than 1
if calculations_done >= 1:

    # dictionary to gather all dataframe information
    results_dict = {
        "Shape": shapes_list,
        "Given Information": given_information_list,
        "Area/Perimeter": results_list

    }
    print()

    # Results Heading
    results_heading = "*********************** Area & Perimeter Results ***********************\n"

    # Units information
    units_display = "Area is in Square units and Perimeter is in units\n"

    frame = pandas.DataFrame(results_dict).set_index("Shape")

    # Capitalize the first letter of each shape name in the "Shape" column
    frame.index = frame.index.str.title()

    # convert frame to string
    frame = str(frame)

    to_write = [results_heading, units_display, frame]

    for item in to_write:
        print(item)

    # Write to file`
    # create file to hold data (add .txt extension)
    file_name = f"{user_program_name}.txt"
    text_file = open(file_name, "w+")

    # heading
    for item in to_write:
        text_file.write(item)
        text_file.write("\n")

    # close file
    text_file.close()

else:

    # If user didn't do any calculations
    print()
    print("Nothing to display")

# Thank the user for using the program
print()
print("***** Thanks for using Area / Perimeter Calculator *****")
