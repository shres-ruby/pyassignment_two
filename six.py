# 6. Create a list with the names of friends and colleagues. Search for the 
# name ‘John’ using a for a loop. Print ‘not found’ if you didn't find it. 

li = ['Ruby', 'Rishi', 'Casper', 'Sonam', 'Angel']

for name in li:
    if name == 'John':
        print('Match found')
        break
    
else:
    print('Not found') 