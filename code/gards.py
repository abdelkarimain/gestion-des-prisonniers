
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
    global date,currenttime
    date=time.strftime("%d/%m/%Y")
    currenttime=time.strftime("%H:%M:%S")
    datetimelabel.config(text=f"  Date: {date}\nTime: {currenttime}")
    datetimelabel.after(1000,clock)

#upload File fct
def upload_file():
    global imageUrl
    f_types = [('Jpg Files', '*.jpg'),('PNG Files','*.png'),('jpeg Files','*.jpeg')]   # type of files to select 
    imageUrl= filedialog.askopenfilename(multiple=True,filetypes=f_types)
    uploadimgBtn.config(text="Image Uploaded")
    uploadimgBtn.config(state=DISABLED)

#la creation de la fenêtre de lajout et l'update
imageUrl=""
def toplevel_data(title,button_text,button_command):
    global firstNameEntry,lastNameEntry,val,shiftstartingtimeEntry,screen,id,uploadimgBtn,shiftendingtimeEntry,shiftendEntry,imageUrl
    
    if button_command==update_data :
        if guardTable.focus()=="":
            messagebox.showerror("Error","You must select a guard")
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
            genderCombobox=ttk.Combobox(rightFrame2,values=["Male","Famale"],textvariable=val,font=("OCR A Std",23,"bold")) 
            genderCombobox.grid(row=4,column=1,pady=20)




            shiftstartingtimeLabel=Label(leftFrame2,text="Shift Starts At",font=("OCR A Std",28,"bold"),bg=move,width=15,fg=red)
            shiftstartingtimeLabel.grid(row=5,column=0,sticky=W,padx=0,pady=20)
            shiftstartingtimeEntry=Entry(rightFrame2,font=("OCR A Std",24,"bold"))
            shiftstartingtimeEntry.grid(row=5,column=1,pady=20)


            shiftendingtimeLabel=Label(leftFrame2,text="Shift Ends At",font=("OCR A Std",28,"bold"),bg=move,width=15,fg=red)
            shiftendingtimeLabel.grid(row=6,column=0,sticky=W,padx=0,pady=20)
            shiftendingtimeEntry=Entry(rightFrame2,font=("OCR A Std",24,"bold"))
            shiftendingtimeEntry.grid(row=6,column=1,pady=20)


            uploadimgLabel=Label(leftFrame2,text="Image",font=("OCR A Std",28,"bold"),bg=move,width=15,fg=red)
            uploadimgLabel.grid(row=7,column=0,sticky=W,padx=0,pady=20)

            uploadimgBtn=Button(rightFrame2,text="Upload Image Here",command=upload_file,font=("OCR A Std",28,"bold"),bg=move,width=375,fg=red,borderless=1)
            uploadimgBtn.grid(row=7,column=1,padx=0,pady=20)  
            

            ajoutButton=Button(leftFrame2,text=button_text,font=("OCR A Std",28,"bold"),bg=move,command=button_command,borderless=1)
            ajoutButton.grid(row=8,column=0,padx=0,pady=20)


            quitterButton=Button(rightFrame2,text="Quitter",font=("OCR A Std",28,"bold"),bg=move,command=screen.destroy,borderless=1,fg=red)
            quitterButton.grid(row=8,column=1,sticky=E,padx=150,pady=20)
            
            indexing=guardTable.focus()
            content=guardTable.item(indexing)
            content_list=content["values"]
            id=content_list[0]
            firstNameEntry.insert(0,content_list[1])
            lastNameEntry.insert(0,content_list[2])
            genderCombobox.current(0)
            shiftstartingtimeEntry.insert(0,content_list[4])
            shiftendingtimeEntry.insert(0,content_list[5])
            imageUrl=content_list[6]
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
        genderCombobox=ttk.Combobox(rightFrame2,values=["Male","Famale"],textvariable=val,font=("OCR A Std",23,"bold")) 
        genderCombobox.grid(row=4,column=1,pady=20)



        shiftstartLabel=Label(leftFrame2,text="Shift Starts At",font=("OCR A Std",28,"bold"),bg=move,width=15,fg=red)
        shiftstartLabel.grid(row=5,column=0,sticky=W,padx=0,pady=20)
        shiftstartingtimeEntry=Entry(rightFrame2,font=("OCR A Std",24,"bold"))
        shiftstartingtimeEntry.grid(row=5,column=1,pady=20)


        shiftendLabel=Label(leftFrame2,text="Shift Ends At",font=("OCR A Std",28,"bold"),bg=move,width=15,fg=red)
        shiftendLabel.grid(row=6,column=0,sticky=W,padx=0,pady=20)
        shiftendEntry=Entry(rightFrame2,font=("OCR A Std",24,"bold"))
        shiftendEntry.grid(row=6,column=1,pady=20)


        



        uploadimgLabel=Label(leftFrame2,text="Image",font=("OCR A Std",28,"bold"),bg=move,width=15,fg=red)
        uploadimgLabel.grid(row=7,column=0,sticky=W,padx=0,pady=20)

        uploadimgBtn=Button(rightFrame2,text="Click to upload",command=upload_file,font=("OCR A Std",28,"bold"),bg=move,width=375,fg=red,borderless=1)
        uploadimgBtn.grid(row=7,column=1,padx=0,pady=20)  
        

  


        ajoutButton=Button(leftFrame2,text=button_text,font=("OCR A Std",28,"bold"),bg=move,command=button_command,borderless=1)
        ajoutButton.grid(row=8,column=0,padx=0,pady=20)


        quitterButton=Button(rightFrame2,text="Quitter",font=("OCR A Std",28,"bold"),bg=move,command=screen.destroy,borderless=1,fg=red)
        quitterButton.grid(row=8,column=1,sticky=E,padx=150,pady=20)

