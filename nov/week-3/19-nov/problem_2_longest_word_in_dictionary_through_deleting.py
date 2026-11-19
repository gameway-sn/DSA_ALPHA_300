class Solution:
    def findLongestWord(self, s: str, dictionary: list[str]) -> str:

        def counter(w):
            h = {}
            for c in w:
                h[c] = 1 + h.get(c, 0)
            return h

        larg = ''

        sh = counter(s)

        for w in dictionary:
            wh = counter(w)

            valid = True
            for c, freq in wh.items():
                if sh.get(c, 0) < freq:
                    valid = False
                    break

            if valid:
                if len(w) > len(larg) or (len(w) == len(larg) and w < larg):
                    larg = w

        return larg
