import math


# choice checker to obtain valid responses from the user
def choice_checker(question, valid_responses, error_message):
    while True:
        response = input(question).lower()

        # Iterating the items in valid responses
        for item in valid_responses:

            # checking if the user input is valid
            if response == item or response == item[0]:

                # returning if it is
                return item
        # output error if input is invalid
        print(error_message)

# Number checker to ontain valid integer and float responses from the user
def num_check(question, num_type=float, exit_code=None):
    # fixed error message
    error = "Please enter an integer that is more than 0"

    # loop to 
    while True:
        response = input(question)
        if response == exit_code:
            return response

        try:
            response = num_type(response)

            if response > 0:
                return response
            else:
                print(error)

        except ValueError:
            print(error)


def circle(var_radius):
    return (f"Area: {round(3.14 * var_radius * var_radius, 2)} square units, "
            f"Perimeter: {round(2 * 3.14 * var_radius, 2)} units")


def square_rectangle(var_length, width):
    return (f"Area: {round(var_length * width, 2)} square units, "
            f"Perimeter: {round(2 * length + 2 * width, 2)} units")


def triangle(var_base=None, var_height=None, var_first_side=None, var_second_side=None, var_third_side=None):
    area = "na"
    perimeter = "na"

    if var_first_side is not None and var_second_side is not None and var_third_side is not None:
        s = (var_first_side + var_second_side + var_third_side) / 2
        area = round(math.sqrt((s * (s - first_side) * (s - second_side) * (s - third_side))), 2)
        perimeter = round(var_first_side + var_second_side + var_third_side, 2)

    if var_base is not None and var_height is not None:
        area = round(0.5 * var_base * var_height, 2)

    return (f"Area: {area} square units, "
            f"Perimeter: {perimeter} units")


def triangle_area_questions():
    base = num_check("Base/Side 1: ")
    height = num_check("Height: ")
    return [base, height]


def triangle_perimeter_questions():
    first_side = num_check("Side 1/Base: ")
    second_side = num_check("Side 2: ")
    third_side = num_check("Side 3: ")
    return first_side, second_side, third_side


# Main Routine

yes_no_list = ['yes', 'no']
yes_no_error_message = "Please enter yes or no"

# Shape list with xxx exit code
shape_selection_list = ['circle', 'square', 'rectangle', 'triangle', 'xxx']

show_instructions = choice_checker("See Instructions? ", yes_no_list, yes_no_error_message)
if show_instructions == "yes":
    print("Displays Instructions")

number_of_calculations = num_check("Enter the number of calculations: ", num_type=int, exit_code='')

if number_of_calculations == "":
    print("infinite mode")

calculations_done = 0

while number_of_calculations == "" or calculations_done < number_of_calculations:
    select_shape = choice_checker('Enter shape("xxx" to quit): ', shape_selection_list,
                                  'Please select circle, square, rectangle or triangle')

    if select_shape == 'xxx':
        break

    print(f'You picked {select_shape}')

    if select_shape == "circle":
        radius = num_check("Radius: ", exit_code='na')
        print(circle(radius))

    elif select_shape == "square":
        length = num_check("Length: ", exit_code='na')
        print(square_rectangle(length, length))

    elif select_shape == "rectangle":
        length = num_check("Length: ", exit_code='na')
        width = num_check("Width: ", exit_code='na')
        print(square_rectangle(length, width))

    elif select_shape == "triangle":

        have_side_lengths = choice_checker("Do you have the lengths of the 3 sides",
                                           yes_no_list, yes_no_error_message)

        if have_side_lengths == "yes" or have_side_lengths == "y":
            sides = triangle_perimeter_questions()
            first_side, second_side, third_side = sides
            if first_side + second_side <= third_side:
                print("Impossible Triangle")
                continue

            print(triangle(None, None, first_side, second_side, third_side))

        else:
            have_base_height = choice_checker("Do you have a base/side 1 and height? ",
                                              yes_no_list, yes_no_error_message)

            if have_base_height == "yes" or have_base_height == "y":
                bh = triangle_area_questions()
                base, height = bh
                print(triangle(base, height, None, None, None))

    calculations_done += 1
