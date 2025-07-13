from tkinter import *
from tkinter import ttk
from tkinter import StringVar
from PIL import Image, ImageTk
from tkinter import messagebox
import mysql.connector
import cv2
import pyttsx3
import threading

class Student:
    # Initialize the text-to-speech engine
    engine = pyttsx3.init()

# Function to convert text to speech
    def speak(self,text):
        # Run the speech in a separate thread to avoid blocking the GUI
        threading.Thread(target=lambda: (self.engine.say(text), self.engine.runAndWait())).start()
    def __init__(self,root):
        self.root=root
        self.root.geometry("1530x800+0+0")
        self.root.title("Face Recognition System")
        
        #variables
        self.var_dep=StringVar()
        self.var_course=StringVar()
        self.var_year=StringVar()
        self.var_sem=StringVar()
        self.var_std_id=StringVar()
        self.var_std_name=StringVar()
        self.var_div=StringVar()
        self.var_roll=StringVar()
        self.var_gender=StringVar()
        self.var_dob=StringVar()
        self.var_email=StringVar()
        self.var_phone=StringVar()
        self.var_address=StringVar()
        self.var_teacher=StringVar()
        self.var_photo=StringVar()
       
        
        #image1
        img=Image.open(r"C:\s_a_m\UI\rear-view-programmer-working-all-night-long.jpg")
        img=img.resize((1530,130),Image.Resampling(Image.BICUBIC))
        self.photoimg=ImageTk.PhotoImage(img)

        f_lbl=Label(self.root,image=self.photoimg)
        f_lbl.place(x=0,y=0,width=1530,height=130)
        # #image2
        # img1=Image.open(r"C:\s_a_m\2023-08-28.png")
        # img1=img1.resize((500,130),Image.Resampling(Image.BICUBIC))
        # self.photoimg1=ImageTk.PhotoImage(img1)

        # f_lbl=Label(self.root,image=self.photoimg1)
        # f_lbl.place(x=500,y=0,width=500,height=130)
        # #image3
        # img2=Image.open(r"C:\s_a_m\2023-08-28.png")
        # img2=img2.resize((500,130),Image.Resampling(Image.BICUBIC))
        # self.photoimg2=ImageTk.PhotoImage(img2)

        # f_lbl=Label(self.root,image=self.photoimg2)
        # f_lbl.place(x=1000,y=0,width=500,height=130)
        
        
        #bg image
        img3=Image.open(r"C:\s_a_m\UI\_train_data_img.jpg")
        img3=img3.resize((1530,710),Image.Resampling(Image.BICUBIC))
        self.photoimg3=ImageTk.PhotoImage(img3)

        bg_img=Label(self.root,image=self.photoimg3)
        bg_img.place(x=0,y=130,width=1530,height=710)
        
        title_lbl=Label(bg_img,text="Student Management System",font=("times new roman",35,"bold"),bg="white",fg="darkblue")
        title_lbl.place(x=0,y=0,width=1530,height=45)
        #main frame
        main_frame=Frame(bg_img,bd=2,bg="white")
        main_frame.place(x=20,y=55,width=1480,height=600)
        #left frame
        left_frame=LabelFrame(main_frame,bd=2,bg="white",relief=RIDGE,text="Student Details",font=("times new roman",12,"bold"))
        left_frame.place(x=10,y=10,width=740,height=580)
        #image left
        img_left=Image.open(r"C:\s_a_m\UI\programming-background-with-person-working-with-codes-computer.jpg")
        img_left=img_left.resize((720,130),Image.Resampling(Image.BICUBIC))
        self.photoimg_left=ImageTk.PhotoImage(img_left)
        #image lable left frame
        f_lbl=Label(left_frame,image=self.photoimg_left)
        f_lbl.place(x=5,y=0,width=720,height=130)
        #current course information
        current_course=LabelFrame(left_frame,bd=2,bg="white",relief=RIDGE,text="Current Course Information",font=("times new roman",12,"bold"))
        current_course.place(x=5,y=135,width=720,height=110)
        #department
        dep_label=Label(current_course,text="Department",font=("times new roman",13,"bold"),bg="white")
        dep_label.grid(row=0,column=0,padx=10,pady=5)
        dep_combo=ttk.Combobox(current_course,textvariable=self.var_dep,font=("times new roman",12,"bold"),state="readonly",width=20)
        dep_combo.grid(row=0,column=1,padx=2,pady=10,sticky=W)
        dep_combo["values"]=("Select Department","Computer Science","IT","Civil","Mechanical")
        dep_combo.current(0)
        #course
        course_label=Label(current_course,text="Course",font=("times new roman",13,"bold"),bg="white")
        course_label.grid(row=0,column=2,padx=10,pady=5)
        course_combo=ttk.Combobox(current_course,textvariable=self.var_course,font=("times new roman",12,"bold"),state="readonly",width=20)
        course_combo.grid(row=0,column=3,padx=2,pady=10,sticky=W)
        course_combo["values"]=("Select Course","B.Tech","M.Tech","BBA","MBA")
        course_combo.current(0)
        #year
        year_label=Label(current_course,text="Year",font=("times new roman",13,"bold"),bg="white")
        year_label.grid(row=1,column=0,padx=10,pady=5)
        year_combo=ttk.Combobox(current_course,textvariable=self.var_year,font=("times new roman",12,"bold"),state="readonly",width=20)
        year_combo.grid(row=1,column=1,padx=2,pady=10,sticky=W)
        year_combo["values"]=("Select Year","2020-2021","2021-2022","2022-2023","2023-2024")
        year_combo.current(0)
        #semester
        semester_label=Label(current_course,text="Semester",font=("times new roman",13,"bold"),bg="white")
        semester_label.grid(row=1,column=2,padx=10,pady=5)
        semester_combo=ttk.Combobox(current_course,textvariable=self.var_sem,font=("times new roman",12,"bold"),state="readonly",width=20)
        semester_combo.grid(row=1,column=3,padx=2,pady=10,sticky=W)
        semester_combo["values"]=("Select Semester","Semester-1","Semester-2","Semester-3","Semester-4","Semester-5","Semester-6","Semester-7","Semester-8")
        semester_combo.current(0)
        
        #class student information
        class_Student=LabelFrame(left_frame,bd=2,bg="white",relief=RIDGE,text="Class Student Information",font=("times new roman",12,"bold"))
        class_Student.place(x=5,y=250,width=720,height=300)
        #studentId
        studentId_label=Label(class_Student,text="StudentID:",font=("times new roman",13,"bold"),bg="white")
        studentId_label.grid(row=0,column=0,padx=10,pady=5,sticky=W)
        studentId_entry=ttk.Entry(class_Student,textvariable=self.var_std_id,width=20,font=("times new roman",13,"bold"))
        studentId_entry.grid(row=0,column=1,padx=10,pady=5,sticky=W)
        #studentName
        studentName_label=Label(class_Student,text="StudentName:",font=("times new roman",13,"bold"),bg="white")
        studentName_label.grid(row=0,column=2,padx=10,pady=5,sticky=W)
        studentName_entry=ttk.Entry(class_Student,textvariable=self.var_std_name,width=20,font=("times new roman",13,"bold"))
        studentName_entry.grid(row=0,column=3,padx=10,pady=5,sticky=W)
        #class division
        class_div_label=Label(class_Student,text="Class Division:",font=("times new roman",13,"bold"),bg="white")
        class_div_label.grid(row=1,column=0,padx=10,pady=5,sticky=W)
        class_div_entry=ttk.Entry(class_Student,textvariable=self.var_div,width=20,font=("times new roman",13,"bold"))
        class_div_entry.grid(row=1,column=1,padx=10,pady=5,sticky=W)
        #roll no
        class_roll_label=Label(class_Student,text="Roll No:",font=("times new roman",13,"bold"),bg="white")
        class_roll_label.grid(row=1,column=2,padx=10,pady=5,sticky=W)
        class_roll_entry=ttk.Entry(class_Student,textvariable=self.var_roll,width=20,font=("times new roman",13,"bold"))
        class_roll_entry.grid(row=1,column=3,padx=10,pady=5,sticky=W)
        #gender
        studentGender_label=Label(class_Student,text="Gender:",font=("times new roman",13,"bold"),bg="white")
        studentGender_label.grid(row=2,column=0,padx=10,pady=5,sticky=W)
       
        studentGender=ttk.Combobox(class_Student,textvariable=self.var_gender,width=15,font=("times new roman",13,"bold"))
        studentGender["values"]=("Select Gender","Male","Female","Other")
        studentGender.current(0)
        studentGender.grid(row=2,column=1,padx=10,pady=5,sticky=W)
        #date of birth
        dob_label=Label(class_Student,text="DOB:",font=("times new roman",13,"bold"),bg="white")
        dob_label.grid(row=2,column=2,padx=10,pady=5,sticky=W)
        dob_entry=ttk.Entry(class_Student,width=20,textvariable=self.var_dob,font=("times new roman",13,"bold"))
        dob_entry.grid(row=2,column=3,padx=10,pady=5,sticky=W)
        #email
        studentEmail_label=Label(class_Student,text="Email:",font=("times new roman",13,"bold"),bg="white")
        studentEmail_label.grid(row=6,column=0,padx=10,pady=5,sticky=W)
        studentEmail_entry=ttk.Entry(class_Student,textvariable=self.var_email,width=20,font=("times new roman",13,"bold"))
        studentEmail_entry.grid(row=6,column=1,padx=10,pady=5,sticky=W)
        #phone
        phone_label=Label(class_Student,text="Phone:",font=("times new roman",13,"bold"),bg="white")
        phone_label.grid(row=6,column=2,padx=10,pady=5,sticky=W)
        phone_entry=ttk.Entry(class_Student,textvariable=self.var_phone,width=20,font=("times new roman",13,"bold"))
        phone_entry.grid(row=6,column=3,padx=10,pady=5,sticky=W)
        #address
        address_label=Label(class_Student,text="Address:",font=("times new roman",13,"bold"),bg="white")
        address_label.grid(row=7,column=0,padx=10,pady=5,sticky=W)
        address_entry=ttk.Entry(class_Student,textvariable=self.var_address,width=20,font=("times new roman",13,"bold"))
        address_entry.grid(row=7,column=1,padx=10,pady=5,sticky=W)
        #teacher
        teacher_label=Label(class_Student,text="Teacher Name:",font=("times new roman",13,"bold"),bg="white")
        teacher_label.grid(row=7,column=2,padx=10,pady=5,sticky=W)
        teacher_entry=ttk.Entry(class_Student,textvariable=self.var_teacher,width=20,font=("times new roman",13,"bold"))
        teacher_entry.grid(row=7,column=3,padx=10,pady=5,sticky=W)
        #radio buttons
        self.var_radio1=StringVar()
        radio_btn1=ttk.Radiobutton(class_Student,variable=self.var_radio1,text="Take Photo Sample",value="yes")
        radio_btn1.grid(row=8,column=0)
        
        radio_btn2=ttk.Radiobutton(class_Student,variable=self.var_radio1,text="No Photo Sample",value="no")
        radio_btn2.grid(row=8,column=1)
        
        #button frame
        btn_frame=Frame(class_Student,bd=2,relief=RIDGE,bg="white")
        btn_frame.place(x=0,y=200,width=715,height=35)
        
        save_btn=Button(btn_frame,text="Save",command=self.add_data,width=15,font=("times new roman",13,"bold"),bg="blue",fg="white")
        save_btn.grid(row=0,column=0)
        
        update_btn=Button(btn_frame,text="Update",command=self.update_data,width=15,font=("times new roman",13,"bold"),bg="blue",fg="white")
        update_btn.grid(row=0,column=1)
        
        delete_btn=Button(btn_frame,text="Delete",command=self.delete_data,width=15,font=("times new roman",13,"bold"),bg="blue",fg="white")
        delete_btn.grid(row=0,column=2)
        
        reset_btn=Button(btn_frame,text="Reset",command=self.reset_data,width=15,font=("times new roman",13,"bold"),bg="blue",fg="white")
        reset_btn.grid(row=0,column=3)
        
        btn_frame1=Frame(class_Student,bd=2,relief=RIDGE,bg="white")
        btn_frame1.place(x=0,y=235,width=715,height=35)
        
        take_photo_btn=Button(btn_frame1,text="Take Photo Sample",command=self.generate_dataset,width=39,font=("times new roman",13,"bold"),bg="blue",fg="white")
        take_photo_btn.grid(row=0,column=0)
        
        update_photo_btn=Button(btn_frame1,text="Update Photo Sample",width=39,font=("times new roman",13,"bold"),bg="blue",fg="white")
        update_photo_btn.grid(row=0,column=1)
        
        #right frame
        right_frame=LabelFrame(main_frame,bd=2,bg="white",relief=RIDGE,text="Student Details",font=("times new roman",12,"bold"))
        right_frame.place(x=760,y=10,width=700,height=580)
        img_right=Image.open(r"C:\s_a_m\UI\programming-background-with-person-working-with-codes-computer.jpg")
        img_right=img_right.resize((700,130),Image.Resampling(Image.BICUBIC))
        self.photoimg_right=ImageTk.PhotoImage(img_right)
        
        f_lbl=Label(right_frame,image=self.photoimg_right)
        f_lbl.place(x=5,y=0,width=700,height=130)
        
        #search frame
        Search_frame=LabelFrame(right_frame,bd=2,bg="white",relief=RIDGE,text="Search Student",font=("times new roman",12,"bold"))
        Search_frame.place(x=5,y=135,width=690,height=70)
        
        search_label=Label(Search_frame,text="Search By",font=("times new roman",15,"bold"),bg="white")
        search_label.grid(row=0,column=0,padx=10,pady=5)
        
        self.search_combo=ttk.Combobox(Search_frame,font=("times new roman",13,"bold"),state="readonly")
        self.search_combo["values"]=("Select","Roll No","Phone_No")
        self.search_combo.current(0)
        self.search_combo.grid(row=0,column=1,padx=2,pady=10,sticky=W)
        
        self.search_entry=ttk.Entry(Search_frame,width=15,font=("times new roman",13,"bold"))
        self.search_entry.grid(row=0,column=2,padx=10,pady=5)
        
        
        search_btn=Button(Search_frame,command=self.search_data,text="Search",width=6,font=("times new roman",13,"bold"),bg="blue",fg="white")
        search_btn.grid(row=0,column=3,padx=4)
        showAll_btn=Button(Search_frame,command=self.fetch_data,text="Show All",width=6,font=("times new roman",13,"bold"),bg="blue",fg="white")
        showAll_btn.grid(row=0,column=4,padx=4)
        
        table_frame=Frame(right_frame,bd=2,bg="white",relief=RIDGE)
        table_frame.place(x=5,y=210,width=690,height=340)
        
        scroll_x=ttk.Scrollbar(table_frame,orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(table_frame,orient=VERTICAL)
        
        self.student_table=ttk.Treeview(table_frame,columns=("dep","course","year","sem","id","name","div","roll","dob","email","phone","address","teacher","photo"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)
        scroll_x.config(command=self.student_table.xview)
        scroll_y.config(command=self.student_table.yview)
        
        self.student_table.heading("dep",text="Department")
        self.student_table.heading("course",text="Course")
        self.student_table.heading("year",text="Year")
        self.student_table.heading("sem",text="Semester")
        self.student_table.heading("id",text="StudentID")
        self.student_table.heading("name",text="Name")
        self.student_table.heading("div",text="DIVISION")
        self.student_table.heading("roll",text="ROLL")
        self.student_table.heading("dob",text="DOB")
        self.student_table.heading("email",text="Email")
        self.student_table.heading("phone",text="Phone")
        self.student_table.heading("address",text="Address")
        self.student_table.heading("teacher",text="Teacher")
        self.student_table.heading("photo",text="PhotoSampleStatus")
        self.student_table["show"]="headings"
        
        self.student_table.column("dep",width=100)
        self.student_table.column("course",width=100)
        self.student_table.column("year",width=100)
        self.student_table.column("sem",width=100)
        self.student_table.column("id",width=100)  
        self.student_table.column("name",width=100)
        self.student_table.column("div",width=100)
        self.student_table.column("roll",width=100)
        self.student_table.column("dob",width=100)
        self.student_table.column("email",width=100)
        self.student_table.column("phone",width=100)
        self.student_table.column("address",width=100)
        self.student_table.column("teacher",width=100)
        self.student_table.column("photo",width=100)
        
        
        self.student_table.pack(fill=BOTH,expand=1)
        self.student_table.bind("<ButtonRelease-1>",self.get_cursor)
        self.fetch_data()
        
    #function declaration
    def add_data(self):
        if self.var_dep.get()=="" or self.var_std_name.get()=="":
            self.speak("All fields are required.")
            messagebox.showerror("Error","All fields are required",parent=self.root)
            
        else:
            try:
                conn=mysql.connector.connect()#datbase connection
                my_cursor=conn.cursor()
                my_cursor.execute("insert into student values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(
                                                                                                self.var_dep.get(),
                                                                                                self.var_course.get(),
                                                                                                self.var_year.get(),
                                                                                                self.var_sem.get(),
                                                                                                self.var_std_id.get(),
                                                                                                self.var_std_name.get(),
                                                                                                self.var_div.get(),
                                                                                                self.var_roll.get(),
                                                                                                self.var_gender.get(),
                                                                                                self.var_dob.get(),
                                                                                                self.var_email.get(),
                                                                                                self.var_phone.get(),
                                                                                                self.var_address.get(),
                                                                                                self.var_teacher.get(),
                                                                                                self.var_radio1.get()
                                                                                                ))
                conn.commit()
                self.fetch_data()
                conn.close()
                self.speak("Student details have been added successfully.")
                messagebox.showinfo("Success","Student details has been added successfully",parent=self.root)
                
            except Exception as es:
                self.speak(f"Error occurred. {str(es)}")
                messagebox.showerror("Error",f"Due To:{str(es)}",parent=self.root)
                
                
    #fetch data
    def fetch_data(self):
        conn=mysql.connector.connect(host="localhost",username="root",password="aryan1525@",database="face_recoginizer")
        my_cursor=conn.cursor()
        my_cursor.execute("select * from student")
        data=my_cursor.fetchall()
        if len(data)!=0:
            self.student_table.delete(*self.student_table.get_children())
            for i in data:
                self.student_table.insert("",END,values=i)
            conn.commit()
        conn.close()            
                

    #get cursor
    def get_cursor(self,event=""):
        cursor_focus=self.student_table.focus()
        content=self.student_table.item(cursor_focus)
        data=content["values"]
        self.var_dep.set(data[0])
        self.var_course.set(data[1])
        self.var_year.set(data[2])
        self.var_sem.set(data[3])
        self.var_std_id.set(data[4])
        self.var_std_name.set(data[5])
        self.var_div.set(data[6])
        self.var_roll.set(data[7])
        self.var_gender.set(data[8])
        self.var_dob.set(data[9])
        self.var_email.set(data[10])
        self.var_phone.set(data[11])
        self.var_address.set(data[12])
        self.var_teacher.set(data[13])
        self.var_radio1.set(data[14]) 
    
    def update_data(self):
        if self.var_dep.get()=="" or self.var_std_name.get()=="":
            self.speak("Error All fields are required.")
            messagebox.showerror("Error","All fields are required",parent=self.root)
        else:
            try:
                Update=messagebox.askyesno("Update","Do you want to update this student details",parent=self.root)
                if Update>0:
                    conn=mysql.connector.connect()#datbase connection
                    my_cursor=conn.cursor()
                    my_cursor.execute("update student set Dep=%s,course=%s,Year=%s,Semester=%s,Name=%s,Division=%s,Roll=%s,Gender=%s,Dob=%s,Email=%s,Phone=%s,Addresss=%s,Teacher=%s,PhotoSample=%s where Student_id=%s",(
                        
                                                                                                                                                                                                          self.var_dep.get(),
                                                                                                                                                                                                          self.var_course.get(),
                                                                                                                                                                                                          self.var_year.get(),
                                                                                                                                                                                                          self.var_sem.get(),
                                                                                                                                                                                                          self.var_std_name.get(),
                                                                                                                                                                                                          self.var_div.get(),
                                                                                                                                                                                                          self.var_roll.get(),
                                                                                                                                                                                                          self.var_gender.get(),
                                                                                                                                                                                                          self.var_dob.get(),
                                                                                                                                                                                                          self.var_email.get(),
                                                                                                                                                                                                          self.var_phone.get(),
                                                                                                                                                                                                          self.var_address.get(),
                                                                                                                                                                                                          self.var_teacher.get(),
                                                                                                                                                                                                          self.var_radio1.get(),
                                                                                                                                                                                                          self.var_std_id.get()
                    ))
                else:
                    if not Update:
                        return
                self.speak("Student details have been added successfully.") 
                messagebox.showinfo("Success","Student details has been updated successfully",parent=self.root)
                conn.commit()
                self.fetch_data()
                conn.close()
            except Exception as es:
                self.speak("Error due to: "+str(es))
                messagebox.showerror("Error",f"Due To:{str(es)}",parent=self.root) 
    
    #delete
    def delete_data(self):
        if self.var_std_id.get()=="":
            self.speak("Error student id must be required.")
            messagebox.showerror("Error","Student id must be required",parent=self.root)
        else:
            try:
                delete=messagebox.askyesno("Student Delete Page","Do you want to delete this student detail?",parent=self.root)
                if delete>0:
                    conn=mysql.connector.connect()#datbase connection
                    my_cursor=conn.cursor()
                    sql="delete from student where Student_Id=%s"
                    val=(self.var_std_id.get(),)
                    my_cursor.execute(sql,val)
                else:
                    if not delete:
                        return
                self.speak("Successfully deleted student detail.")
                messagebox.showinfo("Delete","Successfully deleted student detail",parent=self.root)
                conn.commit()
                self.fetch_data()
                conn.close()
                
            except Exception as es:
                self.speak("Error due to: "+str(es))
                messagebox.showerror("Error",f"Due To:{str(es)}",parent=self.root)    
                
    #Reset
    def reset_data(self):
        self.var_dep.set("Select Department")
        self.var_course.set("Select Course")
        self.var_year.set("Select Year")
        self.var_sem.set("Select Semester")
        self.var_std_id.set("")
        self.var_std_name.set("")
        self.var_div.set("")
        self.var_roll.set("")
        self.var_gender.set("")
        self.var_dob.set("")
        self.var_email.set("")
        self.var_phone.set("")
        self.var_address.set("")
        self.var_teacher.set("")
        self.var_radio1.set("")
    

    def search_data(self):
        search_by = self.search_combo.get()  # Get search type (Roll No or Phone_No)
        search_value = self.search_entry.get()  # Get user input

        # Map dropdown values to actual database column names
        column_mapping = {
            "Roll No": "roll",      # Make sure this matches the actual DB column
            "Phone_No": "phone"     # Check if it's 'phone' or something else in DB
        }
        search_column = column_mapping.get(search_by)

        if search_column and search_value:
            try:
                conn=mysql.connector.connect()#datbase connection
                my_cursor = conn.cursor()

                # Use parameterized query to prevent SQL injection
                query = f"SELECT * FROM student WHERE `{search_column}` = %s"
                my_cursor.execute(query, (search_value,))

                rows = my_cursor.fetchall()
                if len(rows) != 0:
                    self.student_table.delete(*self.student_table.get_children())  # Clear table
                    for row in rows:
                        self.student_table.insert("", "end", values=row)  # Insert matching data
                    conn.commit()
                else:
                    messagebox.showinfo("Not Found", "No student found with the given details.")

                self.speak("Search successful.")
                conn.close()
            except mysql.connector.Error as err:
                self.speak("Database Error: " + str(err))
                messagebox.showerror("Database Error", f"Error: {err}")
        else:
            messagebox.showwarning("Input Error", "Please select a search type and enter a value.")

        
    
    #generate dataset take photo sample  
    def generate_dataset(self):
        if self.var_dep.get()=="" or self.var_std_name.get()=="" or self.var_std_id.get()=="":
            self.speak("All fields are required.")
            messagebox.showerror("Error","All fields are required",parent=self.root)
        else:
            try:
                conn=mysql.connector.connect()#datbase connection
                my_cursor=conn.cursor()
                my_cursor.execute("select * from student")
                myresult=my_cursor.fetchall()
                id=0
                for x in myresult:
                    id+=1
                my_cursor.execute("update student set Dep=%s,course=%s,Year=%s,Semester=%s,Name=%s,Division=%s,Roll=%s,Gender=%s,Dob=%s,Email=%s,Phone=%s,Addresss=%s,Teacher=%s,PhotoSample=%s where Student_id=%s",(
                        
                                                                                                                                                                                                          self.var_dep.get(),
                                                                                                                                                                                                          self.var_course.get(),
                                                                                                                                                                                                          self.var_year.get(),
                                                                                                                                                                                                          self.var_sem.get(),
                                                                                                                                                                                                          self.var_std_name.get(),
                                                                                                                                                                                                          self.var_div.get(),
                                                                                                                                                                                                          self.var_roll.get(),
                                                                                                                                                                                                          self.var_gender.get(),
                                                                                                                                                                                                          self.var_dob.get(),
                                                                                                                                                                                                          self.var_email.get(),
                                                                                                                                                                                                          self.var_phone.get(),
                                                                                                                                                                                                          self.var_address.get(),
                                                                                                                                                                                                          self.var_teacher.get(),
                                                                                                                                                                                                          self.var_radio1.get(),
                                                                                                                                                                                                          self.var_std_id.get()==id+1
                ))
                conn.commit()
                self.fetch_data()
                self.reset_data()
                conn.close()
                
                #load predefined data on face frontals from opencv
                face_classifier=cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
                def face_cropped(img):
                    gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
                    faces=face_classifier.detectMultiScale(gray,1.3,5)
                    #scaling factor=1.3
                    #minimum neighbor=5
                    for(x,y,w,h) in faces:
                        face_cropped=img[y:y+h,x:x+w]
                        return face_cropped
                    
                cap=cv2.VideoCapture(0)
                img_id=0
                while True:
                    ret,my_frame=cap.read()
                    if face_cropped(my_frame) is not None:
                        img_id=img_id+1
                        face=cv2.resize(face_cropped(my_frame),(450,450))
                        face=cv2.cvtColor(face,cv2.COLOR_BGR2GRAY)
                        file_name_path="Data/user."+str(id)+"."+str(img_id)+".jpg"
                        cv2.imwrite(file_name_path,face)
                        cv2.putText(face,str(img_id),(50,50),cv2.FONT_HERSHEY_COMPLEX,1,(0,255,0),2)
                        cv2.imshow("face cropped",face)
                    if cv2.waitKey(1)==13 or img_id>=100:
                        break
                cap.release()
                cv2.destroyAllWindows()
                self.speak("Generating data sets completed!!!")
                messagebox.showinfo("Result","Generating data sets completed!!!")
            except Exception as es:
                self.speak("Error due to: "+str(es))
                messagebox.showerror("Error",f"Due To:{str(es)}",parent=self.root)
            

if __name__ == "__main__":
    root = Tk()
    obj = Student(root)
    obj.speak("Welcome to Student details")
    root.mainloop()