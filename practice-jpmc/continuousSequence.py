def find_continuous_sequence(nums):
    """
    Function to find continuous sequence of numbers in the given input list.
    
    :param nums: List of integers
    :return: List of continuous sequences
    """
    # Your implementation here
    if not nums:
        return []

    nums.sort()
    sequence = []
    curr = [nums[0]]
    
    for i in range(1, len(nums)):
        if nums[i] == nums[i - 1] + 1:
            curr.append(nums[i])
        else:
            sequence.append(curr)
            curr = [nums[i]]
    sequence.append(curr)
    
    return sequence
    
if __name__ == "__main__":
    # Test cases
    test_cases = [
        ([1, 2, 3, 4, 5], [[1, 2, 3, 4, 5]]),
        ([1, 2, 4, 5, 6], [[1, 2], [4, 5, 6]]),
        ([10, 11, 12, 14, 15, 16, 18], [[10, 11, 12], [14, 15, 16], [18]]),
        ([1], [[1]]),
        ([], [])
    ]

    for i, (nums, expected) in enumerate(test_cases):
        result = find_continuous_sequence(nums)
        assert result == expected, f"Test case {i+1} failed: expected {expected}, got {result}"
    
    print("All test cases passed!")