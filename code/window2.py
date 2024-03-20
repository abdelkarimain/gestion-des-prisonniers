from tkinter import *
import pymysql
import mysql.connector
from mysql.connector import Error
import io
from tkinter import ttk,messagebox,filedialog
import pandas
from PIL import ImageTk, Image
from tkmacosx import Button
from tkmacosx import *
from fpdf import FPDF
from subprocess import call
import pyttsx3
from termcolor import colored


gray="#ffaa00"
move="#ccc"
red="#303030"
font1=("OCR A Std",48,"italic")
font2=("OCR A Std",35,"bold")
font3=("OCR A Std",20,"bold")
font4=("OCR A Std",25,"bold")
############################################################# 
 
#=========== fonction pour vider le contenu du frame
def delete_frames():
    for frame in rightFrame.winfo_children():
        frame.destroy()
        
#===== fonction pour vider et afficher une nouveau contenu au frame       
def showIndicator(page):
    delete_frames()
    page()

def showIndicator2(page,a):
    delete_frames()
    page(a)

#===== fonction pour creer le contenu du frame acceuil
def acceuil_frame(username):
    con=pymysql.connect(host="localhost",user="root",password="roottaya")
    mycursor=con.cursor()
    query="use prisonmanagmentsysteme"
    mycursor.execute(query)
    query= "select firstname,lastname from user where username=%s"
    mycursor.execute(query,username)
    username_data=mycursor.fetchall()
    
    nom=username_data[0][0]
    prenom=username_data[0][1]

    # ADD WAHD LIMAGE OFF USER
    btn_profile.config(bg="white")
    btn_informations.config(bg="white")
    btn_Home.config(bg="#BDBD3A")
    btn_securite.config(bg="white")
    btn_parametre.config(bg="white")
    #==========================================

    frame4=Frame(rightFrame,bg="#303030")
    frame4.pack()
    frame4.pack_propagate(False)
    frame4.configure(width=900,height=700)
    
    nom_label=Label(frame4,text=f"Welcome Mr(s){str(prenom)} {str(nom)} ",font=font1)
    nom_label.pack(pady=60)
    txt="""
At the end of the day, you
put all the work in, and
eventually it’ll pay off. It
could be in a year, it could
be in 30 years. Eventually,
your hard work will pay
off.
Kevin Hart
"""

    nom_label=Label(frame4,text=txt,font=font2,borderwidth=5,bg=gray, relief="solid")
    nom_label.pack(pady=60,padx=90)
    
    

#===== fonction pour creer le contenu du frame profile
def profile_frame():
    global img_prisonnier,btn_prisonnier,img_guard,btn_guard,img_visitor,btn_visitor,img_username,btn_username
    #--------------------------------------------
    btn_profile.config(bg="#BDBD3A")
    btn_informations.config(bg="white")
    btn_Home.config(bg="white")
    btn_securite.config(bg="white")
    btn_parametre.config(bg="white")
    
    #--------------------------------------------
    frame1=Frame(rightFrame,bg="#303030")
    frame1.pack()
    frame1.pack_propagate(False)
    frame1.configure(width=900,height=700)
    #--------------------------------------------
    # Button prisonnier 
    def callprisoner():
        root.withdraw()
        call(["python3","/Users/tayastudios/Desktop/complete/seperatedprisonnier/prisoner.py"])
        root.deiconify()

    img_prisonnier = PhotoImage(
    file=("/Users/tayastudios/Desktop/complete/seperatedprisonnier/images/button_1.png"))
    btn_prisonnier = Button(frame1,
        image=img_prisonnier,
        borderwidth=0,
        highlightthickness=0,
        command=callprisoner,
        relief="flat",
        width=304,
        height=175,
        borderless=1
    )
    btn_prisonnier.grid(row=0,column=0,padx=80,pady=120)

    # Button Gardien

    def callGuardien():
        root.withdraw()
        call(["python3","/Users/tayastudios/Desktop/complete/seperatedprisonnier/gards.py"])
        root.deiconify()


    img_guard = PhotoImage(
        file=("/Users/tayastudios/Desktop/complete/seperatedprisonnier/images/button_2.png"))
    btn_guard = Button(frame1,
        image=img_guard,
        borderwidth=0,
        highlightthickness=0,
        command=callGuardien,
        relief="flat",
        width=304,
        height=175,
        borderless=1
    )
    btn_guard.grid(row=0,column=1,padx=80,pady=120)

    # button Visiteur

    def callvisitor():
        root.withdraw()
        call(["python3","/Users/tayastudios/Desktop/complete/seperatedprisonnier/visitors.py"])
        root.deiconify()


    img_visitor = PhotoImage(
        file=("/Users/tayastudios/Desktop/complete/seperatedprisonnier/images/button_3.png"))
    btn_visitor = Button(frame1,
        image=img_visitor,
        borderwidth=0,
        highlightthickness=0,
        command=callvisitor,
        relief="flat",
        width=304,
        height=175,
        borderless=1
    )
    btn_visitor.grid(row=1,column=0,padx=80,pady=0)

    # button Utilisateur


    def calluser():
        root.withdraw()
        call(["python3","/Users/tayastudios/Desktop/complete/seperatedprisonnier/user.py"])
        root.deiconify()


    img_username = PhotoImage(
        file=("/Users/tayastudios/Desktop/complete/seperatedprisonnier/images/button_4.png"))
    btn_username = Button(frame1,
        image=img_username,
        borderwidth=0,
        highlightthickness=0,
        command=calluser,
        relief="flat",
        width=304,
        height=175,
        borderless=1

    )
    btn_username.grid(row=1,column=1,padx=80,pady=0)
