#!/usr/bin/env python
# coding: utf-8

# In[1]:


#Creating the list of students
students = [("John", 18, ["Math", "Science", "English"]),
            ("Sarah", 17, ["History", "Math", "Geography"]),
            ("Alex", 16, ["Science", "French", "Math"]),
            ("Emily", 19, ["English", "Hindi", "Chemistry"]),
            ("Jacob", 18, ["Math", "Physics", "Chemistry"])]


# In[2]:


#Printing the name and age of each student
for student in students:
    print(student[0], student[1])


# In[3]:


#Converting the list into set
unique_subjects = []
for student in students:
    unique_subjects.append(set(student[2]))


# In[4]:


#Print the unique subject
for subjects in unique_subjects:
    print(subjects)


# In[5]:


#Creating the function get_students_by_subject
def get_students_by_subject(subject):
    matching_students = []
    for student in students:
        if subject in student[2]:
            matching_students.append(student)
    return matching_students


# In[6]:


#Testing the get_students_by_subject
matching_students = get_students_by_subject("Math")
for student in matching_students:
    print(student[0], student[1])


# In[ ]:




