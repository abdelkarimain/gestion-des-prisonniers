




from classes import*
from tkinter import *
from customtkinter import *
import time
import ttkthemes
from tkinter import ttk,messagebox,filedialog
import pymysql
import pandas
from tkmacosx import *
from tkmacosx import SFrame
from tkinter.filedialog import askopenfile
from PIL import Image, ImageTk
from fpdf import FPDF



gray="#303030"
move="#ccc"
red="#303030"
font1=("OCR A Std",48,"italic")
font2=("OCR A Std",14,"bold")
font3=("OCR A Std",25,"bold")













#################################################
#                  functions                    #
#################################################

#time
def clock():
    global date, currenttime    # declaring global variables
    date = time.strftime("%d/%m/%Y")    # getting current date in dd/mm/yyyy format
    currenttime = time.strftime("%H:%M:%S")   # getting current time in HH:MM:SS format
    datetimelabel.config(text=f"  Date: {date}\nTime: {currenttime}")   # updating label text with current date and time
    datetimelabel.after(1000, clock)   # calling clock() function again after 1 second

#upload File fct
def upload_file():
    global imageUrl   # declaring global variable
    f_types = [('Jpg Files', '*.jpg'),('PNG Files','*.png'),('jpeg Files','*.jpeg')]   # creating a tuple of file types to select
    imageUrl= filedialog.askopenfilename(multiple=True,filetypes=f_types)   # opening a file dialog box to select image files of the given types
    uploadimgBtn.config(text="Image Uploaded")   # changing the text of a button widget named `uploadimgBtn` to "Image Uploaded"
    uploadimgBtn.config(state=DISABLED)   # disabling the `uploadimgBtn` button

