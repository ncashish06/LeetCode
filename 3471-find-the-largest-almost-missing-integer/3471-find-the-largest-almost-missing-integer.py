class Solution:
    # Date Solved: 18 August 2026, Tuesday, POTD
    # Refer: codestorywithMIK
    def largestInteger(self, nums: List[int], k: int) -> int:
        """
        # Approach-1: Sliding Window
        # Time: O(n*k), Space: O(n)
        # Go to each subarray of size k (window of size k) and mark which element came in that subarray. In the end, check which element came in exactly 1 subarray
        n = len(nums)

        i = 0
        j = 0

        mp = defaultdict(int)

        st = set()

        while j < n:
            if j - i + 1 == k:  # k sized subarray

                # Collect which elements are in this window
                for l in range(i, j + 1):
                    st.add(nums[l])

                # Mark those elements
                for x in st:
                    mp[x] += 1

                st.discard(nums[i])  # shifting window
                i += 1
            j += 1

        result = -1

        # Find the largest element which appeared in one subarray only
        for num, count in mp.items():
            if count == 1 and num > result:
                result = num

        return result
        """
        # Approach-2: Simple Observation
        # Time: O(n), Space: O(1)
        n = len(nums)

        # case 1 : When k == n
        if k == n:  # only one subarray possible. Select the largest element
            return max(nums)

        # case 2 : When k == 1
        freq = [0] * 51
        for num in nums:
            freq[num] += 1

        # every index is one subarray. Find largest element which appears only once
        if k == 1:
            for num in range(50, -1, -1):
                if freq[num] == 1:
                    return num
            return -1

        # case 3 : 1 < k < n
        # Notice that only the first and last element are going to be the
        # ones which will appear only in one subarray. Others will be part
        # of more than one subarray always

        maxResult = -1
        # So, if nums[0] appeared only at index 0, then it appeared only in one subarray
        if freq[nums[0]] == 1:
            maxResult = max(maxResult, nums[0])

        # Same, if nums[n-1] appeared only at index n-1, then it appeared only in one subarray
        if freq[nums[n - 1]] == 1:
            maxResult = max(maxResult, nums[n - 1])

        return maxResult
