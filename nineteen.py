# 19. Write a Python class to find validity of a string of parentheses, '(', ')', '{', '}', '[' and '].
#  These brackets must be close in the correct order, for example "()" and "()[]{}" are valid but "[)", "({[)]" 
# and "{{{" are invalid 

class Parenthesis():

    def __init__(self, a='()',b='{}',c='[]'):
        self.a = a
        self.b = b
        self.c = c

    def check(self,x):
        if self.a in x or self.b in x or self.c in x:
            return "Valid parentheses"
        
        else:
            return "Invalid parentheses"

p = Parenthesis()
print(p.check("()[]{}"))