#===== fonction pour creer le contenu du frame profile de prisonier
def profile_frame_prisoner():
    global img_prisonnier,btn_prisonnier,img_guard,btn_guard,img_visitor,btn_visitor,img_username,btn_username
    #--------------------------------------------
    btn_profile.config(bg="#BDBD3A")
    btn_informations.config(bg="white")
    btn_Home.config(bg="white")
    btn_securite.config(bg="white")
    btn_parametre.config(bg="white")
    
    #--------------------------------------------
    frame1=Frame(rightFrame,bg="#303030")
    frame1.pack()
    frame1.pack_propagate(False)
    frame1.configure(width=900,height=700)
    #--------------------------------------------
    # Button prisonnier 
    def callprisoner():
        root.withdraw()
        call(["python3","/Users/tayastudios/Desktop/complete/seperatedprisonnier/prisoner.py"])
        root.deiconify()

    img_prisonnier = PhotoImage(
    file=("/Users/tayastudios/Desktop/complete/seperatedprisonnier/images/button_1v.png"))
    btn_prisonnier = Button(frame1,
        image=img_prisonnier,
        borderwidth=0,
        highlightthickness=0,
        command=callprisoner,
        relief="flat",
        width=500,
        height=288,
        borderless=1
    )
    btn_prisonnier.pack(pady=200)


#===== fonction pour creer le contenu du frame profile de guardian
def profile_frame_guardien():
    global img_prisonnier,btn_prisonnier,img_guard,btn_guard,img_visitor,btn_visitor,img_username,btn_username
    #--------------------------------------------
    btn_profile.config(bg="#BDBD3A")
    btn_informations.config(bg="white")
    btn_Home.config(bg="white")
    btn_securite.config(bg="white")
    btn_parametre.config(bg="white")
    
    #--------------------------------------------
    frame1=Frame(rightFrame,bg="#303030")
    frame1.pack()
    frame1.pack_propagate(False)
    frame1.configure(width=900,height=700)
    #--------------------------------------------

    # Button Gardien
    def callGuardien():
        root.withdraw()
        call(["python3","/Users/tayastudios/Desktop/complete/seperatedprisonnier/gards.py"])
        root.deiconify()


    img_guard = PhotoImage(
        file=("/Users/tayastudios/Desktop/complete/seperatedprisonnier/images/button_2v.png"))
    btn_guard = Button(frame1,
        image=img_guard,
        borderwidth=0,
        highlightthickness=0,
        command=callGuardien,
        relief="flat",
        width=500,
        height=288,
        borderless=1
    )
    
    btn_guard.pack(pady=200)

