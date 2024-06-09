# Given an array nums containing n distinct numbers in the range [0, n], return the only number in the range that is missing from the array.
# https://youtube.com/shorts/MGYuYoXHv3w?si=l6IomA7z7TA7v8GC

# This method allows any positive range with any starting point
# Does not work for an array with length of 1
def find_missing_number(nums):
    sum = 0
    minimum = nums[0]

    for num in nums:
        sum += num
        minimum = min(minimum, num)

    n = minimum + len(nums)

    target_total = n * (n + 1) // 2 + minimum * (minimum - 1) // 2

    return target_total - sum

# This solution is from the video and only works with starting points of 0
# def find_missing_number(nums):
#     n = len(nums)
# 
#     expected = n * (n + 1) // 2
# 
#     return expected - sum(nums)

if __name__ == "__main__":
    print(f'[1, 2, 4, 5]: {find_missing_number([1, 2, 4, 5])}')
