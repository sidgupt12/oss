'''this block imports all the necessary modules'''
from tkinter import *
import tkinter.messagebox as tsmg
from tkinter.font import Font
import csv


def edit():
    '''
    Name - edit
    This function is used to edit student's information.
    works on the basis of admission number, asks
    for other specifics and edit its using the nested
    function edit.
    All the values asked are packed inside a new tkinter window
    # CLASS used is Toplevel
    working:
    makes a new popup window and asks for different specifics and edit it as per entries filled
    gives error if no value found
    '''
    def actual_edit():
        '''
        Name - actual_edit
        This function uses the values from edit function and edits them in the csv file.
        working:
        It copies the values from student.csv and copies them to a buffer file except the
        value to be edited and add the edited value while copying to buffer.
        it then overwrite the content from buffer to studen.csv
        '''
        adm=oldadmval.get()
        newrec=[newadmval.get(),fnameval.get(), lnameval.get(), classval.get(), secval.get(), dobval.get()]
        f=open("delete.csv","w")
        f.close()
        fin = open("student.csv", "r")
        fout = open("delete.csv", "a", newline="\n")
        records = csv.reader(fin)
        wrt=csv.writer(fout)
        for i in records:
            if i[0].lower()!=adm.lower():
                wrt.writerow(i)
            else:
                wrt.writerow(newrec)

        fin.close()
        fout.close()
        fin=open("student.csv","w")
        fin.close()
        fin=open("student.csv","a",newline="\n")
        wrt=csv.writer(fin)
        fout=open("delete.csv","r")
        rec=csv.reader(fout)
        for i in rec:
            wrt.writerow(i)
        fin.close()
        fout.close()
        tsmg.showinfo("done!", "Data Succesfully Edited")
        edit_student.destroy()

    edit_student = Toplevel()
    edit_student.geometry("680x280")
    edit_student.maxsize(680,280)
    edit_student.title("EDIT STUDENT")

    f=Frame(edit_student, relief=GROOVE, borderwidth=8, bg="SpringGreen2")
    f.pack(fill="x", side=TOP)
    fcenter = Frame(edit_student)
    fcenter.pack(side=LEFT,fill=Y)
    Label(fcenter, text="                                             ").pack()
    heading_text=Label(f, text="EDIT STUDENT DETAIL", font=heading_font, fg="RoyalBlue1", bg="SpringGreen2")
    f1 = Frame(edit_student)
    f1.pack(fill="y", side="left")
    f2 = Frame(edit_student)
    f2.pack(fill=Y, side=LEFT)
    oldadm = Label(f1, text="1. Old Admission Number")
    oldadm.pack(side="top")
    newadm = Label(f1, text= "2. New Admission Number(*write old if no change)")
    newadm.pack(side="top")
    fname = Label(f1, text= "3. New First Name")
    fname.pack(side="top")
    lname = Label(f1, text= "4. New Last Name")
    lname.pack(side="top")
    nclass = Label(f1, text= "5. New Class")
    nclass.pack(side="top")
    section = Label(f1,  text="6. New Section")
    section.pack(side="top")
    dob = Label(f1, text="7. New DOB")
    dob.pack(side="top")
    oldadmval = StringVar()
    newadmval = StringVar()
    fnameval = StringVar()
    lnameval = StringVar()
    classval = StringVar()
    secval = StringVar()
    dobval = StringVar()

    oldadmentry = Entry(f2, textvariable=oldadmval)
    oldadmentry.pack(side=TOP)
    newadmentry = Entry(f2, textvariable=newadmval)
    newadmentry.pack(side=TOP)
    fnameentry = Entry(f2, textvariable=fnameval)
    fnameentry.pack(side=TOP)
    lnameentry = Entry(f2, textvariable=lnameval)
    lnameentry.pack(side=TOP)
    classentry = Entry(f2, textvariable=classval)
    classentry.pack(side=TOP)
    secentry = Entry(f2, textvariable=secval)
    secentry.pack(side=TOP)
    dobentry = Entry(f2, textvariable=dobval)
    dobentry.pack(side=TOP)

    Button(f2, text="submit", command=actual_edit).pack(pady=15,padx=20)

    heading_text.pack()


