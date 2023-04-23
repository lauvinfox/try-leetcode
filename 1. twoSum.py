def twoSum(nums, target):
    # Hashmap
    seen = {}
    for i, value in enumerate(nums):
        remaining = target - nums[i]

        if remaining in seen:
            return [seen[remaining], i]

        seen[value] = i


def twoSum1(nums, target):
    # Brute Force
    n = len(nums)
    i = 0
    j = i + 1
    while (i < n-1):
        while (j < n):
            if nums[i] + nums[j] == target:
                return [i, j]
            j += 1
        i += 1