#===== fonction pour creer le contenu du frame profile de visitor
def profile_frame_visitor():
    global img_prisonnier,btn_prisonnier,img_guard,btn_guard,img_visitor,btn_visitor,img_username,btn_username
    #--------------------------------------------
    btn_profile.config(bg="#BDBD3A")
    btn_informations.config(bg="white")
    btn_Home.config(bg="white")
    btn_securite.config(bg="white")
    btn_parametre.config(bg="white")
    
    #--------------------------------------------
    frame1=Frame(rightFrame,bg="#303030")
    frame1.pack()
    frame1.pack_propagate(False)
    frame1.configure(width=900,height=700)
    #--------------------------------------------

    # button Visiteur

    def callvisitor():
        root.withdraw()
        call(["python3","/Users/tayastudios/Desktop/complete/seperatedprisonnier/visitors.py"])
        root.deiconify()


    img_visitor = PhotoImage(
        file=("/Users/tayastudios/Desktop/complete/seperatedprisonnier/images/button_3v.png"))
    btn_visitor = Button(frame1,
        image=img_visitor,
        borderwidth=0,
        highlightthickness=0,
        command=callvisitor,
        relief="flat",
        width=500,
        height=288,
        borderless=1
    )
    btn_visitor.grid(row=1,column=0,padx=80,pady=0)

    btn_visitor.pack(pady=200)

##################
######
###
#


#===== fonction pour creer le contenu du frame informations
def info_frame(username):
    global frame2, affiche_img,nom,prenom,gender,id
    #==========================================
    btn_profile.config(bg="white")
    btn_informations.config(bg="#BDBD3A")
    btn_Home.config(bg="white")
    btn_securite.config(bg="white")
    btn_parametre.config(bg="white")
    #==========================================

    frame2=Frame(rightFrame,bg="#303030")
    frame2.pack()
    frame2.pack_propagate(False)
    frame2.configure(width=900,height=700)
    #==========================================
    con=pymysql.connect(host="localhost",user="root",password="roottaya") 
    mycursor=con.cursor()
    query="use prisonmanagmentsysteme"
    mycursor.execute(query)
    query= "select firstname,lastname,gender,image from user where username=%s"
    mycursor.execute(query,username)
    username_data=mycursor.fetchall()
    
    id=username
    nom=username_data[0][0]
    prenom=username_data[0][1]
    gender=username_data[0][2]
    photo_filename=username_data[0][3]
    #==========================================
    
    # convert the binary data to a PIL Image object
    image = Image.open(photo_filename)
           
    resize_image = image.resize((300, 300))        
    affiche_img = ImageTk.PhotoImage(resize_image) 
    image_label = Label(frame2,image=affiche_img)
    image_label.pack(pady=30)
    #==========================================
    id_label=Label(frame2,text="usernamen : "+str(id),font=font2)
    id_label.pack(pady=10)
    
    nom_label=Label(frame2,text="First Name : "+str(nom),font=font2)
    nom_label.pack(pady=10)
    
    prenom_label=Label(frame2,text="Last Name : "+str(prenom),font=font2)
    prenom_label.pack(pady=10)
    
    gender_label=Label(frame2,text="Gender : "+str(gender),font=font2)
    gender_label.pack(pady=10)
    
    
#===== fonction pour creer le contenu du frame parametre
file_path=""
def valider_modification(username):
    global file_path
    # Connect to the MySQL database
    try:
        connection = pymysql.connect(
            host="localhost",
            user="root",
            password="roottaya",
            database="prisonmanagmentsysteme"
        )
        

            # creer table username
        cursor = connection.cursor()
        try:  


            if file_path=="":
                file_path=photo_filename       

            sql="UPDATE user SET firstname =%s ,lastname =%s ,gender =%s,image =%s WHERE username=%s"
            val = (entry_nom.get(),entry_prenom.get(),entry_gender.get(),file_path,username)
            # Execute the SQL statement
            cursor.execute(sql, val)
            connection.commit()
            messagebox.showinfo("Enfo","Data Updated Succusfully")
        except :
            messagebox.showerror("ERROR",f"Insert Error")

    except :
        messagebox.showerror("ERROR",f"Database Connection Error")
    

