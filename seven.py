# 7. Create a list of tuples of first name, last name, and age for your friends and colleagues. 
# If you don't know the age, put in None. Calculate the average age, skipping over any None values. 
# Print out each name, followed by old or young if they are above or below the average age. 

from statistics import mean

ls = [('Kamal','Shrestha',None), ('Sunita','Gurung',30),('Dolma','Sherpa',28),('Tenzin','Thupten',25)]
age = []

for i in ls:
    if i[2] == None:
        continue
    
    else:
        age.append(i[2])
        
average = mean(age)

for i in ls:
    if i[2] != None:
        if int(i[2]) > average:
            print(f"{i[0]} {i[1]} : 'Old'")

        else:
            print(f"{i[0]} {i[1]} : 'Young'")