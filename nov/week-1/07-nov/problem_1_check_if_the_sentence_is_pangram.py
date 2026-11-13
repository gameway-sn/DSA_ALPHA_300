from string import ascii_lowercase as az

class Solution:
    def checkIfPangram(self, sentence: str) -> bool:
        set_az = set(az)

        if set_az.issubset(set(sentence)):
            return True

        return False

