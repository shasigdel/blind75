def move_zeros(nums):
    """
    Moves all zeros in the list nums to the end while maintaining the relative order of the non-zero elements.
    
    :param nums: List[int] - List of integers
    :return: None - Modifies nums in-place
    """
    
    l = 0
    for r in range(len(nums)):
        if nums[r]:
            nums[l], nums[r] = nums[r], nums[l]
            l+=1
    return nums

# Test cases
if __name__ == "__main__":
    # Test case 1
    nums1 = [0, 1, 0, 3, 12]
    move_zeros(nums1)
    print(nums1)  # Expected output: [1, 3, 12, 0, 0]

    # Test case 2
    nums2 = [0, 0, 1]
    move_zeros(nums2)
    print(nums2)  # Expected output: [1, 0, 0]

    # Test case 3
    nums3 = [1, 2, 3, 4, 5]
    move_zeros(nums3)
    print(nums3)  # Expected output: [1, 2, 3, 4, 5]

    # Test case 4
    nums4 = [0, 0, 0, 0, 0]
    move_zeros(nums4)
    print(nums4)  # Expected output: [0, 0, 0, 0, 0]

    # Test case 5
    nums5 = []
    move_zeros(nums5)
    print(nums5)  # Expected output: []