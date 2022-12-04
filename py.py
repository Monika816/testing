class Solution:
     def countDigit(n):
            count = 0
            while n > 0:
                count = count+1
                n = n/10
            return count          
    
    
    
    
    
     def isPalindrome(self, x: int) -> bool:
            if(x<0): return False
            cd = countDigit(x)
            if(cd >= 0 and cd<10): return True
            n = x
            rev = 0
            while x>0:
              last = x % 10
            rev = rev*10+last
            if n==rev:
                return True
        

x = int(input()) 
obj = Solution()
res = obj.isPalindrome(x)
print(res)

#  * Licensed to the Apache Software Foundation (ASF) under one