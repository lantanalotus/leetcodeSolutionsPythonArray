from typing import List

def removeDuplicates(nums: List[int]) -> int:
    if not nums:
        return 0
    
    k = 1 # Next position for a unique number

    for i in range(1, len(nums)):
        if nums[i] != nums[i - 1]:
            nums[k] = nums[i]
            k += 1

    return k

# Example usage:
nums = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]

print("Original array:", nums)
k = removeDuplicates(nums)

print("New length:", k)
print("Array after removing duplicates:", nums[:k]) # Only the first k elements are unique

