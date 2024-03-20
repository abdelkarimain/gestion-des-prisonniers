from tkinter import *
from PIL import ImageTk, Image
from tkinter import messagebox
import pymysql
import os
from tkmacosx import Button
from window2 import *
from subprocess import call



gray="#303030"
move="#ffce00"
red="#303030"
font1=("OCR A Std",48,"bold")
font2=("OCR A Std",14,"bold")
font3=("OCR A Std",25,"bold")
##################################### Back End  #############################################
#creation de la fonction de login
def login():
    user=entry_username.get()
    code=entry_password.get()
    try:
        conn = pymysql.connect(
            host='localhost',
            user='root', 
            password = "roottaya",
            database='PrisonManagmentSysteme',
            )
    except:
        messagebox.showerror("connection","Database Connection Error")
        return

    cur = conn.cursor()
    command="select * from user where username=%s and password=%s"
    cur.execute(command,(user,code))

    result=cur.fetchone()
    if result==None:
        messagebox.showerror("INVALIDE","Invalid Password or Username")
    else:
        entry_password.delete(0, END) 
        if result[4]=="Manager":
            window_admin(entry_username.get())
        elif result[4]=="Prisoners manager":
            window_prisoner(entry_username.get())
        elif result[4]=="Visitors manager":
            window_visitor(entry_username.get())
        elif result[4]=="Guards boss":
            window_guardien(entry_username.get())  


#creation de la fonction de lafichage des donnes
def afficherPassword():
    if entry_password.cget('show')=="*":
        entry_password.config(show="")
        btn_afficher.config(text="Hide")
    else:
        entry_password.config(show="*")

        btn_afficher.configure(text="Show")

        
##################################### Front END  #############################################
# creation de fenetre window
window = Tk()
window.geometry("1135x768")
window.configure(bg = "#FFFFFF")
window.title("Connection")

width=1500
height=900


#lajout de la lariere plane image
image = Image.open("/Users/tayastudios/Desktop/prison/prison/images/image_1.png")
image =image.resize((width,height))
background_image = ImageTk.PhotoImage(image)

##creation de background de login
background_label = Label(window, image=background_image)
background_label.place(x=0, y=0, relwidth=1, relheight=1)

#la creation de frame de login
centerFrame=Frame(window,bg=move,width=400,height=500 )
centerFrame.pack(pady=170)

#creation d'label de titre(connection)
connecionLabel=Label(centerFrame,text="Connection",font=font1,bg=move,fg=gray)
connecionLabel.place(
    x=25,
    y=40,

)

#creation de label de username
usernameLabel=Label(centerFrame,text="Username",font=font3,bg=move,fg=gray)
usernameLabel.place(
    x=40,
    y=120,
    width=323,
    height=49
)
#creation d'entry de username
entry_username = Entry(centerFrame,
    bd=0,
    bg="#D9D9D9",
    fg="#000716",
    highlightthickness=4,
    font=("Consolas",15,"bold")
)
entry_username.place(
    x=40,
    y=180,
    width=323,
    height=49
)



#creation de label de password
PasswordLabel=Label(centerFrame,text="Password",font=font3,bg=move,fg=gray)
PasswordLabel.place(
    x=40,
    y=240,
    width=323,
    height=49
)
#creation d'entry de password
entry_password = Entry(centerFrame,
    bd=0,
    bg="#D9D9D9",
    fg="#000716",
    highlightthickness=4,
    font=("Consolas",15,"bold"),
    show="*"
)
entry_password.place(
    x=40,
    y=300,
    width=225,
    height=49
)

# creation de button de afficher password
btn_afficher = Button(
    centerFrame,
    text="Show",
    borderwidth=0,
    highlightthickness=0,
    relief="flat",
    bg=gray,fg=move,
    font=("Consolas", 12 ,"bold"),
    command=afficherPassword,
    borderless=1,
    padx=-2,
    pady=13
)
btn_afficher.place(
    x=270,
    y=300,
    width=90,
    height=49
)

# creation de button de login
button_login=Button(centerFrame,text="Login",borderwidth=0,highlightthickness=0,font=font3,bg=gray,fg=move ,command=login,borderless=1)
button_login.place(
    x=40,
    y=380,
    width=323,
    height=51
)





window.state("zoomed")
window.mainloop()
























