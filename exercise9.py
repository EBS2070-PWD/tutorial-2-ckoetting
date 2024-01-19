def get_values_and_positions(lst):
    return "\n".join([f"{value}, {index}" for index, value in enumerate(lst, start=1)])
