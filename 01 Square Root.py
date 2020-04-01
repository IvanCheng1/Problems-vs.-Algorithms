
def sqrt(number):
    """
    Calculate the floored square root of a number

    Args:
       number(int): Number to find the floored squared root
    Returns:
       int: Floored Square Root
    """
    # check for negative inputs
    if number < 0:
        return None
    # square root of 1 and 0 is 1 and 0
    elif number in [1, 0]:
        return number

    # initialise upper and lower bound
    high = number
    low = 0

    while low < high:
        # mid is the average of high and low
        mid = (high + low) // 2
        # if mid ** 2 is the number, return the mid value
        # OR, if mid ** 2 is smaller than the number and (mid + 1) ** 2 is larger than the number,
        # return the mid number as it's the floor value
        if mid**2 <= number < (mid+1)**2:
            return mid
        # mid is too high, change high var to mid
        elif mid**2 > number:
            high = mid
        # mid is too low, change low var to mid
        else:
            low = mid

# =================================================================================
#                                      Tests
# =================================================================================

print ("Pass" if  (3 == sqrt(9)) else "Fail")
print ("Pass" if  (0 == sqrt(0)) else "Fail")
print ("Pass" if  (4 == sqrt(16)) else "Fail")
print ("Pass" if  (1 == sqrt(1)) else "Fail")
print ("Pass" if  (5 == sqrt(27)) else "Fail")
print ("Pass" if  (27 == sqrt(783)) else "Fail")
print ("Pass" if  (28 == sqrt(784)) else "Fail")
print ("Pass" if  (28 == sqrt(785)) else "Fail")
print ("Pass" if  (99999 == sqrt(9999800001)) else "Fail")
print ("Pass" if  (99998 == sqrt(9999800000)) else "Fail")
