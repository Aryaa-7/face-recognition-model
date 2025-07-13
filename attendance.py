from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
import mysql.connector
import cv2
import os
import csv
from tkinter import filedialog
from tkinter import StringVar 

my_data=[]
class Attendance:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face Recognition System")
        
        #variables
        self.var_atten_id= StringVar()
        self.var_atten_roll= StringVar()
        self.var_atten_name= StringVar()
        self.var_atten_dep= StringVar()
        self.var_atten_time= StringVar()
        self.var_atten_date= StringVar()
        self.var_atten_attendance= StringVar()
         
         
        #image1
        img=Image.open(r"C:\s_a_m\UI\Screenshot 2025-04-17 193405.png")
        img=img.resize((1530,130),Image.Resampling(Image.BICUBIC))
        self.photoimg=ImageTk.PhotoImage(img)

        f_lbl=Label(self.root,image=self.photoimg)
        f_lbl.place(x=0,y=0,width=1530,height=130)
        #image2
        #img1=Image.open(r"C:\s_a_m\2023-08-28.png")
        # img1=img1.resize((500,130),Image.Resampling(Image.BICUBIC))
        # self.photoimg1=ImageTk.PhotoImage(img1)

        # f_lbl=Label(self.root,image=self.photoimg1)
        # f_lbl.place(x=500,y=0,width=500,height=130)
        #  #image3
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
        
        title_lbl=Label(bg_img,text="Attendance",font=("times new roman",35,"bold"),bg="white",fg="darkblue")
        title_lbl.place(x=0,y=0,width=1530,height=45)
        
        #main frame
        main_frame=Frame(bg_img,bd=2,bg="white")
        main_frame.place(x=20,y=55,width=1480,height=600)
        #left frame
        left_frame=LabelFrame(main_frame,bd=2,bg="white",relief=RIDGE,text="Student Attendance Details",font=("times new roman",12,"bold"))
        left_frame.place(x=10,y=10,width=740,height=580)
        #image left
        img_left=Image.open(r"C:\s_a_m\UI\Screenshot 2025-04-17 194137.png")
        img_left=img_left.resize((720,130),Image.Resampling(Image.BICUBIC))
        self.photoimg_left=ImageTk.PhotoImage(img_left)
        #image lable left frame
        f_lbl=Label(left_frame,image=self.photoimg_left)
        f_lbl.place(x=5,y=0,width=720,height=130)
        
        #class student information
        left_inside_frame=LabelFrame(left_frame,bd=2,bg="white",relief=RIDGE,text="Class Student Information",font=("times new roman",12,"bold"))
        left_inside_frame.place(x=5,y=135,width=720,height=400)
        
        #attwndance id
        attendanceId_label=Label(left_inside_frame,text="Attendance ID:",font=("times new roman",12,"bold"),bg="white")
        attendanceId_label.grid(row=0,column=0,padx=10,pady=5)
        attendanceId_entry=ttk.Entry(left_inside_frame, textvariable=self.var_atten_id,width=20,font=("times new roman",12,"bold"))
        attendanceId_entry.grid(row=0,column=1,padx=10,pady=5,sticky=W)
        
        #student name
        studentName_label=Label(left_inside_frame,text="Student Name:",font=("times new roman",12,"bold"),bg="white")
        studentName_label.grid(row=1,column=0,padx=10,pady=5)
        studentName_entry=ttk.Entry(left_inside_frame, textvariable=self.var_atten_name,width=20,font=("times new roman",12,"bold"))
        studentName_entry.grid(row=1,column=1,padx=10,pady=5,sticky=W)
        
        #roll no
        rollNo_label=Label(left_inside_frame,text="Roll No:",font=("times new roman",12,"bold"),bg="white")
        rollNo_label.grid(row=0,column=2,padx=10,pady=5)
        rollNo_entry=ttk.Entry(left_inside_frame, textvariable=self.var_atten_roll,width=20,font=("times new roman",12,"bold"))
        rollNo_entry.grid(row=0,column=3,padx=10,pady=5,sticky=W)
        
        #department
        department_label=Label(left_inside_frame,text="Department:",font=("times new roman",12,"bold"),bg="white")
        department_label.grid(row=1,column=2,padx=10,pady=5)
        department_entry=ttk.Entry(left_inside_frame, textvariable=self.var_atten_dep,width=20,font=("times new roman",12,"bold"))
        department_entry.grid(row=1,column=3,padx=10,pady=5,sticky=W)
        
        #date
        date_label=Label(left_inside_frame,text="Date:",font=("times new roman",12,"bold"),bg="white")
        date_label.grid(row=2,column=2,padx=10,pady=5)
        date_entry=ttk.Entry(left_inside_frame, textvariable=self.var_atten_date,width=20,font=("times new roman",12,"bold"))
        date_entry.grid(row=2,column=3,padx=10,pady=5,sticky=W)
        
        #time
        time_label=Label(left_inside_frame,text="Time:",font=("times new roman",12,"bold"),bg="white")
        time_label.grid(row=2,column=0,padx=10,pady=5)
        time_entry=ttk.Entry(left_inside_frame, textvariable=self.var_atten_time,width=20,font=("times new roman",12,"bold"))
        time_entry.grid(row=2,column=1,padx=10,pady=5,sticky=W)
        
        #attendance status
        attendance_status_label=Label(left_inside_frame,text="Attendance Status:",font=("times new roman",12,"bold"),bg="white")
        attendance_status_label.grid(row=3,column=0,padx=10,pady=5)
        attendance_status_combo=ttk.Combobox(left_inside_frame, textvariable=self.var_atten_attendance,width=20,font=("times new roman",12,"bold"),state="readonly")
        attendance_status_combo.grid(row=3,column=1,padx=10,pady=5,sticky=W)
        attendance_status_combo["values"]=("Select","Present","Absent")
        attendance_status_combo.current(0)
        
        #button frame
        btn_frame=Frame(left_inside_frame,bd=2,bg="white",relief=RIDGE)
        btn_frame.place(x=0,y=300,width=715,height=35)
        
        exit_frame=Frame(left_inside_frame,bd=2,bg="white",relief=RIDGE)
        exit_frame.place(x=300,y=340,width=100,height=35)
        
        
        import_btn=Button(btn_frame,text="Import CSV",command=self.import_csv,width=17,font=("times new roman",12,"bold"),bg="darkblue",fg="white")
        import_btn.grid(row=0,column=0,padx=10,pady=5)
        
        export_btn=Button(btn_frame,text="Export CSV",command=self.export_csv,width=17,font=("times new roman",12,"bold"),bg="darkblue",fg="white")
        export_btn.grid(row=0,column=1,padx=10,pady=5)
        
        update_btn=Button(btn_frame,text="Update",width=17,font=("times new roman",12,"bold"),bg="darkblue",fg="white")
        update_btn.grid(row=0,column=2,padx=10,pady=5)
        
        reset_btn=Button(btn_frame,text="Reset", command=self.reset_data,width=17,font=("times new roman",12,"bold"),bg="darkblue",fg="white")
        reset_btn.grid(row=0,column=3,padx=10,pady=5)
        
        exit_btn=Button(exit_frame,text="Exit",command=self.exit,width=17,font=("times new roman",12,"bold"),bg="darkblue",fg="white")
        exit_btn.place(x=0,y=0,width=100,height=35)
       
        
        #right frame
        right_frame=LabelFrame(main_frame,bd=2,bg="white",relief=RIDGE,text="Student Attendance Details",font=("times new roman",12,"bold"))
        right_frame.place(x=760,y=10,width=700,height=580)
        img_right=Image.open(r"C:\s_a_m\UI\Screenshot 2025-04-17 194137.png")
        img_right=img_right.resize((700,130),Image.Resampling(Image.BICUBIC))
        self.photoimg_right=ImageTk.PhotoImage(img_right)
        
        f_lbl=Label(right_frame,image=self.photoimg_right)
        f_lbl.place(x=5,y=0,width=700,height=130)
        
        table_frame=Frame(right_frame,bd=2,bg="white",relief=RIDGE)
        table_frame.place(x=5,y=131,width=700,height=420)
        
        scroll_x=ttk.Scrollbar(table_frame,orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(table_frame,orient=VERTICAL)
        
        self.attendance_report=ttk.Treeview(table_frame,column=("id","roll","name","department","date","time","status"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)
        
        scroll_x.config(command=self.attendance_report.xview)
        scroll_y.config(command=self.attendance_report.yview)
        
        self.attendance_report.heading("id",text="Attendance ID")
        self.attendance_report.heading("roll",text="Roll No")
        self.attendance_report.heading("name",text="Name")
        self.attendance_report.heading("department",text="Department")
        self.attendance_report.heading("date",text="Date")
        self.attendance_report.heading("time",text="Time")
        self.attendance_report.heading("status",text="Status")
        
        self.attendance_report["show"]="headings"
        
        self.attendance_report.column("id",width=100)
        self.attendance_report.column("roll",width=100)
        self.attendance_report.column("name",width=100)
        self.attendance_report.column("department",width=100)
        self.attendance_report.column("date",width=100)
        self.attendance_report.column("time",width=100)
        self.attendance_report.column("status",width=100)
        
        self.attendance_report.pack(fill=BOTH,expand=1)
        self.attendance_report.bind("<ButtonRelease>",self.get_cursor)
        
    #Fetch data
    def fetch_data(self,rows):
        self.attendance_report.delete(*self.attendance_report.get_children())
        for i in rows:
            self.attendance_report.insert("",END,values=i)
            
    #Fetch Data
    def import_csv(self):
        global my_data
        my_data.clear()
        fin=filedialog.askopenfilename(initialdir=os.getcwd(),title="Open CSV",filetypes=(("CSV File","*.csv"),("All File","*.*")),parent=self.root)
        with open(fin) as csvfile:
            csvread=csv.reader(csvfile,delimiter=",")
            for i in csvread:
                my_data.append(i)
            self.fetch_data(my_data)    
        
    def export_csv(self):
        try:
            if len(my_data)<1:
                messagebox.showerror("Error","No data found",parent=self.root)
                return False
            export_file=filedialog.asksaveasfilename(initialdir=os.getcwd(),title="Open CSV",filetypes=(("CSV File","*.csv"),("All File","*.*")),parent=self.root)
            with open(export_file,mode="w",newline="") as csvfile:
                csv_write=csv.writer(csvfile,delimiter=",")
                for i in my_data:
                    csv_write.writerow(i)
            messagebox.showinfo("Data Export","Your data exported to: "+export_file,parent=self.root)
        except Exception as es:
            messagebox.showerror("Error",f"Due To:{str(es)}",parent=self.root)
        
    #Get cursor
    def get_cursor(self,event=""):
        cursor_row=self.attendance_report.focus()
        content=self.attendance_report.item(cursor_row)
        rows=content['values']
        self.var_atten_id.set(rows[0])
        self.var_atten_roll.set(rows[1])
        self.var_atten_name.set(rows[2])
        self.var_atten_dep.set(rows[3])
        self.var_atten_time.set(rows[4])
        self.var_atten_date.set(rows[5])
        self.var_atten_attendance.set(rows[6])
        
    def reset_data(self):
        self.var_atten_id.set("")
        self.var_atten_roll.set("")
        self.var_atten_name.set("")
        self.var_atten_dep.set("")
        self.var_atten_time.set("")
        self.var_atten_date.set("")
        self.var_atten_attendance.set("")
        
    def exit(self):
        self.root.destroy()
    
    


if __name__ == "__main__":
    root = Tk()
    obj = Attendance(root)
    root.mainloop()