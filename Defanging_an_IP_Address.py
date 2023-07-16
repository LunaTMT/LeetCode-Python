def defangIPaddr(self, address: str) -> str:
    #For the sake of an algorithm
    new_add = ""
    for c in address:
        if c == ".":
            new_add += "[.]"
        else:
            new_add += c
    return new_add

    #OR simply
    #return address.replace('.', '[.]')