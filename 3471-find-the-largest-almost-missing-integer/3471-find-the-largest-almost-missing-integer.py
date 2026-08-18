class Solution:
    # Date Solved: 18 August 2026, Tuesday, POTD
    # Refer: codestorywithMIK
    # Approach: Sliding Window
    # Go to each subarray of size k (window of size k) and mark which element came in that subarray. In the end, check which element came in exactly 1 subarray
    def largestInteger(self, nums: List[int], k: int) -> int:
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
