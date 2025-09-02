from typing import List

def removeElements(nums: List[int], val: int) -> int:

    k = 0 # Pointer for the next position to place a non-val element

    for i in range(len(nums)):
        if nums[i] != val: # Keep the element
            nums[k] = nums[i] # Move it to the front
            k += 1 # Increment the count of non-val elements
    
    return k # New length of the array without val elements

# Example usage:

nums = [3, 2, 2, 3]
val = 3

print("Original array:", nums)
k = removeElements(nums, val)
print("Array after removeing elements:", nums[:k]) # Print only the first k elements