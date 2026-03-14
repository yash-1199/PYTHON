#ETL
Training intitute

4-csv

1.students

student_id      studentName     age

2.courses.csv
course_id       course_name

3.enrollment.csv
 student_id     course_id

4.scores.csv

student_id  course_id   score


Requirement:
Manger in the training intitute wants one clean report showing

student_name        course_name     score
   Ravi                 Python          55
   Raju                 Sql             60

#Problems
1.The data is scattered across multiple files
2.No single file shows which student scored what in which course

We are going to solve this problem using python 

1.Read the data from csv files
2.Combine them
3.Genearte a clean output dataset/csv


ETL=Extract,transform and load


students_etl_project
    -data
        students.csv
        enrllment.csv
        scores.csv
        courses.csv
etl
        extract.py
        tranform.py
        load.py
main.py

















