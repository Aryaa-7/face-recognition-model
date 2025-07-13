from tkinter import *
from tkinter import ttk, messagebox
import pyttsx3
import threading
import datetime

class ChatbotApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Help Desk Chatbot - Ava")
        self.root.geometry("900x500")

        self.bot_name = "Sakshi"  # Name of the bot

        self.faq_data = {
            "General Questions": {
                "How does the face recognition attendance system work?": "The system captures your face and matches it with stored records to mark attendance.",
                "What should I do if my face is not recognized?": "Ensure proper lighting and that your face is clearly visible. Try again or contact support.",
                "Can I use the system if I wear glasses or a mask?": "Yes, but it works best when your full face is visible.",
                "Is my face data stored securely?": "Yes, all face data is encrypted and stored securely.",
                "How do I register my face in the system?": "Go to the registration section and follow the instructions to capture your face."
            },
            "Attendance & Logs": {
                "How can I check my attendance record?": "You can check your attendance through the user panel or contact admin.",
                "What happens if my attendance is not recorded?": "Ensure proper positioning in front of the camera. If the issue persists, contact support.",
                "Can I manually mark my attendance if my face is not detected?": "No, attendance is based on facial recognition only.",
                "How do I report incorrect attendance records?": "You can report incorrect records to the admin for verification."
            },
            "Technical Support": {
                "Why is the camera not detecting my face?": "Check if your camera is properly connected and has the necessary permissions.",
                "What are the best lighting conditions for face recognition?": "Use bright and even lighting to avoid shadows.",
                "Why is the system taking too long to recognize my face?": "Ensure good lighting and a clear face position in front of the camera.",
                "How do I reset the system if it stops working?": "Restart the application or check system settings."
            },
            "Security & Privacy": {
                "Is my face data shared with anyone?": "No, your data is kept private and not shared with third parties.",
                "How do I delete my face data from the system?": "Contact the admin to request data deletion.",
                "What security measures are in place to protect my data?": "We use encryption and secure storage to protect all data."
            }
        }

        # Initialize text-to-speech engine
        self.engine = pyttsx3.init()
        self.engine.setProperty("rate", 160)  # Natural speech speed
        self.engine.setProperty("volume", 1.0)  # Max volume

        voices = self.engine.getProperty("voices")
        self.engine.setProperty("voice", voices[1].id)  # Use a more natural voice (adjust if needed)

        self.title_label = Label(self.root, text=f"{self.bot_name} - Help Desk Chatbot", font=("Arial", 16, "bold"))
        self.title_label.pack(pady=10)

        # Frame for buttons
        self.button_frame = Frame(self.root)
        self.button_frame.pack(pady=5)

        # Frame for questions
        self.question_listbox = Listbox(self.root, width=80, height=10)
        self.question_listbox.pack(pady=5)
        self.question_listbox.bind("<Double-Button-1>", self.display_answer)

        # Buttons to display categories
        for section in self.faq_data.keys():
            btn = Button(self.button_frame, text=section, command=lambda sec=section: self.show_questions(sec))
            btn.pack(side=LEFT, padx=5)

        # Answer label
        self.answer_label = Label(self.root, text="Select a question to see the answer here.", wraplength=600, justify="left", font=("Arial", 12))
        self.answer_label.pack(pady=10)

        # Contact Admin button (hidden initially)
        self.contact_admin_button = Button(self.root, text="Contact Admin", command=self.contact_admin, font=("Arial", 12), bg="red", fg="white")
        self.contact_admin_button.place_forget()  # Hide it at the start

        # Greet user when the chatbot starts
        self.greet_user()

    def speak(self, text):
        """ Run text-to-speech in a separate thread to prevent UI freezing. """
        def run():
            self.engine.say(text)
            self.engine.runAndWait()

        threading.Thread(target=run, daemon=True).start()

    def greet_user(self):
        """ Determine the time of day and greet the user interactively. """
        current_hour = datetime.datetime.now().hour
        if 5 <= current_hour < 12:
            greeting = "Good morning!"
        elif 12 <= current_hour < 18:
            greeting = "Good afternoon!"
        elif 18 <= current_hour < 22:
            greeting = "Good evening!"
        else:
            greeting = "Good night!"

        introduction = f"{greeting} I am {self.bot_name}, your help desk assistant. How can I assist you today?"
        self.speak(introduction)

    def show_questions(self, section):
        """ Display questions when a section button is clicked. """
        self.question_listbox.delete(0, END)
        for question in self.faq_data[section]:
            self.question_listbox.insert(END, question)

        # Hide Contact Admin button when selecting a new section
        self.contact_admin_button.place_forget()

    def display_answer(self, event):
        """ Show the selected question's answer and speak it. """
        selected_question = self.question_listbox.get(ANCHOR)
        if not selected_question:  # If no question is selected
            return
        
        answer = None
        for section in self.faq_data:
            if selected_question in self.faq_data[section]:
                answer = self.faq_data[section][selected_question]
                break

        if answer:
            self.answer_label.config(text=answer)
            self.speak(answer)

            # Check if answer mentions "contact admin"
            if "admin" in answer.lower():
                self.contact_admin_button.place(x=680, y=320)  # Show the button
            else:
                self.contact_admin_button.place_forget()  # Hide the button if it's not needed

    def contact_admin(self):
        """ Action when the Contact Admin button is clicked. """
        messagebox.showinfo("Contact Admin", "Please reach out to the admin at admin@example.com or visit the admin office.")

if __name__ == "__main__":
    root = Tk()
    app = ChatbotApp(root)
    root.mainloop()