#l'apload de limage
binary_data=[]
def uploadImg():
    global binary_data, file_path,lab_photo,affiche_img,resize_image
    for elt in img_Label.winfo_children():
        elt.destroy()
    # Show the file dialog and allow username to select an image

    f_types = [('Jpg Files', '*.jpg'),('PNG Files','*.png'),('jpeg Files','*.jbeg')]   # type of files to select
    file_path =filedialog.askopenfilename(multiple=True,filetypes=f_types)

    
    try:
        image = Image.open(file_path[0])
        resize_image = image.resize((300, 300))
        affiche_img = ImageTk.PhotoImage(resize_image)
        img_Label.config(image=affiche_img)
    except:
        pass

# les parametres de frame   
def parametre_frame(username):
    global entry_nom,entry_prenom,entry_adresse,entry_email,entry_gender,entry_telephone,frame3,img_Label,show_img,lab_photo,photo_filename
    
    btn_profile.config(bg="white")
    btn_informations.config(bg="white")
    btn_Home.config(bg="white")
    btn_securite.config(bg="white")
    btn_parametre.config(bg="#BDBD3A")
    
    frame3=Frame(rightFrame,bg="#303030")
    frame3.pack()
    frame3.pack_propagate(False)
    frame3.configure(width=920,height=580)
    
    # labels/entry pour modification
    img_Label =Label(frame3, text="")
    img_Label.grid(row=0,column=1,pady=30)
    btn_upload_img = Button(frame3,text="Upload Image", fg="#303030",bg="#FFCE00",font=font4,borderless=1, command= uploadImg)
    btn_upload_img.grid(row=0,column=0,pady=20)
    
    lab_nom=Label(frame3,text="Nom :",bg="#303030",fg="white",font=font4)
    lab_nom.grid(row=1,column=0,pady=20,sticky=W)
    entry_nom=Entry(frame3,font=font4)
    entry_nom.grid(row=1,column=1,pady=20)
    entry_nom.focus()
    
    lab_prenom=Label(frame3,text="Prenom :",bg="#303030",fg="white",font=font4)
    lab_prenom.grid(row=2,column=0,pady=20,sticky=W)
    entry_prenom=Entry(frame3,font=font4)
    entry_prenom.grid(row=2,column=1,pady=20)
   
    
    lab_gender=Label(frame3, text = "Gendre :",font=font4,bg="#303030",fg="white")
    lab_gender.grid(row=3,column=0,pady=20,sticky=W)
    entry_gender = StringVar()
    gendre = ttk.Combobox(frame3,font=font4,textvariable = entry_gender)
    gendre['values'] = ('Homme','Femme')
    gendre.grid(row=3,column=1,pady=20)
    gendre.current(0)
    
    
    con=pymysql.connect(host="localhost",user="root",password="roottaya") 
    mycursor=con.cursor()
    query="use prisonmanagmentsysteme"
    mycursor.execute(query)
    query= "select firstname,lastname,image from user where username=%s"
    mycursor.execute(query,username)
    username_data=mycursor.fetchall()
    
    nom=username_data[0][0]
    prenom=username_data[0][1]
    photo_filename=username_data[0][2]
    
    entry_nom.insert(0, str(nom))
    entry_prenom.insert(0,str(prenom))
    img2 = Image.open(photo_filename)

    resized_image = img2.resize((300, 300))
    show_img = ImageTk.PhotoImage(resized_image)
    lab_photo = Label(img_Label,image=show_img)
    lab_photo["image"] = show_img
    lab_photo.pack()
    
    btn_valider = Button(frame3,text="Valider", fg="#303030",bg="#53B332",font=font2,borderless=1,command=lambda:valider_modification(username))
    btn_valider.grid(row=4,columnspan=2,pady=20)

