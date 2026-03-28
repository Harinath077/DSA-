class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        # Separate positive and negative numbers
        pos, neg = [],[]
        n = len(nums)
        
        # compute the pos[], neg[]
        for num in nums:
            if( num < 0 ):
                neg.append(num)
            else:
                pos.append(num)
        res = [0] * n
        # main logic
        if( len(pos) > len(neg) ):
            for i in range(len(neg)):
                res[i*2] = pos[i]
                res[i*2+1] = neg[i]
            
            index = 2 * len(neg)
            for i in range(len(pos) - len(neg)):
                res[index] = pos[len(neg) + i]
                index += 1
        else:
            for i in range(len(pos)):
                res[i*2] = pos[i]
                res[i*2+1] = neg[i]
            
            index = 2 * len(pos)
            for i in range(len(neg) - len(pos)):
                res[index] = neg[len(pos) + i]
                index += 1
        return res