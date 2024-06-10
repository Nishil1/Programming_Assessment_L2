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
    select_shape = choice_checker('Enter shape: ', shape_selection_list,
                                  'Please select circle, square, rectangle or triangle')

    if select_shape == 'xxx':
        break

    print(f'You picked {select_shape}')

    if select_shape == "circle":
        radius = num_check("Radius: ")
        area_circle = 3.14 * radius * radius
        perimeter_circle = 2 * 3.14 * radius
    elif select_shape == "square":
        length = num_check("Length: ")
        square_perimeter = length * 4
        square_area = length * length
    elif select_shape == "rectangle":
        length = num_check("Length: ")
        width = num_check("Width: ")
        rectangle_perimeter = 2 * length + 2 * width
        rectangle_area = length * width
    elif select_shape == "Triangle":
        base = num_check("Base: ")
        height = num_check("Height: ")
        triangle_perimeter = base + height + math.sqrt(base * base + height * height)
        triangle_area = 0.5 * base * height

    calculations_done += 1
