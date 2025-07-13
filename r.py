from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
import mysql.connector
from datetime import datetime
import cv2
import csv
import numpy as np
import pyttsx3
import threading


class FaceRecognition:
    
    engine = pyttsx3.init()

# Function to convert text to speech
    def speak(self,text):
        threading.Thread(target=lambda: (self.engine.say(text), self.engine.runAndWait())).start()
    
    def __init__(self, root):
        self.root = root
        self.root.geometry("1530x800+0+0")
        self.root.title("Face Recognition")

        # ========== Main Title ===========
        title_lbl = Label(self.root, text="Face Recognition System", font=("times new roman", 35, "bold"), bg="white", fg="darkblue")
        title_lbl.pack(side=TOP, fill=X)

        # ========== Main Frame ===========
        main_frame = Frame(self.root, bd=2, relief=RIDGE, bg="white")
        main_frame.place(x=10, y=60, width=1500, height=730)

        # ========== Left Section (Webcam & Buttons) ===========
        left_frame = Frame(main_frame, bd=2, relief=RIDGE, bg="white")
        left_frame.place(x=10, y=10, width=730, height=700)

        img_top = Image.open(r"C:\s_a_m\UI\2494968.jpg")
        img_top = img_top.resize((730, 300), Image.Resampling.LANCZOS)
        self.photoimg_top = ImageTk.PhotoImage(img_top)

        f_lbl = Label(left_frame, image=self.photoimg_top)
        f_lbl.pack(side=TOP, fill=X)

        b1_1 = Button(left_frame, text="Start Face Recognition", command=self.face_recog, font=("times new roman", 20, "bold"), bg="darkblue", fg="white", cursor="hand2")
        b1_1.pack(side=TOP, fill=X, pady=10, padx=20)

        right_frame = Frame(main_frame, bd=2, relief=RIDGE, bg="white")
        right_frame.place(x=750, y=10, width=730, height=700)

        lbl_attendance = Label(right_frame, text="Attendance List", font=("times new roman", 25, "bold"), bg="white", fg="darkblue")
        lbl_attendance.pack(side=TOP, fill=X)

        self.tree = ttk.Treeview(right_frame, columns=("ID", "Roll", "Name", "Dept", "Time", "Date", "Status"), show="headings")
        self.tree.pack(fill=BOTH, expand=1)

        for col in self.tree['columns']:
            self.tree.heading(col, text=col)
            self.tree.column(col, width=100)

        self.attendance_marked_today = set()
        self.load_attendance_data()
        self.already_spoken = set()

    def load_attendance_data(self):
        filename = "attendance.csv"
        self.tree.delete(*self.tree.get_children())
        try:
            with open(filename, "r", newline="\n") as f:
                csv_reader = csv.reader(f)
                for row in csv_reader:
                    if len(row) == 7:
                        self.tree.insert("", "end", values=row)
        except FileNotFoundError:
            print("⚠ No attendance record found!")

    def mark_attendance(self, i, r, n, d):
        filename = "attendance.csv"
        now = datetime.now()
        date_today = now.strftime("%d/%m/%Y")
        time_now = now.strftime("%H:%M:%S")

        if (i, date_today) in self.attendance_marked_today:
            print(f"⚠ Attendance already recorded for {n} ({r}) today! Skipping...")
            return

        try:
            with open(filename, "a", newline="\n") as f:
                csv_writer = csv.writer(f)
                csv_writer.writerow([i, r, n, d, time_now, date_today, "Present"])
            self.attendance_marked_today.add((i, date_today))
            self.load_attendance_data()
        except Exception as e:
            print("Error in marking attendance:", str(e))

    def speak(self, text):
        if text not in self.already_spoken:
            engine = pyttsx3.init()
            engine.setProperty('rate', 150)
            engine.setProperty('volume', 1)
            engine.say(text)
            engine.runAndWait()
            self.already_spoken.add(text)

    def face_recog(self):
        faceCascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
        clf = cv2.face.LBPHFaceRecognizer_create()
        clf.read("Classifier.xml")

        video_cap = cv2.VideoCapture(0)
        while video_cap.isOpened():
            ret, frame = video_cap.read()
            if not ret:
                break

            gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            features = faceCascade.detectMultiScale(gray, 1.1, 10)
            for (x, y, w, h) in features:
                cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 3)
                id, predict = clf.predict(gray[y:y + h, x:x + w])
                confidence = int((100 * (1 - predict / 300)))
                conn = mysql.connector.connect(host="localhost", username="root", password="aryan1525@", database="face_recoginizer")
                cursor = conn.cursor()
                cursor.execute("SELECT Name, Roll, Dep FROM student WHERE Student_id=%s", (id,))
                result = cursor.fetchone()
                if result and confidence >50:
                    n, r, d = result
                    cv2.putText(frame, f"Name: {n}", (x, y - 75), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255, 255, 255), 2)
                    cv2.putText(frame, f"Roll: {r}", (x, y - 55), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255, 255, 255), 2)
                    cv2.putText(frame, f"Dept: {d}", (x, y - 35), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255, 255, 255), 2)
                    self.mark_attendance(id, r, n, d)
                    self.speak(f"Attendance marked for {n}")
                else:
                    cv2.putText(frame, "Unknown", (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0, 0, 255), 2)

            cv2.imshow("Face Recognition", frame)
            if cv2.waitKey(1) & 0xFF in [13, 27]:
                break

        video_cap.release()
        cv2.destroyAllWindows()

if __name__ == "__main__":
    root = Tk()
    app = FaceRecognition(root)
    app.speak("Welcome to Face Recognition")
    root.mainloop()
