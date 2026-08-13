class Solution:
    def canFinish(self, numCourses, prerequisites):

        graph = {}

        for i in range(numCourses):
            graph[i] = []

        for course, pre in prerequisites:
            graph[pre] = graph[pre] + [course]

        visited = [0] * numCourses

        def dfs(course):

            if visited[course] == 1:
                return False

            if visited[course] == 2:
                return True

            visited[course] = 1

            for neighbour in graph[course]:

                if not dfs(neighbour):
                    return False

            visited[course] = 2

            return True

        for course in range(numCourses):

            if not dfs(course):
                return False

        return True


numCourses = 4

prerequisites = [
    [1, 0],
    [2, 0],
    [3, 1],
    [3, 2]
]

obj = Solution()

print(obj.canFinish(numCourses, prerequisites))