def twoSum(numbers, targetSum):
    numberToIndex = {}  # Dictionary: key = number, value = its index
    
    for currentIndex, currentNumber in enumerate(numbers):
        requiredNumber = targetSum - currentNumber  # The complement we need
        
        if requiredNumber in numberToIndex:  # Check if complement exists
            return [numberToIndex[requiredNumber], currentIndex]
        
        numberToIndex[currentNumber] = currentIndex  # Store current number with its index
    
    return []

numbers = [2, 7, 11, 15]
targetSum = 9
print(twoSum(numbers, targetSum))
