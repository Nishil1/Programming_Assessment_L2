def num_check(question):

    error = "Please enter an integer that is more than zero"

    while True:
        try:
            response = int(input(question))

            if response > 0:
                return response
            else:
                print(error)

        except ValueError:
            print(error)


calculations = num_check("Enter the number of calculations: ")

