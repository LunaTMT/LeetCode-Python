def uniqueMorseRepresentations(words: list[str]) -> int:

    morse_code = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",
    ".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-",
    "-.--","--.."]
    alphabet = list(map(chr, range(97, 123)))
    lookup = { k:v for k, v in zip(alphabet, morse_code)}
    

    set_trans = set()
    for word in words:
        morse = ""
        for char in word:
            morse += lookup[char]
        set_trans.add(morse)
    return len(set_trans)

        
    #or simply 
    """
    morse_code = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",
    ".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-",
    "-.--","--.."]
    return len({"".join(morse_code[ord(c) - 97] for c in w) for w in words})
    """
         
            

uniqueMorseRepresentations(["gin","zen","gig","msg"])