from typing import List
def merge(nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        
        nums1=[x for x in nums1 if x!=0]
        nums2=[x for x in nums2 if x!=0]
        a=len(nums1)
        b=len(nums2)   
        for i in range (a):
            for k in range(b):
                if(nums1[i]<=nums2[k]):
                    i+=1
                    m-=1
            
                if (nums1[i]>nums2[k]) :
                    nums1.insert(i,nums2[k])
                    k+=1
                    n-=1    
        print(nums1)
merge([1,2,0,8,0,9,0],3,[2,5,6],3)        