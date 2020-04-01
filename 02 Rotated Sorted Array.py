
def rotated_array_search(input_list, number, low=0, high=''):
    """
    Find the index by searching in a rotated sorted array

    Args:
       input_list(array), number(int), low(int), high(int):
       - Input array to search;
       - the target;
       - lower bound index (default is 0 for initial search);
       - upper bound index (len of array - 1)
    Returns:
       int: Index or -1
    """
    # set initial high index
    if high == '':
        high = (len(input_list)-1)
    # if low index is higher than high index, break and return -1
    if low > high:
        return -1
    # find the mid index
    mid = (low + high) // 2
    # return mid index if mid index of input_list is the number
    if input_list[mid] == number:
        return mid
    # if low index < mid index, means left half is sorted
    if input_list[low] < input_list[mid]:
        # check if number is in left sorted half
        if input_list[low] <= number <= input_list[mid]:
            # if so, recur into left half
            return rotated_array_search(input_list, number, low, mid - 1)
        # else, recur into right half
        return rotated_array_search(input_list, number, mid + 1, high)
    # else, left half is not sorted, meaning right half is sorted
    else:
        # check if number is in right sorted half
        if input_list[mid] <= number <= input_list[high]:
            # if so, recur into right half
            return rotated_array_search(input_list, number, mid + 1, high)
        # else, recur into left half
        return rotated_array_search(input_list, number, low, mid - 1)


def linear_search(input_list, number):
    for index, element in enumerate(input_list):
        if element == number:
            return index
    return -1


# =================================================================================
#                                      Tests
# =================================================================================

def test_function(test_case):
    input_list = test_case[0]
    number = test_case[1]
    if linear_search(input_list, number) == rotated_array_search(input_list, number):
        print("Pass")
    else:
        print("Fail")


test_function([[6, 7, 8, 9, 10, 1, 2, 3, 4], 6])
test_function([[6, 7, 8, 9, 10, 1, 2, 3, 4], 1])
test_function([[6, 7, 8, 1, 2, 3, 4], 8])
test_function([[6, 7, 8, 1, 2, 3, 4], 1])
test_function([[6, 7, 8, 1, 2, 3, 4], 10])
test_function([[1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 9])
