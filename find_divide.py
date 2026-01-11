def findDivide(nums):
    left = 0
    right = len(nums) - 1
    while left < right - 1:
        mid = (left + right + 1) // 2

        if nums[right] >= nums[mid] >= nums[left]: return left
        if nums[mid] <= nums[right]: right = mid
        if nums[mid] >= nums[left]: left = mid
    return left


def search(nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: int
    """
    divide = findDivide(nums)
    try:
        if target < nums[0]:
            return nums.index(target, divide, len(nums))
        else:
            return nums.index(target, 0, divide + 1)
    except:
        return -1

if __name__ == '__main__':
    search([1], 1)