#===== fonction pour creer le contenu du frame securite
def valider_password(username):
    try:
        connection = pymysql.connect(
            host="localhost",
            user="root",
            password="roottaya",
            database="prisonmanagmentsysteme"
        )
        cursor = connection.cursor()
        query1= """select password from user WHERE username= '%s'""" %username
        cursor.execute(query1)
        password_data=cursor.fetchall()
       
        passw=str(password_data[0][0]) 
        try:
            if passw==entry_pass_old.get():
                if entry_new_pass.get()==entry_confirm_pass.get():
                    sql="UPDATE user SET password =%s WHERE username=%s"
                    val = (entry_new_pass.get(),username)
                    # Execute the SQL statement
                    cursor.execute(sql, val)
                    connection.commit()
                    messagebox.showinfo("done","password changed")
                else:
                    messagebox.showerror("ERROR","confirm password entry is incorrect!")
            else:
                messagebox.showerror("ERROR","old password entry is incorrect!")
        except Error as e1:
            messagebox.showerror("ERROR",f"erreur d'insersion :{e1}")

    except Error as e2:
        messagebox.showerror("ERROR",f"Error while connecting to MySQL :{e2}")
        print(e2)

#function de  changement de password
def securite_frame(username):
    global frame4,entry_new_pass,entry_confirm_pass,entry_pass_old,lab_pass_old,lab_new_pass,lab_confirm_pass,btn_valider
    btn_profile.config(bg="white")
    btn_informations.config(bg="white")
    btn_Home.config(bg="white")
    btn_securite.config(bg="#BDBD3A")
    btn_parametre.config(bg="white")
    frame4=Frame(rightFrame,bg="#303030")
    frame4.pack()
    frame4.pack_propagate(False)
    frame4.configure(width=920,height=580)
    
    lab_pass_old=Label(frame4,text="Mot de passe actuelle :",bg="#303030",fg="white",font=font4)
    lab_pass_old.place(x=240,y=50)
    entry_pass_old=Entry(frame4,font=font4)
    entry_pass_old.place(x=215,y=120,width=500,height=50)
    entry_pass_old.focus()
    
    lab_new_pass=Label(frame4,text="Nouveau mot de passe :",bg="#303030",fg="white",font=font4)
    lab_new_pass.place(x=240,y=190)
    entry_new_pass=Entry(frame4,font=font4,show="*")
    entry_new_pass.place(x=215,y=260,width=500,height=50)
    
    lab_confirm_pass=Label(frame4,text="Confirmer le mot de passe :",bg="#303030",fg="white",font=font4)
    lab_confirm_pass.place(x=240,y=330)
    entry_confirm_pass=Entry(frame4,font=font4,show="*")
    entry_confirm_pass.place(x=215,y=400,width=500,height=50)
    
    btn_valider = Button(frame4,text="Valider", fg="#303030",bg="#53B332",font=font4,borderless=1,command=lambda:valider_password(username))
    btn_valider.place(x=330, y=500, width= 300 , height=60)

#===== fonction pour creer le contenu du frame Logout
def exit_frame():
    global frame1
    btn_profile.config(bg="white")
    btn_informations.config(bg="white")
    btn_Home.config(bg="white")
    btn_securite.config(bg="white")
    btn_parametre.config(bg="white")
    frame1=Frame(rightFrame,bg="#303030")
    frame1.pack()
    frame1.pack_propagate(False)
    frame1.configure(width=900,height=700)
    sure = messagebox.askyesno("Logout","Are you sure you want to logout ?", parent=root)
    if sure:
        root.destroy()


