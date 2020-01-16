# -*- coding: utf-8 -*-
"""
Created on Wed Jan 15 11:44:16 2020

@author: spiridiv
"""

studentName=(input("Enter Student Name:"))
mathMarks=float(input("Enter Student Math Scores(0-100):"))
physicsMarks=float(input("Enter Student Physics Scores (0-100):"))
chemistryMarks=float(input("Enter Student Chemistry Scores (0-100):"))
#print("Name is %s, Marks are %.2f"%(name,marks))
average=0
grade="Z"
if (mathMarks <= 35 or physicsMarks <= 35 or chemistryMarks <= 35):
    print("Student %s failed!"%(studentName))
else:
    average = (mathMarks+physicsMarks+chemistryMarks)/3
if (average <= 59 and average != 0):
    grade = "C"
elif (average >= 59 and average <= 69 and average != 0):
    grade="B"
elif(average >= 69 and average != 0):
    grade = "A"
   # print("ID: %i, Name: %s, Marks:%.2f"%(studentid,name,marks))
if (grade != "Z"):
    print("Student %s, passed with grade:%s"%(studentName,grade))