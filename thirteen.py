# 13. Write a function to write a comma-separated value (CSV) file. It should accept a filename and 
# a list of tuples as parameters. The tuples should have a name, address, and age. The file should 
# create a header row followed by a row for each tuple. If the following list of tuples was passed in: 
# [('George', '4312 Abbey Road', 22), ('John', '54 Love Ave', 21)] it should write the following in the file: 
# name,address,age 
# George,4312 Abbey Road,22 
# John,54 Love Ave,21 

def make_csv(fname,tups):

    try:
        f = open(fname, 'w')
        f.write("name,address,age\n")
        for i in tups:
            f.write(i[0])
            f.write(',')
            f.write(i[1])
            f.write(',')
            f.write(str(i[2]))
            f.write("\n")      

    finally:
        f.close()

make_csv("test.txt", [('George', '4312 Abbey Road', 22), ('John', '54 Love Ave', 21)])