class Solution(object):
    def findAnagrams(self, s, p):
        n=len(p)
        left=0
        forstring={}
        forgoal={}
        out=[]

        for ch in p:
            if ch in forgoal:
                forgoal[ch]+=1
            else:
                forgoal[ch]=1

        for right in range(len(s)):
            if s[right] in forstring:
                forstring[s[right]]+=1
            else:
                forstring[s[right]]=1
            
            if right-left+1>n:
                forstring[s[left]]-=1
                if forstring[s[left]]==0:
                    del forstring[s[left]]
                left+=1
            if forstring==forgoal:
                out.append(left)
        return out
