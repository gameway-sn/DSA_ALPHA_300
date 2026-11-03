class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        hm = {}
        out = []
        
        for i in range(len(strs)):
            w = strs[i]
            idt = [0] * 26
            for c in w:
                idt[ord(c) - 97] += 1
            idt = tuple(idt)
            if idt not in hm:
                hm[idt] = []
        
            hm[idt].append(i)
    
        i = 0
        for k, v in hm.items():
            out.append([])
            for j in range(len(v)):
                out[i].append(strs[v[j]])
            i += 1

        return out

