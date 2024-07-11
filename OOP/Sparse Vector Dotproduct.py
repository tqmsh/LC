class SparseVector: 
    def __init__(self, nums):
        self.d = {i: v for i, v in enumerate(nums) if v}

    def dotProduct(self, vec):
        a, b = self.d, vec.d
        if len(b) < len(a): a, b = b, a
        return sum(v * b.get(i, 0) for i, v in a.items())

nums1 = SparseVector([0,1,0,0,2,0,0])
nums2 = SparseVector([1,0,0,0,3,0,4])  # Create nums2 as a SparseVector object

result = nums1.dotProduct(nums2)
print("Dot product:", result)
