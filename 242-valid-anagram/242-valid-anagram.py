class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        list1 = []
        list2 = []
        list1[:0] = s
        list2[:0] = t
        
        if(len(list1) != len(list2)):
            return False
        
        for i in list1:
            if i in list2:
                list2.remove(i)
                continue
            return False
        
        return True