# Given an array of ints, return the number of 9's in the array.

def array_count9(nums):
  count=0
  arr_len = len(nums)
  for i in range(arr_len):
    if(nums[i] == 9):
      count+=1
  return count



# array_count9([1, 2, 9]) → 1
# array_count9([1, 9, 9]) → 2
# array_count9([1, 9, 9, 3, 9]) → 3