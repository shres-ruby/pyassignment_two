# 5. Create a tuple with your first name, last name, and age. Create a list, people, and append your tuple 
# to it. Make more tuples with the corresponding information from your friends and append them to the list. 
# Sort the list. When you learn about sort method, you can use the key parameter to sort by any field in the 
# tuple, first name, last name, or age. 

t = ('Ruby', 'Shrestha', 28)

people = []
people.append(t)

a = ('Rishi', 'Ghatani', 30)
b = ('Kavita', 'Shrestha', 26)
c = ('Dibya', 'Shrestha', 29)

for x in a,b,c:
    people.append(x)

print(people)
# Output: [('Ruby', 'Shrestha', 28), ('Rishi', 'Ghatani', 30), ('Kavita', 'Shrestha', 26), ('Dibya', 'Shrestha', 29)]

def firstname(f):

    '''Returns the first name'''

    return f[0]


def lastname(f):

    '''Returns the last name'''

    return f[1]


def age(f):

    '''Returns the age'''

    return f[2]


sortbyfirstname = sorted(people, key=firstname)
sortbylastname = sorted(people, key=lastname)
sortbyage = sorted(people, key=age)

print("List sorted by first name : ", sortbyfirstname)
# List sorted by first name :  [('Dibya', 'Shrestha', 29), ('Kavita', 'Shrestha', 26), 
# ('Rishi', 'Ghatani', 30), ('Ruby', 'Shrestha', 28)]

print("List sorted by last name : ", sortbylastname)
# List sorted by last name :  [('Rishi', 'Ghatani', 30), ('Ruby', 'Shrestha', 28), 
# ('Kavita', 'Shrestha', 26), ('Dibya', 'Shrestha', 29)]

print("List sorted by age : ", sortbyage)
# List sorted by age :  [('Kavita', 'Shrestha', 26), ('Ruby', 'Shrestha', 28), 
# ('Dibya', 'Shrestha', 29), ('Rishi', 'Ghatani', 30)]