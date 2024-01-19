def check_voting_age(age):
    return True if age >= 18 else False


def check_years_until_retirement(age):
    return max(0, 65 - age)
