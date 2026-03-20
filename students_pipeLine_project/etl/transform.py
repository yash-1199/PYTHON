def transform(students,courses,scores):
    final_data=[]
    # create a students lookup
    final_data_students={}
    

    for student in students:
        final_data_students[student['student_id']] = student['name']

    #create course lookup
    course_dict={}
    for row in courses:
            course_dict[row['course_id']]=row['course_name']

    for row in scores:
         student_id=row['student_id'] #1
         course_id=row['course_id'] #111

         score=row['score']   #95
         student_name=final_data_students[student_id] #Ravi
         course_name=course_dict[course_id] #python
         final_data.append(
              {
                 'student_name':student_name,
                 'course_name' :course_name,
                 'score':score
              })
         
    return final_data

# [{}]
# #select student_name,course_name,score
# #from scores
# #Join students
# #join courses

# 1,111,95

# 47,108,94

# 47
# Student_47


# [{'student_id':1,'Name':'ravi','age':23},{'student_id':1,'Name':'ravi','age':23}]==students

# {'student_id':1,'Name':'ravi','age':23}=student

# {'1':'Ravi',2:'Raju',3,'Ram'}#final_data_students
# {111:'Pyhhon',222:datascience}#course_dict
# {}

# Ravi   