#la creation de la fenêtre de la roucherche
def toplevel_searche():
    global firstNameEntry,lastNameEntry,val,screen,firstnameRechercheEntry,guardTable2,guardTable3,guardTable4,lastnameRechercheEntry,genderRechercheEntry,idRechercheEntry,shiftstartRechercheEntry,guardTable5
    screen=Toplevel(root)
    screen.state("zoomed")
    screen.config(background=gray)
    screen.geometry("2000x900+100+20")
    tabControl = ttk.Notebook(screen)
    tab1 =Frame(tabControl,background=gray)
    tab2 =Frame(tabControl,bg=red)
    tab3 =Frame(tabControl,background=gray)
    

    tabControl.add(tab1, text ='Recherche psr Id')
    tabControl.add(tab2, text ='Searche by Name')
    tabControl.add(tab3, text ='Searche by Gender')
    
    tabControl.pack(expand = 1, fill ="both")

################### Searche by Id

    titleLabel=Label(tab1,text="Searche by Id",font=("OCR A Std",48,"italic"),bg=gray,borderwidth=5,fg=move, relief="solid")
    titleLabel.grid(row=0,columnspan=2,pady=50)

    idRechercheLabel=Label(tab1,text="Id",font=("OCR A Std",28,"bold"),bg=move,width=15)
    idRechercheLabel.grid(row=1,column=0,sticky=W,padx=200,pady=20)
    idRechercheEntry=Entry(tab1,font=("OCR A Std",18,"bold"))
    idRechercheEntry.grid(row=1,column=1)


    rechercheButton=Button(tab1,text="Recherche",font=("OCR A Std",28,"bold"),bg=move,borderless=1,command=lambda:search_guardian_data1(idRechercheEntry.get(),guardTable2))
    rechercheButton.grid(row=3,column=0,sticky=W,padx=200,pady=20)


    quitterButton=Button(tab1,text="Quitter",font=("OCR A Std",28,"bold"),bg=move,borderless=1,command=screen.destroy)
    quitterButton.grid(row=3,column=1,sticky=E,padx=200,pady=20)


    RechercheButton=Button(tab1,text="Save Profile",font=("OCR A Std",28,"bold"),borderless=1,command=lambda:profile_export_data(guardTable2))
    RechercheButton.grid(row=4,columnspan=2)


    buttomFrame=Frame(tab1 ,padx=95,pady=20,height=3000,bg=gray)
    buttomFrame.grid(row=5,columnspan=2)


    ScrollbarX=Scrollbar(buttomFrame,orient=HORIZONTAL)
    ScrollbarY=Scrollbar(buttomFrame,orient=VERTICAL)
    ScrollbarX.pack(side=BOTTOM,fill=X)
    ScrollbarY.pack(side=RIGHT,fill=Y)

    guardTable2=ttk.Treeview(buttomFrame,columns=("Id","First Name","Last Name","Gender","Shift Starts At","Added Date","Shift Ends At"),xscrollcommand=ScrollbarX.set,yscrollcommand=ScrollbarY.set)
    guardTable2.pack(fill=BOTH,expand=1)

    ScrollbarX.config(command=guardTable2.xview)
    ScrollbarY.config(command=guardTable2.yview)
    ScrollbarX.config(background=red)
    guardTable2.heading("Id",text="Id")
    guardTable2.heading("First Name",text="First Name")
    guardTable2.heading("Last Name",text="Last Name")
    guardTable2.heading("Gender",text="Gender")
    guardTable2.heading("Shift Starts At",text="Shift Starts At")
    guardTable2.heading("Added Date",text="Added Date")
    guardTable2.heading("Shift Ends At",text="Shift Ends At")
    guardTable2.config(show="headings")

    guardTable2.column("Id",width=50,anchor=CENTER)
    guardTable2.column("First Name",width=200,anchor=CENTER)
    guardTable2.column("Last Name",width=200,anchor=CENTER)
    guardTable2.column("Gender",width=150,anchor=CENTER)
    guardTable2.column("Shift Starts At",width=250,anchor=CENTER)
    guardTable2.column("Added Date",width=150,anchor=CENTER)
    guardTable2.column("Shift Ends At",width=150,anchor=CENTER)

