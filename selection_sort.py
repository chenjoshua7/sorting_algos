from typing import List

def selection_sort(nums: List[int]) -> List[int]:
    """ Selection Sort works by going through 
    the list and sorting in place.

    Args:
        nums (List[int]): list of numbers

    Returns:
        List[int]: sorted ist of numbers
    """
    
    for index, nunber in enumerate(nums):
        min_value = float('inf')
        min_position = None
        
        for j, num in enumerate(nums[index:]):
            if num <= min_value:
                min_value = num
                min_position = j
        
        if min_position:
            nums[index], nums[min_position] = nums[min_position], nums[index]    
        
    return nums
            
            