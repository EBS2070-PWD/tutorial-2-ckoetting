# Pay attention to the use of multiple returns in a function. If you are unsure, save the results in a variable and
# return only once at the end of the function.
def calculate_points(score_t1, score_t2):
    if score_t1 > score_t2:
        return 3, 0
    elif score_t1 < score_t2:
        return 0, 3
    else:
        return 1, 1


# This function was done in two steps. First the input was done, then the check_points was added later.
# Work iteratively, and test often.
def input_names_scores():
    name_team1 = input("Enter the name of team 1: ")
    name_team2 = input("Enter the name of team 2: ")
    score_team1 = int(input(f"Enter the score of the {name_team1}: "))  # fails if not int
    score_team1 = check_points(score_team1)  # fails if negative
    score_team2 = int(input(f"Enter the score of the {name_team2}: "))
    score_team2 = check_points(score_team2)
    return name_team1, name_team2, score_team1, score_team2


def output_results(name_team1, name_team2, score_team1, score_team2, points_team1, points_team2):
    print(f"Team {name_team1}: Score: {score_team1}, Points: {points_team1}\n"
          f"Team {name_team2}: Score: {score_team2}, Points: {points_team2}")


def check_points(score_team):
    if score_team < 0:
        raise ValueError("Invalid Score")
    else:
        return score_team


# This is the main function. It serves as an example of how this program can run. It is the first function that is
# called when the program is run. Note that it is not called when you import the module or when you run the tests.
if __name__ == '__main__':
    n_team1, n_team2, s_team1, s_team2 = input_names_scores()
    p_team1, p_team2 = calculate_points(s_team1, s_team2)
    output_results(n_team1, n_team2, s_team1, s_team2, p_team1, p_team2)
