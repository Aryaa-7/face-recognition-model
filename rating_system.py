from tkinter import *
from tkinter import ttk, messagebox
from PIL import Image, ImageTk
import csv
import matplotlib.pyplot as plt
import pandas as pd
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

RATING_FILE = "ratings.csv"

class Responses:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1530x800+0+0")
        self.root.title("Response Desk")

        # Header Frame
        h_frame = Frame(self.root, bd=2, relief=RIDGE, bg="white")
        h_frame.pack(fill=X)
        
        title = Label(h_frame, text="Response Desk", font=("times new roman", 20, "bold"), bg="white", fg="darkblue")
        title.pack(fill=X)

        # Image Frame
        
        i_frame = Frame(h_frame, bd=2, relief=RIDGE, bg="green")
        i_frame.place(x=0, y=0, width=55, height=55)

        img = Image.open(r"C:\s_a_m\2023-08-28.png")
        img = img.resize((55, 55), Image.Resampling.LANCZOS)
        self.photoimg = ImageTk.PhotoImage(img)

        i_lbl = Label(i_frame, image=self.photoimg)
        i_lbl.place(x=0, y=0, width=55, height=55)

        
        # Layout Frames
        bd_frame = Frame(self.root, bd=2, relief=RIDGE, bg="white")
        bd_frame.pack(fill=BOTH, expand=True)

        bd_frame.columnconfigure(0, weight=1)  # Left panel
        bd_frame.columnconfigure(1, weight=2)  # Right panel
        bd_frame.rowconfigure(0, weight=1)

        left_frame = Frame(bd_frame, bd=2, relief=RIDGE, bg="white")
        left_frame.grid(row=0, column=0, sticky="nsew", padx=5, pady=5)
        
        # ✅ Store `right_frame` as an instance variable
        self.right_frame = Frame(bd_frame, bd=2, relief=RIDGE, bg="white")
        self.right_frame.grid(row=0, column=1, sticky="nsew", padx=5, pady=5)

        # Input Fields
        Label(left_frame, text="User:",font=("Times New Roman", 14, "bold"), bg="white").grid(row=0, column=0, padx=10, pady=10, sticky="w")
        self.entry_user = Entry(left_frame,width=20,font=("Times New Roman", 14, "bold"), bg="lightgray")
        self.entry_user.grid(row=0, column=1, padx=10, pady=10)
        
        #exit button
        exit_button = Button(left_frame, text="Exit", font=("Arial", 10, "bold"), bg="red", fg="white", bd=0, command=self.exit)
        exit_button.grid(row=5, column=0, columnspan=2, pady=10)

        # Star Rating System
        self.rating_value = IntVar(value=0)
        Label(left_frame, text="Rate your satisfaction:", bg="white").grid(row=1, column=0, columnspan=2, padx=10, pady=5)

        self.stars = []
        star_frame = Frame(left_frame, bg="white")
        star_frame.grid(row=2, column=0, columnspan=2, pady=5)

        for i in range(1, 6):
            star_button = Button(star_frame, text="★", font=("Arial", 20), fg="gray", bd=0,
                                 command=lambda i=i: self.update_stars(i))
            star_button.grid(row=0, column=i, padx=5)
            self.stars.append(star_button)

        # Label to display selected rating
        self.selected_rating_label = Label(left_frame, text="Selected: 0 ★", bg="white", font=("Arial", 12))
        self.selected_rating_label.grid(row=3, column=0, columnspan=2, pady=5)

        # Submit Button
        self.btn_save = Button(left_frame, text="Submit Rating", bg="green", fg="white", command=self.save_rating)
        self.btn_save.grid(row=4, column=0, columnspan=2, pady=10)

        # Right Panel - Table & Graph
        table_frame = Frame(self.right_frame, bd=2, relief=RIDGE, bg="white")
        table_frame.pack(side=TOP, fill=X, padx=5, pady=5)

        self.table = ttk.Treeview(table_frame, columns=("User", "Rating"), show="headings", height=5)
        self.table.heading("User", text="User")
        self.table.heading("Rating", text="Rating")
        self.table.column("User", width=150, anchor=CENTER)
        self.table.column("Rating", width=100, anchor=CENTER)
        self.table.pack(fill=X, padx=5, pady=5)

        # ✅ Store Graph Frame
        self.graph_frame = Frame(self.right_frame, bd=2, relief=RIDGE, bg="white")
        self.graph_frame.pack(fill=BOTH, expand=True, padx=5, pady=5)

        self.fig, self.ax = plt.subplots(figsize=(5, 3))
        self.canvas = FigureCanvasTkAgg(self.fig, master=self.graph_frame)
        self.canvas.get_tk_widget().pack(fill=BOTH, expand=True)

        self.load_ratings()
        self.update_graph()

    def update_stars(self, rating):
        """Update star colors based on selection."""
        self.selected_rating_label.config(text=f"Selected: {rating} ★", fg="blue")
        self.rating_value.set(rating)
        for i in range(5):
            self.stars[i].config(fg="gold" if i < rating else "gray")

    def save_rating(self):
        """Save rating to CSV and update UI."""
        user = self.entry_user.get()
        rating = self.rating_value.get()

        if not user or rating == 0:
            messagebox.showerror("Error", "Enter a valid user and select a rating!")
            return

        with open(RATING_FILE, "a", newline="") as file:
            writer = csv.writer(file)
            writer.writerow([user, rating])

        self.entry_user.delete(0, END)
        self.rating_value.set(0)
        self.update_stars(0)
        self.load_ratings()
        self.update_graph()

    def load_ratings(self):
        """Load ratings from CSV to table."""
        for row in self.table.get_children():
            self.table.delete(row)

        try:
            with open(RATING_FILE, "r") as file:
                reader = csv.reader(file)
                for row in reader:
                    self.table.insert("", "end", values=row)
        except FileNotFoundError:
            open(RATING_FILE, "w").close()

    def update_graph(self):
        """Update and display the ratings graph using a histogram."""
        try:
            df = pd.read_csv(RATING_FILE, names=["User", "Rating"])
            df["Rating"] = pd.to_numeric(df["Rating"], errors="coerce").dropna()

            self.ax.clear()
            self.ax.hist(df["Rating"], bins=5, color="purple", edgecolor="black", alpha=0.7)
            self.ax.set_xlabel("Rating")
            self.ax.set_ylabel("Frequency")
            self.ax.set_title("Rating Distribution")
            self.ax.set_xticks(range(1, 6))

            if self.canvas:
                self.canvas.get_tk_widget().destroy()

            # ✅ Corrected `master=self.graph_frame`
            self.canvas = FigureCanvasTkAgg(self.fig, master=self.graph_frame)
            self.canvas.get_tk_widget().pack(fill=BOTH, expand=True)
            self.canvas.draw()

        except Exception as e:
            messagebox.showerror("Error", f"Could not generate graph: {e}")
            
    
            
    def exit(self):
        self.root.destroy()

if __name__ == "__main__":
    root = Tk()
    app = Responses(root)
    root.mainloop()
