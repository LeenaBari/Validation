from  tkinter import *
root=Tk()
root.title('Codemy.com')
root.geometry("400x400")

def number():
    try:
        float(my_box.get())
        answer.config(text="That is number! Congrates!")
    except ValueError:
        answer.config(text="That is not number!")

my_label=Label(root,text="Enter a Number")
my_label.pack(pady=20)

my_box=Entry(root)
my_box.pack(pady=10)

my_button=Button(root,text="Submit",command=number)
my_button.pack(pady=5)

answer=Label(root,text='')
answer.pack(pady=20)









root.mainloop()