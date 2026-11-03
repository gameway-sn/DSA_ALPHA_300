class Solution(object):
    def capitalizeTitle(self, title):
        """
        :type title: str
        :rtype: str
        """
        lw = title.split()
        r = []
            
        for w in lw:
            if len(w) <= 2:
                temp = []
                for c in w:
                    cv = ord(c)
                    if cv >= 65 and cv <= 90:
                        temp.append(chr(cv + 32))
                    else:
                        temp.append(c)
                r.append("".join(temp))
            else:
                temp = []
                for i in range(len(w)):
                    cv = ord(w[i])
                    
                    if i == 0:
                        if cv >= 97 and cv <= 122:
                            temp.append(chr(cv - 32))
                        else:
                            temp.append(w[i])
                    else:
                        if cv >= 65 and cv <= 90:
                            temp.append(chr(cv + 32))
                        else:
                            temp.append(w[i])    
                
                r.append("".join(temp))
        
        return " ".join(r)

