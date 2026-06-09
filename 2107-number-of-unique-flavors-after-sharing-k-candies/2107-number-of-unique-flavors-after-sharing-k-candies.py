from collections import defaultdict


class Solution:
    # Date Solved: 9 June 2026, Tuesday, June Weekly Premium W2
    # Sliding window
    # Time: O(n) not O(n*k) as we are not recomputing in every window, Space: O(n)
    """
    candies = [1,2,2,3,4,3]
    Initial freq (all candies):   {1:1, 2:2, 3:2, 4:1}
    Remove first window [1,2,2]:  {3:2, 4:1}          -> unique = 2

    i=3: add 1, remove 3  ->  {1:1, 3:1, 4:1}          -> unique = 3 , max
    i=4: add 2, remove 4  ->  {1:1, 2:1, 3:1}          -> unique = 3 , max
    i=5: add 2, remove 3  ->  {1:1, 2:2}               -> unique = 2
    """

    def shareCandies(self, candies: List[int], k: int) -> int:
        freq = defaultdict(int)

        # Start by putting all candies in the "outside" map
        for candy in candies:
            freq[candy] += 1

        # Remove the first window (we're giving it away)
        for i in range(k):
            freq[candies[i]] -= 1
            if freq[candies[i]] == 0:
                del freq[candies[i]]

        result = len(freq)  # unique flavors outside first window

        # Slide the window
        for i in range(k, len(candies)):
            # Add left-departing element back to outside (window moves right, so candies[i-k] leaves the window)
            freq[candies[i - k]] += 1

            # Remove newly entered element from outside (candies[i] enters the window)
            freq[candies[i]] -= 1
            if freq[candies[i]] == 0:
                del freq[candies[i]]

            result = max(result, len(freq))

        return result
