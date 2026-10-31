class Solution:
    def countFreq(self, arr, target):
        # code here
        l = 0
        h = len(arr) - 1
        start = -1
        end = -1
        
        while l <= h:
            m = (l + h)//2
            n = arr[m]
            
            if n == target:
                start = m
                h = m - 1
            elif n < target:
                l = m + 1
            else:
                h = m - 1
                
        l = 0
        h = len(arr) - 1
        
        while l <= h:
            m = (l + h)//2
            n = arr[m]
            
            if n == target:
                end = m
                l = m + 1
            elif n < target:
                l = m + 1
            else:
                h = m - 1
            
        #print(start,end)
        return 0 if start == -1 else abs(start - end) + 1
