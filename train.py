from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
import mysql.connector
import cv2
import os
import numpy as np
import threading
import pyttsx3

class Train:
    
    engine = pyttsx3.init()

# Function to convert text to speech
    def speak(self,text):
        threading.Thread(target=lambda: (self.engine.say(text), self.engine.runAndWait())).start()
        
    def __init__(self,root):
        self.root=root
        self.root.geometry("1530x800+0+0")
        self.root.title("Face Recognition System")
        
        title_lbl=Label(self.root,text="TRAIN DATASET",font=("times new roman",35,"bold"),bg="white",fg="darkblue")
        title_lbl.place(x=0,y=0,width=1530,height=45)
        
        img_top=Image.open(r"C:\s_a_m\UI\_top_img_.webp")
        img_top=img_top.resize((1530,325),Image.Resampling(Image.BICUBIC))
        self.photoimg_top=ImageTk.PhotoImage(img_top)

        f_lbl=Label(self.root,image=self.photoimg_top)
        f_lbl.place(x=0,y=55,width=1530,height=325)
        
        b1_1=Button(self.root,text="Train Data",command=self.train_classifier,cursor="hand2",font=("times new roman",30,"bold"),bg="darkblue",fg="white")
        b1_1.place(x=0,y=385,width=1530,height=60)
        
        img_bottom=Image.open(r"C:\s_a_m\UI\_top_img_.webp")
        img_bottom=img_bottom.resize((1530,325),Image.Resampling(Image.BICUBIC))
        self.photoimg_bottom=ImageTk.PhotoImage(img_bottom)

        f_lbl=Label(self.root,image=self.photoimg_bottom)
        f_lbl.place(x=0,y=450,width=1530,height=325)
        
    def train_classifier(self):
        data_dir = "Data"
        path = [os.path.join(data_dir, file) for file in os.listdir(data_dir) if file.endswith(('.jpg', '.jpeg', '.png'))]

        faces = []
        ids = []

        for image in path:
            try:
                img = Image.open(image).convert('L')  # Convert to grayscale
                imageNp = np.array(img, 'uint8')
                id = int(os.path.split(image)[1].split('.')[1])

                faces.append(imageNp)
                ids.append(id)
                cv2.imshow("Training", imageNp)
                cv2.waitKey(100)  # Delay for better visualization
            except (IndexError, ValueError) as e:
                print(f"Skipping invalid file: {image}, Error: {e}")
                continue

        if not faces or not ids:
            self.speak("Error No valid images found for training!")
            messagebox.showerror("Error", "No valid images found for training!", parent=self.root)
            return

        ids = np.array(ids)

        # Train the classifier and save
        clf = cv2.face.LBPHFaceRecognizer_create()
        clf.train(faces, ids)
        clf.write("Classifier.xml")
        cv2.destroyAllWindows()
        self.speak("Training datasets completed successfully!")
        messagebox.showinfo("Result", "Training datasets completed successfully!", parent=self.root)


if __name__ == "__main__":
    root=Tk()
    obj=Train(root)
    obj.speak("Welcome to Train Data")
    root.mainloop()