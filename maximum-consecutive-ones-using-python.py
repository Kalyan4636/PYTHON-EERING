def findMaxConsecutiveOnes(nums):
    max_count = 0
    count = 0
    for i in nums:
        if i == 1:
            count += 1
        else:
            max_count = max(max_count, count)
            count = 0
    return max(max_count, count)

nums = [1,1,0,1,1,1]
print(findMaxConsecutiveOnes(nums))
