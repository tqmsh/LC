def diff(arrA, arrB):  
    # symmetric_difference 模版 
    return list(set(arrA).symmetric_difference(set(arrB)))

# Example usage
a = [1, 2, 3, 4]
b = [3, 4, 5, 6]

print(diff(a, b))  # Output: [1, 2, 5, 6]
