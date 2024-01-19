def check_voting_age(age, voting_age=18):
    return age >= voting_age


def check_years_until_retirement(age):
    return max(0, 65 - age)
