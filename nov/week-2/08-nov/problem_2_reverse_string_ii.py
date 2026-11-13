# strug
class Solution:
    def reverseStr(self, s: str, k: int) -> str:

        def rev(ss):
            return ss[::-1]

        i = 0
        r = []

        while i < len(s):
            r.append(rev(s[i:i + k]))
            r.append(s[i + k:i + 2 * k])
            i += 2 * k

        return "".join(r)
