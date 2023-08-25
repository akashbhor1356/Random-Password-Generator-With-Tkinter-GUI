import random #IMPORT RANDOM MODULE
from tkinter import *

# ROOT METHODS.................................................
root = Tk()
root.geometry('800x400+350+100')
root.configure(bg='black')
root.title('Random Password Generator')

#PASSWORD GENERATE FUNCTION
def password_generate():
    # DEFINE CHARACTERS SET AS VARIABLES
    x = [1,2,3,4]
    y = [5,6,7,8]
    z = ["A","B","C","D","E"]
    w = ["!","@","#","$","%","^"]
    v = ["F","G","H","I","J"]
    u = ["&","*","+","=","-","_"]
    T = ["a","b","c","d","e"]
    global password
    #THEN JOIN THEM EACH BY RANDOMLY USING RANDOM MODULE
    password = str(random.choice(x)) + str(random.choice(v)) + random.choice(z) + random.choice(u) + str(random.choice(y)) + random.choice(v) + random.choice(T)

    #ADD VALUE TO THE LABEL
    label_2.configure(text=password)


#DEFINE TKINTER LABELS
label_1 = Label(root,text='RANDOM PASSWORD',font=('airal',40,'bold'),bg='black',fg='white')
label_1.place(x=140,y=50)

label_2 = Label(root,font=('airal',60,'bold'),bg='black',fg='yellow',bd=3)
label_2.place(x=260,y=150)

#DEFINE BUTTONS
button_1 = Button(root,bg='black',text='GENERATE',fg='white',font=('airal',25),bd=5,command=password_generate)
button_1.place(x=300,y=300)


root.mainloop()

