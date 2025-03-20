from tkinter import *
from tkinter import ttk, messagebox
from PIL import Image, ImageTk
from db import Database

db = Database("Employee.db")

root = Tk()
# ===== Globals =====
GFont = ("Calibri", 16)
primaryColor = "#2c3e50"

root.title("Employee Management System")
root.geometry("1240x615+0+0")
root.resizable(False, False)
root.configure(bg=primaryColor)

name = StringVar()
age = StringVar()
job = StringVar()
email = StringVar()
gender = StringVar()
mobile = StringVar()
address = StringVar()

# ===== Resize Image to Fit Width =====
target_width = 200  # Set the desired width (same as Label width)
image = Image.open("logo.png")  # Open the image
aspect_ratio = image.height / image.width  # Calculate aspect ratio
new_height = int(target_width * aspect_ratio)  # Scale height
# Resize while keeping quality
resized_image = image.resize((target_width, new_height), Image.LANCZOS)

# Convert image for Tkinter
logo = ImageTk.PhotoImage(resized_image)

# Create and place the image label
lbl_logo = Label(root, image=logo, bg=primaryColor)
lbl_logo.place(x=65, y=475, width=target_width, height=new_height)

# Prevent garbage collection
lbl_logo.image = logo


# ===== Entries Frame =====
entries_frame = Frame(root, bg=primaryColor)
entries_frame.place(x=0, y=0, width=360, height=510)
title = Label(entries_frame, text="Employee Company", font=(
    "Calibri", 18, "bold"), bg=primaryColor, fg="white",)
title.place(x=10, y=1)

# Name Input
lblName = Label(entries_frame, text="Name",
                font=GFont, bg=primaryColor, fg="white",)
lblName.place(x=10, y=50)
txtName = Entry(entries_frame, width=20, textvariable=name, font=GFont,)
txtName.place(x=120, y=50)
# Job Input
lblJob = Label(entries_frame, text="Job",
               font=GFont, bg=primaryColor, fg="white",)
lblJob.place(x=10, y=90)
txtJob = Entry(entries_frame, width=20, textvariable=job, font=GFont,)
txtJob.place(x=120, y=90)
# Gender Combobox
lblGender = Label(entries_frame, text="Gender",
                  font=GFont, bg=primaryColor, fg="white",)
lblGender.place(x=10, y=130)
comboGender = ttk.Combobox(
    entries_frame, state="readonly", width=18, textvariable=gender, font=GFont)
comboGender["values"] = ("Male", "Female")
comboGender.place(x=120, y=130)
# Age Input
lblAge = Label(entries_frame, text="Age",
               font=GFont, bg=primaryColor, fg="white",)
lblAge.place(x=10, y=170)
txtAge = Entry(entries_frame, width=20, textvariable=age, font=GFont,)
txtAge.place(x=120, y=170)
# Email Input
lblEmail = Label(entries_frame, text="Email",
                 font=GFont, bg=primaryColor, fg="white",)
lblEmail.place(x=10, y=210)
txtEmail = Entry(entries_frame, width=20, textvariable=email, font=GFont,)
txtEmail.place(x=120, y=210)
# Mobile Input
lblMobile = Label(entries_frame, text="Mobile",
                  font=GFont, bg=primaryColor, fg="white",)
lblMobile.place(x=10, y=250)
txtMobile = Entry(entries_frame, width=20, textvariable=mobile, font=GFont,)
txtMobile.place(x=120, y=250)
# Address Input
lblAddress = Label(entries_frame, text="Address:",
                   font=GFont, bg=primaryColor, fg="white",)
lblAddress.place(x=10, y=290)
txtAddress = Text(entries_frame, width=30, height=2, font=GFont)
txtAddress.place(x=10, y=330)

# ===== [Define] =====


def hide():
    root.geometry("375x510")


def show():
    root.geometry("1240x615+0+0")


btn_hide = Button(entries_frame, text="HIDE", cursor="hand2", bg="white", bd=1, relief=SOLID,
                  command=hide).place(x=270, y=10)
btn_show = Button(entries_frame, text="SHOW", cursor="hand2", bg="white", bd=1, relief=SOLID,
                  command=show).place(x=310, y=10)


