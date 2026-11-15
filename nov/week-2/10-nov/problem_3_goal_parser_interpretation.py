class Solution:
    def interpret(self, command: str) -> str:
        r = []
        prev = ""
        for c in command:
            if c == 'G':
                r.append(c)
            elif c == ')' and prev == '(':
                r.append('o')
            elif prev == 'l' and c == ')':
                r.append('al')

            prev = c
        return "".join(r)