###################### Searche by Name



    titleLabel=Label(tab2,text="Searche by Name",font=("OCR A Std",48,"italic"),bg=gray,borderwidth=5,fg=move, relief="solid")
    titleLabel.grid(row=0,columnspan=2,pady=50)

    firstnameRechercheLabel=Label(tab2,text="First Name",font=("OCR A Std",28,"bold"),bg=move,width=21)
    firstnameRechercheLabel.grid(row=1,column=0,sticky=W,padx=200,pady=20)
    firstnameRechercheEntry=Entry(tab2,font=("OCR A Std",18,"bold"))
    firstnameRechercheEntry.grid(row=1,column=1)


    lastnameRechercheLabel=Label(tab2,text="First Name",font=("OCR A Std",28,"bold"),bg=move,width=21)
    lastnameRechercheLabel.grid(row=2,column=0,sticky=W,padx=200,pady=20)
    lastnameRechercheEntry=Entry(tab2,font=("OCR A Std",18,"bold"))
    lastnameRechercheEntry.grid(row=2,column=1)


    rechercheButton=Button(tab2,text="Recherche",font=("OCR A Std",28,"bold"),bg=move,borderless=1,command=lambda:search_guardian_data2(firstnameRechercheEntry.get(),lastnameRechercheEntry.get(),guardTable3))
    rechercheButton.grid(row=3,column=0,sticky=W,padx=200,pady=20)


    quitterButton=Button(tab2,text="Quitter",font=("OCR A Std",28,"bold"),bg=move,borderless=1,command=screen.destroy)
    quitterButton.grid(row=3,column=1,sticky=E,padx=200,pady=20)


    RechercheButton=Button(tab2,text="Save Profile",font=("OCR A Std",28,"bold"),borderless=1,command=lambda:profile_export_data(guardTable3))
    RechercheButton.grid(row=4,columnspan=2)


    buttomFrame=Frame(tab2 ,padx=95,pady=20,height=3000,bg=gray)
    buttomFrame.grid(row=5,columnspan=2)


    ScrollbarX=Scrollbar(buttomFrame,orient=HORIZONTAL)
    ScrollbarY=Scrollbar(buttomFrame,orient=VERTICAL)
    ScrollbarX.pack(side=BOTTOM,fill=X)
    ScrollbarY.pack(side=RIGHT,fill=Y)

    guardTable3=ttk.Treeview(buttomFrame,columns=("Id","First Name","Last Name","Gender","Shift Starts At","Added Date","Shift Ends At"),xscrollcommand=ScrollbarX.set,yscrollcommand=ScrollbarY.set)
    guardTable3.pack(fill=BOTH,expand=1)

    ScrollbarX.config(command=guardTable3.xview)
    ScrollbarY.config(command=guardTable3.yview)
    ScrollbarX.config(background=red)
    guardTable3.heading("Id",text="Id")
    guardTable3.heading("First Name",text="First Name")
    guardTable3.heading("Last Name",text="Last Name")
    guardTable3.heading("Gender",text="Gender")
    guardTable3.heading("Shift Starts At",text="Shift Starts At")
    guardTable3.heading("Added Date",text="Added Date")
    guardTable3.heading("Shift Ends At",text="Shift Ends At")
    guardTable3.config(show="headings")

    guardTable3.column("Id",width=50,anchor=CENTER)
    guardTable3.column("First Name",width=200,anchor=CENTER)
    guardTable3.column("Last Name",width=200,anchor=CENTER)
    guardTable3.column("Gender",width=150,anchor=CENTER)
    guardTable3.column("Shift Starts At",width=250,anchor=CENTER)
    guardTable3.column("Added Date",width=150,anchor=CENTER)
    guardTable3.column("Shift Ends At",width=150,anchor=CENTER)
