import math, pandas


# Function containing instructions
def instructions():
    print("Welcome to the Shape Area and Perimeter Calculator!\n "
          "This program allows you to calculate the area and perimeter (or circumference) of various shapes\n"
          "including circles, squares, rectangles, and triangles. Simply follow the prompts to input the necessary\n"
          "dimensions for your chosen shape, and the program will provide the calculated results. \n"
          "You can perform multiple calculations in one session, and a summary of all your calculations will be \n"
          "displayed at the end. Type 'xxx' at any prompt to exit the program.\n")


# choice checker to obtain valid responses from the user
def choice_checker(question, valid_responses, error_message):
    while True:
        response = input(question).lower()

        # Iterating the items in valid responses
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
    return (f"{round(3.14 * var_radius * var_radius, 2)} SU"
            f"/{round(2 * 3.14 * var_radius, 2)} U")


# function to calculate area / perimeter of squares and rectangles
def square_rectangle(var_length, var_width):
    return (f"{round(var_length * var_width, 2)} "
            f"SU/{round(2 * length + 2 * var_width, 2)} U")


# calculated area / perimeter using herons law or base and height
def triangle(var_base=None, var_height=None, var_first_side=None, var_second_side=None, var_third_side=None):
    area = "N/A"
    perimeter = "N/A"

    # if herons law can be used, calculate area and perimeter
    if var_first_side is not None and var_second_side is not None and var_third_side is not None:
        s = (var_first_side + var_second_side + var_third_side) / 2
        area = f"{round(math.sqrt((s * (s - first_side) * (s - second_side) * (s - third_side))), 2)}"
        perimeter = f"{round(var_first_side + var_second_side + var_third_side, 2)}"

    # if base and height given, calculate area
    elif var_base is not None and var_height is not None:
        area = f"{round(0.5 * var_base * var_height, 2)} SU"

    # returns area and perimeter
    return f"{area} SU/{perimeter} U"


# questions to ask for area of triangle
def triangle_area_questions():
    var_base = num_check("Base/Side 1: ")
    var_height = num_check("Height: ")
    return [var_base, var_height]


# questions to ask for area and perimeter of triangle
def triangle_perimeter_questions():
    first_side = num_check("Side 1/Base: ")
    second_side = num_check("Side 2: ")
    third_side = num_check("Side 3: ")
    return first_side, second_side, third_side


# Main Routine

# Get name to be reference while executing write to file
user_program_name = input("File Name: ")

# yes no list and fixed error message used thrice
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
    print("infinite mode")

# variable to track # of calculations done by the user
calculations_done = 0

# Set up lists
shapes_list = []
given_information_list = []
results_list = []

# Main while loop to
while number_of_calculations == "" or calculations_done < number_of_calculations:
    select_shape = choice_checker('Enter shape("xxx" to quit): ', shape_selection_list,
                                  'Please select circle, square, rectangle or triangle')

    if select_shape == 'xxx' or select_shape == 'x':
        break

    print(f'You picked {select_shape}')

    if select_shape == "circle":
        radius = num_check("Radius: ", exit_code='na')
        given_information = f"Radius: {str(radius)}"
        results = circle(radius)

    elif select_shape == "square":
        length = num_check("Length: ", exit_code='na')
        given_information = f"Length: {str(length)}"
        results = square_rectangle(length, length)

    elif select_shape == "rectangle":
        length = num_check("Length: ", exit_code='na')
        width = num_check("Width: ", exit_code='na')
        given_information = f"Length: {str(length)}, Width: {str(width)}"
        results = square_rectangle(length, width)

    elif select_shape == "triangle":

        given_information = "-- No information given --"
        results = "No results available"

        have_side_lengths = choice_checker("Do you have the lengths of the 3 sides",
                                           yes_no_list, yes_no_error_message)

        if have_side_lengths == "yes" or have_side_lengths == "y":
            given_information = triangle_perimeter_questions()
            first_side, second_side, third_side = given_information
            given_information = (f"Side 1: {str(first_side)},"
                                 f"Side 2: {str(second_side)},Side 3: {str(third_side)}")

            # Check for impossible Triangle
            if (first_side + second_side < third_side or first_side + third_side < second_side
                    or second_side + third_side < first_side):
                print("Impossible Triangle")
                continue

            results = triangle(None, None, first_side, second_side, third_side)

        else:
            have_base_height = choice_checker("Do you have a base/side 1 and height? ",
                                              yes_no_list, yes_no_error_message)

            if have_base_height == "yes" or have_base_height == "y":
                given_information = triangle_area_questions()
                base, height = given_information
                given_information = f"Base: {str(base)},Height: {str(height)}"
                results = triangle(base, height, None, None, None)

    shapes_list.append(select_shape)
    given_information_list.append(given_information)
    results_list.append(results)

    calculations_done += 1

if calculations_done >= 1:

    # dictionary to gather all dataframe information
    results_dict = {
        "Shape": shapes_list,
        "Given Information": given_information_list,
        "Area/Perimeter": results_list

    }
    print()

    # Results Heading
    results_heading = ("*********************** Area & Perimeter Results"
                       " ***********************\n")

    frame = pandas.DataFrame(results_dict).set_index("Shape")

    # Capitalize the first letter of each shape name in the "Shape" column
    frame.index = frame.index.str.title()

    # convert frame to string
    frame = str(frame)

    to_write = [results_heading, frame]

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
    print("You have quit this program")
