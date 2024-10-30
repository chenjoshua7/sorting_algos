from merge_sort import merge_sort

def test_merge_sort_sorted():
    assert merge_sort([1, 2, 3, 4, 5]) == [1, 2, 3, 4, 5]

def test_merge_sort_unsorted():
    assert merge_sort([5, 4, 3, 2, 1]) == [1, 2, 3, 4, 5]

def test_merge_sort_mixed():
    assert merge_sort([64, 25, 12, 22, 11]) == [11, 12, 22, 25, 64]

def test_merge_sort_with_duplicates():
    assert merge_sort([3, 5, 3, 2, 8, 5, 6]) == [2, 3, 3, 5, 5, 6, 8]

def test_merge_sort_single_element():
    assert merge_sort([1]) == [1]

def test_merge_sort_empty():
    assert merge_sort([]) == []

def test_merge_sort_negative_numbers():
    assert merge_sort([3, -2, -5, 0, 6]) == [-5, -2, 0, 3, 6]