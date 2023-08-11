def makeEqual(self, words: list[str]) -> bool:
    joint = ''.join(words)
    set1 = set(joint)
    
    for i in set1 :
        if joint.count(i) % len(words) != 0 : return False 
    return True