#la creation de la fenêtre de lajout et l'update
imageUrl=""
def toplevel_data(title,button_text,button_command):
    global firstNameEntry,lastNameEntry,val,crimeEntry,screen,id,uploadimgBtn,punishmentEntry
    
    if button_text=="Update Prisonneir":
        if prisonnierTable.focus()=="":
            messagebox.showerror("Error","You must select a prisonnier")
        else:
            screen=Toplevel(root)
            screen.state("zoomed")
            screen.config(background=gray)
            screen.geometry("2000x900+100+20")
            leftFrame2=Frame(screen,background=gray)
            rightFrame2=Frame(screen,background=gray)
            leftFrame2.place(x=150,y=150,width=600,height=1000)
            rightFrame2.place(x=800,y=150,width=500,height=1000)
            ajoutLabel=Label(screen,text=title,font=("OCR A Std",48,"italic"),bg=red,borderwidth=5,fg=move, relief="solid")
            ajoutLabel.place(x=400,y=0,width=600,height=100)



            firstNameLabel=Label(leftFrame2,text="firstname",font=("OCR A Std",28,"bold"),bg=move,width=15,fg=red)
            firstNameLabel.grid(row=2,column=0,sticky=W,padx=0,pady=20)
            firstNameEntry=Entry(rightFrame2,font=("OCR A Std",24,"bold"))
            firstNameEntry.grid(row=2,column=1,pady=20)





            lastNameLabel=Label(leftFrame2,text="lastname",font=("OCR A Std",28,"bold"),bg=move,width=15,fg=red)
            lastNameLabel.grid(row=3,column=0,sticky=W,padx=0,pady=20)
            lastNameEntry=Entry(rightFrame2,font=("OCR A Std",24,"bold"))
            lastNameEntry.grid(row=3,column=1,pady=20)

            

            genderLabel=Label(leftFrame2,text="gender",font=("OCR A Std",28,"bold"),bg=move,width=15,fg=red)
            genderLabel.grid(row=4,column=0,sticky=W,padx=0,pady=20)
            val= StringVar() 
            genderCombobox=ttk.Combobox(rightFrame2,values=["Male","Famale"],textvariable=val,font=("OCR A Std",24,"bold")) 
            genderCombobox.grid(row=4,column=1,pady=20)
            





            crimeLabel=Label(leftFrame2,text="crime",font=("OCR A Std",28,"bold"),bg=move,width=15,fg=red)
            crimeLabel.grid(row=5,column=0,sticky=W,padx=0,pady=20)
            crimeEntry=Entry(rightFrame2,font=("OCR A Std",24,"bold"))
            crimeEntry.grid(row=5,column=1,pady=20)


            punishmentLabel=Label(leftFrame2,text="The Punishment",font=("OCR A Std",28,"bold"),bg=move,width=15,fg=red)
            punishmentLabel.grid(row=6,column=0,sticky=W,padx=0,pady=20)
            punishmentEntry=Entry(rightFrame2,font=("OCR A Std",24,"bold"))
            punishmentEntry.grid(row=6,column=1,pady=20)


            uploadimgLabel=Label(leftFrame2,text="Image",font=("OCR A Std",28,"bold"),bg=move,width=15,fg=red)
            uploadimgLabel.grid(row=7,column=0,sticky=W,padx=0,pady=20)

            uploadimgBtn=Button(rightFrame2,text="Upload Image Here",command=upload_file,font=("OCR A Std",28,"bold"),bg=move,width=375,fg=red,borderless=1)
            uploadimgBtn.grid(row=7,column=1,padx=0,pady=20)  
            

            ajoutButton=Button(leftFrame2,text=button_text,font=("OCR A Std",28,"bold"),bg=move,command=button_command,borderless=1)
            ajoutButton.grid(row=8,column=0,padx=0,pady=20)


            CloseButton=Button(rightFrame2,text="Close",font=("OCR A Std",28,"bold"),bg=move,command=screen.destroy,borderless=1,fg=red)
            CloseButton.grid(row=8,column=1,sticky=E,padx=150,pady=20)
            
            indexing=prisonnierTable.focus()
            content=prisonnierTable.item(indexing)
            content_list=content["values"]
            id=content_list[0]
            firstNameEntry.insert(0,content_list[1])
            lastNameEntry.insert(0,content_list[2])
            crimeEntry.insert(0,content_list[4])
            punishmentEntry.insert(0,content_list[5])
            imageUrl.config(text=content_list[6])
    else:  
        screen=Toplevel(root)
        screen.state("zoomed")
        screen.config(background=gray)
        screen.geometry("2000x900+100+20")                 
        leftFrame2=Frame(screen,background=gray)
        rightFrame2=Frame(screen,background=gray)
        leftFrame2.place(x=150,y=150,width=600,height=1000)
        rightFrame2.place(x=800,y=150,width=500,height=1000)
        ajoutLabel=Label(screen,text=title,font=("OCR A Std",48,"italic"),bg=red,borderwidth=5,fg=move, relief="solid")
        ajoutLabel.place(x=400,y=0,width=600,height=100)




        firstNameLabel=Label(leftFrame2,text="firstname",font=("OCR A Std",28,"bold"),bg=move,width=15,fg=red)
        firstNameLabel.grid(row=2,column=0,sticky=W,padx=0,pady=20)
        firstNameEntry=Entry(rightFrame2,font=("OCR A Std",24,"bold"))
        firstNameEntry.grid(row=2,column=1,pady=20)





        lastNameLabel=Label(leftFrame2,text="lastname",font=("OCR A Std",28,"bold"),bg=move,width=15,fg=red)
        lastNameLabel.grid(row=3,column=0,sticky=W,padx=0,pady=20)
        lastNameEntry=Entry(rightFrame2,font=("OCR A Std",24,"bold"))
        lastNameEntry.grid(row=3,column=1,pady=20)


        genderLabel=Label(leftFrame2,text="gender",font=("OCR A Std",28,"bold"),bg=move,width=15,fg=red)
        genderLabel.grid(row=4,column=0,sticky=W,padx=0,pady=20)
        val= StringVar() 
        genderCombobox=ttk.Combobox(rightFrame2,values=["Male","Famale"],textvariable=val,font=("OCR A Std",24,"bold")) 
        genderCombobox.grid(row=4,column=1,pady=20)




        crimeLabel=Label(leftFrame2,text="crime",font=("OCR A Std",28,"bold"),bg=move,width=15,fg=red)
        crimeLabel.grid(row=5,column=0,sticky=W,padx=0,pady=20)
        crimeEntry=Entry(rightFrame2,font=("OCR A Std",24,"bold"))
        crimeEntry.grid(row=5,column=1,pady=20)


        punishmentLabel=Label(leftFrame2,text="The Punishment",font=("OCR A Std",28,"bold"),bg=move,width=15,fg=red)
        punishmentLabel.grid(row=6,column=0,sticky=W,padx=0,pady=20)
        punishmentEntry=Entry(rightFrame2,font=("OCR A Std",24,"bold"))
        punishmentEntry.grid(row=6,column=1,pady=20)


        



        uploadimgLabel=Label(leftFrame2,text="Image",font=("OCR A Std",28,"bold"),bg=move,width=15,fg=red)
        uploadimgLabel.grid(row=7,column=0,sticky=W,padx=0,pady=20)

        uploadimgBtn=Button(rightFrame2,text="Click to upload",command=upload_file,font=("OCR A Std",28,"bold"),bg=move,width=375,fg=red,borderless=1)
        uploadimgBtn.grid(row=7,column=1,padx=0,pady=20)  
        




        ajoutButton=Button(leftFrame2,text=button_text,font=("OCR A Std",28,"bold"),bg=move,command=button_command,borderless=1)
        ajoutButton.grid(row=8,column=0,padx=0,pady=20)


        CloseButton=Button(rightFrame2,text="Close",font=("OCR A Std",28,"bold"),bg=move,command=screen.destroy,borderless=1,fg=red)
        CloseButton.grid(row=8,column=1,sticky=E,padx=150,pady=20)

