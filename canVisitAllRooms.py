class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        def dfs(room_index,visited):
            visited.add(room_index)
            for key in rooms[room_index]:
                if key not in visited:
                    dfs(key,visited)
        visited = set()
        dfs(0,visited)
        return len(visited)==len(rooms)