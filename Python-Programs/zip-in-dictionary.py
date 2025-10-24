emp_id = [101,102,103]
emp_name = ["lokesh","suresh","ramesh"]
emp_info = dict(zip(emp_id,emp_name))

student_id = [1,2,3,4,5]
student_name = ["A","B","C","D"]
student_age = [16,17,18]
# student_info = dict(zip(student_id,student_name))
# print(student_info)

"""overcoming error"""
s1 = dict(zip(student_name,student_age))
print(s1)
s2 = dict(zip(student_id,s1))
print(s2)

#zip_longest in dictionary
from itertools import  zip_longest
emp_ids = [101,102,104]
emp_names = ["lokesh","Ramesh"]
emp1 = dict(zip(emp_ids,emp_names))
print(emp1)
emp2 = dict(zip_longest(emp_id,emp_names))
print(emp2)
emp3 = dict(zip_longest(emp_id,emp_names,fillvalue="Empty"))
print(emp3)

e_id  = [101,102,102]
e_name = ["lokesh","ramesh","suresh"]
e1 = dict(zip(e_id,e_name))
print(e1)

e2 = dict(zip(e_name,e_id))
print(e2)

