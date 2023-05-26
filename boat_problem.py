# boat problem original:
# there are two boats on opposite ends of a river
# the two boats start heading in the direction of the other boat at the same time with different but constant speeds
# they first meet each other 700 feet from the left shore
# then they at different time hit the opposite shore and turn back with no time loss
# they meet again 300 feet from the right shore
# how wide is the river?
# solution: 1800 feet
# how:
# by the time they first meet, the boats collectively traveled the width once.
# by the time they meet again, the boats have collectively traveled the width 3 times(both hit the opposite end, then turn around to meet each other)
# because they are going at constant speeds with no time loss at the ends, we know that the time it takes from the start for the boats to meet the second time is 3 times the time it takes for the boats to meet the first time from the start
# this tells us that the boat on the left travels 700 feet in x time(first meeting) and 2100 feet in 3x time(second meeting)
# therefore, the width is the distance from the left they meet times 3 minus the distance from the right they meet the second time (700 * 3 - 300)

# the function is a calculator that determines the width of the river from whatever information is passed in(not necessarily the same as the above problem)
# pieces of information are input as integers with missing values as -1
# if the information is sufficient and consistent, then the answer is returned
# if the information is insufficient, then that will be portrayed with returning -1
# if the information is inconsistent(multiple ways of determining the width and they give different answers), then that will be portrayed with returning -2

def boat_river_width(first_left:int, second_left:int, first_right:int, second_right:int):
    # initial value of to_return: if all the if checks for sufficient information fail, then return initial to_return of -1 to portray insufficient info
    to_return = -1
    # example problem information condition
    if (first_left != -1 & second_right != -1):
        to_return = first_left * 3 - second_right
    if (first_left != -1 & second_left != -1):
        if to_return != -1 & to_return != (first_left * 3 + second_left) / 2:
            return -2
        if to_return == -1:
            to_return = (first_left * 3 + second_left) / 2
    if (first_right != -1 & second_right != -1):
        if to_return != -1 & to_return != (first_right * 3 + second_right) / 2:
            return -2
        if to_return == -1:
            to_return = (first_right * 3 + second_right) / 2
    if (first_right != -1 & second_left != -1):
        if to_return != -1 & to_return != (first_right * 3 + second_left) / 2:
            return -2
        if to_return == -1:
            to_return = (first_right * 3 - second_right) / 2
    return to_return