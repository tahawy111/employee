from tkinter import *
from tkinter import ttk

root = Tk()
# ===== Globals =====
GFont = ("Calibri", 16)
primaryColor = "#2c3e50"

root.title("Employee Management System")
root.geometry("1210x615+0+0")
root.resizable(False, False)
root.configure(bg=primaryColor)


logo = PhotoImage(file="logo.png")
lbl_logo = Label(root, image=logo, bg=primaryColor)
lbl_logo.place(x=80, y=520,)

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
txtName = Entry(entries_frame, width=20, font=GFont,)
txtName.place(x=120, y=50)
# Job Input
lblJob = Label(entries_frame, text="Job",
               font=GFont, bg=primaryColor, fg="white",)
lblJob.place(x=10, y=90)
txtJob = Entry(entries_frame, width=20, font=GFont,)
txtJob.place(x=120, y=90)
# Gender Combobox
lblGender = Label(entries_frame, text="Gender",
                  font=GFont, bg=primaryColor, fg="white",)
lblGender.place(x=10, y=130)
comboGender = ttk.Combobox(
    entries_frame, state="readonly", width=18, font=GFont)
comboGender["values"] = ("Male", "Female")
comboGender.place(x=120, y=130)
# Age Input
lblAge = Label(entries_frame, text="Age",
               font=GFont, bg=primaryColor, fg="white",)
lblAge.place(x=10, y=170)
txtAge = Entry(entries_frame, width=20, font=GFont,)
txtAge.place(x=120, y=170)
# Email Input
lblEmail = Label(entries_frame, text="Email",
                 font=GFont, bg=primaryColor, fg="white",)
lblEmail.place(x=10, y=210)
txtEmail = Entry(entries_frame, width=20, font=GFont,)
txtEmail.place(x=120, y=210)
# Contact Input
lblContact = Label(entries_frame, text="Mobile",
                   font=GFont, bg=primaryColor, fg="white",)
lblContact.place(x=10, y=250)
txtContact = Entry(entries_frame, width=20, font=GFont,)
txtContact.place(x=120, y=250)
# Address Input
lblAddress = Label(entries_frame, text="Address:",
                   font=GFont, bg=primaryColor, fg="white",)
lblAddress.place(x=10, y=290)
txtAddress = Text(entries_frame, width=30, height=2, font=GFont)
txtAddress.place(x=10, y=330)

# ===== Buttons =====
btn_frame = Frame(entries_frame, bg=primaryColor, bd=1, relief=SOLID)
btn_frame.place(x=10, y=400, width=335, height=100)
btnAdd = Button(btn_frame, text="Add Details", width=14, font=GFont,
                height=1, fg="white", bg="#16a085", bd=0).place(x=4, y=5)
btnEdit = Button(btn_frame, text="Update Details", width=14, font=GFont,
                 height=1, fg="white", bg="#2980b9", bd=0).place(x=4, y=50)
btnDelete = Button(btn_frame, text="Delete Details", width=14, font=GFont,
                   height=1, fg="white", bg="#c0392b", bd=0).place(x=170, y=5)
btnClear = Button(btn_frame, text="Clear Details", width=14, font=GFont,
                  height=1, fg="white", bg="#f39c12", bd=0).place(x=170, y=50)
# ===== [Table Frame] =====
tree_frame = Frame(root, bg="white")
tree_frame.place(x=365, y=0, width=875, height=610)
style = ttk.Style()
style.configure("mystyle.Treeview", font=("Calibri", 13), rowheight=50)
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
tv.column("8", width=120)
tv["show"] = "headings"
tv.pack()


root.mainloop()
