# 11. Create a variable, filename. Assuming that it has a three-letter extension, and using slice operations, 
# find the extension. For README.txt, the extension should be txt. Write code using slice operations that will 
# give the name without the extension. Does your code work on filenames of arbitrary length? 

filename = "pythonassignment.doc"

r = filename[-1:-4:-1]
ext = r[::-1]
print(ext) #doc

fn = filename[:len(filename)-4]
print(fn) #pythonassignment

# Since my code takes the total length of the filename into account, it will work on filenames 
# of arbitrary length as well.