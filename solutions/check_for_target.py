def check_for_target(nums, target):
    left = 0
    right = len(nums) - 1

    while left < right:
        sum = nums[left] + nums[right]
        if sum == target:
            return True
        if sum < target:
            left += 1
        else:
            right -= 1
    
    return False