def show_allstudents():
    '''
    Name - show_allstudents
    This function is used to show details of all the students in a user friendly
    table format.
    Working:
    It creates five frames in vertical allignment for 5 details of students.
    It then extract a list of details of all students one by one
    and pack one value a frame.
    '''

    show_all = Toplevel()
    show_all.geometry("680x480")
    show_all.title("Student List")
    fin = open('student.csv', 'r')
    data = list(csv.reader(fin))
    heading_frame = Frame(show_all, borderwidth=5, relief=RIDGE, bg="light sea green")
    heading_frame.pack(fill=X)
    headingfont = Font(family="Verdana", size=16, weight="bold", slant="italic", underline=1)
    frame=Frame(show_all)
    frame.pack(side=LEFT, fill=Y, padx=50)
    Label(heading_frame, text="STUDENTS TABLE", font=headingfont).pack()
    frm1 = Frame(show_all, borderwidth=3, relief=GROOVE, bg="cyan")
    frm2 = Frame(show_all, borderwidth=3, relief=GROOVE, bg="cyan")
    frm3 = Frame(show_all, borderwidth=3, relief=GROOVE, bg="cyan")
    frm4 = Frame(show_all, borderwidth=3, relief=GROOVE, bg="cyan")
    frm5 = Frame(show_all, borderwidth=3, relief=GROOVE, bg="cyan")
    frm6 = Frame(show_all, borderwidth=3, relief=GROOVE, bg="cyan")

    frm1.pack(side=LEFT)
    frm2.pack(side=LEFT)
    frm3.pack(side=LEFT)
    frm4.pack(side=LEFT)
    frm5.pack(side=LEFT)
    frm6.pack(side=LEFT)


    Label(frm1, text="Admission number", bg="RoyalBlue1").pack()
    Label(frm2, text="First Name", bg="RoyalBlue1").pack()
    Label(frm3, text="Last Name", bg="RoyalBlue1").pack()
    Label(frm4, text="Class", bg="RoyalBlue1").pack()
    Label(frm5, text="Section", bg="RoyalBlue1").pack()
    Label(frm6, text="DOB", bg="RoyalBlue1").pack(fill=X)

    for r in data:
        Label(frm1, text=f'{r[0]}', bg="cyan").pack()
        Label(frm2, text=f'{r[1]}', bg="cyan").pack()
        Label(frm3, text=f'{r[2]}', bg="cyan").pack()
        Label(frm4, text=f'{r[3]}', bg="cyan").pack()
        Label(frm5, text=f'{r[4]}', bg="cyan").pack()
        Label(frm6, text=f'{r[5]}', bg="cyan").pack()
    fin.close()

def backup():
    '''
    Name - backup
    this function create a backup file of student.csv
    working:
    this function creates a new file named backup.csv in D drive in write mode.
    It then closes that file and open it again in append mode and copies all
    data from student.csv to backup.csv
    '''
    fin = open("student.csv")
    fout = open("Backup.csv", "w", newline="\n")
    fout.close()
    fout = open("Backup.csv", "a", newline="\n")
    wrt = csv.writer(fout)
    records = csv.reader(fin)
    for i in records:
        rec=[i[0], i[1], i[2], i[3], i[4], i[5]]
        wrt.writerow(rec)
    fout.close()
    fin.close()
    tsmg.showinfo("Completed", "A backup is created at backup.csv")

