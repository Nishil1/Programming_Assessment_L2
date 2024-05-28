import math


def choice_checker(question, valid_responses, error_message):
    while True:
        response = input(question).lower()

        for item in valid_responses:
            if response == item or response == item[0]:
                return item

        print(error_message)


def num_check(question, num_type=float, exit_code=None):
    error = "Please enter an integer that is more than 0"

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
    return f"Area: {3.14 * var_radius * var_radius}, Perimeter: {2 * 3.14 * var_radius}"


def square_rectangle(var_length, width):
    return f"Area: {var_length * width}, Perimeter: {2 * length + 2 * width}"


def triangle(var_base, var_height):
    return (f"Area: {0.5 * var_base * var_height}, "
            f"Perimeter: {var_base + var_height + math.sqrt(var_base * var_base + var_height * var_height)}")


# Main Routine

yes_no_list = ['yes', 'no']

# Shape list with xxx exit code
shape_selection_list = ['circle', 'square', 'rectangle', 'triangle', 'xxx']

show_instructions = choice_checker("See Instructions? ", yes_no_list, "Please enter yes or no")
if show_instructions == "yes":
    print("Displays Instructions")

number_of_calculations = num_check("Enter the number of calculations: ", num_type=int, exit_code='')

calculations_done = 0

while number_of_calculations == "" or calculations_done < number_of_calculations:
    select_shape = choice_checker('Enter shape("xxx" to quit): ', shape_selection_list,
                                  'Please select circle, square, rectangle or triangle')

    if select_shape == 'xxx':
        break

    print(f'You picked {select_shape}')

    if select_shape == "circle":
        radius = num_check("Radius: ")
        print(circle(radius))


    elif select_shape == "square" or select_shape == "rectangle":
        length = num_check("Length: ")
        width = num_check("Width: ")
        print(square_rectangle(length, width))

    elif select_shape == "triangle":
        base = num_check("Base: ")
        height = num_check("Height: ")
        print(triangle(base, height))

    calculations_done += 1
