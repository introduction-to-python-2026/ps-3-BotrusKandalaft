ddef move(my_list, direction=None):
    # Finds the index of the one in the list
    index_of_one = my_list.index(1)
    # Move the one to the left or to the right
    
    edge_number = my_list[0] or my_list[-1]
    if edge_number == 1:
       my_list[index_of_one] = 1
       return my_list
    
    if edge_number == 1:
       my_list[index_of_one] = 1
       return my_list

    if direction == 'right':
        my_list[index_of_one] = 0
        my_list[index_of_one + 1] = 1

    elif direction == 'left':
        my_list[index_of_one] = 0
        my_list[index_of_one - 1] = 1

    return my_list
