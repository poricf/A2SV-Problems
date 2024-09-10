# Problem: Fraction Addition and Subtraction - https://leetcode.com/problems/fraction-addition-and-subtraction/

class Solution:
    def fractionAddition(self, expression: str) -> str:
        result = []
        current = ""
        
        for i, char in enumerate(expression):
            if char == "+":
                result.append(current)
                current = ""
            elif char == '-' and i != 0:
                result.append(current)
                current = ""
                
                current += '-'
            else:
                current += char

        result.append(current)  


        _lcm = 1
        denominator = []
        numerator = []
        for elem in result:
            num,denom = map(int,elem.split('/'))
            _lcm = lcm(denom,_lcm)
            denominator.append(denom)
            numerator.append(num)
            
        
        ansnum = 0
        for i in range(len(numerator)):
            chung = _lcm//denominator[i]

            ansnum += (chung*numerator[i])
        
        comdiv = gcd(ansnum,_lcm)

        ansnum//=comdiv
        _lcm//=comdiv

        return f"{ansnum}/{_lcm}"

        '''
        2 + 5  = 6 + 14 = 20
        -   -
        3   9

        ()/9
        '''
        



