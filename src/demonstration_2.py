"""
You are given a non-empty array that represents the digits of a non-negative integer.

Write a function that increments the number by 1.

The digits are stored so that the digit representing the most significant place value is at the beginning of the array. Each element in the array only contains a single digit.

You will not receive a leading 0 in your input array (except for the number 0 itself).

Example 1:

Input: [1,3,2]
Output: [1,3,3]
Explanation: The input array represents the integer 132. 132 + 1 = 133.

Example 2:

Input: [3,2,1,9]
Output: [3,2,2,0]
Explanation: The input array represents the integer 3219. 3219 + 1 = 3220.

Example 3:

Input: [9,9,9]
Output: [1,0,0,0]
Explanation: The input array represents the integer 999. 999 + 1 = 1000.
"""
def plus_one(digits):
    # Your code here
    # Given a list of single-digit numbers that together represent a single number, increment the number by 1
    # Case 1: the right most digit is not 9, just increment the right-most digit by 1
    # Case 2: the right most digit is 9, change the 9 to 0 and the we might need to add one digit to the left
    # Note that this might cascade if we have more that one 9 to the left
    # If all nums are 9 we have to add digit to the list

    # Idea 1 -> Work with the input we are given (in-place)
    # Idea 2 -> Transform the input into integers to more easily solve this

    # Start iterating from the right to left
    # If we realize we don't need to continue iterating (cause the digit is not a 9) we can just break out of the loop
    # Otherwise we will continue iterating from right to left so long as we need to continue carrrying a one over to the next digit

    for i in range(len(digits) - 1, -1, -1):
        if digits[i] == 9:
            digits[i] = 0
        else:
            digits[i] += 1
            return digits
    
    # If we reach here, every number in the list was a 9, we need to add a one to the front of the digits list
    digits.insert(0, 1)
    return digits

print(plus_one([9,9,9,9]))

