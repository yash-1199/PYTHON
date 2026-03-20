from etl.extract import read_csv
from etl.transform import transform
from etl.load import write_csv

students=read_csv('Data\\raw\\students.csv')
courses=read_csv('Data\\raw\\courses.csv')
scores=read_csv('Data\\raw\\scores.csv')

final_data=transform(students,courses,scores)

write_csv(final_data,'Data\\processed_data\\final_report.csv')
#print(final_data)
print('pipeline ran succesfully')