#la creation de la fenêtre de la roucherche 
def toplevel_searche():
    global firstNameEntry,lastNameEntry,val,crimeEntry,screen,firstnameSearchEntry,prisonnierTable2,prisonnierTable3,prisonnierTable4,lastnameSearchEntry,genderSearchEntry,idSearchEntry,crimeSearchEntry,prisonnierTable5
    screen=Toplevel(root)
    screen.state("zoomed")
    screen.config(background=gray)
    screen.geometry("2000x900+100+20")
    tabControl = ttk.Notebook(screen)
    tab1 =Frame(tabControl,background=gray)
    tab2 =Frame(tabControl,bg=red)
    tab3 =Frame(tabControl,background=gray)
    tab4 =Frame(tabControl,background=gray)

    tabControl.add(tab1, text ='Search psr Id')
    tabControl.add(tab2, text ='Search By Nom')
    tabControl.add(tab3, text ='Search By Gender')
    tabControl.add(tab4, text ='Search By Crime')
    tabControl.pack(expand = 1, fill ="both")

################### Search By Id

    titleLabel=Label(tab1,text="Search By Id",font=("OCR A Std",48,"italic"),bg=gray,borderwidth=5,fg=move, relief="solid")
    titleLabel.grid(row=0,columnspan=2,pady=50)

    idSearchLabel=Label(tab1,text="Id",font=("OCR A Std",28,"bold"),bg=move,width=15)
    idSearchLabel.grid(row=1,column=0,sticky=W,padx=195,pady=20)
    idSearchEntry=Entry(tab1,font=("OCR A Std",18,"bold"))
    idSearchEntry.grid(row=1,column=1)


    SearchButton=Button(tab1,text="Search Id",font=("OCR A Std",28,"bold"),bg=move,borderless=1,command=lambda:search_data1(idSearchEntry.get(),prisonnierTable2))
    SearchButton.grid(row=3,column=0,sticky=W,padx=195,pady=20)


    CloseButton=Button(tab1,text="Close Window",font=("OCR A Std",28,"bold"),bg=move,borderless=1,command=screen.destroy)
    CloseButton.grid(row=3,column=1,sticky=E,padx=195,pady=20)


    SearchButton=Button(tab1,text="Save Profile",font=("OCR A Std",28,"bold"),borderless=1,command=lambda:profile_export_data(prisonnierTable2))
    SearchButton.grid(row=4,columnspan=2)

    

    buttomFrame=Frame(tab1 ,padx=95,pady=20,height=3000,bg=gray)
    buttomFrame.place(x=15,y=380,height=445,width=1360)


    ScrollbarX=Scrollbar(buttomFrame,orient=HORIZONTAL)
    ScrollbarY=Scrollbar(buttomFrame,orient=VERTICAL)
    ScrollbarX.pack(side=BOTTOM,fill=X)
    ScrollbarY.pack(side=RIGHT,fill=Y)

    prisonnierTable2=ttk.Treeview(buttomFrame,columns=("Id","First Name","Last Name","Gender","Crime","Added Date","The Punishment"),xscrollcommand=ScrollbarX.set,yscrollcommand=ScrollbarY.set)
    prisonnierTable2.pack(fill=BOTH,expand=1)

    ScrollbarX.config(command=prisonnierTable.xview)
    ScrollbarY.config(command=prisonnierTable.yview)
    ScrollbarX.config(background=red)
    prisonnierTable2.heading("Id",text="Id")
    prisonnierTable2.heading("First Name",text="First Name")
    prisonnierTable2.heading("Last Name",text="Last Name")
    prisonnierTable2.heading("Gender",text="Gender")
    prisonnierTable2.heading("Crime",text="Crime")
    prisonnierTable2.heading("Added Date",text="Added Date")
    prisonnierTable2.heading("The Punishment",text="The Punishment")
    prisonnierTable2.config(show="headings")

    prisonnierTable2.column("Id",width=50,anchor=CENTER)
    prisonnierTable2.column("First Name",width=200,anchor=CENTER)
    prisonnierTable2.column("Last Name",width=200,anchor=CENTER)
    prisonnierTable2.column("Gender",width=150,anchor=CENTER)
    prisonnierTable2.column("Crime",width=250,anchor=CENTER)
    prisonnierTable2.column("Added Date",width=150,anchor=CENTER)
    prisonnierTable2.column("The Punishment",width=150,anchor=CENTER)