def Clear():
    name.set("")
    age.set("")
    job.set("")
    email.set("")
    gender.set("")
    mobile.set("")
    txtAddress.delete(1.0, END)


def getData(event):
    selected_row = tv.focus()
    data = tv.item(selected_row)
    global row
    row = data["values"]
    name.set(row[1])
    age.set(row[2])
    job.set(row[3])
    email.set(row[4])
    gender.set(row[5])
    mobile.set(row[6])
    txtAddress.delete(1.0, END)
    txtAddress.insert(END, row[7])


def displayAll():
    tv.delete(*tv.get_children())
    for row in db.fetch():
        tv.insert("", "end", values=row)


def add_employee():
    if txtName.get() == "" or txtAge.get() == "" or txtJob.get() == "" or txtEmail.get() == "" or comboGender.get() == "" or txtMobile.get() == "" or txtAddress.get(1.0, END) == "":
        messagebox.showerror("Error", "Please fill in all the entries")
        return
    db.insert(
        txtName.get(), txtAge.get(), txtJob.get(
        ), txtEmail.get(), comboGender.get(), txtMobile.get(), txtAddress.get(1.0, END)
    )
    messagebox.showinfo("Success", "Added new employee")
    displayAll()
    Clear()


def update_employee():
    if txtName.get() == "" or txtAge.get() == "" or txtJob.get() == "" or txtEmail.get() == "" or comboGender.get() == "" or txtMobile.get() == "" or txtAddress.get(1.0, END) == "":
        messagebox.showerror("Error", "Please fill in all the entries")
        return

    db.update(row[0], txtName.get(), txtAge.get(), txtJob.get(),
              txtEmail.get(), comboGender.get(), txtMobile.get(), txtAddress.get(1.0, END))

    messagebox.showinfo("Success", "Employee details updated successfully")
    displayAll()
    Clear()


def delete():
    db.remove(row[0])
    Clear()
    displayAll()


# ===== Buttons =====
btn_frame = Frame(entries_frame, bg=primaryColor, bd=1, relief=SOLID)
btn_frame.place(x=10, y=400, width=335, height=100)
btnAdd = Button(btn_frame, text="Add Details", command=add_employee, width=14, font=GFont,
                height=1, fg="white", bg="#16a085", bd=0).place(x=4, y=5)
btnEdit = Button(btn_frame, text="Update Details", command=update_employee, width=14, font=GFont,
                 height=1, fg="white", bg="#2980b9", bd=0).place(x=4, y=50)
btnDelete = Button(btn_frame, text="Delete Details", width=14, font=GFont,
                   height=1, fg="white", bg="#c0392b", command=delete, bd=0).place(x=170, y=5)
btnClear = Button(btn_frame, text="Clear Details", command=Clear, width=14, font=GFont,
                  height=1, fg="white", bg="#f39c12", bd=0).place(x=170, y=50)
# ===== [Table Frame] =====
tree_frame = Frame(root, bg="white")
tree_frame.place(x=365, y=0, width=875, height=610,)
style = ttk.Style()
style.configure("mystyle.Treeview", font=("Calibri", 13), rowheight=50, )
style.configure("mystyle.Treeview.Heading", font=("Calibri", 13))
tv = ttk.Treeview(tree_frame, columns=(
    1, 2, 3, 4, 5, 6, 7, 8), style="mystyle.Treeview")
tv.heading("1", text="ID")
tv.column("1", width=40)
tv.heading("2", text="Name")
tv.column("2", width=140)
tv.heading("3", text="Age")
tv.column("3", width=50)
tv.heading("4", text="Job")
tv.column("4", width=120)
tv.heading("5", text="Email")
tv.column("5", width=150)
tv.heading("6", text="Gender")
tv.column("6", width=90)
tv.heading("7", text="Mobile")
tv.column("7", width=150)
tv.heading("8", text="Address")
tv.column("8", width=150)
tv["show"] = "headings"
tv.bind("<ButtonRelease-1>", getData)
tv.place(x=1, y=1, height=610)

displayAll()

root.mainloop()
