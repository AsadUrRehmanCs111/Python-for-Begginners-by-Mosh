def find_max(array_of_ints):
    maximum = array_of_ints[0]
    for nums in array_of_ints:
        if nums > maximum:
            maximum = nums
    return maximum
