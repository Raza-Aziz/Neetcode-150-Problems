class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # built an adjacency list
        pre_map = {i: [] for i in range(numCourses)}

        # Just add all the courses and their prerequisites in the list
        for crs, pre in prerequisites:
            pre_map[crs].append(pre)

        # Make a set of visited courses
        visited = set()

        # nested dfs
        def dfs(crs):
            # if a course is in visited, it means it's a cycle, then False
            if crs in visited:
                return False
            # if a course has no prerequisite, then it's a final prerequisite, then True
            if pre_map[crs] == []:
                return True

            # Finally, for all other courses, add in visited
            visited.add(crs)

            # check for every prerequisite in that course
            for pre in pre_map[crs]:
                if not dfs(pre):  # if not dfs (meaning if in visited)
                    return False

            visited.remove(crs)
            pre_map[crs] = []

            return True

        for crs in range(numCourses):
            if not dfs(crs):
                return False

        return True