def addstudent():
    '''this function will popup using TopLevel func in tkinter a new window and will take
    student information and saves it in a file named student.csv'''
    def addvalue_to_file():
        with open("student.csv", "a", newline="\n") as fin:
            rec = [admnovalue.get(), fnamevalue.get(),lnamevalue.get(),clsvalue.get(),secvalue.get(),datevalue.get()]
            wrt = csv.writer(fin)
            wrt.writerow(rec)
            tsmg.showinfo('Record Saved', "One Record saved successfully.")
            add_student_root.destroy()

    add_student_root=Toplevel()
    add_student_root.geometry("680x480")
    add_student_root.title("Add Student")
    add_student_root.configure(bg="DarkOliveGreen1")

    add_student_font = Font(family="Verdana", size=20, weight="bold", slant="italic", underline=1)
    heading = Label(add_student_root, text="Enter Student Detail", bg="DarkOliveGreen1", fg="dark violet",
                    font=add_student_font, pady=50)

    label_font = Font(family="Times", size=15, weight="bold", slant="italic")
    admno = Label(add_student_root, text="Admission Number", fg="RoyalBlue1", bg="DarkOliveGreen1", font=label_font)
    fname = Label(add_student_root, text="First name", fg="RoyalBlue1", bg="DarkOliveGreen1", font=label_font)
    lname = Label(add_student_root, text="Last Name", fg="RoyalBlue1", bg="DarkOliveGreen1", font=label_font)
    cls = Label(add_student_root, text="Class(Enter Number)", fg="RoyalBlue1", bg="DarkOliveGreen1", font=label_font)
    sec = Label(add_student_root, text="Section", fg="RoyalBlue1", bg="DarkOliveGreen1", font=label_font)
    date = Label(add_student_root, text="DOB(dd/mm/yy)", fg="RoyalBlue1", bg="DarkOliveGreen1", font=label_font)

    heading.grid(row=0, column=3)
    admno.grid(row=1,column=2)
    fname.grid(row=2, column=2)
    lname.grid(row=3, column=2)
    cls.grid(row=4, column=2)
    sec.grid(row=5, column=2)
    date.grid(row=6, column=2)

    admnovalue = StringVar()
    fnamevalue = StringVar()
    lnamevalue = StringVar()
    clsvalue = StringVar()
    secvalue = StringVar()
    datevalue = StringVar()

    admno_entry = Entry(add_student_root, textvariable=admnovalue)
    fname_entry = Entry(add_student_root, textvariable=fnamevalue)
    lname_entry = Entry(add_student_root, textvariable=lnamevalue)
    cls_entry = Entry(add_student_root, textvariable=clsvalue)
    sec_entry = Entry(add_student_root, textvariable=secvalue)
    date_entry = Entry(add_student_root, textvariable=datevalue)


    admno_entry.grid(row=1,column=3)
    fname_entry.grid(row=2, column=3)
    lname_entry.grid(row=3, column=3)
    cls_entry.grid(row=4, column=3)
    sec_entry.grid(row=5, column=3)
    date_entry.grid(row=6, column=3)

    Button(add_student_root, text="SUBMIT", bg="medium spring green", fg="sea green", command=addvalue_to_file,
           pady=5).grid(row=7, column=3)

def search():
    '''
    Name - search
    This function creates a popup window and ask user to enter admission number.
    Working:
    This function creates a tk window and asks user to input a admission number in the
    given Entry box.
    '''

    def show():
        '''
        Name - show
        This function the actual work of searching a student
        Working:
        This function extract the admission number from search function and
        opens the student.csv file and using for loop searches the record
        with given admission number.
        It then creates a message box showing details of student.
        '''

        with open("student.csv") as fin:
            records = csv.reader(fin)
            rec=None
            for i in records:
                if i[0]==admnoval.get():

                    rec="The record of the student with Admission Number "+str(admnoval.get())+" is\n "+'|'.join([i[0],i[1],i[2],i[3],i[4],i[5]])
                    tsmg.showinfo("record",rec)
                    search_root.destroy()
            if rec==None:
                f = Frame(search_root, bg="red", borderwidth=4, relief=GROOVE)
                tsmg.showerror("Not Found!", "No record with Admission Number " + str(admnoval.get()) + " was found")

                search_root.destroy()
    search_root = Toplevel()
    search_root.geometry("480x180")
    Label(search_root, text = "SEARCH STUDENT", font = heading_font, pady=15).grid(row = 0, column = 3)
    admno = Label(search_root, text = "Enter Admission Number\nof student", padx=9)
    admno.grid(row=3,column=2)
    admnoval = StringVar()
    Entry(search_root, textvariable=admnoval).grid(row=3, column=3)
    Button(search_root, text="SUBMIT", bg="red", fg="cyan",command=show).grid(row=4,column=3)
# function made just to test different parts no use in final code

