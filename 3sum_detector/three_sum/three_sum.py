from collections import defaultdict

def detect_three_sum(element_list:list[int]) -> list[tuple[int]]:
    solution = set()
    missing_values_dict = defaultdict(list)
    for index, elem in enumerate(element_list[1:], 1):
        if elem in missing_values_dict:
            for pre_solution in missing_values_dict[elem]:
                solution.add(order_tuple(pre_solution, elem))
        for e in range(index):
            missing_sum = -(elem+element_list[e])
            sub_solution_tuple = (element_list[e], elem) if (elem > element_list[e]) else (elem, element_list[e])
            if sub_solution_tuple not in missing_values_dict[missing_sum]:
                missing_values_dict[missing_sum].append(sub_solution_tuple)
            
    return list(solution)

def order_tuple(my_tuple, element):
    if element >= my_tuple[1]:
        return (*my_tuple, element)
    elif element <= my_tuple[0]:
        return (element, *my_tuple)
    else:
        return (my_tuple[0], element, my_tuple[1])