###################### Search By Nome



    titleLabel=Label(tab2,text="Search By Name",font=("OCR A Std",48,"italic"),bg=gray,borderwidth=5,fg=move, relief="solid")
    titleLabel.grid(row=0,columnspan=2,pady=50)

    firstnameSearchLabel=Label(tab2,text="First Name",font=("OCR A Std",28,"bold"),bg=move,width=21)
    firstnameSearchLabel.grid(row=1,column=0,sticky=W,padx=165,pady=20)
    firstnameSearchEntry=Entry(tab2,font=("OCR A Std",18,"bold"))
    firstnameSearchEntry.grid(row=1,column=1)


    lastnameSearchLabel=Label(tab2,text="First Name",font=("OCR A Std",28,"bold"),bg=move,width=21)
    lastnameSearchLabel.grid(row=2,column=0,sticky=W,padx=165,pady=20)
    lastnameSearchEntry=Entry(tab2,font=("OCR A Std",18,"bold"))
    lastnameSearchEntry.grid(row=2,column=1)


    SearchButton=Button(tab2,text="Search Name",font=("OCR A Std",28,"bold"),bg=move,borderless=1,command=lambda:search_data2(firstnameSearchEntry.get(),lastnameSearchEntry.get(),prisonnierTable3))
    SearchButton.grid(row=3,column=0,sticky=W,padx=165,pady=20)


    CloseButton=Button(tab2,text="Close Window",font=("OCR A Std",28,"bold"),bg=move,borderless=1,command=screen.destroy)
    CloseButton.grid(row=3,column=1,sticky=E,padx=165,pady=20)


    SearchButton=Button(tab2,text="Save Profile",font=("OCR A Std",28,"bold"),borderless=1,command=lambda:profile_export_data(prisonnierTable3))
    SearchButton.grid(row=4,columnspan=2)


    buttomFrame=Frame(tab2 ,padx=95,pady=20,height=3000,bg=gray)
    buttomFrame.place(x=15,y=480,height=340,width=1360)


    ScrollbarX=Scrollbar(buttomFrame,orient=HORIZONTAL)
    ScrollbarY=Scrollbar(buttomFrame,orient=VERTICAL)
    ScrollbarX.pack(side=BOTTOM,fill=X)
    ScrollbarY.pack(side=RIGHT,fill=Y)

    prisonnierTable3=ttk.Treeview(buttomFrame,columns=("Id","First Name","Last Name","Gender","Crime","Added Date","The Punishment"),xscrollcommand=ScrollbarX.set,yscrollcommand=ScrollbarY.set)
    prisonnierTable3.pack(fill=BOTH,expand=1)

    ScrollbarX.config(command=prisonnierTable.xview)
    ScrollbarY.config(command=prisonnierTable.yview)
    ScrollbarX.config(background=red)
    prisonnierTable3.heading("Id",text="Id")
    prisonnierTable3.heading("First Name",text="First Name")
    prisonnierTable3.heading("Last Name",text="Last Name")
    prisonnierTable3.heading("Gender",text="Gender")
    prisonnierTable3.heading("Crime",text="Crime")
    prisonnierTable3.heading("Added Date",text="Added Date")
    prisonnierTable3.heading("The Punishment",text="The Punishment")
    prisonnierTable3.config(show="headings")

    prisonnierTable3.column("Id",width=50,anchor=CENTER)
    prisonnierTable3.column("First Name",width=200,anchor=CENTER)
    prisonnierTable3.column("Last Name",width=200,anchor=CENTER)
    prisonnierTable3.column("Gender",width=150,anchor=CENTER)
    prisonnierTable3.column("Crime",width=250,anchor=CENTER)
    prisonnierTable3.column("Added Date",width=150,anchor=CENTER)
    prisonnierTable3.column("The Punishment",width=150,anchor=CENTER)
############## Search By Genre



    titleLabel=Label(tab3,text="Search By Genre",font=("OCR A Std",48,"italic"),bg=gray,borderwidth=5, fg=move,relief="solid")
    titleLabel.grid(row=0,columnspan=2,pady=50)

    genderSearchLabel=Label(tab3,text="genre :",font=("OCR A Std",28,"bold"),bg=move,width=21)
    genderSearchLabel.grid(row=1,column=0,sticky=W,padx=160,pady=20)
    genderSearchEntry=Entry(tab3,font=("OCR A Std",18,"bold"))
    genderSearchEntry.grid(row=1,column=1)


    SearchButton=Button(tab3,text="Search Gender",font=("OCR A Std",28,"bold"),borderless=1,bg=move,command=lambda:search_data3(genderSearchEntry.get(),prisonnierTable4))
    SearchButton.grid(row=3,column=0,sticky=W,padx=160,pady=20)


    CloseButton=Button(tab3,text="Close Window",font=("OCR A Std",28,"bold"),bg=move,borderless=1,command=screen.destroy)
    CloseButton.grid(row=3,column=1,sticky=E,padx=160,pady=20)


    SearchButton=Button(tab3,text="Save Profile",font=("OCR A Std",28,"bold"),borderless=1,command=lambda:profile_export_data(prisonnierTable4))
    SearchButton.grid(row=4,columnspan=2)


    buttomFrame=Frame(tab3 ,padx=95,pady=20,height=3000,bg=gray)
    buttomFrame.place(x=15,y=380,height=445,width=1360)


    ScrollbarX=Scrollbar(buttomFrame,orient=HORIZONTAL)
    ScrollbarY=Scrollbar(buttomFrame,orient=VERTICAL)
    ScrollbarX.pack(side=BOTTOM,fill=X)
    ScrollbarY.pack(side=RIGHT,fill=Y)

    prisonnierTable4=ttk.Treeview(buttomFrame,columns=("Id","First Name","Last Name","Gender","Crime","Added Date","The Punishment"),xscrollcommand=ScrollbarX.set,yscrollcommand=ScrollbarY.set)
    prisonnierTable4.pack(fill=BOTH,expand=1)

    ScrollbarX.config(command=prisonnierTable.xview)
    ScrollbarY.config(command=prisonnierTable.yview)
    ScrollbarX.config(background=red)
    prisonnierTable4.heading("Id",text="Id")
    prisonnierTable4.heading("First Name",text="First Name")
    prisonnierTable4.heading("Last Name",text="Last Name")
    prisonnierTable4.heading("Gender",text="Gender")
    prisonnierTable4.heading("Crime",text="Crime")
    prisonnierTable4.heading("Added Date",text="Added Date")
    prisonnierTable4.heading("The Punishment",text="The Punishment")
    prisonnierTable4.config(show="headings")

    prisonnierTable4.column("Id",width=50,anchor=CENTER)
    prisonnierTable4.column("First Name",width=200,anchor=CENTER)
    prisonnierTable4.column("Last Name",width=200,anchor=CENTER)
    prisonnierTable4.column("Gender",width=150,anchor=CENTER)
    prisonnierTable4.column("Crime",width=250,anchor=CENTER)
    prisonnierTable4.column("Added Date",width=150,anchor=CENTER)
    prisonnierTable4.column("The Punishment",width=150,anchor=CENTER)       

