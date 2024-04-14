from tkinter import *
from tkinter import font

root = Tk()
root.title("Tip Calculator")
root.geometry("450x450")
root.configure(bg='purple')

bold_font = font.Font(family="Helvetica", size=14, weight="bold")
Label(root, text="Tip Calculator", font=bold_font).place(x=130, y=10)

Label(root, text="Total Bill", font='Helvetica').place(x=30, y=50)
Label(root, text="Your Tip", font='Helvetica').place(x=30, y=95)
Label(root, text="No.People", font='Helvetica').place(x=30, y=140)

Totalbill_entry=Entry(root)
Totalbill_entry.place(x=140, y=50)

Yourtip_entry = Entry(root)
Yourtip_entry.place(x=140, y=95)


No_people = Entry(root)
No_people.place(x=140, y=140)

    
def on_click():
    text_output1 = Yourtip_entry.get()
    text_output2 = Totalbill_entry.get()
    text_output3 = No_people.get()
    result_var.set(f'{int(text_output2) + int(text_output1)*int(text_output3)/int(text_output3)-int(text_output2)} is money for you to Split')

result_var=IntVar() # create a integer variable to hold  result.
result_label = Label(root, textvariable=result_var, font=("Helvetica", 16, "bold"), fg="blue")
result_label.place(x=50, y=280)
    
button=Button(root, text="Click Me!",  bg="#008CBA",command=on_click, fg="white", activebackground="#4CAF50", activeforeground="white", bd=0, padx=20, pady=10, font=("Helvetica", 12, "bold"))#command=on_click
button.place(x=140, y=200)

root.mainloop()

