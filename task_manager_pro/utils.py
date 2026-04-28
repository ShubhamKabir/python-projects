def get_choice():
    choice = input("Enter option: ")
    if not choice.isdigit():
        raise ValueError("Please enter a valid number.")
    return int(choice)


def get_non_empty_input(prompt):
    value = input(prompt)
    if not value.strip():
        raise ValueError("Input cannot be empty.")
    return value