############## Searche by Genre


    buttomFrame=Frame(tab3 ,padx=95,pady=20,height=3000,bg=gray)
    buttomFrame.grid(row=5,columnspan=2)



    titleLabel=Label(tab3,text="Searche by Genre",font=("OCR A Std",48,"italic"),bg=gray,borderwidth=5, fg=move,relief="solid")
    titleLabel.grid(row=0,columnspan=2,pady=50)

    genderRechercheLabel=Label(tab3,text="genre :",font=("OCR A Std",28,"bold"),bg=move,width=21)
    genderRechercheLabel.grid(row=1,column=0,sticky=W,padx=200,pady=20)
    genderRechercheEntry=Entry(tab3,font=("OCR A Std",18,"bold"))
    genderRechercheEntry.grid(row=1,column=1)


    rechercheButton=Button(tab3,text="Recherche",font=("OCR A Std",28,"bold"),borderless=1,bg=move,command=lambda:search_guardian_data3(genderRechercheEntry.get(),guardTable4))
    rechercheButton.grid(row=3,column=0,sticky=W,padx=200,pady=20)


    quitterButton=Button(tab3,text="Quitter",font=("OCR A Std",28,"bold"),bg=move,borderless=1,command=screen.destroy)
    quitterButton.grid(row=3,column=1,sticky=E,padx=200,pady=20)


    RechercheButton=Button(tab3,text="Save Profile",font=("OCR A Std",28,"bold"),borderless=1,command=lambda:profile_export_data(guardTable4))
    RechercheButton.grid(row=4,columnspan=2)



    ScrollbarX=Scrollbar(buttomFrame,orient=HORIZONTAL)
    ScrollbarY=Scrollbar(buttomFrame,orient=VERTICAL)
    ScrollbarX.pack(side=BOTTOM,fill=X)
    ScrollbarY.pack(side=RIGHT,fill=Y)

    guardTable4=ttk.Treeview(buttomFrame,columns=("Id","First Name","Last Name","Gender","Shift Starts At","Added Date","Shift Ends At"),xscrollcommand=ScrollbarX.set,yscrollcommand=ScrollbarY.set)
    guardTable4.pack(fill=BOTH,expand=1)

    ScrollbarX.config(command=guardTable.xview)
    ScrollbarY.config(command=guardTable.yview)
    ScrollbarX.config(background=red)
    guardTable4.heading("Id",text="Id")
    guardTable4.heading("First Name",text="First Name")
    guardTable4.heading("Last Name",text="Last Name")
    guardTable4.heading("Gender",text="Gender")
    guardTable4.heading("Shift Starts At",text="Shift Starts At")
    guardTable4.heading("Added Date",text="Added Date")
    guardTable4.heading("Shift Ends At",text="Shift Ends At")
    guardTable4.config(show="headings")

    guardTable4.column("Id",width=50,anchor=CENTER)
    guardTable4.column("First Name",width=200,anchor=CENTER)
    guardTable4.column("Last Name",width=200,anchor=CENTER)
    guardTable4.column("Gender",width=150,anchor=CENTER)
    guardTable4.column("Shift Starts At",width=250,anchor=CENTER)
    guardTable4.column("Added Date",width=150,anchor=CENTER)
    guardTable4.column("Shift Ends At",width=150,anchor=CENTER)       

