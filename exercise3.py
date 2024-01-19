def check_voting_age(age):
    return age >= 18


def check_years_until_retirement(age):
    return max(0, 65 - age)


def check_years_until_pre_retirement(age):
    return max(0, 60 - age)


def calculate_retirement_percentage(age):
    if age < 60:
        return 0
    elif age <= 65:
        return 60 + (age - 60) * 8  # Linear increase from 60% to 100% over 5 years
    else:
        return 100
