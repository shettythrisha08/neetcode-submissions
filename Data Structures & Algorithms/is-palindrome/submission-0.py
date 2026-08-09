class Solution:
    def isPalindrome(self, s: str) -> bool:
        pali=[]
        for char in s:
            if char.isalnum():
                pali.append(char.lower())
        pali="".join(pali) 
         
        if pali==pali[::-1]:
            return True
        return False