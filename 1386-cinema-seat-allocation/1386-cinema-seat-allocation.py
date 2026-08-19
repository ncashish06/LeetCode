class Solution:
    # Date Solved: 19 August 2026, Wednesday, POTD
    # Refer: codestorywithMIK
    def maxNumberOfFamilies(self, n: int, reservedSeats: List[List[int]]) -> int:
        # Approach-1: Greedy Pick using map
        # Time: O(N), N = len(reservedSeats), Space: O(N), for storing reserved seats in map (in form of set)
        mp = defaultdict(set)  # row -> seats in each row booked

        for reservedSeat in reservedSeats:
            row = reservedSeat[0]
            seat = reservedSeat[1]

            mp[row].add(seat)

        result = (n - len(mp)) * 2

        for row, bookedSeats in mp.items():

            def isAvailable(seat):
                return seat not in bookedSeats

            graupA = (
                isAvailable(2) and isAvailable(3) and isAvailable(4) and isAvailable(5)
            )
            graupB = (
                isAvailable(4) and isAvailable(5) and isAvailable(6) and isAvailable(7)
            )
            graupC = (
                isAvailable(6) and isAvailable(7) and isAvailable(8) and isAvailable(9)
            )

            if graupA and graupC:
                result += 2
            elif graupA or graupB or graupC:
                result += 1

        return result
        """
        # Approach-2: Greedy Pick using bit mask
        # Time: O(N), N = len(reservedSeats), Space: O(N), for storing reserved seats in the form of mask
        mp = defaultdict(int)  # row -> seats in each row booked

        for reservedSeat in reservedSeats:  # O(10^4)
            row = reservedSeat[0]
            seat = reservedSeat[1]

            mp[row] |= 1 << seat  # set bits are the booked seats

        result = (n - len(mp)) * 2

        maskA = (
            (1 << 2) | (1 << 3) | (1 << 4) | (1 << 5)
        )  # set bits are the ones which I need empty for Group A
        maskB = (
            (1 << 4) | (1 << 5) | (1 << 6) | (1 << 7)
        )  # set bits are the ones which I need empty for Group B
        maskC = (
            (1 << 6) | (1 << 7) | (1 << 8) | (1 << 9)
        )  # set bits are the ones which I need empty for Group C

        for row, bookedSeatsMask in mp.items():  # min(10*n, 10^4)
            graupA = (bookedSeatsMask & maskA) == 0
            graupB = (bookedSeatsMask & maskB) == 0
            graupC = (bookedSeatsMask & maskC) == 0

            if graupA and graupC:
                result += 2
            elif graupA or graupB or graupC:
                result += 1

        return result
        """
