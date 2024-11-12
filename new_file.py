from random import randint

random_list = []

for value in range(40):
    random_list.append(randint(1,50))

def list_sorter(list):
    return sorted(list, reverse=True)


def my_sorting_function(random_order_list):

    my_sorted_list = list()

    for i in range(len(random_order_list)):
        my_sorted_list.append('')

    for value in random_order_list:
        number_of_next_value_is_greater = 0
        number_of_next_value_is_equal = 0
        for next_value in random_order_list:
            if value > next_value:
                number_of_next_value_is_greater = number_of_next_value_is_greater + 1
            if next_value == value:
                number_of_next_value_is_equal = number_of_next_value_is_equal + 1

        new_list_index = len(random_order_list) - number_of_next_value_is_greater - 1
        for number_of_equal_value in range(number_of_next_value_is_equal):
            my_sorted_list[new_list_index - number_of_equal_value] = value

    return my_sorted_list


def bubble_sorting_function(bubble_random_order_list):
    last_element = len(bubble_random_order_list) - 1
    for pass_no in range(last_element, 0, -1):
        for idx in range(pass_no):
            if bubble_random_order_list[idx] > bubble_random_order_list[idx + 1]:
                bubble_random_order_list[idx], bubble_random_order_list[idx + 1] = bubble_random_order_list[idx + 1], bubble_random_order_list[idx]
    bubble_random_order_list.reverse()
    return bubble_random_order_list

sorted_list_function = list_sorter(random_list)
my_sorted_list = my_sorting_function(random_list)
bubble_sorted_list = bubble_sorting_function(random_list)

print(random_list)
print(sorted_list_function)
print(my_sorted_list)
print(bubble_sorted_list)
