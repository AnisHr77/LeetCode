from typing import List
def removeDuplicates(nums: List[int]) -> int:
    if not nums:
            return 0
    k=0
    for i in range(1,len(nums)):
        if(nums[i]!=nums[k]):
            k=k+1
            nums[k]=nums[i]
            print(nums)
    return k+1      
print(removeDuplicates([0,0,0,1,1,1,2,3,4,4,5]))       