#la fonction de lajout des prisonier
def add_data():
    global mycursor,con,fetched_data
    if  firstNameEntry.get()==''or lastNameEntry.get()==''or val.get()==''or shiftstartingtimeEntry.get()=='' or shiftendEntry.get()=="" or imageUrl=="":
        messagebox.showerror("Error","All feilds are requied",parent=screen)
    else:
        newguard=guard(firstNameEntry.get(),lastNameEntry.get(),val.get(),shiftstartingtimeEntry.get(),shiftendEntry.get(),imageUrl)
        newguard.addguard()

        result=messagebox.askyesno("Confirm","Data addes successfully. Do you want to clean the form")
        if result:
            firstNameEntry.delete(0,END)
            lastNameEntry.delete(0,END)

            shiftstartingtimeEntry.delete(0,END)
            shiftendEntry.delete(0,END)
            uploadimgBtn.config(text="Click to upload")
            uploadimgBtn.config(state=NORMAL)
            
        
        show_guardian_data(guardTable)

#la fonction de la moudefication des donnes de la base de donne
def update_data():
    global firstNameEntry,lastNameEntry,val,shiftstartingtimeEntry,shiftendingtimeEntry,imageUrl,id

    updateGuard(firstNameEntry.get(),lastNameEntry.get(),val.get(),shiftstartingtimeEntry.get(),shiftendingtimeEntry.get(),imageUrl,id,screen,guardTable)

#la fonction de la quittation des programe
def exit_programe():
    result=messagebox.askyesno("confirm","Do you want to exit?")
    if result:
        root.destroy()
    else:
        pass

#la fonction de l'exportation des donnes d'un guardian
def profile_export_data(guardTablex):
    indexing=guardTablex.focus()
    if len(guardTablex.get_children())==1 :
        indexing=guardTablex.get_children()[0]
    elif guardTablex.focus()=="":
        export_data(guardTablex)
        return
    
    content=guardTablex.item(indexing)
    content_list=content["values"]
    url=filedialog.asksaveasfilename(defaultextension="pdf")
    if url!="":
        pdf=FPDF()
        x = (pdf.w - 50) / 2
        y = 30
        pdf.add_page()
        a = (pdf.w - 20) / 2
        b = 5
        pdf.image("/Users/tayastudios/Desktop/project/seperatedprisonnier/images/Seal_of_the_Federal_Bureau_of_Prisons.svg.png", a, b, 20)
        pdf.set_font('Arial', 'B', 26)


        pdf.cell(20, 90, txt="", ln=1)
        pdf.set_line_width(2)

        pdf.set_text_color(255, 55, 0)
        pdf.cell(20, 10, txt="", ln=1)
        pdf.cell(0, 10, f"guard N° {content_list[0]}", 0, 1, "C")
        pdf.cell(20, 10, txt="", ln=1)

        pdf.image(content_list[6], x, y, 50)
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
        pdf.cell(95, 25, "Shift Starting Time", border=1,align="C")
        pdf.set_text_color(0, 0, 0)
        pdf.set_font('Arial', 'B', 22)
        pdf.cell(95, 25, f"{content_list[4]}", border=1,align="C")
        pdf.ln()


        pdf.set_text_color(255, 0, 0)
        pdf.set_font('Arial', 'B', 26)
        pdf.cell(95, 25, "Shft Ending Time", border=1,align="C")
        pdf.set_text_color(0, 0, 0)
        pdf.set_font('Arial', 'B', 22)
        pdf.cell(95, 25, f"{content_list[5]}", border=1,align="C")
        pdf.ln()


        pdf.set_font('Arial', 'B', 8)
        pdf.set_xy(160, 250)  # adjust the x and y position to position the signature
        pdf.cell(30, 10, "The signature of the director and the seal of the prison institution :", align="R")

        
        # pdf.cell(260, 20, "The signature of the director and the seal of the prison institution :", 0, 40, "C")


        pdf.output(url, 'F') 
        messagebox.showinfo("Enfo","file saved successfully")
        
