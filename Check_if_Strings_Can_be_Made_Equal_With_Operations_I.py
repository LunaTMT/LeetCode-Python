class Solution:
    def canBeEqual(self, s1: str, s2: str) -> bool:
        s1 = [*s1]
        s2 = [*s2]
        if s1[0] != s2[0]:
            if s1[2] != s2[2]:
                s1[0], s1[2] = s1[2], s1[0]
                
                if s1[0] == s2[0] and s1[2] == s2[2]:
                    pass
                else: 
                    return False
            else:
                return False
        else:
            if s1[2] != s2[2]:
                return False

        if s1[1] != s2[1]:
            if s1[3] != s2[3]:
                s1[1], s1[3] = s1[3], s1[1]
                
                if s1[1] == s2[1] and s1[3] == s2[3]:
                    pass
                else: 
                    return False
            else:
                return False
        else:
            if s1[3] != s2[3]:
                return False

        return True

        #Or simply
        return ({s1[0], s1[2]} == {s2[0], s2[2]} and
                {s1[1], s1[3]} == {s2[1], s2[3]})
