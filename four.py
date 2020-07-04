# 4. Create a list. Append the names of your colleagues and friends to it. Has the id of the list changed? Sort the list.
#  What is the first item on the list? What is the second item on the list? 

x = []
print(id(x))
#The id of the list is 75397419592

for name in ('Rishi', 'Kavita', 'Dibya', 'Esha', 'Tenzin'):
    x.append(name)

print(id(x))
# The id of the list again is 75397419592 so it has not changed.

print(x)
#The list as is in the same order as it was entered

x.sort()
print(x)
# The list is now sorted in ascending order. The first item is 'Dibya' and the second item is 'Esha'