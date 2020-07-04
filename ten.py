# 10. Write a function that takes camel-cased strings (i.e. ThisIsCamelCased), and converts them 
# to snake case (i.e. this_is_camel_cased). Modify the function by adding an argument, separator, 
# so it will also convert to the kebab case (i.e.this-is-camel-case) as well. 

def converter(string, c):
    x = list(string)
    up = []

    for i in string:
        if i.isupper():
            up.append(i)

    for i in x:
        if i in up[1:]:
            l = x.index(i)
            x[l] = "_"+i
            
    result = (''.join(x)).lower()

    kebab = result.replace("_","-")
        
    return result, kebab

c = converter("ThisIsCamelCased","-")
print(c)