#################### Search By Crime


    titleLabel=Label(tab4,text="Search By Crime",font=("OCR A Std",48,"italic"),bg=gray,borderwidth=5,fg=move, relief="solid")
    titleLabel.grid(row=0,columnspan=2,pady=50)

    crimeSearchLabel=Label(tab4,text="Crime",font=("OCR A Std",28,"bold"),bg=move,width=21)
    crimeSearchLabel.grid(row=1,column=0,sticky=W,padx=160,pady=20)
    crimeSearchEntry=Entry(tab4,font=("OCR A Std",18,"bold"))
    crimeSearchEntry.grid(row=1,column=1)


    SearchButton=Button(tab4,text="Search Crime",font=("OCR A Std",28,"bold"),borderless=1,bg=move,command=lambda:search_data4(crimeSearchEntry.get(),prisonnierTable5))
    SearchButton.grid(row=3,column=0,sticky=W,padx=160,pady=20)


    CloseButton=Button(tab4,text="Close Window",font=("OCR A Std",28,"bold"),borderless=1,bg=move,command=screen.destroy)
    CloseButton.grid(row=3,column=1,sticky=E,padx=160,pady=20)


    SearchButton=Button(tab4,text="Save Profile",font=("OCR A Std",28,"bold"),borderless=1,command=lambda:profile_export_data(prisonnierTable5))
    SearchButton.grid(row=4,columnspan=2)


    buttomFrame=Frame(tab4 ,padx=95,pady=20,height=3000,bg=gray)
    buttomFrame.place(x=15,y=380,height=445,width=1360)


    ScrollbarX=Scrollbar(buttomFrame,orient=HORIZONTAL)
    ScrollbarY=Scrollbar(buttomFrame,orient=VERTICAL)
    ScrollbarX.pack(side=BOTTOM,fill=X)
    ScrollbarY.pack(side=RIGHT,fill=Y)

    prisonnierTable5=ttk.Treeview(buttomFrame,columns=("Id","First Name","Last Name","Gender","Crime","Added Date","The Punishment"),xscrollcommand=ScrollbarX.set,yscrollcommand=ScrollbarY.set)
    prisonnierTable5.pack(fill=BOTH,expand=1)

    ScrollbarX.config(command=prisonnierTable.xview)
    ScrollbarY.config(command=prisonnierTable.yview)
    ScrollbarX.config(background=red)
    prisonnierTable5.heading("Id",text="Id")
    prisonnierTable5.heading("First Name",text="First Name")
    prisonnierTable5.heading("Last Name",text="Last Name")
    prisonnierTable5.heading("Gender",text="Gender")
    prisonnierTable5.heading("Crime",text="Crime")
    prisonnierTable5.heading("Added Date",text="Added Date")
    prisonnierTable5.heading("The Punishment",text="The Punishment")
    prisonnierTable5.config(show="headings")

    prisonnierTable5.column("Id",width=50,anchor=CENTER)
    prisonnierTable5.column("First Name",width=200,anchor=CENTER)
    prisonnierTable5.column("Last Name",width=200,anchor=CENTER)
    prisonnierTable5.column("Gender",width=150,anchor=CENTER)
    prisonnierTable5.column("Crime",width=250,anchor=CENTER)
    prisonnierTable5.column("Added Date",width=150,anchor=CENTER)
    prisonnierTable5.column("The Punishment",width=150,anchor=CENTER)

#la fonction de lajout des prisoniers
def add_data():
    global mycursor,con,fetched_data
    if  firstNameEntry.get()==''or lastNameEntry.get()==''or val.get()==''or crimeEntry.get()=='' or punishmentEntry.get()=="" or imageUrl=="":
        messagebox.showerror("Error","All feilds are requied",parent=screen)
    else:
        newPrisonnier=Prisoner(firstNameEntry.get(),lastNameEntry.get(),val.get(),crimeEntry.get(),punishmentEntry.get(),imageUrl)
        newPrisonnier.addPrisonnier()

        result=messagebox.askyesno("Confirm","Data addes successfully. Do you want to clean the form")
        if result:
            firstNameEntry.delete(0,END)
            lastNameEntry.delete(0,END)
            crimeEntry.delete(0,END)
            punishmentEntry.delete(0,END)
            uploadimgBtn.config(text="Click to upload")
            uploadimgBtn.config(state=NORMAL)
            
        
        show_data(prisonnierTable)

