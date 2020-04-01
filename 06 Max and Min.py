
import random


def get_min_max(ints=None):
    """
    Return a tuple(min, max) out of list of unsorted integers.

    Args:
       ints(list): list of integers containing one or more integers
    """
    # if input is empty or an empty array, return (0, 0)
    if ints is None or len(ints) == 0:
        return (0, 0)
    # initialize small and big variables for comparison
    small, big = ints[0], ints[0]
    # loop through each input number
    for num in ints:
        # if input number is smaller, update var small
        if num < small:
            small = num
        # if input number is larger, update var big
        elif num > big:
            big = num
    # return small and big as tuple
    return (small, big)


# =================================================================================
#                                      Test one
# =================================================================================

l = [i for i in range(0, 10)]  # a list containing 0 - 9
random.shuffle(l)

print ("Pass" if ((0, 9) == get_min_max(l)) else "Fail")

# =================================================================================
#                                      Test two
# =================================================================================

l = [i for i in range(-100, 100)]  # a list containing 0 - 9
random.shuffle(l)

print ("Pass" if ((-100, 99) == get_min_max(l)) else "Fail")

# =================================================================================
#                                      Test three
# =================================================================================

print ("Pass" if ((0,0) == get_min_max([0])) else "Fail")

# =================================================================================
#                                      Test four
# =================================================================================

print ("Pass" if ((0,0) == get_min_max([])) else "Fail")
