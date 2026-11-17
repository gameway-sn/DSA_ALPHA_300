class Solution:
    def countVowelSubstrings(self, word: str) -> int:
        vowels = set("aeiou")
        ans = 0

        for i in range(len(word)):
            if word[i] not in vowels:
                continue

            seen = set()

            for j in range(i, len(word)):
                if word[j] not in vowels:
                    break

                seen.add(word[j])

                if len(seen) == 5:
                    ans += 1

        return ans
