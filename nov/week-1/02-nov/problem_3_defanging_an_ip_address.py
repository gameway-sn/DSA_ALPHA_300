class Solution(object):
    def defangIPaddr(self, address):
        """
        :type address: str
        :rtype: str
        """
        r = []

        for c in address:
            if c == ".":
                r.append("[.]")
            else:
                r.append(c)

        return "".join(r)

