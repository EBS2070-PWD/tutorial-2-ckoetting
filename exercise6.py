def find_numbers():
    result = []
    for number in range(2000, 3201):  # 3201 is used to include 3200
        if number % 7 == 0 and number % 5 != 0:
            result.append(number)
    return result