# la creation de fenetre de ladmine
def window_admin(username):

    
    global root,leftFrame,rightFrame,topFrame,btn_Home,btn_profile,btn_parametre,btn_securite,btn_Logout,btn_informations,logo_image,titlelabel,logo_Label  
    root=Toplevel() 
    root.config(background = gray) 
    root.geometry("3174x2780+0+5")
    root.title("Prison Managment Systeme")
    root.state("zoomed")
    root.config(background=gray)



    ########################################################
    #                      topframe                      #
    ########################################################
    topFrame=Frame(root,bg=gray)
    topFrame.place(x=400,y=5,width=900,height=100)

    titlelabel=Label(topFrame,text="Prison Management System",font=font1,bg=gray,fg="black")
    titlelabel.pack(pady=10)

    ########################################################
    #               leftframe /right frame                 #
    ########################################################
    leftFrame=Frame(root,bg=gray)
    leftFrame.place(x=50,y=30,width=300,height=800)

    rightFrame=Frame(root,bg="#303030")
    rightFrame.place(x=400,y=110,width=950,height=700)



    logo_image=PhotoImage(file="/Users/tayastudios/Desktop/complete/seperatedprisonnier/images/Seal_of_the_Federal_Bureau_of_Prisons copy 3.svg.png")
    logo_Label=Label(leftFrame,image=logo_image,bg=gray)
    logo_Label.pack()


    # button Home
    btn_Home = Button(leftFrame,
        text="Home",
        borderwidth=0,
        highlightthickness=0,
        command=lambda:showIndicator2(acceuil_frame,username),
        relief="flat",
        font=font3, 
        width=291,
        height=58,
        borderless=1

    )
    btn_Home.pack(pady=20)




    # button profile
    btn_profile = Button(leftFrame,
        text="Profile",
        borderwidth=0,
        highlightthickness=0,
        command=lambda:showIndicator(profile_frame),
        relief="flat",
        font=font3, 
        width=291,
        height=58,
        borderless=1

    )
    btn_profile.pack(pady=20)



    btn_informations = Button(leftFrame,
        text="Informations",
        borderwidth=0,
        highlightthickness=0,
        command=lambda:showIndicator2(info_frame,username),
        relief="flat",
        font=font3,
        width=291,
        height=58,
        borderless=1,

    )
    btn_informations.pack(pady=20)

    #button Parametres
    btn_parametre = Button(leftFrame,
        text="Parametres",
        borderless=1,
        command=lambda:showIndicator2(parametre_frame,username),
        font=font3,
        width=291,
        height=58,
    )
    btn_parametre.pack(pady=20)


    # button securite
    btn_securite = Button(leftFrame,
        text="Security",
        borderwidth=0,
        highlightthickness=0,
        command=lambda: showIndicator2(securite_frame,username),
        relief="flat",
        font=font3,
        width=291,
        height=58,
        borderless=1,

    )
    btn_securite.pack(pady=20)

    # button Logout
    btn_Logout = Button(leftFrame,text="Logout",
        borderwidth=0,
        bg="#B92B2B",
        highlightthickness=0,
        command=exit_frame,
        relief="flat",
        font=font3,
        width=291,
        height=58,
        borderless=1,

    )
    btn_Logout.pack(pady=20)
    showIndicator2(acceuil_frame,username)
    ##############################################################

    root.mainloop()


# la creation de fenetre de prisonier
def window_prisoner(username):

    
    global root,leftFrame,rightFrame,topFrame,btn_Home,btn_profile,btn_parametre,btn_securite,btn_Logout,btn_informations,logo_image,titlelabel,logo_Label  
    root=Toplevel() 
    root.config(background = gray) 
    root.geometry("3174x2780+0+5")
    root.title("Prison Managment Systeme")
    root.state("zoomed")
    root.config(background=gray)

    ########################################################
    #                      topframe                      #
    ########################################################
    topFrame=Frame(root,bg=gray)
    topFrame.place(x=400,y=5,width=900,height=100)

    titlelabel=Label(topFrame,text="Prison Management System",font=font1,bg=gray,fg="black")
    titlelabel.pack(pady=10)

    ########################################################
    #               leftframe /right frame                 #
    ########################################################
    leftFrame=Frame(root,bg=gray)
    leftFrame.place(x=50,y=30,width=300,height=800)

    rightFrame=Frame(root,bg="#303030")
    rightFrame.place(x=400,y=110,width=950,height=700)



    logo_image=PhotoImage(file="/Users/tayastudios/Desktop/complete/seperatedprisonnier/images/Seal_of_the_Federal_Bureau_of_Prisons copy 3.svg.png")
    logo_Label=Label(leftFrame,image=logo_image,bg=gray)
    logo_Label.pack()


    # button Home
    btn_Home = Button(leftFrame,
        text="Home",
        borderwidth=0,
        highlightthickness=0,
        command=lambda:showIndicator2(acceuil_frame,username),
        relief="flat",
        font=font3, 
        width=291,
        height=58,
        borderless=1

    )
    btn_Home.pack(pady=20)




    # button profile
    btn_profile = Button(leftFrame,
        text="Profile",
        borderwidth=0,
        highlightthickness=0,
        command=lambda:showIndicator(profile_frame_prisoner),
        relief="flat",
        font=font3, 
        width=291,
        height=58,
        borderless=1

    )
    btn_profile.pack(pady=20)



    btn_informations = Button(leftFrame,
        text="Informations",
        borderwidth=0,
        highlightthickness=0,
        command=lambda:showIndicator2(info_frame,username),
        relief="flat",
        font=font3,
        width=291,
        height=58,
        borderless=1,

    )
    btn_informations.pack(pady=20)

    #button Parametres
    btn_parametre = Button(leftFrame,
        text="Parametres",
        borderless=1,
        command=lambda:showIndicator2(parametre_frame,username),
        font=font3,
        width=291,
        height=58,
    )
    btn_parametre.pack(pady=20)


    # button securite
    btn_securite = Button(leftFrame,
        text="Security",
        borderwidth=0,
        highlightthickness=0,
        command=lambda: showIndicator2(securite_frame,username),
        relief="flat",
        font=font3,
        width=291,
        height=58,
        borderless=1,

    )
    btn_securite.pack(pady=20)

    # button Logout
    btn_Logout = Button(leftFrame,text="Logout",
        borderwidth=0,
        bg="#B92B2B",
        highlightthickness=0,
        command=exit_frame,
        relief="flat",
        font=font3,
        width=291,
        height=58,
        borderless=1,

    )
    btn_Logout.pack(pady=20)
    showIndicator2(acceuil_frame,username)
    ##############################################################
    root.mainloop()


