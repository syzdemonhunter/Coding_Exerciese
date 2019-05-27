# https://leetcode.com/problems/find-the-duplicate-number/
# https://www.jiuzhang.com/solution/flatten-2d-vector/
# T: O(n)
# S: O(1)

class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        if len(nums) <= 1:
            return -1
        
        slow = nums[0]
        fast = nums[nums[0]]
        while slow != fast:
            slow = nums[slow]
            fast = nums[nums[fast]]
            
        fast = 0
        while fast != slow:
            fast = nums[fast]
            slow = nums[slow]
            
        return slow
        