def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
    graph = {i: [] for i in range(numCourses)}
    indegree = [0] * numCourses

    for course, prereq in prerequisites:
        graph[prereq].append(course)
        indegree[course] += 1

    queue = [course for course in range(numCourses) if indegree[course] == 0]
    visited = 0

    while queue:
        current = queue.pop()
        visited += 1

        for neighbour in graph[current]:
            indegree[neighbour] -= 1  
            if indegree[neighbour] == 0: 
                queue.append(neighbour)
    return visited == numCourses