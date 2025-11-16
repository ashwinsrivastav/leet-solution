class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        intersec=[]
        for i in set(nums1):
            count=nums1.count(i)
            if i in nums2:
                count2=nums2.count(i)
                if count>=count2:
                    for a in range(count2):
                        intersec.append(i)
                else:
                    for a in range(count):
                        intersec.append(i)
        return intersec