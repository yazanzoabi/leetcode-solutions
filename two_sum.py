def two_sum(nums, target):
    # Sort the array
    nums.sort()
    
    # Initialize two pointers
    left = 0
    right = len(nums) - 1
    
    while left < right:
        # Calculate the sum of the current pair
        current_sum = nums[left] + nums[right]
        
        if current_sum == target:
            # Return the indices of the two numbers
            return [left, right]
        elif current_sum < target:
            # Move the left pointer to the right
            left += 1
        else:
            # Move the right pointer to the left
            right -= 1
    
    # If no pair is found, return an empty list
    return []

# Example usage
nums = [2, 7, 11, 15]
target = 9
result = two_sum(nums, target)
print(result)  # Output: [0, 1]