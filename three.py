# # 3. Write code that will print out the anagrams (words that use the same letters) from a paragraph of text. 

text = "When the room suddenly went silent everyone started to listen closely."
l = text.lower()
t = l.split() 
result=[]

for i in t:  
    for j in t[t.index(i)+1:]:
        if sorted(i) == sorted(j):
            result.append([i,j])

print(result)