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