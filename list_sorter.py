from random import randint

random_list = []

for value in range(40):
    random_list.append(randint(1,50))

def py_list_sorter(random_list):
    return sorted(random_list, reverse=True)



def my_sort_function(random_list):

    my_sorted_list = list()

    for i in range(len(random_list)):
        my_sorted_list.append('')

    for value in random_list:
        number_of_next_value_is_greater = 0
        number_of_next_value_is_equal = 0
        for next_value in random_list:
            if value > next_value:
                number_of_next_value_is_greater = number_of_next_value_is_greater + 1
            if next_value == value:
                number_of_next_value_is_equal = number_of_next_value_is_equal + 1

        new_list_index = len(random_list) - number_of_next_value_is_greater - 1
        for number_of_equal_value in range(number_of_next_value_is_equal):
            my_sorted_list[new_list_index - number_of_equal_value] = value

    return my_sorted_list


def bubble_sort_function(random_list):
    last_element = len(random_list) - 1
    for lenght in range(last_element, 0, -1):
        for indx in range(lenght):
            if random_list[indx] > random_list[indx + 1]:
                random_list[indx], random_list[indx + 1] = random_list[indx + 1], random_list[indx]
    random_list.reverse()
    return random_list


py_sorted_list = py_list_sorter(random_list)
my_sorted_list = my_sort_function(random_list)
bubble_sorted_list = bubble_sort_function(random_list)


print('random random_list: ', random_list)
print('python sorting function: ', py_sorted_list)
print('my sorting function: ', my_sorted_list)
print('bubble sorting: ', bubble_sorted_list)
