def longestCommonPrefix(strs):

        if len(strs) == 1:
            return strs[0]
        

        valid = []
        for i in range(1, len(max(strs, key=len)) + 1):

            slices = [item[0 : 0 + i] for item in strs]

            if len((set(slices))) != 1:
                try:
                    return valid[-1]
                except:
                    return ""
        
            valid.append(slices[0])

        try:
            return valid[-1]
        except:
            return ""

if __name__ == "__main__":
    strs = ["flower","flower","flower","flower"]
    longestCommonPrefix(strs)