#la fonction de lafichage des prisoniers
def guardProfile():
    if guardTable.focus()=="":
        messagebox.showerror("Error","You must select a guard")
    else:
        screen=Toplevel(root)
        screen.state("zoomed")
        screen.config(background=gray)
        screen.geometry("2000x900+100+20")
        indexing=guardTable.focus()
        content=guardTable.item(indexing)
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

        profileshiftstartLabel=Label(allFrame,text="shiftstart       :"+content_list[4],font=font3,height=2,width=25,fg=move,bg=gray)
        profileshiftstartLabel.grid(row=3,column=0,pady=35,padx=80)


        profileshiftendLabel=Label(allFrame,text="shiftend  :"+content_list[5],font=font3,height=2,width=25,fg=move,bg=gray)
        profileshiftendLabel.grid(row=3,column=1,pady=35,padx=80)

        exit_button=Button(allFrame,text="Save",font=font3,width=450,height=60,borderless=1,command=lambda:profile_export_data(guardTable))
        exit_button.grid(row=4,column=0)
        exit_button=Button(allFrame,text="Exit",font=font3,width=450,height=60,borderless=1,command=lambda:screen.destroy())
        exit_button.grid(row=4,column=1)



        filename = (content_list[6],)
        col=0 # start from column 1
        row=0 # start from row 3 

        img=Image.open(filename[0]) # read the image file
        img=img.resize((300,400)) # new width & height
        img=ImageTk.PhotoImage(img)
        e1 =CircleButton(allFrame,height=300,borderless=1)
        e1.grid(row=row,columnspan=2,pady=10)
        e1.image = img # keep a reference! by attaching it to a widget attribute
        e1['image']=img # Show Image 


        


 
 
  
    screen.mainloop()

#la fonction de l'exportation des donnes
def export_data(guardTable):
    url=filedialog.asksaveasfilename(defaultextension="pdf")
    if url!="":
        indexing=guardTable.get_children()
        newlist=[]
        pdf=FPDF()
        x = (pdf.w - 50) / 2
        y = 10
        pdf.add_page()
        
        pdf.image("/Users/tayastudios/Desktop/project/seperatedprisonnier/images/Seal_of_the_Federal_Bureau_of_Prisons copy.svg.png", x, y, 50)
        pdf.set_text_color(255, 55, 0)
        pdf.set_font('Arial', 'B', 26)
        pdf.cell(20, 10, txt="", ln=1)
        pdf.cell(20, 10, txt="", ln=1)
        pdf.cell(20, 10, txt="", ln=1)
        pdf.cell(20, 10, txt="", ln=1)
        pdf.cell(20, 10, txt="", ln=1)
        pdf.set_font('Arial', 'B', 36)
        pdf.cell(0, 10, "Guards List", 0, 1, "C")
        pdf.cell(20, 10, txt="", ln=1)
        pdf.set_font("Arial", "B", 12)
        pdf.cell(10, 10, " Id ", border=1,align="C")
        pdf.cell(45, 10, "The Full Name ", border=1,align="C")
        pdf.cell(45, 10, "The Gender", border=1,align="C")
        pdf.cell(45, 10, "Shift Starting Time", border=1,align="C")
        pdf.cell(45, 10, "Shift Ending Time", border=1,align="C")
        pdf.ln()
        pdf.set_font('Arial', 'B', 8)
        pdf.set_text_color(0, 0, 0)
        for index in indexing:
            content =guardTable.item(index)
            datalist=content["values"]
            pdf.cell(10, 10, f"{datalist[0]}", border=1,align="C")
            pdf.cell(45, 10, f"{datalist[1]} {datalist[2]}", border=1,align="C")
            pdf.cell(45, 10, f"{datalist[3]}", border=1,align="C")
            pdf.cell(45, 10, f"{datalist[4]}", border=1,align="C")
            pdf.cell(45, 10, f"{datalist[5]}", border=1,align="C")
            pdf.ln()


        pdf.set_font('Arial', 'B', 8)
        pdf.set_xy(160, 266)  # adjust the x and y position to position the signature
        pdf.cell(30, 10, "The signature of the director and the seal of the prison institution :", align="R")

        
        # pdf.cell(260, 10, "The signature of the director and the seal of the prison institution", 0, 0, "C")
        pdf.output(url, 'F') 
        messagebox.showinfo("Enfo","file saved successfully")


