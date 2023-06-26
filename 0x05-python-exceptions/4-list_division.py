#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    result = [0] * list_length
    for i in range(list_length):
        try:
            element_1 = my_list_1[i]
            element_2 = my_list_2[i]
            if not isinstance(element_1, (int, float)) or not
            isinstance(element_2, (int, float)):
                raise TypeError("wrong type")
            if element_2 == 0:
                raise ZeroDivisionError("division by 0")
            division_result = element_1 / element_2
            result[i] = division_result
        except (IndexError, TypeError, ZeroDivisionError) as e:
            print("Error: {}".format(e))

    return result