# la creation de fenetre de guardien
def window_guardien(username):
    
    global root,leftFrame,rightFrame,topFrame,btn_Home,btn_profile,btn_parametre,btn_securite,btn_Logout,btn_informations,logo_image,titlelabel,logo_Label  
    root=Toplevel() 
    root.config(background = gray) 
    root.geometry("3174x2780+0+5")
    root.title("Prison Managment Systeme")
    root.state("zoomed")
    root.config(background=gray)

    ########################################################
    #                      topframe                      #
    ########################################################
    topFrame=Frame(root,bg=gray)
    topFrame.place(x=400,y=5,width=900,height=100)

    titlelabel=Label(topFrame,text="Prison Management System",font=font1,bg=gray,fg="black")
    titlelabel.pack(pady=10)

    ########################################################
    #               leftframe /right frame                 #
    ########################################################
    leftFrame=Frame(root,bg=gray)
    leftFrame.place(x=50,y=30,width=300,height=800)

    rightFrame=Frame(root,bg="#303030")
    rightFrame.place(x=400,y=110,width=950,height=700)



    logo_image=PhotoImage(file="/Users/tayastudios/Desktop/complete/seperatedprisonnier/images/Seal_of_the_Federal_Bureau_of_Prisons copy 3.svg.png")
    logo_Label=Label(leftFrame,image=logo_image,bg=gray)
    logo_Label.pack()


    # button Home
    btn_Home = Button(leftFrame,
        text="Home",
        borderwidth=0,
        highlightthickness=0,
        command=lambda:showIndicator2(acceuil_frame,username),
        relief="flat",
        font=font3, 
        width=291,
        height=58,
        borderless=1

    )
    btn_Home.pack(pady=20)




    # button profile
    btn_profile = Button(leftFrame,
        text="Profile",
        borderwidth=0,
        highlightthickness=0,
        command=lambda:showIndicator(profile_frame_guardien),
        relief="flat",
        font=font3, 
        width=291,
        height=58,
        borderless=1

    )
    btn_profile.pack(pady=20)



    btn_informations = Button(leftFrame,
        text="Informations",
        borderwidth=0,
        highlightthickness=0,
        command=lambda:showIndicator2(info_frame,username),
        relief="flat",
        font=font3,
        width=291,
        height=58,
        borderless=1,

    )
    btn_informations.pack(pady=20)

    #button Parametres
    btn_parametre = Button(leftFrame,
        text="Parametres",
        borderless=1,
        command=lambda:showIndicator2(parametre_frame,username),
        font=font3,
        width=291,
        height=58,
    )
    btn_parametre.pack(pady=20)


    # button securite
    btn_securite = Button(leftFrame,
        text="Security",
        borderwidth=0,
        highlightthickness=0,
        command=lambda: showIndicator2(securite_frame,username),
        relief="flat",
        font=font3,
        width=291,
        height=58,
        borderless=1,

    )
    btn_securite.pack(pady=20)

    # button Logout
    btn_Logout = Button(leftFrame,text="Logout",
        borderwidth=0,
        bg="#B92B2B",
        highlightthickness=0,
        command=exit_frame,
        relief="flat",
        font=font3,
        width=291,
        height=58,
        borderless=1,

    )
    btn_Logout.pack(pady=20)
    showIndicator2(acceuil_frame,username)
    ##############################################################
    root.mainloop()