#la fonction de la moudefication des donnes de la base de donne
def update_data():
    global firstNameEntry,lastNameEntry,val,crimeEntry,punishmentEntry,imageUrl,id

    update(firstNameEntry.get(),lastNameEntry.get(),val.get(),crimeEntry.get(),punishmentEntry.get(),imageUrl,id,screen,prisonnierTable)



#la fonction de la quittation des programe
def exit_programe():
    result=messagebox.askyesno("confirm","Do you want to exit?")
    if result:
        root.destroy()
    else:
        pass


#la fonction de lexportation des donnes d'un prisonier
def profile_export_data(prisonnierTablex):
    indexing=prisonnierTablex.focus()
    if len(prisonnierTablex.get_children())==1 :
        indexing=prisonnierTablex.get_children()[0]
    elif prisonnierTablex.focus()=="":
        export_data(prisonnierTablex)
        return
    
    content=prisonnierTablex.item(indexing)
    content_list=content["values"]
    url=filedialog.asksaveasfilename(defaultextension="pdf")
    if url!="":
        pdf=FPDF()
        pdf.add_page()
        a = (pdf.w - 20) / 2
        b = 5
        pdf.image("/Users/tayastudios/Desktop/project/seperatedprisonnier/images/Seal_of_the_Federal_Bureau_of_Prisons.svg.png", a, b, 20)
        x = (pdf.w - 50) / 2
        y = 30
        pdf.set_font('Arial', 'B', 26)
        pdf.set_text_color(255, 55, 0)


        pdf.cell(20, 90, txt="", ln=1)
        pdf.set_line_width(2)
        pdf.cell(20, 10, txt="", ln=1)
        pdf.cell(0, 10, f"prisoner N° {content_list[0]}", 0, 1, "C")
        pdf.cell(20, 10, txt="", ln=1)
        pdf.image(content_list[7], x, y, 50)
        pdf.set_text_color(255, 0, 0)
        pdf.set_font('Arial', 'B', 26)
        pdf.cell(95, 25, "The Full Name", border=1,align="C")
        pdf.set_text_color(0, 0, 0)
        pdf.set_font('Arial', 'B', 22)
        pdf.cell(95, 25, f"{content_list[1]} {content_list[2]}", border=1,align="C")
        pdf.ln()



        pdf.set_text_color(255, 0, 0)
        pdf.set_font('Arial', 'B', 26)
        pdf.cell(95, 25, "The Gender", border=1,align="C")
        pdf.set_text_color(0, 0, 0)
        pdf.set_font('Arial', 'B', 22)
        pdf.cell(95, 25, f"{content_list[3]}", border=1,align="C")
        pdf.ln()


        pdf.set_text_color(255, 0, 0)
        pdf.set_font('Arial', 'B', 26)
        pdf.cell(95, 25, "The Crime", border=1,align="C")
        pdf.set_text_color(0, 0, 0)
        pdf.set_font('Arial', 'B', 22)
        pdf.cell(95, 25, f"{content_list[4]}", border=1,align="C")
        pdf.ln()


        pdf.set_text_color(255, 0, 0)
        pdf.set_font('Arial', 'B', 26)
        pdf.cell(95, 25, "The punishment", border=1,align="C")
        pdf.set_text_color(0, 0, 0)
        pdf.set_font('Arial', 'B', 22)
        pdf.cell(95, 25, f"{content_list[5]}", border=1,align="C")
        pdf.ln()



        pdf.set_text_color(255, 0, 0)
        pdf.set_font('Arial', 'B', 26)
        pdf.cell(95, 25, "Added date", border=1,align="C")
        pdf.set_text_color(0, 0, 0)
        pdf.set_font('Arial', 'B', 22)
        pdf.cell(95, 25, f"{content_list[6]}", border=1,align="C")
        pdf.ln()






        pdf.set_font('Arial', 'B', 8)
        pdf.set_xy(160, 260)  # adjust the x and y position to position the signature
        pdf.cell(30, 10, "The signature of the director and the seal of the prison institution :", align="R")

        

        pdf.output(url, 'F') 
        messagebox.showinfo("Enfo","file saved successfully")
        

