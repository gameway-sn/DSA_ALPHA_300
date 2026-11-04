class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """
        hm = {}

        for i in magazine:
            hm[i] = 1 + hm.get(i, 0)

        for c in ransomNote:
            if c not in hm:
                return False
            else:
                hm[c] -= 1
                if hm[c] == -1:
                    return False

        return True
