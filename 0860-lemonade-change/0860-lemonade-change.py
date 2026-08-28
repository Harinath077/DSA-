class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        
        five = 0
        ten = 0
        

        for coin in bills:

            if coin == 5:
                five += 1

            elif( coin == 10 ):

                if five == 0:
                    return False
                
                five -= 1
                ten += 1
            
            else:
                
                if ten > 0 and five > 0:
                    five -= 1
                    ten -= 1
                elif five >= 3:
                    five -= 3
                
                else:
                    return False
        
        return True