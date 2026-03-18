def transform(students,courses,scores):
    final_data=[]
    # create a students lookup
    final_data_students={}
    for student in students:
        final_data_students[student['student_id']]=student['name']

    #create course lookup
    course_dict={}
    for row in courses:
            course_dict[row['course_id']]=row['course_name']

    for row in scores:
         student_id=row['student_id']
         course_id=row['course_id']
         score=row['score']
         student_name=final_data_students[student_id]
         course_name=course_dict[course_id]
         final_data.apppend(
              {
                 'student_name':student_name,
                 'course_name' :course_name,
                 'score':score
              })
         
    return final_data




