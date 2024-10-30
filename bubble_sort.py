from typing import List

def bubble_sort(nums: List[int]) -> List[int]:
    nums_ = nums.copy()
    n = len(nums_)
    count = 0
    
    while count:
        count = 0
        for i in range(n-1):
            if nums_[i] > nums_[i+1]:
                nums_[i], nums_[i+1] = nums_[i+1], nums_[i]
                count += 1
        
    return nums_
    