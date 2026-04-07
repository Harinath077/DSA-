class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand) % groupSize != 0:
            return False

        count = Counter(hand)       # Step 1: Count frequency of each card
        hand.sort()                 # Step 2: Sort the hand (important for greedy)

        for num in hand:           # Step 3: Try to form groups
            if count[num] > 0:
                for i in range(num, num + groupSize):
                    if count[i] == 0:
                        return False
                    count[i] -= 1
        return True