#la fonction de lafichage des prisoniers
def prisonnierProfile():
    if prisonnierTable.focus()=="":
        messagebox.showerror("Error","You must select a prisoner")
    else:
        screen=Toplevel(root)
        screen.state("zoomed")
        screen.config(background=gray)
        screen.geometry("2000x900+100+20")
        indexing=prisonnierTable.focus()
        content=prisonnierTable.item(indexing)
        content_list=content["values"]
        allFrame=Frame(screen,bg=move)
        allFrame.place(x=100,y=25,width=1250,height=800)
        profileidLabel=Label(allFrame,text="Id          :"+str(content_list[0]),font=font3,height=2,width=25,fg=move,bg=gray)
        profileidLabel.grid(row=1,column=0,pady=35,padx=80)
        profilefirstnameLabel=Label(allFrame,text="First Name  :"+content_list[1],font=font3,height=2,width=25,fg=move,bg=gray)
        profilefirstnameLabel.grid(row=1,column=1,pady=35,padx=80)
        profilelastnameLabel=Label(allFrame,text="Last Name   :"+content_list[2],font=font3,height=2,width=25,fg=move,bg=gray)
        profilelastnameLabel.grid(row=2,column=0,pady=35,padx=80)
        profilegenderLabel=Label(allFrame,text="Gender      :"+content_list[3],font=font3,height=2,width=25,fg=move,bg=gray)
        profilegenderLabel.grid(row=2,column=1,pady=35,padx=80)

        profilecrimeLabel=Label(allFrame,text="Crime:"+content_list[4],font=font3,height=2,width=25,fg=move,bg=gray)
        profilecrimeLabel.grid(row=3,column=0,pady=35,padx=80)


        profilepunishmentLabel=Label(allFrame,text="Punishment  :"+content_list[5],font=font3,height=2,width=25,fg=move,bg=gray)
        profilepunishmentLabel.grid(row=3,column=1,pady=35,padx=80)

        close_button=Button(allFrame,text="Save",font=font3,width=450,height=60,borderless=1,command=lambda:profile_export_data(prisonnierTable))
        close_button.grid(row=4,column=0)

        close_button=Button(allFrame,text="Close",font=font3,width=450,height=60,borderless=1,command=lambda:screen.destroy())
        close_button.grid(row=4,column=1)


        filename = (content_list[7],)
        col=0 # start from column 1
        row=0 # start from row 3 

        img=Image.open(filename[0]) # read the image file
        img=img.resize((300,400)) # new width & height
        img=ImageTk.PhotoImage(img)
        e1 =CircleButton(allFrame,height=300,borderless=1,state=DISABLED)
        e1.grid(row=row,columnspan=2,pady=10)
        e1.image = img # keep a reference! by attaching it to a widget attribute
        e1['image']=img # Show Image 
    screen.mainloop()

#la fonction de l'exportation des donnes
def export_data(prisonnierTable):
    url=filedialog.asksaveasfilename(defaultextension="pdf")
    if url!="":
        indexing=prisonnierTable.get_children()
        newlist=[]
        pdf=FPDF()
        x = (pdf.w - 50) / 2
        y = 10
        pdf.add_page()
        img="/Users/tayastudios/Desktop/project/seperatedprisonnier/images/Seal_of_the_Federal_Bureau_of_Prisons.svg.png"
        pdf.image(img, x, y, 50)
        pdf.set_text_color(255, 55, 0)
        pdf.set_font('Arial', 'B', 26)
        pdf.cell(20, 10, txt="", ln=1)
        pdf.cell(20, 10, txt="", ln=1)
        pdf.cell(20, 10, txt="", ln=1)
        pdf.cell(20, 10, txt="", ln=1)
        pdf.cell(20, 10, txt="", ln=1)
        pdf.set_font('Arial', 'B', 36)
        pdf.cell(0, 10, "Prisoners List", 0, 1, "C")
        pdf.cell(20, 10, txt="", ln=1)
        pdf.set_font("Arial", "B", 12)
        pdf.cell(10, 10, "Id ", border=1,align="C")
        pdf.cell(45, 10, "The Full Name ", border=1,align="C")
        pdf.cell(35, 10, "The Gender", border=1,align="C")
        pdf.cell(55, 10, "The Crime", border=1,align="C")
        pdf.cell(45, 10, "The punishment", border=1,align="C")
        pdf.ln()
        pdf.set_font('Arial', 'B', 8)
        pdf.set_text_color(0, 0, 0)
        for index in indexing:
            content =prisonnierTable.item(index)
            datalist=content["values"]
            pdf.cell(10, 10, f"{datalist[0]}", border=1,align="C")
            pdf.cell(45, 10, f"{datalist[1]} {datalist[2]}", border=1,align="C")
            pdf.cell(35, 10, f"{datalist[3]}", border=1,align="C")
            pdf.cell(55, 10, f"{datalist[4]}", border=1,align="C")
            pdf.cell(45, 10, f"{datalist[5]}", border=1,align="C")
            pdf.ln()


        pdf.set_font('Arial', 'B', 8)
        pdf.set_xy(160, 266)  # adjust the x and y position to position the signature
        pdf.cell(30, 10, "The signature of the director and the seal of the prison institution :", align="R")

        
        # pdf.cell(260, 10, "The signature of the director and the seal of the prison institution", 0, 0, "C")
        pdf.output(url, 'F') 
        messagebox.showinfo("Enfo","file saved successfully")




