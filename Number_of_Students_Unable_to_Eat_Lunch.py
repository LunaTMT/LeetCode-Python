from collections import Counter
def countStudents(students, sandwiches):
    count = Counter(students)
    n, k = len(students), 0
    
    while k < n and count[sandwiches[k]]:
        count[sandwiches[k]] -= 1
        k += 1
    return n - k


""" or 

       while sand:
            if sand[0] in stu:
                stu.remove(sand[0])
                sand.pop(0)
            else:break
        return len(sand)

"""
countStudents(students = [1,1,1,0,0,1], sandwiches = [1,0,0,0,1,1])