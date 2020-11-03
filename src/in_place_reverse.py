# How do we reverse an array in place?
def reverse(array):
    left = 0
    right = len(arr) - 1
    # Iterate so long as left < right
    # If there's an odd number of elements in the input arr we have a case where left and right land on the middle element
    while left < right:
        # Swap the elements they are pointing at
        # This does use an extra 'temp' variable under hood, but a single variable doesn't negate this being in place
        arr[left], arr[right] = arr[right], arr[left]
        left += 1
        right -= 1
    

arr = [26, 42, 16, 22, 8]
reverse(arr)
print(arr)