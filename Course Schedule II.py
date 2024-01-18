class Solution:
    def findOrder(self, numCourses, prerequisites):
        graph = defaultdict(list)
        in_degree = [0] * numCourses

        for course, prereq in prerequisites:
            graph[prereq].append(course)
            in_degree[course] += 1

        queue = deque(course for course in range(numCourses) if in_degree[course] == 0)

        result = []
        while queue:
            current_course = queue.popleft()
            result.append(current_course)

            for neighbor in graph[current_course]:
                in_degree[neighbor] -= 1

                if in_degree[neighbor] == 0:
                    queue.append(neighbor)

        return [] if len(result) != numCourses else result