from tkinter import Button, Label, Tk, Text, INSERT, END

button_height = 3
button_width = 5

output = "|"
shiftval = 0               #is "SHIFT" pressed or not?
alphaval = 0               #is "ALPHA" pressed or not?
position = len(output)-1   #position of cursor

def shift_comm():
    global shiftval
    if shiftval == 0:
        shiftval=1
        shift.configure(bg="#2b2212")
    else:
        shiftval=0
        shift.configure(bg="#4a3f2b")

def alpha_comm():
    global alphaval
    if alphaval == 0:
        alphaval=1
        alpha.configure(bg="#3b1d1d")
    else:
        alphaval=0
        alpha.configure(bg="#593d3d")

def left_comm():
    global output, position
    if position != 0:
        output = output.replace("|", "")
        position = position-1
        output = output[:position] + "|" + output[position:]
        display.config(state="normal")
        display.delete('1.0', END)
        display.insert(INSERT, output)
        display.config(state="disabled")

def right_comm():
    global output, position

    if position != len(output)-1:
        output = output.replace("|", "")
        position = position+1
        output = output[:position] + "|" + output[position:]
        display.config(state="normal")
        display.delete('1.0', END)
        display.insert(INSERT, output)
        display.config(state="disabled")

def num_disp(norm_imp="", shift_imp=None):
    global output, position
    if (shiftval==1) and (not (shift_imp is None)):        #if shift is pressed and the key has a "SHIFT" value
        text=shift_imp
    else:
        text=norm_imp

    output = output[:position] + text + output[position:]
    position=position+len(text)
    display.config(state="normal")
    display.delete('1.0', END)
    display.insert(INSERT, output)
    display.config(state="disabled")

def clear_disp():
    global output, position

    output="|"
    position=0
    display.config(state="normal")
    display.delete('1.0', END)
    display.insert(INSERT, output)
    display.config(state="disabled")

def delete_key():
    global output, position

    output = output[:position-1] + output[position:]
    position=position-1
    display.config(state="normal")
    display.delete('1.0', END)
    display.insert(INSERT, output)
    display.config(state="disabled")
#---------------------------------Main Window Script-----------------------------------------------

root=Tk()
root.title("Calculator")

display = Text(root, font=("Helvetica", 16), height=3, width=18, bd=5,)
display.config(state="normal")
display.insert(INSERT, output, "justified")
display.config(state="disabled")
#------------------------GUI Buttons Definition------------------------
#Numbers
one = Button(root, text="(     \n1", command=lambda: num_disp("1", "("), height=button_height, width=button_width)
two = Button(root, text=")     \n2", command=lambda: num_disp("2", ")"), height=button_height, width=button_width)
three = Button(root, text="      \n3", command=lambda: num_disp("3"), height=button_height, width=button_width)
four = Button(root, text="      \n4", command=lambda: num_disp("4"), height=button_height, width=button_width)
five = Button(root, text="      \n5", command=lambda: num_disp("5"), height=button_height, width=button_width)
six = Button(root, text="      \n6", command=lambda: num_disp("6"), height=button_height, width=button_width)
seven = Button(root, text="      \n7", command=lambda: num_disp("7"), height=button_height, width=button_width)
eight = Button(root, text="      \n8", command=lambda: num_disp("8"), height=button_height, width=button_width)
nine = Button(root, text="      \n9", command=lambda: num_disp("9"), height=button_height, width=button_width)
zero = Button(root, text="      \n0", command=lambda: num_disp("0"), height=button_height, width=button_width)
point = Button(root, text=".", command=lambda: num_disp("."), height=button_height, width=button_width)

#Normal Operations
delete = Button(root, text="DEL", command=delete_key, height=button_height, width=button_width, bg="#d6d6d6")
clear = Button(root, text="C", command=clear_disp, height=button_height, width=button_width, bg="#d6d6d6")

multiply = Button(root, text="×", command=lambda: num_disp("×"), height=button_height, width=button_width, bg="#d6d6d6")
divide = Button(root, text="÷", command=lambda: num_disp("÷"), height=button_height, width=button_width, bg="#d6d6d6")
plus = Button(root, text="+", command=lambda: num_disp("+"), height=button_height, width=button_width, bg="#d6d6d6")
minus = Button(root, text="-", command=lambda: num_disp("-"), height=button_height, width=button_width, bg="#d6d6d6")
equals = Button(root, text="=", height=button_height, width=button_width, bg="#d6d6d6")
answer = Button(root, text="ANS", height=button_height, width=button_width, bg="#d6d6d6")
square = Button(root, text="√     \nx^2", command=lambda: num_disp("^(2)", "√"), height=button_height, width=button_width)

#Functions
alpha = Button(root, text="ALPHA", command=alpha_comm, height=button_height-1, width=button_width, bg="#593d3d", fg="#ffffff")
shift = Button(root, text="SHIFT", command=shift_comm, height=button_height-1, width=button_width, bg="#4a3f2b", fg="#ffffff")
clear_all = Button(root, text="CE", height=button_height-1, width=button_width, bg="#4a4a4a", fg="#ffffff")
right = Button(root, text="▷", command=right_comm, height=button_height-1, width=button_width, bg="#828282", fg="#ffffff")
left = Button(root, text="◁", command=left_comm, height=button_height-1, width=button_width, bg="#828282", fg="#ffffff")
#-------------------------------------GUI Def------------------------------------


#-------------------------------------GUI Displays------------------------------------
display.grid(columnspan=5)

seven.grid(row=2, column=0)
eight.grid(row=2, column=1)
nine.grid(row=2, column=2)
four.grid(row=3, column=0)
five.grid(row=3, column=1)
six.grid(row=3, column=2)
one.grid(row=4, column=0)
two.grid(row=4, column=1)
three.grid(row=4, column=2)
zero.grid(row=5, column=1)
point.grid(row=5, column=2)
delete.grid(row=2, column=3)
clear.grid(row=2, column=4)
multiply.grid(row=3, column=3)
divide.grid(row=3, column=4)
plus.grid(row=4, column=3)
minus.grid(row=4, column=4)
answer.grid(row=5, column=3)
equals.grid(row=5, column=4)
clear_all.grid(row=1, column=4)
shift.grid(row=1, column=3)
right.grid(row=1, column=2)
left.grid(row=1, column=1)
alpha.grid(row=1, column=0)
square.grid(row=5, column=0)
#-------------------------------------GUI Displays------------------------------------

root.mainloop() 