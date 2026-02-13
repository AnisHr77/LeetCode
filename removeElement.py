from typing import List 
def removeElement(nums: List[int], val: int) -> int:
     if nums == []:
         return 0
     k=0
     for i in range (len(nums)):
         if nums[i]!=val:
             nums[k]=nums[i]
             k+=1
             print(nums)
     return k        
print(removeElement([0,0,0,1,1,1,2,3,4,4,5],0))              