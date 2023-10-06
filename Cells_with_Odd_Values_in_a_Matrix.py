    def oddCells(self, m: int, n: int, indices: List[List[int]]) -> int:
        #Bit maniuplation
        odd_rows, odd_cols = [False] * n, [False] * m
        for r, c in indices:
            odd_rows[r] ^= True
            odd_cols[c] ^= True
        return sum(ro ^ cl for ro in odd_rows for cl in odd_cols)

        #Or this slower version of populating an array with actual values and determining if it is odd by modulo    
        matrix = [[0 for i in range(n)] for j in range(m)]
        count = 0
        for (r,c) in indices:
            for i in range(n):
                matrix[r][i] += 1
                count += (1 if matrix[r][i] % 2 else -1) 
            for j in range(m):
                matrix[j][c] += 1
                count += (1 if matrix[j][c] % 2 else -1)
        
        return count

        