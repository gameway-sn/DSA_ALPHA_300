from collections import Counter
from itertools import permutations

class Solution:
    def allPalindromes(self, s: str) -> list[str]:

        hm = Counter(s)

        odd = []
        half = []

        # Step 1: Count characters and construct half
        for c, v in hm.items():

            if v % 2 != 0:
                odd.append(c)

            half.extend([c] * (v // 2))

        # Step 2: More than one odd frequency means impossible
        if len(odd) > 1:
            return []

        # Step 3: Generate unique permutations of half
        p = set(permutations(half))

        result = []

        # Step 4: Construct complete palindromes
        middle = odd[0] if odd else ""

        for w in p:
            left = "".join(w)
            right = left[::-1]

            result.append(left + middle + right)

        return sorted(result)
