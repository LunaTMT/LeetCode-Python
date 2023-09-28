class Solution:
    def countValidWords(self, s: str) -> int:
        if s == "!":
            return 1

        punctuation = set(",!.")

        s = s.split()
        n = len(s)
        tokens = 0

        for i, word in enumerate(s):
            valid = True
            wL = len(word)-1
            punctuation_number = 0
            hypen_number = 0
            for j, c in enumerate(word):
                if ((c.isdigit()) or
                    (c.isalpha() and c != c.lower()) or
                    (c in punctuation and j != wL) or 
                    (punctuation_number > 1 or hypen_number > 1) or
                    (c == "-"    and ((j == 0 or j == wL) or (not word[j-1].isalpha() or not word[j+1].isalpha())))):
                    valid = False
                    break
                punctuation_number += (1 if c in punctuation  else 0)
                hypen_number += (1 if c == "-" else 0)
            tokens += (1 if valid else 0)
        
        return tokens


        """ or simply 

    

        class Solution:
            def countValidWords(self, sentence: str) -> int:
                pattern = re.compile('(^[a-z]+(-[a-z]+)?)?[,.!]?$')
                word_count = 0
                for word in sentence.split():
                    if pattern.match(word):
                        word_count += 1
                        
                return word_count
        
        
        """