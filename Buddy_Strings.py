class Solution:
    def buddyStrings(self, s: str, goal: str) -> bool:

        n = len(s)
        if len(goal) != n:
            return False

        if s == goal:
            return len(set(s)) < len(goal)
    
        wrong = 0
        found = []
        for i in range(len(s)):
            if s[i] != goal[i]:
                wrong += 1
                found.append((s[i], goal[i]))
            
            if wrong > 2:
                return False
        
        if len(found) == 2:
            return found[0][0] == found[1][1] and found[0][1] == found[1][0]
        

"""
or in short form
class Solution:
    def buddyStrings(self, s: str, goal: str) -> bool:
        n = len(s)
        if n != len(goal): return False
        diff = [(s[i], goal[i]) for i in range(n) if s[i] != goal[i]]
        return (len(diff) == 0 and len(set(s)) < n) or (len(diff) == 2 and diff[0] == diff[1][::-1])


"""