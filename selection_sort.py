from typing import List

def selection_sort(nums: List[int]) -> List[int]:
    """ Selection Sort works by going through 
    the list and sorting in place.

    Args:
        nums (List[int]): list of numbers

    Returns:
        List[int]: sorted list of numbers
    """
    nums_ = nums.copy()
    
    n = len(nums_)
    
    for index in range(n):
        min_position = index
        
        for j in range(index, n):
            if nums_[j] <= nums_[min_position]:
                min_position = j
        
        if min_position is not None:
            nums_[index], nums_[min_position] = nums_[min_position], nums_[index]    
        
    return nums_
            
            