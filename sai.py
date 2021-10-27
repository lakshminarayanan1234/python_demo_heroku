import flask
from tkinter import*
def getvals():
    print("Accepted")


root=Tk()
root.geometry("500x300")
Label(root,text="student registration details",font="arial 15 bold").grid(row=0,column=3)

Student_Name=Label(root,text="Student_Name")
College_Name=Label(root,text="College_Name")
Specialistion=Label(root,text="Specialistion")
Degree_Name=Label(root,text="Degree_Name")
Internship_Applied_for=Label(root,text="Internship_Applied_for")
Phone_Nos=Label(root,text="Phone")
Email_ID=Label(root,text="Email_ID")
Location=Label(root,text="Location")
Gender=Label(root,text="Gender")
Notes=Label(root,text="Notes")
Student_Name.grid(row=1,column=2)
College_Name.grid(row=2,column=2)
Specialistion.grid(row=3,column=2)
Degree_Name.grid(row=4,column=2)
Internship_Applied_for.grid(row=5,column=2)
Phone_Nos.grid(row=6,column=2)
Email_ID.grid(row=7,column=2)
Location.grid(row=8,column=2)
Gender.grid(row=9,column=2)
Notes.grid(row=10,column=2)

Student_Namevalue=StringVar
College_Namevalue=StringVar
Speclalistionvalue=StringVar
Degree_Namevalue=StringVar
Internship_Applied_forvalue=StringVar
Phone_Nosvalue=IntVar
Email_IDvalue=StringVar
Locationvalue=StringVar
Gendervalue=StringVar
Notesvalue=StringVar
checkvalue=IntVar


College_Name=Entry(root,textvariable=College_Namevalue)
Specialistion=Entry(root,textvariable=Speclalistionvalue)
Degree_Name=Entry(root,textvariable=Degree_Namevalue)
Internship_Applied_for=Entry(root,textvariable=Internship_Applied_forvalue)
Phone_Nos=Entry(root,textvariable=Phone_Nosvalue)
Email_ID=Entry(root,textvariable=Email_IDvalue)
Location=Entry(root,textvariable=Locationvalue)
Gender=Entry(root,textvariable=Gendervalue)
Notes=Entry(root,textvariable=Notesvalue)
Student_Nameentry=Entry(root,textvariable=Student_Namevalue)

Student_Name.grid(row=1,column=2)
College_Name.grid(row=2,column=3)
Specialistion.grid(row=3,column=3)
Degree_Name.grid(row=4,column=3)
Internship_Applied_for.grid(row=5,column=3)
Phone_Nos.grid(row=6,column=3)
Email_ID.grid(row=7,column=3)
Location.grid(row=8,column=3)
Gender.grid(row=9,column=3)
Notes.grid(row=10,column=3)

checkbtn=Checkbutton(text="remember me ?",variable=checkvalue)
checkbtn.grid(row=  20,column=3)

Button(text="submit",command=getvals).grid(row=25,column=3)
root.mainloop()