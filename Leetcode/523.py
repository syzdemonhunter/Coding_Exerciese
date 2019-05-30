# https://leetcode.com/problems/continuous-subarray-sum/

# If k == 0, then search for any consecutive pair of 0s.

# Else, we will keep track of indices of the cumulative sum (or prefix sum) mod by k in a dictionary. We will return True if we've seen a cumulative sum % k at least 2 indices before.

# This means that there is a subarray that has a sum(subarray) % k == 0 and that subarray contains at least 2 elements.

# T: O(n)
# S: O(n)

class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        if k == 0:
            return any(nums[i] == 0 and nums[i + 1] == 0 for i in range(len(nums) - 1))
        
        mods, cum_sum_mod_k = {0: -1}, 0
        for i, num in enumerate(nums):
            cum_sum_mod_k = (cum_sum_mod_k + num) % k
            if cum_sum_mod_k in mods and i - mods[cum_sum_mod_k] > 1:
                return True
            if cum_sum_mod_k not in mods:
                mods[cum_sum_mod_k] = i
                
        return False
        
        