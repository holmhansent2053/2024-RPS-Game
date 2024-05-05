def rps_compare(comp, user):

    if comp == user:
        var_result = "tie"

    # Three ways to win...
    elif comp == "rock" user == "paper":
        var_result = "win"

    else:
        var_result = "loss"

    return var_result

user_choice = "rock"
comp_choice = "paper"

result = rps_compare(user_choice, comp_choice)