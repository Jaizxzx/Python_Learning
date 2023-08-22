def fancy_divide(list_of_numbers, index):
   denom = list_of_numbers[index]
   return [simple_divide(item, denom) for item in list_of_numbers]


def simple_divide(item, denom):
    while denom == 0:
        return 0
    else:
        return item / denom
fancy_divide([0, 2, 4], 0)