class Solution:
    # Date Solved: 30 July 2026, Thursday
    # codestorywithMIK says Asked by Sprinkler in Online Assessment on 27 July 2026.
    # Refer: codestorywithMIK
    """
    # Approach-1: Using Prefix Sum array
    # Time: O(n), Space: O(n)
    def helper(self, prefix_sum: List[int], L: int, M: int) -> int:
        n = len(prefix_sum)
        best_l = 0  # best (max) sum seen so far for the L-length block
        best = 0  # best total (L-block + M-block)

        for m_end in range(L + M - 1, n):
            l_end = m_end - M
            l_start = l_end - L

            m_sum = prefix_sum[m_end] - prefix_sum[l_end]
            l_sum = prefix_sum[l_end] - (0 if l_start < 0 else prefix_sum[l_start])

            best_l = max(best_l, l_sum)
            best = max(best, best_l + m_sum)

        return best

    def maxSumTwoNoOverlap(self, nums: List[int], firstLen: int, secondLen: int) -> int:
        n = len(nums)

        prefix_sum = [0] * n
        prefix_sum[0] = nums[0]
        for i in range(1, n):
            prefix_sum[i] = prefix_sum[i - 1] + nums[i]

        return max(
            self.helper(prefix_sum, firstLen, secondLen),
            self.helper(prefix_sum, secondLen, firstLen),
        )
    """

    # Approach-2: Using Sliding Window
    # Time: O(n), Space: O(1)
    def helper(self, nums: List[int], L: int, M: int) -> int:
        n = len(nums)

        l_sum = 0
        m_sum = 0

        # starting window from index 0 to L+M-1
        for i in range(L + M):
            if i < L:
                l_sum += nums[i]
            else:
                m_sum += nums[i]

        best_l = l_sum
        best = best_l + m_sum

        for m_end in range(L + M, n):
            l_sum += nums[m_end - M] - nums[m_end - M - L]
            m_sum += nums[m_end] - nums[m_end - M]

            best_l = max(best_l, l_sum)
            best = max(best, best_l + m_sum)

        return best

    def maxSumTwoNoOverlap(self, nums: List[int], firstLen: int, secondLen: int) -> int:
        n = len(nums)
        return max(
            self.helper(nums, firstLen, secondLen),
            self.helper(nums, secondLen, firstLen),
        )
