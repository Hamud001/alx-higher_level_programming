#!/usr/bin/python3
# Hamud001


def weight_average(my_list=[]):
    """function return the weighted average of all integers tuple."""
    if not isinstance(my_list, list) or len(my_list) == 0:
        return (0)

    score = 0
    weight = 0
    for tup in my_list:
        score += (tup[0] * tup[1])
        weight += tup[1]
    return (score / weight)
