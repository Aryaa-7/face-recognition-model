from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import winsound  # Keep this at the top of the file

class SettingsPannel:
    
    def __init__(self, root):
        self.root = root  # Root Window
        self.root.title("Settings Panel")
        self.root.geometry("1530x800+0+0")

        # Default Theme Colors
        self.bg_color = "white"
        self.fg_color = "black"
        self.btn_bg = "lightgray"
        self.btn_fg = "black"
        self.default_font_size = 12
        
        # Title Label
        title_label = Label(self.root, text="⚙️ Settings Panel", font=("Arial", 16, "bold"), bg="white")
        title_label.place(x=0, y=20, width=1530, height=50)

        # Sidebar for Navigation Buttons
        left_frame = Frame(self.root, width=200, height=750, bg="lightgray")
        left_frame.place(x=0, y=60, height=750)

        # Buttons
        self.general_btn = Button(left_frame, text="General", width=20, command=lambda: self.show_frame("General"))
        self.display_btn = Button(left_frame, text="Display", width=20, command=lambda: self.show_frame("Display"))
        self.notification_btn = Button(left_frame, text="Notifications", width=20, command=lambda: self.show_frame("Notifications"))
        self.security_btn = Button(left_frame, text="Security", width=20, command=lambda: self.show_frame("Security"))

        # Placing buttons in the left panel
        self.general_btn.place(x=20, y=50, width=160, height=40)
        self.display_btn.place(x=20, y=100, width=160, height=40)
        self.notification_btn.place(x=20, y=150, width=160, height=40)
        self.security_btn.place(x=20, y=200, width=160, height=40)

        # Button colors
        self.general_btn.config(bg=self.btn_bg, fg=self.btn_fg)
        self.display_btn.config(bg=self.btn_bg, fg=self.btn_fg)
        self.notification_btn.config(bg=self.btn_bg, fg=self.btn_fg)
        self.security_btn.config(bg=self.btn_bg, fg=self.btn_fg)

        # Content Frame (Right Side for Settings Pages)
        self.content_frame = Frame(self.root, bg=self.bg_color, width=1330, height=750)
        self.content_frame.place(x=200, y=60, width=1330, height=750)

        self.frames = {}  # Store pages
        for page in ("General", "Display", "Notifications", "Security"):
            frame = Frame(self.content_frame, bg="white")
            self.frames[page] = frame

        self.create_general_page()
        self.create_display_page()
        self.create_notification_page()
        self.create_security_page()

        self.show_frame("General")  # Show General by default
        
    def logout(self):
        """Logout and close the application"""
        confirm = messagebox.askyesno("Logout", "Are you sure you want to logout?")
        if confirm:
            self.root.destroy()  # This will close the root window and exit the application

        
    def show_sample_notification(self):
        if self.enable_notifications_var.get():
            msg = "✅ This is a test notification."
            self.notification_log.insert(END, msg + "\n")
            self.notification_log.see(END)

            if self.enable_sounds_var.get():
                try:
                    winsound.Beep(1000, 300)
                except RuntimeError:
                    self.notification_log.insert(END, "⚠️ Sound failed to play.\n")

            # Instead of messagebox, use non-blocking popup
            notif = Toplevel(self.root)
            notif.title("Notification")
            notif.geometry("300x100+600+300")
            Label(notif, text=msg, font=("Arial", 12)).pack(pady=20)
            Button(notif, text="OK", command=notif.destroy).pack()
        else:
            self.notification_log.insert(END, "❌ Notifications are disabled.\n")
            messagebox.showwarning("Notifications Disabled", "Enable notifications to receive alerts.")
        
        
    def change_theme(self, event=None):
        """ Ask for confirmation before changing the theme """
        theme = self.theme_dropdown.get()

        confirm = messagebox.askyesno("Confirm Theme Change", f"Are you sure you want to change the theme to {theme}?")
        if confirm:
            if theme == "Dark":
                self.bg_color = "black"
                self.fg_color = "white"
                self.btn_bg = "#444"
                self.btn_fg = "white"
            else:
                self.bg_color = "white"
                self.fg_color = "black"
                self.btn_bg = "lightgray"
                self.btn_fg = "black"

            self.update_theme()  # Apply the theme
        else:
            self.theme_dropdown.current(0)  # Reset to previous selection if canceled

    def update_theme(self):
        """ Apply theme settings to all frames, labels, and buttons globally """
        self.root.config(bg=self.bg_color)  # Change root window color
        self.content_frame.config(bg=self.bg_color)  # Change main content area
     
        # Update sidebar
        for widget in self.root.winfo_children():
            if isinstance(widget, Frame):
                widget.config(bg=self.bg_color)

        # Update each settings page
        for page in self.frames.values():
            page.config(bg=self.bg_color)
            for widget in page.winfo_children():
                if isinstance(widget, Label):
                    widget.config(bg=self.bg_color, fg=self.fg_color)
                elif isinstance(widget, Button):
                    widget.config(bg=self.btn_bg, fg=self.btn_fg)
                elif isinstance(widget, Checkbutton):
                    widget.config(bg=self.bg_color, fg=self.fg_color, activebackground=self.bg_color)
                elif isinstance(widget, Scale):
                    widget.config(bg=self.bg_color, fg=self.fg_color)
                elif isinstance(widget, ttk.Combobox):
                    widget.config(background=self.bg_color, foreground=self.fg_color)

        # Update sidebar buttons
        self.general_btn.config(bg=self.btn_bg, fg=self.btn_fg)
        self.display_btn.config(bg=self.btn_bg, fg=self.btn_fg)
        self.notification_btn.config(bg=self.btn_bg, fg=self.btn_fg)
        self.security_btn.config(bg=self.btn_bg, fg=self.btn_fg)


    def show_frame(self, page):
        """ Show the selected page and hide others """
        for frame in self.frames.values():
            frame.place_forget()
        self.frames[page].place(x=50, y=50, width=1200, height=600)

    def create_display_page(self):
        frame = self.frames["Display"]
        label = Label(frame, text="Display Settings", font=("Arial", 14, "bold"), bg="white")
        label.place(x=10, y=10)
    
        Label(frame, text="Font Size:", font=("Arial", 12), bg="white").place(x=10, y=50)
    
        # ✅ Initialize preview_label properly
        self.preview_label = Label(frame, text="Preview Text", font=("Arial", self.default_font_size), bg="white")
        self.preview_label.place(x=10, y=100)

        # ✅ Font size slider
        self.font_size_slider = Scale(frame, from_=10, to=30, orient="horizontal", command=self.update_font_size)
        self.font_size_slider.set(self.default_font_size)  # Set initial slider value
        self.font_size_slider.place(x=100, y=50, width=200)

    def update_font_size(self, size):
        """ Update the preview text's font size dynamically based on slider value """
        new_size = int(size)
        self.preview_label.config(font=("Arial", new_size))  # ✅ Apply the change correctly


    def create_general_page(self):
        frame = self.frames["General"]
        label = Label(frame, text="General Settings", font=("Arial", 14, "bold"), bg="white")
        label.place(x=10, y=10)

        # Theme Selection
        Label(frame, text="Theme:", font=("Arial", 12), bg="white").place(x=10, y=50)
        self.theme_dropdown = ttk.Combobox(frame, values=["Light", "Dark"],state="readonly")
        self.theme_dropdown.place(x=120, y=50, width=150)
        self.theme_dropdown.current(0)  # Default selection
        self.theme_dropdown.bind("<<ComboboxSelected>>", self.change_theme)

        # Language Selection
        Label(frame, text="Language:", font=("Arial", 12), bg="white").place(x=10, y=100)
        self.language_dropdown = ttk.Combobox(frame, values=["English", "Hindi"])
        self.language_dropdown.place(x=120, y=100, width=150)
        self.language_dropdown.current(0)  # Default selection

        # Reset to Default Settings Button
        reset_button = Button(frame, text="Reset to Default", font=("Arial", 12), bg="red", fg="white", command=self.reset_settings)
        reset_button.place(x=10, y=150, width=200, height=40)
        
         # Logout Button
        logout_button = Button(frame, text="Logout", font=("Arial", 12), bg="gray", fg="white", command=self.logout)
        logout_button.place(x=10, y=200, width=200, height=40)


    def create_notification_page(self):
        frame = self.frames["Notifications"]
        label = Label(frame, text="Notification Settings", font=("Arial", 14, "bold"), bg="white")
        label.place(x=10, y=10)

        # State variables
        self.enable_notifications_var = IntVar(value=1)
        self.enable_sounds_var = IntVar(value=1)

        # Checkbuttons
        enable_notifications = Checkbutton(frame, text="Enable Notifications", variable=self.enable_notifications_var, bg="white")
        enable_sounds = Checkbutton(frame, text="Enable Sound Alerts", variable=self.enable_sounds_var, bg="white")
        enable_notifications.place(x=10, y=50)
        enable_sounds.place(x=10, y=80)

        # Test Notification Button
        test_button = Button(frame, text="Test Notification", font=("Arial", 12), command=self.show_sample_notification)
        test_button.place(x=10, y=120, width=180)

        # Notification Log Box
        Label(frame, text="Notification Log:", font=("Arial", 12), bg="white").place(x=10, y=170)
        self.notification_log = Text(frame, height=10, width=80, bg="#f5f5f5")
        self.notification_log.place(x=10, y=200)
        self.notification_log.insert(END, "No new notifications...\n")

    def create_security_page(self):
        frame = self.frames["Security"]
        label = Label(frame, text="Security Settings", font=("Arial", 14, "bold"), bg="white")
        label.place(x=10, y=10)

        auto_logout = Checkbutton(frame, text="Enable Auto Logout", bg="white")
        encrypt_data = Checkbutton(frame, text="Enable Data Encryption", bg="white")
        auto_logout.place(x=10, y=50)
        encrypt_data.place(x=10, y=80)

    def reset_settings(self):
        """ Ask for confirmation before resetting settings and restore the original UI """
        confirm = messagebox.askyesno("Reset Settings", "Are you sure you want to reset all settings to default?")
    
        if confirm:
            # Reset to Light Theme
            self.bg_color = "white"
            self.fg_color = "black"
            self.btn_bg = "lightgray"
            self.btn_fg = "black"
            self.default_font_size = 12  # Reset font size

            # Reset dropdown selections
            self.theme_dropdown.current(0)  # Set Theme to Light
            self.language_dropdown.current(0)  # Set Language to English

            # Reset font size slider (if used)
            if hasattr(self, 'font_size_slider'):
                self.font_size_slider.set(self.default_font_size)

            # Apply theme update to refresh the UI completely
            self.update_theme()
        
            messagebox.showinfo("Reset Complete", "All settings have been restored to default.")
        else:
            print("Reset canceled.")


if __name__ == "__main__":
    root = Tk()
    obj = SettingsPannel(root)
    root.mainloop()
