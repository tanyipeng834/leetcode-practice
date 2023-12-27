class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        
        def dfs(province_no,visited):
            if province_no in visited:
                return 0
            visited.add(province_no)
            for i in range(len(isConnected[province_no])):
                if i not in visited and isConnected[province_no][i] ==1:
                    dfs(i,visited)
            return 1
        visited = set()
        provinces =0
        for i in range (len(isConnected)):
            provinces += dfs(i,visited)
        return provinces
