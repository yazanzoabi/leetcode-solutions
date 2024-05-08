def two_sum(nums, target):
    nums = [(num, i) for i, num in enumerate(nums)]
    nums.sort()
    print(nums)
    l, r = 0, len(nums) - 1
    while l < r:
        sum = nums[l][0] + nums[r][0]
        if sum == target:
            return [nums[l][1], nums[r][1]]
        elif sum > target:
            r -= 1
            continue
        l += 1
    
    return None

# Example usage
nums = [2, 7, 11, 15]
target = 9
result = two_sum(nums, target)
print(result)  # Output: [0, 1]