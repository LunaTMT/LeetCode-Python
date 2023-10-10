def heightChecker(heights: list[int]) -> int:
    n = len(heights)
    max_height = max(heights)

    #First we count the frequency and store the number in its associated index 
    freq = [0] * (max_height+1)
    for number in heights:
        freq[number] += 1

    #Calculate cumulative frequency
    cum_freq = [0] * (max_height + 1)
    for index, number in enumerate(freq[1:],start=1):
        cum_freq[index] = number + cum_freq[index-1]

    #Setting values from original array into their correct positions based on cumulative index.
    #then decrementing
    sorted_heights = [0] * n
    for h in heights:
        sorted_heights[cum_freq[h]-1] = h
        cum_freq[h] -= 1
    

    return sum(1 for i in range(n) if heights[i] != sorted_heights[i])
    
    """
    or simply

    expected = sorted(heights)
    return sum(1 for i in range(len(heights)) if heights[i] != expected[i])
    """

heightChecker(heights = [5,1,2,3,4])