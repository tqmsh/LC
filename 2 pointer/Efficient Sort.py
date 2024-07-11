def sorted_squares_two_pointers(a): 
    ans = [0] * len(a); l = 0; r = len(arr) - 1; id = len(arr) - 1
    while l <= r:
        # 从大到小填 ans, 目前这个坑必然是剩下的最负/最正的来的
        if a[r] ** 2 >= a[l] ** 2:
            ans[id] = a[r] ** 2
            r -= 1
        else:
            ans[id] = a[l] ** 2
            l += 1 
        id -= 1
    return ans
# Example usage
arr = [-4, -1, 0, 3, 10]
print(sorted_squares_two_pointers(arr))  # Output: [0, 1, 9, 16, 100]
