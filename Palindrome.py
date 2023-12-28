class Palindrome:
    def __init__(self, val): 
        self.val = val
        self.isPal = True

    def isPalindrome(self):
        i=0
        V_Length = self.val.__len__()
        for car in self.val:
            if not(self.val[V_Length-1-i:V_Length-i].__eq__(car)):
                self.isPal = False
                return False
            i=i+1
        return True
    
    def __str__(self):
        isPalindrome = "est"
        if not self.isPal :
            isPalindrome = "n'est pas"
        return f"La valeur '{self.val}' {isPalindrome} un palindrome"        

p1 = Palindrome("010")
p1.isPalindrome()
print(p1)
p2 = Palindrome("0210")
p2.isPalindrome()
print(p2)