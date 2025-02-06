class SparseVector:
    def __init__(self, nums: List[int]):
        self.indexMapping = {i:x for i,x in enumerate(nums) if x}

    # Return the dotProduct of two sparse vectors
    def dotProduct(self, vec: 'SparseVector') -> int:
        out = 0
        
        for i in self.indexMapping:
            if i in vec.indexMapping:
                out += self.indexMapping[i] *  vec.indexMapping[i]
        return out

# Your SparseVector object will be instantiated and called as such:
# v1 = SparseVector(nums1)
# v2 = SparseVector(nums2)
# ans = v1.dotProduct(v2)