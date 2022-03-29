class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        sum_right = sum(nums)
        sum_left = 0

        for i in range(len(nums)):

            sum_right -= nums[i]

            if sum_left == sum_right:
                return i

            sum_left += nums[i]

        return -1