def prisonerpage():
    global prisonnierTable,root,datetimelabel

    #################################################
    #                     root                      #
    #################################################

    root=Tk() 

    root.config(background = gray) 
    root.geometry("2174x1780+100+20")
    root.title("Prison Managment Systeme")
    root.state("zoomed")


    #################################################
    #                  datetime                     #
    #################################################
    datetimelabel=Label(root,text="hello",font=("OCR A Std",20,"bold"),bg=gray,fg="#ccc")
    datetimelabel.place(x=3,y=5)
    clock()


    #################################################
    #                    slide                      #
    #################################################

    titleLabel=Label(root,text="Prisonniers List",font=font1,bg=gray,borderwidth=0,fg="#ccc", relief="solid",padx=300)
    titleLabel.place(x=300,y=5)

    #################################################
    #                  left frame                   #
    #################################################
    leftFrame=Frame(root,bg=gray)
    leftFrame.place(x=50,y=80,width=300,height=800)
    logo_image=PhotoImage(file="/Users/tayastudios/Desktop/project/seperatedprisonnier/images/convict.png")
    logo_Label=Label(leftFrame,image=logo_image,bg=gray)
    logo_Label.grid(row=0,column=0)

    #button d'ajout
    addprisonnierButton=Button(leftFrame,text="Add Prisonneir",width=250,height=50,fg=red,bg=move,font=font2,command=lambda:toplevel_data("Add Prisonneir","ADD",add_data),borderless=1,activebackground="red")
    addprisonnierButton.grid(row=1,column=0,pady=15)








    #button de roucherche
    searchprisonnierButton=Button(leftFrame,text="Search Prisonneir",width=250,height=50,fg=red,bg=move,font=font2,command=toplevel_searche,borderless=1)
    searchprisonnierButton.grid(row=2,column=0,pady=15)

    #button de supretion
    deleteprisonnierButton=Button(leftFrame,text="Delete Prisonneir",width=250,height=50,fg=red,bg=move,font=font2,command=lambda:delete_prisonnier(prisonnierTable),borderless=1)
    deleteprisonnierButton.grid(row=3,column=0,pady=15)

    #button d'update
    updateprisonnierButton=Button(leftFrame,text="Update Prisonneir",width=250,height=50,fg=red,bg=move,font=font2,command=lambda:toplevel_data("Update Prisonneir","Update Prisonneir",update_data),borderless=1)
    updateprisonnierButton.grid(row=4,column=0,pady=15)

    #button d'affichage
    showprisonnierButton=Button(leftFrame,text="Show Prisonneir",width=250,height=50,fg=red,font=font2,command=prisonnierProfile,bg=move, borderless=1)
    showprisonnierButton.grid(row=5,column=0,pady=15)

    #button d'enregenstrement
    exportprisonnierButton=Button(leftFrame,text="Save File",width=250,height=50,fg=red,bg=move,font=font2,command=lambda:export_data(prisonnierTable),borderless=1)
    exportprisonnierButton.grid(row=6,column=0,pady=15)

    #button de quittation
    exitButton=Button(leftFrame,text="exit",width=250,height=50,fg=red,background=move,font=font2,command=exit_programe,borderless=1)
    exitButton.grid(row=7,column=0,pady=15)


    #################################################
    #                  right frame                   #
    #################################################
    rightFrame=Frame(root,bg=red )
    rightFrame.place(x=350,y=90,width=1010,height=757)
    
    ScrollbarX=Scrollbar(rightFrame,orient=HORIZONTAL)
    ScrollbarY=Scrollbar(rightFrame,orient=VERTICAL)
    ScrollbarX.pack(side=BOTTOM,fill=X)
    ScrollbarY.pack(side=RIGHT,fill=Y)

    prisonnierTable=ttk.Treeview(rightFrame,columns=("Id","First Name","Last Name","Gender","Crime","The Punishment","Added Date"),xscrollcommand=ScrollbarX.set,yscrollcommand=ScrollbarY.set)
    prisonnierTable.pack(fill=BOTH,expand=1)

    ScrollbarX.config(command=prisonnierTable.xview)
    ScrollbarY.config(command=prisonnierTable.yview)

    prisonnierTable.heading("Id",text="Id")
    prisonnierTable.heading("First Name",text="First Name")
    prisonnierTable.heading("Last Name",text="Last Name")
    prisonnierTable.heading("Gender",text="Gender")
    prisonnierTable.heading("Crime",text="Crime")
    prisonnierTable.heading("The Punishment",text="The Punishment")
    prisonnierTable.heading("Added Date",text="Added Date")
    prisonnierTable.config(show="headings")

    prisonnierTable.column("Id",width=50,anchor=CENTER)
    prisonnierTable.column("First Name",width=200,anchor=CENTER)
    prisonnierTable.column("Last Name",width=200,anchor=CENTER)
    prisonnierTable.column("Gender",width=150,anchor=CENTER)
    prisonnierTable.column("Crime",width=250,anchor=CENTER)
    prisonnierTable.column("The Punishment",width=150,anchor=CENTER)
    prisonnierTable.column("Added Date",width=150,anchor=CENTER)


    style=ttk.Style()
    style.configure("Treeview",rowheight=51,font=("arial",16,"bold"),foreground=gray,background="#ffce00",fieldbackground=move)
    style.configure("Treeview.Heading",font=("arial",15,"bold"),foreground=red)



    #la connection de la base des donnes
    databaseconnect()


    connectPrisonnier()
    try:
        show_data(prisonnierTable)
    except:
        pass


    root.mainloop()
prisonerpage()