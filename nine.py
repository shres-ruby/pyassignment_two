# 9. Write a binary search function. It should take a sorted sequence and the item it is looking for. 
# It should return the index of the item if found. It should return -1 if the item is not found. 

def search(seq, num):
    seq.sort()
    if num in seq:
        return seq, seq.index(num)

    else:
        return -1

result = search([3,4,1,2,9], 9)   
print(result)