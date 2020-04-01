
def sort_012(input_list):
    """
    Given an input array consisting on only 0, 1, and 2, sort the array in a single traversal.

    Args:
       input_list(list): List to be sorted
    """
    zero = []
    one = []
    two = []
    # loop through input numbers
    for num in input_list:
        # check if number is 0, 1, or 2, else return
        if num not in [0,1,2]:
            return "Contain digits other than [0, 1, 2]"
        # append to 'one' if number is 1
        elif num == 1:
            one.append(num)
        # append to 'two' if number is 2
        elif num == 2:
            two.append(num)
        # else, must be zero
        else:
            zero.append(num)
    # return 0,1,2 list
    return zero + one + two


# =================================================================================
#                                      Tests
# =================================================================================

def test_function(test_case):
    sorted_array = sort_012(test_case)
    print(sorted_array)
    if sorted_array == sorted(test_case):
        print("Pass")
    else:
        print("Fail")


test_function([0, 0, 2, 2, 2, 1, 1, 1, 2, 0, 2])
test_function([2, 1, 2, 0, 0, 2, 1, 0, 1, 0, 0, 2, 2, 2, 1, 2, 0, 0, 0, 2, 1, 0, 2, 0, 0, 1])
test_function([0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2])
