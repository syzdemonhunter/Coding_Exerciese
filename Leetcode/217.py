# https://leetcode.com/problems/contains-duplicate/
# T: O(n)
# S: O(n)

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        my_set = set()
        for num in nums:
            if num in my_set:
                return True
            my_set.add(num)
        return False
        