# 12. Create a function, is_palindrome, to determine if a supplied word is the 
# same if the letters are reversed. 

def is_palindrome(word):
    
    rev = word[::-1]
    
    if rev == word:
        return "It is a palindrome"
    
    else:
        return "Not palindrome"

result = is_palindrome("mom")
print(result)