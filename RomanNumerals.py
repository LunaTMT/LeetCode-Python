class Solution:
    def romanToInt(self, s: str) -> int:
        
        R2I = {
        "I":             1,
        "V":             5,
        "X":             10,
        "L":             50,
        "C":             100,
        "D":             500,
        "M":             1000
        }
        
        roman = [*s]
        sum = 0
        for idx, value in enumerate(roman):
            try:
                if value == 'I' and roman[idx+1] in {"V", "X"}:
                    sum -= 2
                elif value == 'X' and roman[idx+1] in {"L", "C"}:
                    sum -= 20
                elif value == 'C' and roman[idx+1] in {"D", "M"}:
                    sum -= 200
            except:
                pass
                
            sum += R2I[value]
        return sum