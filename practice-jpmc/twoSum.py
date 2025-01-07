# HashMap
def twoSum(nums, target):
    hashMap = {}
    
    for i in range(len(nums)):
        diff = target - nums[i]
        
        if diff in hashMap:
            return [i, hashMap[diff]]
        hashMap[nums[i]] = i
        
    return []
    
        

# Test data
if __name__ == "__main__":
    nums = [2, 7, 11, 15]
    target = 9
    result = twoSum(nums, target)
    print(f"Indices of the two numbers that add up to {target} are: {result}")