def delete():
    '''
    Name - delete
    This function asks user for admission number of student whose details has to be deleted.
    Working:
    This function creates a Toplevel window and gives a Entry box to user to enter admission no.
    '''
    def internal_delete():
        '''
        Name - internal_delete
        This function does the actual deletion of the record.
        Working:
        This function extracts the value from the entry box in delete function. It
        then open buffer file in write mode to delete any existing data from it.
        It then opens the buffer file in append mode and student.csv in read and
        using loop it copies the data of all student except of the given admission
        number whose record has to be deleted from student.csv to buffer.
        It then overwrite data from buffer to student.csv
        '''
        fout = open("delete.csv", "w")
        fout.close()
        fin = open("student.csv")
        fout = open("delete.csv", "a", newline="\n")
        records = csv.reader(fin)
        wrt = csv.writer(fout)
        l=[]
        for i in records:
            l.append(i[0])
            if i[0] != admval.get():
                wrt.writerow(i)
        fout.close()
        fin.close()
        fout = open("student.csv", "w")
        fout.close()
        fin = open("delete.csv")
        fout = open("student.csv", "a", newline="\n")
        records = csv.reader(fin)
        wrt = csv.writer(fout)
        for i in records:
                wrt.writerow(i)
        fout.close()
        fin.close()
        if admval.get() in l:
            tsmg.showinfo("record deleted","Record of student with admission number "+str(admval.get())+" was deleted")

            delete_root.destroy()
        else:
            tsmg.showerror("Not Found", "Record of student with admission number "+str(admval.get())+" was not found")

            delete_root.destroy()
    delete_root = Toplevel()
    delete_root.geometry("480x180")
    Label(delete_root, text = "DELETE STUDENT", font = heading_font, pady=15).grid(row = 0, column = 3)
    admno = Label(delete_root, text = "Enter Admission Number\nof student", padx=8)
    admno.grid(row=3,column=2)
    admval = StringVar()
    Entry(delete_root, textvariable=admval).grid(row=3, column=3)
    Button(delete_root, text="SUBMIT", bg="red", fg="cyan",command=internal_delete).grid(row=4,column=3)
    delete_root.mainloop()


# gives choice while deleting should be included in final project
def suredel():
    '''
    Name - suredel
    This function is called during a record deletion for conformation to delete.
    '''
    choice = tsmg.askquestion("DELETE", "are you sure you want to delete \n all you unsaved data will be deleted")
    print(choice)

# thanks us for rating
def rateus():
    '''
    Name - rateus
    This function is called when you click on rate button inside know_root window.
    '''
    tsmg.showinfo("Thanks", "Thanks for rating us.")

# gives info about the creators of this software.

def knowmore():
    '''
    Name - knowmore
    This function creates a new window and and tell about the software and ask user to rate the software.
    Working:
    This function creates a new Tk window and frame 5 radio buttons and a rateus button giving user
    various rating option.
    '''
    know_root = Tk()
    know_root.geometry("480x500")
    know_root.title("about us")
    heading = Frame(know_root, bg="black", borderwidth=14, height=30, relief=RIDGE)
    heading.pack(fill=X, side=TOP)
    headingknow_text = Label(heading, text="ABOUT US", bg="black", fg="white", font="f 14 bold")
    headingknow_text.pack()
    fr = Frame(know_root, bg="white", borderwidth=13, relief=RIDGE)
    fr.pack(side=LEFT, fill=Y)
    about = Label(fr, text="Student information system(SIS) is used to maintain students' records."
                           "\nThis software is to help school maintain its data"
                           "\nmore efficiently and easily without spending more money."

                           , relief=SUNKEN, bg="black", fg="cyan"
                  )
    ty = Label(fr, text='''Thanks for showing\nus support.''', bg="black", fg="white", font="comicsans 10 italic"
               )

    fr.pack()
    about.pack(padx=20, pady=12)
    ty.pack()
    rate = Label(fr, text="support us more by rating us", bg="white", fg="black", font="comicsans 10 bold")
    rate.pack(padx=12)

    var = StringVar()
    var.set("Radio")
    experience = Label(fr, text="HOW WAS YOUR EXPERIENCE WITH US")
    experience.pack()
    Radiobutton(fr, bg="white", text="Excellent", variable=var, value="Excellent", padx=155).pack(anchor="w")
    Radiobutton(fr, bg="white", text="Very Good", variable=var, value="Very Good", padx=155).pack(anchor="w")
    Radiobutton(fr, bg="white", text="Good", variable=var, value="Good", padx=155).pack(anchor="w")
    Radiobutton(fr, bg="white", text="Bad", variable=var, value="Bad", padx=155).pack(anchor="w")
    Radiobutton(fr, bg="white", text="Will never use it again!", variable=var, value="baddest", padx=155).pack(
        anchor="w")
    Button(fr, text="rate us", command=rateus, bg="light green", font="s 10 bold").pack()
    know_root.mainloop()

# Main code starts from here

root = Tk()
root.configure(bg="aquamarine")
# root.configure(bg="white")
root.geometry("1200x700")
root.maxsize(width=1200, height=700)
root.minsize(width=1200, height=700)

root.title("STUDENT INFORMATION SYSTEM")

# relief = SUNKEN , RAISED , GROOVE , RIDGE
f1 = Frame(root, bg="cadet blue", borderwidth=6, relief=GROOVE)
f1.pack(side=TOP, fill=X)


