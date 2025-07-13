import os
from tkinter import *
from tkinter import ttk
from tkinter import simpledialog, messagebox
from PIL import Image, ImageTk
from report import Reports
from rating_system import Responses
from settings import SettingsPannel
from bot import ChatbotApp
import pyttsx3
import threading

class helpdesk:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1530x800+0+0")
        self.root.title("Face Recognition Help Desk")
        
        # Initialize TTS Engine
        self.engine = pyttsx3.init()

        # Header Frame
        h_frame = Frame(self.root, bd=2, relief=RIDGE, bg="white")
        h_frame.place(x=0, y=0, width=1535, height=55)

        title = Label(h_frame, text="Help Desk", font=("times new roman", 20, "bold"), bg="white", fg="darkblue")
        title.place(x=0, y=17, width=1535, height=35)

        img_frame = Frame(h_frame, bd=2, relief=RIDGE, bg="green")
        img_frame.place(x=0, y=0, width=55, height=55)

        img = Image.open(r"C:\s_a_m\UI\Screenshot 2025-04-17 194319.png")
        img = img.resize((55, 55), Image.Resampling.LANCZOS)
        self.photoimg = ImageTk.PhotoImage(img)

        i_lbl = Label(img_frame, image=self.photoimg)
        i_lbl.place(x=0, y=0, width=55, height=55)

        # Sidebar Navigation
        s_frame = Frame(self.root, bd=2, relief=RIDGE, bg="white")
        s_frame.place(x=0, y=55, width=145, height=750)

        inner_lbl = Label(s_frame, text="NAVIGATION", font=("times new roman", 14, "bold"), bg="white", fg="darkblue")
        inner_lbl.place(x=5, y=0, width=130, height=35)

        n_bttn = [("HOME", self.exit), ("RESPONSE", self.response), ("REPORT", self.report), ("SETTING", self.setting)]
        y_pos = 50
        for text, command in n_bttn:
            Button(s_frame, command=lambda t=text, c=command: self.speak_and_open(t, c),
                   text=text, width=15, bg="white", fg="black").place(x=5, y=y_pos)
            y_pos += 40

        # Main Body Frame
        bd_frame = Frame(self.root, width=1385, height=750, bg="white")
        bd_frame.place(x=145, y=60)

        bt_lbl = Label(bd_frame, text="Recent Activity", font=("Times New Roman", 28, "bold"), fg="blue", bg="white")
        bt_lbl.place(x=500, y=10)

        # Table for Displaying Issues
        columns = ("ID", "ISSUE", "DATE", "STATUS")
        self.tree = ttk.Treeview(bd_frame, columns=columns, show="headings")

        for col in columns:
            self.tree.heading(col, text=col)
            self.tree.column(col, width=150)

        self.tree.place(x=200, y=80, width=900, height=300)

        # Report Button
        r_btn = Button(bd_frame, command=self.report, text="Report an Issue", font=("times new roman", 15, "bold"), bg="darkblue", fg="white", cursor="hand2")
        r_btn.place(x=500, y=400, width=200, height=40)
        
        update_status_btn = Button(bd_frame, text="Update Status", font=("times new roman", 15, "bold"), 
                           bg="green", fg="white", cursor="hand2", command=self.update_status)
        update_status_btn.place(x=500, y=450, width=200, height=40)
        
        # Chat Button
        c_btn = Button(bd_frame, command=self.chat, text="Chat with Bot", font=("times new roman", 15, "bold"), bg="yellow", fg="black", cursor="hand2")
        c_btn.place(x=500, y=500, width=200, height=40)
        
        # Load problems into the table
        self.load_problems()

    def speak(self, text):
        """Speaks the given text"""
        def run():
            self.engine.say(text)
            self.engine.runAndWait()

        threading.Thread(target=run, daemon=True).start()
        
    def speak_and_open(self, text, command):
        """Speaks the text and then opens the corresponding function"""
        self.speak(f"Opening {text}")
        self.root.after(1000, command)  # Delay to allow speech before opening

    def load_problems(self):
        """Load data from PROBLEMS folder into the Treeview table"""
        problems_folder = "PROBLEMS"

        # Clear existing data in the table
        for row in self.tree.get_children():
            self.tree.delete(row)

        if not os.path.exists(problems_folder):
            return

        # Read each problem file and extract data
        for filename in sorted(os.listdir(problems_folder), key=lambda x: int(x.split('.')[0])):
            if filename.endswith(".txt"):
                file_path = os.path.join(problems_folder, filename)
                with open(file_path, "r", encoding="utf-8") as file:
                    lines = file.readlines()

                # Extract required details
                problem_id = lines[0].split(":")[1].strip()  # Problem ID
                date_time = lines[1].split(":")[1].strip()  # Date & Time

                # Find the problem description
                issue_index = lines.index("Problem Description:\n") + 1  # Line after "Problem Description:"
                issue = lines[issue_index].strip() if issue_index < len(lines) else "No issue provided"

                # Insert into the table (Leave Status empty)
                self.tree.insert("", "end", values=(problem_id, issue, date_time, ""))

    def update_status(self):
        """Allow admin to update the status field"""
        selected_item = self.tree.focus()  # Get selected row

        if not selected_item:
            messagebox.showerror("Error", "Please select an issue to update!")
            return

        # Retrieve values from the selected row
        values = self.tree.item(selected_item, "values")

        if not values:
            messagebox.showerror("Error", "No valid data found!")
            return

        problem_id = values[0]  # Extract problem ID (First column)
        issue = values[1]        # Extract issue description
        date = values[2]         # Extract date

        # Authenticate Admin with a password
        password = simpledialog.askstring("Admin Login", "Enter Admin Password:", show="*")
        if password != "admin123":  # Change this password
            messagebox.showerror("Error", "Incorrect Password!")
            return

        # Show new window for status selection after password authentication
        self.show_status_selection(problem_id, issue, date)

    def show_status_selection(self, problem_id, issue, date):
        """Show the status selection window after admin login"""
        status_window = Toplevel(self.root)
        status_window.title("Update Status")

        Label(status_window, text=f"Update Status for Problem ID: {problem_id}", font=("times new roman", 14, "bold")).pack(pady=10)

        # Buttons for selecting status
        Button(status_window, text="Processing", font=("times new roman", 12, "bold"), bg="yellow", fg="black",
               command=lambda: self.update_table_status(status_window, problem_id, issue, date, "Processing")).pack(pady=5)

        Button(status_window, text="Fixed", font=("times new roman", 12, "bold"), bg="green", fg="white",
               command=lambda: self.update_table_status(status_window, problem_id, issue, date, "Fixed")).pack(pady=5)

        Button(status_window, text="Not Fixed", font=("times new roman", 12, "bold"), bg="red", fg="white",
               command=lambda: self.update_table_status(status_window, problem_id, issue, date, "Not Fixed")).pack(pady=5)

    def update_table_status(self, window, problem_id, issue, date, new_status):
        """Update the status in the table and the respective file"""
        # Update table
        for item in self.tree.get_children():
            if self.tree.item(item, "values")[0] == problem_id:
                self.tree.item(item, values=(problem_id, issue, date, new_status))

        # Update the corresponding text file
        problem_file = os.path.join("PROBLEMS", f"{problem_id}.txt")

        if os.path.exists(problem_file):
            with open(problem_file, "r", encoding="utf-8") as file:
                lines = file.readlines()

        # Add or update the status line
        status_line = f"Status: {new_status}\n"
        if any("Status:" in line for line in lines):  # If status exists, update it
            lines = [status_line if "Status:" in line else line for line in lines]
        else:  # Otherwise, append the status at the end
            lines.append("\n" + status_line)

        with open(problem_file, "w", encoding="utf-8") as file:
            file.writelines(lines)

        messagebox.showinfo("Success", f"Status updated for Problem ID {problem_id}!")
        window.destroy()

    def report(self):
        """Open the report window"""
        self.new_window = Toplevel(self.root)
        self.new_window = Reports(self.new_window)

    def response(self):
        """Open the response window"""
        self.new_window = Toplevel(self.root)
        self.new_window = Responses(self.new_window)

    def setting(self):
        """Open the setting window"""
        self.new_window = Toplevel(self.root)
        self.new_window = SettingsPannel(self.new_window)

    def chat(self):
        """Open the chat window"""
        self.new_window = Toplevel(self.root)
        self.new_window = ChatbotApp(self.new_window)

    def exit(self):
        """Close the application"""
        self.root.destroy()


if __name__ == "__main__":
    root = Tk()
    obj = helpdesk(root)
    root.mainloop()
