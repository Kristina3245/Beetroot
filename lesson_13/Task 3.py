def choose_func(nums: list, func1, func2):
    if all(num > 0 for num in nums):
        return func1(nums)
    else:
        return func2(nums)

def square_nums(nums):
    return [num ** 2 for num in nums]

def remove_negatives(nums):
    return [num for num in nums if num > 0]

nums1 = [1, 2, 3, 4, 5]
nums2 = [1, -2, 3, -4, 5]

result1 = choose_func(nums1, square_nums, remove_negatives)
print(result1)
assert result1 == [1, 4, 9, 16, 25]

result2 = choose_func(nums2, square_nums, remove_negatives)
print(result2)
assert result2 == [1, 3, 5]