heading_font = Font(family="verdana", size=20, weight="bold", slant="italic", underline=1)
heading_text = Label(f1, text="STUDENT INFORMATION SYSTEM", bg="medium aquamarine", fg="white", font=heading_font)
heading_text.pack()

root.minsize(880, 380)
f2 = Frame(root, bg="slate blue", borderwidth=6, relief=RIDGE)
f2.pack(side=LEFT, anchor="nw", fill=Y)
# root.maxsize(880,380)
img_text = Label(f2, text='Creators', bg="deep pink", fg="snow2", borderwidth=3, relief=RIDGE)
img_text.pack(side=TOP, pady=5)

siddhant_image = PhotoImage(file="founder.png")
siddhant_photo = Label(f2, image=siddhant_image, bg="gold", borderwidth=5, relief=GROOVE)
siddhant_photo.pack()

founder_font = Font(family="Verdana", size=10, weight="bold", slant="italic", underline=1)
siddhant_info = Label(f2, text='Siddhant Gupta', bg="pale violet red", fg="aquamarine", font=founder_font
                      , borderwidth=3, relief=RIDGE)
siddhant_info.pack(pady=9)

shashwat_image = PhotoImage(file="shashwat.png")
shashwat_photo = Label(f2, image=shashwat_image, bg="gold", borderwidth=5, relief=GROOVE)
shashwat_photo.pack(pady=9)

shashwat_info = Label(f2, text='Shashwat Awasthi', bg="pale violet red", fg="aquamarine",
                      font=founder_font
                      , borderwidth=3, relief=RIDGE)
shashwat_info.pack()

f3 = Frame(root, bg="floral white", borderwidth=9, relief=SUNKEN)
f3.pack(side=TOP, fill=X,pady=30)

siddhant_text = Label(f3, text="We're Shashwat Awasthi and Siddhant Gupta and we've created this is project in accordance to board\n"
                               "curriculum. This project is used to add,retrieve,edit,and delete the information of any\n "
                               "student. To know more about this software click on the know more button on the side",
                      bg="midnight blue", fg='navajo white', borderwidth=12,
                      relief=RIDGE, font='italia 11 italic', padx=15, pady=15
                      )

siddhant_text.pack(side=LEFT, fill=X, padx=10, pady=10)

but1 = Button(f3, bg="black", fg="cyan", width=20, height=2, text="know more about us >", command=knowmore)
but1.pack(side=RIGHT, anchor="se")

f5 = Frame(root, bg="thistle", height=40, borderwidth=7, relief=GROOVE)
f5.pack(side=BOTTOM, fill=X)
but6 = Button(f5, text="EXIT", height=2, width=9, bg="magenta", fg="ghost white", command=quit)
but6.pack(side=RIGHT, anchor='se')

p = PhotoImage(file="std1.png")
i = Label(image=p, bg="aquamarine")
i.pack(side=RIGHT)

f4 = Frame(root, bg="medium violet red", borderwidth=9, relief=SUNKEN)
f4.pack(padx=95, pady=50)
but2 = Button(f4, text="PRESS TO\n ADD STUDENT", bg="RoyalBlue3", fg="aquamarine", command=addstudent, width=15, height=3)
but2.pack(side=LEFT, fill=X)

but3 = Button(f4, text="PRESS TO\nDELETE STUDENT", bg="bisque", fg="deep pink", command=delete, width=15, height=3)
but3.pack(side=LEFT, fill=X)

but4 = Button(f4, text="PRESS TO\nSHOW ALL\nSTUDENTS", bg="RoyalBlue3", fg="aquamarine",
              command=show_allstudents, width=15, height=3)
but4.pack(side=LEFT, fill=X)


but5 = Button(f4, text="PRESS TO \nEDIT STUDENT\nDETAILS", bg="bisque", fg="deep pink", command=edit, width=20, height=3)
but5.pack(side=LEFT, fill=X)

f6 = Frame(root, bg="medium violet red", borderwidth=9, relief=SUNKEN)
f6.pack(pady=20,side=TOP, padx=160)

but7=Button(f6, text="PRESS TO\nSEARCH STUDENT", bg="bisque", fg="deep pink", command=search, width=15, height=3)
but8=Button(f6, text="PRESS TO\nCREATE BACKUP\n FILE ", bg="RoyalBlue3", fg="aquamarine", command=backup, width=15, height=3)
but7.pack(side=LEFT,fill=X)
but8.pack()

root.mainloop()