# la creation de fenetre de visitor
def window_visitor(username):
    
    global root,leftFrame,rightFrame,topFrame,btn_Home,btn_profile,btn_parametre,btn_securite,btn_Logout,btn_informations,logo_image,titlelabel,logo_Label  
    root=Toplevel() 
    root.config(background = gray) 
    root.geometry("3174x2780+0+5")
    root.title("Prison Managment Systeme")
    root.state("zoomed")
    root.config(background=gray)

    ########################################################
    #                      topframe                      #
    ########################################################
    topFrame=Frame(root,bg=gray)
    topFrame.place(x=400,y=5,width=900,height=100)

    titlelabel=Label(topFrame,text="Prison Management System",font=font1,bg=gray,fg="black")
    titlelabel.pack(pady=10)

    ########################################################
    #               leftframe /right frame                 #
    ########################################################
    leftFrame=Frame(root,bg=gray)
    leftFrame.place(x=50,y=30,width=300,height=800)

    rightFrame=Frame(root,bg="#303030")
    rightFrame.place(x=400,y=110,width=950,height=700)



    logo_image=PhotoImage(file="/Users/tayastudios/Desktop/complete/seperatedprisonnier/images/Seal_of_the_Federal_Bureau_of_Prisons copy 3.svg.png")
    logo_Label=Label(leftFrame,image=logo_image,bg=gray)
    logo_Label.pack()


    # button Home
    btn_Home = Button(leftFrame,
        text="Home",
        borderwidth=0,
        highlightthickness=0,
        command=lambda:showIndicator2(acceuil_frame,username),
        relief="flat",
        font=font3, 
        width=291,
        height=58,
        borderless=1

    )
    btn_Home.pack(pady=20)




    # button profile
    btn_profile = Button(leftFrame,
        text="Profile",
        borderwidth=0,
        highlightthickness=0,
        command=lambda:showIndicator(profile_frame_visitor),
        relief="flat",
        font=font3, 
        width=291,
        height=58,
        borderless=1

    )
    btn_profile.pack(pady=20)



    btn_informations = Button(leftFrame,
        text="Informations",
        borderwidth=0,
        highlightthickness=0,
        command=lambda:showIndicator2(info_frame,username),
        relief="flat",
        font=font3,
        width=291,
        height=58,
        borderless=1,

    )
    btn_informations.pack(pady=20)

    #button Parametres
    btn_parametre = Button(leftFrame,
        text="Parametres",
        borderless=1,
        command=lambda:showIndicator2(parametre_frame,username),
        font=font3,
        width=291,
        height=58,
    )
    btn_parametre.pack(pady=20)


    # button securite
    btn_securite = Button(leftFrame,
        text="Security",
        borderwidth=0,
        highlightthickness=0,
        command=lambda: showIndicator2(securite_frame,username),
        relief="flat",
        font=font3,
        width=291,
        height=58,
        borderless=1,

    )
    btn_securite.pack(pady=20)

    # button Logout
    btn_Logout = Button(leftFrame,text="Logout",
        borderwidth=0,
        bg="#B92B2B",
        highlightthickness=0,
        command=exit_frame,
        relief="flat",
        font=font3,
        width=291,
        height=58,
        borderless=1,

    )
    btn_Logout.pack(pady=20)
    showIndicator2(acceuil_frame,username)
    ##############################################################
    root.mainloop()


