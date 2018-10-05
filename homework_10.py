# homework10
from items import ITEMS
from itertools import chain
from itertools import combinations


def knapsack_problem(items_lst):
    combinations_list = []
    sets = chain(*map(lambda x: combinations(items_lst, x),
                      range(0, len(items_lst) + 1)))
    for subset in sets:
        if 350 < sum([int(item.weight) for item in subset]) < 400:
            combinations_list.append(subset)

    result = max(combinations_list,
                 key=lambda x: sum([int(item.value) for item in x]))
    knapsack_items = ",".join([item.name for item in result])
    knapsack_weight = sum([item.weight for item in result])
    knapsack_value = sum([item.value for item in result])
    return "List of items in knapsack: {}." \
           "\nTotal weight: {}.\nTotal Value: {}.".format(knapsack_items,
                                                          knapsack_weight,
                                                          knapsack_value)


print(knapsack_problem(ITEMS))
