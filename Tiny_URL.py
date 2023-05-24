import random as r
import string

class Codec:

    def __init__(self):
        self.char_set = [*string.ascii_lowercase + string.ascii_uppercase + "0123456789"]
        self.map = {}

    def encode(self, longUrl: str) -> str:
        key = "".join([self.char_set[r.randrange(0,61)] for i in range(7)])
        self.map[key] = longUrl
        return "http://tinyurl.com/" + key

    def decode(self, shortUrl: str) -> str:
        return self.map[shortUrl[-7:]]
        