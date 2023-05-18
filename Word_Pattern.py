  def wordPattern(self, pattern: str, s: str) -> bool:
      hash_ = {}
      s = s.split()

      if len(pattern) < len(s) or len(s) < len(pattern): return False

      for letter, word in zip(pattern, s):

          if word in hash_.values() and hash_.get(letter, False) != word: 
              return False #word conflicts

          elif letter not in hash_: #does the letter have a map
              hash_[letter] = word

          elif hash_[letter] != word: 
              return False  #letter conflics

      return True
