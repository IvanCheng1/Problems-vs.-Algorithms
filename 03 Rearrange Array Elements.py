
def mergesort(items):
    # list of 0 or 1 items are already sorted
    if len(items) <= 1:
        return items
    # find the mid point, and divide into left and right lists
    mid = len(items) // 2
    left = items[:mid]
    right = items[mid:]
    # recur into each half
    left = mergesort(left)
    right = mergesort(right)

    return merge(left, right)


def merge(left, right):
    # initialise output list and indices
    merged = []
    left_index = 0
    right_index = 0
    # move through the lists until one is exhausted
    while left_index < len(left) and right_index < len(right):
        # if left item is larger, append right item and update right index
        if left[left_index] > right[right_index]:
            merged.append(right[right_index])
            right_index += 1
        # else, append left item and update left index as right item is larger
        else:
            merged.append(left[left_index])
            left_index += 1

    merged += left[left_index:]
    merged += right[right_index:]

    return merged


def rearrange_digits(input_list):
    """
    Rearrange Array Elements so as to form two number such that their sum is maximum.

    Args:
       input_list(list): Input List
    Returns:
       (int),(int): Two maximum sums
    """
    # check if input has 'enough' numbers
    if len(input_list) == 0:
        return [0, 0]
    elif len(input_list) == 1:
        return input_list + [0]
    elif len(input_list) == 2:
        return input_list

    # using mergesort to sort numbers
    sorted_list = mergesort(input_list)
    # initialise two outputs var
    one = ""
    two = ""
    # loop through sort list with len(nput_list)
    for i in range(len(sorted_list)):
        # ensure the number of digits in each list are not differ by more than 1
        if len(one) <= len(two):
            one += str(sorted_list.pop(-1))
        else:
            two += str(sorted_list.pop(-1))
    # return tuple of two numbers, that sum to the maximum
    return [int(one), int(two)]


# =================================================================================
#                                      Tests
# =================================================================================

def test_function(test_case):
    output = rearrange_digits(test_case[0])
    solution = test_case[1]
    if sum(output) == sum(solution):
        print("Pass")
    else:
        print("Fail")


test_function([[1, 2, 3, 4, 5], [531, 42]])
test_function([[4, 6, 2, 5, 9, 8], [964, 852]])
test_function([[0, 0, 1, 1, 1], [110, 10]])
test_function([[2], [2, 0]])
test_function([[], [0, 0]])
