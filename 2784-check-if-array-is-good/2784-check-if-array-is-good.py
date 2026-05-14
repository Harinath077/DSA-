class Solution:
    def isGood(self, nums: List[int]) -> bool:
        # maxmun as Two occurance (check 1)
        # check with hashmap ( check 2)

        n = len(nums)
        mapp = {}

        for num in nums:
            if( num not in mapp):
                mapp[num] = 0
            mapp[num] += 1

        size = len(mapp)
        maxNum = max(nums)

        #check 1
        if( mapp[maxNum] != 2):
            return False
        
        # check 2
        for i in range(1, maxNum):
            if(i not in mapp or mapp[i] != 1):
                return False
        
        return True