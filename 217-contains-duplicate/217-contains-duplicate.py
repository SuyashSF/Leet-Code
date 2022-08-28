class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        Hashset = set()
        
        for i in nums:
            if i in Hashset:
                return True
            Hashset.add(i)
        return False