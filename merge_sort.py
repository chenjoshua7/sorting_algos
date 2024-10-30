from typing import List

def merge_sort(nums: List[int]) -> List[int]:
    nums_ = nums.copy()
    n = len(nums_)
    
    first_half = nums_[:n//2]
    second_half = nums_[n//2:]

    if len(first_half) > 1:
        first_half = merge_sort(first_half)
    
    if len(second_half) > 1:
        second_half = merge_sort(second_half)
    
    sorted_list = []
    
    while first_half and second_half:
        if first_half[0] <= second_half[0]:
            sorted_list.append(first_half.pop(0))
        else:
            sorted_list.append(second_half.pop(0))
        
    if first_half:
        sorted_list.extend(first_half)
    elif second_half:
        sorted_list.extend(second_half)
        
    return sorted_list