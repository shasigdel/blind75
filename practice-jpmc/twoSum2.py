def two_sum_two(numbers, target):
    """
    :type numbers: List[int]
    :type target: int
    :rtype: List[int]
    """
    # Your implementation here
    l = 0
    r = len(numbers) - 1
    
    while l < r:
        curr = numbers[l] + numbers[r]
        if curr > target:
            r-=1
        elif curr < target:
            l+=1
        else:
            return [l + 1, r + 1]

    return []
# Test cases
if __name__ == "__main__":
    # Test case 1
    numbers = [2, 7, 11, 15]
    target = 9
    print(two_sum_two(numbers, target))  # Expected output: [1, 2]

    # Test case 2
    numbers = [2, 3, 4]
    target = 6
    print(two_sum_two(numbers, target))  # Expected output: [1, 3]

    # Test case 3
    numbers = [-1, 0]
    target = -1
    print(two_sum_two(numbers, target))  # Expected output: [1, 2]