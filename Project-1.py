from tkinter import *
from tkinter import font

root = Tk()
root.title("Band Name Generator")
root.geometry("450x450")
root.configure(bg='light blue')

bold_font = font.Font(family="Helvetica", size=14, weight="bold")
Label(root, text="Band Name Generator", font=bold_font).place(x=100, y=10)

Label(root, text="Name", font='Helvetica').place(x=30, y=50)
Label(root, text="Pet Name", font='Helvetica').place(x=30, y=90)

name_entry = Entry(root)
name_entry.place(x=140, y=50)

pet_entry = Entry(root)
pet_entry.place(x=140, y=90)

result_var=StringVar() # create a string variable to hold  result.
result_label = Label(root, textvariable=result_var, font=("Helvetica", 16, "bold"), fg="blue")
result_label.place(x=140, y=280)


def on_click():
    text_output1 = name_entry.get()
    text_output2 = pet_entry.get()
    result_var.set(text_output1 + " " + text_output2)# update variable with results
    
button=Button(root, text="Click Me!", command=on_click, bg="#008CBA", fg="white", activebackground="#4CAF50", activeforeground="white", bd=0, padx=20, pady=10, font=("Helvetica", 12, "bold"))
button.place(x=140, y=200)


root.mainloop()
