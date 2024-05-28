def choice_checker(question, valid_responses, error_message):

    while True:
        response = input(question).lower()

        for item in valid_responses:
            if response == item or response == item[0]:

                return item

        print(error_message)

yes_no_list = ['yes', 'no']
shape_selection_list = ['circle', 'square', 'rectangle', 'triangle']


show_instructions = choice_checker("See Instructions? ",yes_no_list, "Please enter yes or no")
if show_instructions == "yes":
    print("Displays Instructions")


select_shape = choice_checker('Enter shape: ', shape_selection_list,
                              'Please select circle, square, rectangle or triangle')
print(f'You picked {select_shape}')
