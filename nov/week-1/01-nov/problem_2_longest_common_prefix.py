class Solution(object):
    def longestCommonPrefix(self, strs):
        pl = 0
        if not strs or strs[0] == "":
            return ""
        t = strs[0][0]
        while True:    
            for i in strs:
                if pl == len(i):
                    return strs[0][0:pl]
                t = strs[0][pl]

                if i[pl] != t:
                    if pl == 0:
                        return ""
                    return strs[0][0:pl]

            pl += 1
        return ""
