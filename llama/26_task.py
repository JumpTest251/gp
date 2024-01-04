def minSubArraySum(nums):
    """
    Given an array of integers nums, find the minimum sum of any non-empty sub-array
    of nums.
    Example
    minSubArraySum([2, 3, 4, 1, 2, 4]) == 1
    minSubArraySum([-1, -2, -3]) == -6
    """
    # Initialize the minimum sum to infinity
    min_sum = float('inf')

    # Iterate over each sub-array of nums
    for i in range(len(nums)):
        # Calculate the sum of the current sub-array
        sum = 0
        for j in range(i, len(nums)):
            sum += nums[j]

        # Update the minimum sum if necessary
        if sum < min_sum:
            min_sum = sum

    return min_sum
