class Solution:
    def buddyStrings(self, s: str, goal: str) -> bool:
        if len(s) != len(goal):
            return False
        
        if s == goal:
            return len(set(s)) < len(s)

        indices = []
        for i in range(len(s)):
            if s[i] != goal[i]:
                indices.append(i)
                if len(indices) > 2:
                    return False

        return len(indices) == 2 and s[indices[0]] == goal[indices[1]] and s[indices[1]] == goal[indices[0]]

