class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        
        #"all the rooms are locked except for room 0. "
        stack=[0]      
        visited =set()
        
        while stack:
            
            room_val = stack.pop()
            visited.add(room_val)
            
            for i in rooms[room_val]:
                
                if i not in visited:
                    stack.append(i)
                    
        return len(rooms) == len(visited)