# we have built in module to handle csv file
import csv
def read_csv(filepath):
    data=[]
    with open(filepath,'r') as file:
        # it converts row into dict format
        reader=csv.DictReader(file)
        for row in reader:
            data.append(row)
    return data


#print(read_csv('Data\\raw\\students.csv'))

#

