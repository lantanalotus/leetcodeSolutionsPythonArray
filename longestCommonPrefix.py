from typing import List

def longestCommonPrefix(strs: List[str]) -> str:
    if not strs: # If list is empty
        return ""
    
    prefix = strs[0] # Take the first string as starting prefix

    for i in range(1, len(strs)):
        j = 0
        # Compare characters while they match

        while j < len(prefix) and j < len(strs[i]) and prefix[j] == strs[i][j]:
            j += 1

        # Shrink the prefix to only the common part
        prefix = prefix[:j]

        if not prefix: # No common prefix
            return ""
        
    return prefix
    

# Example usage
example = ["flower", "flow", "flight"]

print("Longest common prefix =", longestCommonPrefix(example))

    
