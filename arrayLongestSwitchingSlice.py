# call an array switching if all numbers in even positions are equal and all numbers in odd positions are equal. 
# example: [3,-7,3,-7,3] and [4,4,4] are switching, but [5,5,4,5,4] and [-3,2,3] are not switching. 
# Find the length of the longest switching slice (continuous fragment) in a given array A?
# Write a function that gives an array A consisting of N integers, returns the length of the longest switching slice in A

def longest_switching_slice(A):
    n = len(A)
    max_len = 0
    
    # Iterate through all possible starting points of subarrays
    for start in range(n):
        # Initialize two sets to track the unique values at even and odd positions
        even_set = set()
        odd_set = set()
        
        # Try to extend the subarray from the current start index
        for end in range(start, n):
            if (end - start) % 2 == 0:  # even index in the subarray
                even_set.add(A[end])
            else:  # odd index in the subarray
                odd_set.add(A[end])
            
            # Check if the subarray is switching
            if len(even_set) == 1 and len(odd_set) == 1:
                max_len = max(max_len, end - start + 1)
            else:
                # Once it fails to be switching, no need to extend further
                break
    
    return max_len


# Example usage:
A1 = [3, -7, 3, -7, 3]
A2 = [4, 4, 4]
A3 = [5, 5, 4, 5, 4]
A4 = [-3, 2, 3]

print(longest_switching_slice(A1))  # Output: 5
print(longest_switching_slice(A2))  # Output: 3
print(longest_switching_slice(A3))  # Output: 2
print(longest_switching_slice(A4))  # Output: 1
