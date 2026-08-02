class Solution:
    # Date Solved: 1 April 2026, Wednesday, POTD
    # Refer: codestorywithMIK
    # Time: O(nlogn), Space: O(n)
    def survivedRobotsHealths(self, positions: List[int], healths: List[int], directions: str) -> List[int]:
        n = len(positions)
        indices = list(range(n))

        # Sort indices by position
        indices.sort(key=lambda i: positions[i])

        stack = []

        for current_index in indices:
            if directions[current_index] == "R":
                stack.append(current_index)
            else:
                # Current robot moves left; resolve collisions with R-robots on the stack
                while stack and healths[current_index] > 0:
                    top_index = stack[-1]

                    if healths[top_index] > healths[current_index]:
                        healths[top_index] -= 1
                        healths[current_index] = 0
                        # top_index survives, stays on stack (no pop needed)
                    elif healths[top_index] < healths[current_index]:
                        stack.pop()
                        healths[current_index] -= 1
                        healths[top_index] = 0
                    else:
                        stack.pop()
                        healths[current_index] = 0
                        healths[top_index] = 0

        return [h for h in healths if h > 0]