#################################################
#                     root                      #
#################################################

root=Tk() 

root.config(background = gray) 
root.geometry("1174x780+100+20")
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

titleLabel=Label(root,text="guards List",font=font1,bg=gray,borderwidth=0,fg="#ccc", relief="solid",padx=300)
titleLabel.place(x=300,y=5)

#################################################
#                  left frame                   #
#################################################
leftFrame=Frame(root,bg=gray)
leftFrame.place(x=50,y=80,width=300,height=800)
logo_image=PhotoImage(file="/Users/tayastudios/Desktop/project/seperatedprisonnier/images/police.png")
logo_Label=Label(leftFrame,image=logo_image,bg=gray)
logo_Label.grid(row=0,column=0)






#button d'ajout
addguardButton=Button(leftFrame,text="Add Gardien",width=250,height=50,fg=red,bg=move,font=font2,command=lambda:toplevel_data("Add Gardien","ADD",add_data),borderless=1,activebackground="red")
addguardButton.grid(row=1,column=0,pady=15)

#button de roucherche
searchguardButton=Button(leftFrame,text="Search Gardien",width=250,height=50,fg=red,bg=move,font=font2,command=toplevel_searche,borderless=1)
searchguardButton.grid(row=2,column=0,pady=15)

#button de supretion
deleteguardButton=Button(leftFrame,text="Delete Gardien",width=250,height=50,fg=red,bg=move,font=font2,command=lambda:delete_guard(guardTable),borderless=1)
deleteguardButton.grid(row=3,column=0,pady=15)

#button d'update
updateguardButton=Button(leftFrame,text="Update Gardien",width=250,height=50,fg=red,bg=move,font=font2,command=lambda:toplevel_data("Update Gardien","Update Gardien",update_data),borderless=1)
updateguardButton.grid(row=4,column=0,pady=15)

#button d'affichage
showguardButton=Button(leftFrame,text="Show Gardien",width=250,height=50,fg=red,font=font2,command=guardProfile,bg=move, borderless=1)
showguardButton.grid(row=5,column=0,pady=15)
#button d'enregenstrement
exportguardButton=Button(leftFrame,text="Save File",width=250,height=50,fg=red,bg=move,font=font2,command=lambda:export_data(guardTable),borderless=1)
exportguardButton.grid(row=6,column=0,pady=15)

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
#la creation des tableaux de lafichage des prisonners
guardTable=ttk.Treeview(rightFrame,columns=("Id","First Name","Last Name","Gender","Shift Starting Time","Shift Ending Time"),xscrollcommand=ScrollbarX.set,yscrollcommand=ScrollbarY.set)
guardTable.pack(fill=BOTH,expand=1)

ScrollbarX.config(command=guardTable.xview)
ScrollbarY.config(command=guardTable.yview)

guardTable.heading("Id",text="Id")
guardTable.heading("First Name",text="First Name")
guardTable.heading("Last Name",text="Last Name")
guardTable.heading("Gender",text="Gender")
guardTable.heading("Shift Starting Time",text="Shift Starting Time")
guardTable.heading("Shift Ending Time",text="Shift Ending Time")
guardTable.config(show="headings")

guardTable.column("Id",width=50,anchor=CENTER)
guardTable.column("First Name",width=200,anchor=CENTER)
guardTable.column("Last Name",width=200,anchor=CENTER)
guardTable.column("Gender",width=150,anchor=CENTER)
guardTable.column("Shift Starting Time",width=150,anchor=CENTER)
guardTable.column("Shift Ending Time",width=150,anchor=CENTER)



style=ttk.Style()
style.configure("Treeview",rowheight=51,font=("arial",16,"bold"),foreground=gray,background="#ffce00",fieldbackground=move)
style.configure("Treeview.Heading",font=("arial",15,"bold"),foreground=red)




#la connection de la base des donnes
databaseconnect()
connectguardian()
try:
    show_guardian_data(guardTable)
except:
    pass


root.mainloop()