def get_input(prompt):
    value = input(prompt)
    if not value.strip():
        raise ValueError("Input cannot be empty")
    return value


def get_number(prompt):
    value = input(prompt)
    if not value.isdigit():
        raise ValueError("Enter a valid number")
    return int(value)