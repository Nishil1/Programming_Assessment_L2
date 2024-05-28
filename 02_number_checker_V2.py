def num_check(question, exit_code, num_type=int):
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


calculations = num_check("Enter the number of calculations: ", "")
question = num_check("Height of square: ", "xxx", num_type=float)