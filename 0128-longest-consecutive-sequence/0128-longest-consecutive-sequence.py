class Solution:
    # Date Solved: 17 September 2026, Thursday
    # B75
    # Refer: B2Go and NeetCode (for Brute Force and Sorting)
    def longestConsecutive(self, nums: list[int]) -> int:
        """
        # Approach 1: Brute Force
        # Time: O(n^2), Space: O(n)
        res = 0
        store = set(nums)

        for num in nums:
            streak, curr = 0, num
            while curr in store:
                streak += 1
                curr += 1
            res = max(res, streak)
        return res

        # Approach 2: Sorting
        # Time: O(nlogn), Space: O(1) (excluding internal space for sort)
        if not nums:
            return 0
        res = 0
        nums.sort()

        curr, streak = nums[0], 0
        i = 0
        while i < len(nums):
            if curr != nums[i]:
                curr = nums[i]
                streak = 0
            while i < len(nums) and nums[i] == curr:
                i += 1
            streak += 1
            curr += 1
            res = max(res, streak)
        return res
        """
        # Approach 3: Hash Set
        # Time: O(n), Space: O(n)
        if not nums:
            return 0
        num_set = set(nums)
        longest_chain = 0

        for num in num_set:
            # If the current number is the smallest number in its chain, search for
            # the length of its chain, else skip
            if num - 1 not in num_set:
                current_num = num
                current_chain = 1

                # Continue to find the next consecutive numbers in the chain.
                while (current_num + 1) in num_set:
                    current_num += 1
                    current_chain += 1

                longest_chain = max(longest_chain, current_chain)

        return longest_chain
