def validate_user_input(user_input, valid_choices, max_attempts=3):
    valid_input = get_valid_input(user_input, lambda inp: validate_choice_input(inp, valid_choices),
                                  "Wrong input. Try again: ", max_attempts)
    return valid_input.upper()

def validate_user_input_payment(user_input, max_attempts=3):
    valid_input = get_valid_input(user_input, validate_numeric_input,
                                  "Only integer numbers are allowed. Please try again: ", max_attempts)
    return int(valid_input)

def validate_choice_input(user_input, valid_choices):
    return user_input.upper() in valid_choices


def validate_numeric_input(user_input):
    return user_input.isnumeric()

def get_valid_input(user_input, validation_func, error_message, max_attempts=3):
    attempts = 0
    while not validation_func(user_input.strip()):
        attempts += 1
        if attempts >= max_attempts:
            raise ValueError("Maximum attempts reached. Try again later.")
        user_input = input(error_message).strip()
    return user_input
