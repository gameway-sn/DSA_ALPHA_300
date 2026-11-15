# this has issue

class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        diff = 0

        if len(s) == 1:
            return s == goal
        if len(s) != len(goal):
            return False
        for i in range(len(s)):
            if s[i] == goal[0]:
                if i == 0:
                    if s[i + 1] == goal[1] and s[-1] == goal[-1]:
                        diff = i
                        
                elif i == len(s) - 1:
                    if s[0] == goal[1] and s[i - 1] == goal[-1]:
                        diff = i
                        
                else:
                    if s[i + 1] == goal[1] and s[i - 1] == goal[-1]:
                        diff = i
        print(diff)
        i = diff
        j = 0
        while j < len(s):
            if i > len(s) - 1:
                i = 0
            if goal[j] != s[i]:
                print(s[i], goal[j])
                return False
            i += 1
            j += 1      

        return True
