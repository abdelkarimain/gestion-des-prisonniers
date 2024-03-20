


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
#upload File fct












#time
def clock():
    global date,currenttime
    date=time.strftime("%d/%m/%Y")
    currenttime=time.strftime("%H:%M:%S")
    datetimelabel.config(text=f"  Date: {date}\nTime: {currenttime}")
    datetimelabel.after(1000,clock)



#la creation de la fenêtre de lajout et l'update
def toplevel_data(title,button_text,button_command):
    global firstNameEntry,lastNameEntry,addressEntry,telEntry,screen,prisoneridEntry,firstnamesearch,lastnamesearch,addresssearch,telsearch,prisoneridsearch,datesearch,id
    
    if button_command==update_data :
        if visitorTable.focus()=="":
            messagebox.showerror("Error","You must select a visitor")
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


            addressLabel=Label(leftFrame2,text="address",font=("OCR A Std",28,"bold"),bg=move,width=15,fg=red)
            addressLabel.grid(row=4,column=0,sticky=W,padx=0,pady=20)
            addressEntry=Entry(rightFrame2,font=("OCR A Std",24,"bold"))
            addressEntry.grid(row=4,column=1,pady=20)



            telLabel=Label(leftFrame2,text="Telephone",font=("OCR A Std",28,"bold"),bg=move,width=15,fg=red)
            telLabel.grid(row=5,column=0,sticky=W,padx=0,pady=20)
            telEntry=Entry(rightFrame2,font=("OCR A Std",24,"bold"))
            telEntry.grid(row=5,column=1,pady=20)


            prisoneridLabel=Label(leftFrame2,text="prisoner Id",font=("OCR A Std",28,"bold"),bg=move,width=15,fg=red)
            prisoneridLabel.grid(row=6,column=0,sticky=W,padx=0,pady=20)
            prisoneridEntry=Entry(rightFrame2,font=("OCR A Std",24,"bold"))
            prisoneridEntry.grid(row=6,column=1,pady=20)



            

            ajoutButton=Button(leftFrame2,text=button_text,font=("OCR A Std",28,"bold"),bg=move,command=button_command,borderless=1)
            ajoutButton.grid(row=8,column=0,padx=0,pady=20)


            CloseButton=Button(rightFrame2,text="Close",font=("OCR A Std",28,"bold"),bg=move,command=screen.destroy,borderless=1,fg=red)
            CloseButton.grid(row=8,column=1,sticky=E,padx=150,pady=20)
            
            indexing=visitorTable.focus()
            content=visitorTable.item(indexing)
            content_list=content["values"]
            id=content_list[0]
            
            
            firstNameEntry.insert(0,content_list[1])
            lastNameEntry.insert(0,content_list[2])
            addressEntry.insert(0,content_list[3])
            telEntry.insert(0,"0"+str(content_list[4]))
            
           
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


        addressLabel=Label(leftFrame2,text="address",font=("OCR A Std",28,"bold"),bg=move,width=15,fg=red)
        addressLabel.grid(row=4,column=0,sticky=W,padx=0,pady=20)
        addressEntry=Entry(rightFrame2,font=("OCR A Std",24,"bold"))
        addressEntry.grid(row=4,column=1,pady=20)



        shiftstartLabel=Label(leftFrame2,text="Telephone",font=("OCR A Std",28,"bold"),bg=move,width=15,fg=red)
        shiftstartLabel.grid(row=5,column=0,sticky=W,padx=0,pady=20)
        telEntry=Entry(rightFrame2,font=("OCR A Std",24,"bold"))
        telEntry.grid(row=5,column=1,pady=20)


        prisoneridLabel=Label(leftFrame2,text="prisoner Id",font=("OCR A Std",28,"bold"),bg=move,width=15,fg=red)
        prisoneridLabel.grid(row=6,column=0,sticky=W,padx=0,pady=20)
        prisoneridEntry=Entry(rightFrame2,font=("OCR A Std",24,"bold"))
        prisoneridEntry.grid(row=6,column=1,pady=20)



        ajoutButton=Button(leftFrame2,text=button_text,font=("OCR A Std",28,"bold"),bg=move,command=button_command,borderless=1)
        ajoutButton.grid(row=8,column=0,padx=0,pady=20)


        CloseButton=Button(rightFrame2,text="Close",font=("OCR A Std",28,"bold"),bg=move,command=screen.destroy,borderless=1,fg=red)
        CloseButton.grid(row=8,column=1,sticky=E,padx=150,pady=20)

#la creation de la fenêtre de la roucherche
def toplevel_search():
    global firstNameEntry,lastNameEntry,addressEntry,screen,firstnamesearchEntry,visitorTable2,visitorTable3,visitorTable4,lastnamesearchEntry,addresssearchEntry,idsearchEntry,shiftstartsearchEntry,visitorTable5
    screen=Toplevel(root)
    screen.state("zoomed")
    screen.config(background=gray)
    screen.geometry("2000x900+100+20")
    tabControl = ttk.Notebook(screen)
    tab1 =Frame(tabControl,background=gray)
    tab2 =Frame(tabControl,bg=red)
    tab3 =Frame(tabControl,background=gray)
    

    tabControl.add(tab1, text ='search by Name')
    tabControl.add(tab2, text ='search by address')
    tabControl.add(tab3, text ='search by telephone N')
    
    tabControl.pack(expand = 1, fill ="both")



###################### search by Name



    titleLabel=Label(tab1,text="search by Name",font=("OCR A Std",48,"italic"),bg=gray,borderwidth=5,fg=move, relief="solid")
    titleLabel.grid(row=0,columnspan=2,pady=50)

    firstnamesearchLabel=Label(tab1,text="First Name",font=("OCR A Std",28,"bold"),bg=move,width=21)
    firstnamesearchLabel.grid(row=1,column=0,sticky=W,padx=157,pady=20)
    firstnamesearchEntry=Entry(tab1,font=("OCR A Std",18,"bold"))
    firstnamesearchEntry.grid(row=1,column=1)


    lastnamesearchLabel=Label(tab1,text="First Name",font=("OCR A Std",28,"bold"),bg=move,width=21)
    lastnamesearchLabel.grid(row=2,column=0,sticky=W,padx=157,pady=20)
    lastnamesearchEntry=Entry(tab1,font=("OCR A Std",18,"bold"))
    lastnamesearchEntry.grid(row=2,column=1)
   


    searchButton=Button(tab1,text="Search Name",font=("OCR A Std",28,"bold"),bg=move,borderless=1,command=lambda:search_visitor_data2(firstnamesearchEntry.get(),lastnamesearchEntry.get(),visitorTable3))
    searchButton.grid(row=3,column=0,sticky=W,padx=157,pady=20)


    CloseButton=Button(tab1,text="Close Window",font=("OCR A Std",28,"bold"),bg=move,borderless=1,command=screen.destroy)
    CloseButton.grid(row=3,column=1,sticky=E,padx=157,pady=20)


    searchButton=Button(tab1,text="Save Profile",font=("OCR A Std",28,"bold"),borderless=1,command=lambda:profile_export_data(visitorTable3))
    searchButton.grid(row=4,columnspan=2)


    buttomFrame=Frame(tab1 ,padx=95,pady=20,height=3000,bg=gray)
    buttomFrame.place(x=15,y=480,height=345,width=1360)

    ScrollbarX=Scrollbar(buttomFrame,orient=HORIZONTAL)
    ScrollbarY=Scrollbar(buttomFrame,orient=VERTICAL)
    ScrollbarX.pack(side=BOTTOM,fill=X)
    ScrollbarY.pack(side=RIGHT,fill=Y)

    visitorTable3=ttk.Treeview(buttomFrame,columns=("Id","First Name","Last Name","address","telephone","Prisoner Name","Current Date"),xscrollcommand=ScrollbarX.set,yscrollcommand=ScrollbarY.set)
    visitorTable3.pack(fill=BOTH,expand=1)

    ScrollbarX.config(command=visitorTable.xview)
    ScrollbarY.config(command=visitorTable.yview)

    visitorTable3.heading("Id",text="Id")
    visitorTable3.heading("First Name",text="First Name")
    visitorTable3.heading("Last Name",text="Last Name")
    visitorTable3.heading("address",text="address")
    visitorTable3.heading("telephone",text="telephone")
    visitorTable3.heading("Prisoner Name",text="Prisoner Name")
    visitorTable3.heading("Current Date",text="Current Date")
    visitorTable3.config(show="headings")


    visitorTable3.column("Id",width=50,anchor=CENTER)
    visitorTable3.column("First Name",width=200,anchor=CENTER)
    visitorTable3.column("Last Name",width=200,anchor=CENTER)
    visitorTable3.column("address",width=200,anchor=CENTER)
    visitorTable3.column("telephone",width=200,anchor=CENTER)
    visitorTable3.column("Prisoner Name",width=200,anchor=CENTER)
    visitorTable3.column("Current Date",width=150,anchor=CENTER)    
############## search by address



    buttomFrame=Frame(tab2 ,padx=95,pady=20,height=3000,bg=gray)
    buttomFrame.place(x=15,y=380,height=445,width=1360)



    titleLabel=Label(tab2,text="search by address",font=("OCR A Std",48,"italic"),bg=gray,borderwidth=5, fg=move,relief="solid")
    titleLabel.grid(row=0,columnspan=2,pady=50)

    addresssearchLabel=Label(tab2,text="address :",font=("OCR A Std",28,"bold"),bg=move,width=21)
    addresssearchLabel.grid(row=1,column=0,sticky=W,padx=165,pady=20)
    addresssearchEntry=Entry(tab2,font=("OCR A Std",18,"bold"))
    addresssearchEntry.grid(row=1,column=1)


    searchButton=Button(tab2,text="Search address",font=("OCR A Std",28,"bold"),borderless=1,bg=move,command=lambda:search_visitor_data3(addresssearchEntry.get(),visitorTable4))
    searchButton.grid(row=3,column=0,sticky=W,padx=165,pady=20)


    CloseButton=Button(tab2,text="Close Window",font=("OCR A Std",28,"bold"),bg=move,borderless=1,command=screen.destroy)
    CloseButton.grid(row=3,column=1,sticky=E,padx=165,pady=20)


    searchButton=Button(tab2,text="Save Profile",font=("OCR A Std",28,"bold"),borderless=1,command=lambda:profile_export_data(visitorTable4))
    searchButton.grid(row=4,columnspan=2)

    ScrollbarX=Scrollbar(buttomFrame,orient=HORIZONTAL)
    ScrollbarY=Scrollbar(buttomFrame,orient=VERTICAL)
    ScrollbarX.pack(side=BOTTOM,fill=X)
    ScrollbarY.pack(side=RIGHT,fill=Y)

    visitorTable4=ttk.Treeview(buttomFrame,columns=("Id","First Name","Last Name","address","telephone","Prisoner Name","Current Date"),xscrollcommand=ScrollbarX.set,yscrollcommand=ScrollbarY.set)
    visitorTable4.pack(fill=BOTH,expand=1)

    ScrollbarX.config(command=visitorTable.xview)
    ScrollbarY.config(command=visitorTable.yview)


    visitorTable4.heading("Id",text="Id")
    visitorTable4.heading("First Name",text="First Name")
    visitorTable4.heading("Last Name",text="Last Name")
    visitorTable4.heading("address",text="address")
    visitorTable4.heading("telephone",text="telephone")
    visitorTable4.heading("Prisoner Name",text="Prisoner Name")
    visitorTable4.heading("Current Date",text="Current Date")
    visitorTable4.config(show="headings")


    visitorTable4.column("Id",width=50,anchor=CENTER)
    visitorTable4.column("First Name",width=200,anchor=CENTER)
    visitorTable4.column("Last Name",width=200,anchor=CENTER)
    visitorTable4.column("address",width=200,anchor=CENTER)
    visitorTable4.column("telephone",width=200,anchor=CENTER)
    visitorTable4.column("Prisoner Name",width=200,anchor=CENTER)
    visitorTable4.column("Current Date",width=150,anchor=CENTER)    



    ############## search by telephone N


    buttomFrame=Frame(tab3 ,padx=95,pady=20,height=3000,bg=gray)
    buttomFrame.place(x=15,y=380,height=445,width=1360)



    titleLabel=Label(tab3,text="search by telephone N",font=("OCR A Std",48,"italic"),bg=gray,borderwidth=5, fg=move,relief="solid")
    titleLabel.grid(row=0,columnspan=2,pady=50)

    telephonesearchLabel=Label(tab3,text="telephone N :",font=("OCR A Std",28,"bold"),bg=move,width=21)
    telephonesearchLabel.grid(row=1,column=0,sticky=W,padx=155,pady=20)
    telephonesearchEntry=Entry(tab3,font=("OCR A Std",18,"bold"))
    telephonesearchEntry.grid(row=1,column=1)


    searchButton=Button(tab3,text="Search Telephone",font=("OCR A Std",28,"bold"),borderless=1,bg=move,command=lambda:search_visitor_data1(telephonesearchEntry.get(),visitorTable5))
    searchButton.grid(row=3,column=0,sticky=W,padx=155,pady=20)


    CloseButton=Button(tab3,text="Close Window",font=("OCR A Std",28,"bold"),bg=move,borderless=1,command=screen.destroy)
    CloseButton.grid(row=3,column=1,sticky=E,padx=155,pady=20)


    searchButton=Button(tab3,text="Save Profile",font=("OCR A Std",28,"bold"),borderless=1,command=lambda:profile_export_data(visitorTable5))
    searchButton.grid(row=4,columnspan=2)



 
    ScrollbarX=Scrollbar(buttomFrame,orient=HORIZONTAL)
    ScrollbarY=Scrollbar(buttomFrame,orient=VERTICAL)
    ScrollbarX.pack(side=BOTTOM,fill=X)
    ScrollbarY.pack(side=RIGHT,fill=Y)

    visitorTable5=ttk.Treeview(buttomFrame,columns=("Id","First Name","Last Name","address","telephone","Prisoner Name","Current Date"),xscrollcommand=ScrollbarX.set,yscrollcommand=ScrollbarY.set)
    visitorTable5.pack(fill=BOTH,expand=1)

    ScrollbarX.config(command=visitorTable.xview)
    ScrollbarY.config(command=visitorTable.yview)


    visitorTable5.heading("Id",text="Id")
    visitorTable5.heading("First Name",text="First Name")
    visitorTable5.heading("Last Name",text="Last Name")
    visitorTable5.heading("address",text="address")
    visitorTable5.heading("telephone",text="telephone")
    visitorTable5.heading("Prisoner Name",text="Prisoner Name")
    visitorTable5.heading("Current Date",text="Current Date")
    visitorTable5.config(show="headings")


    visitorTable5.column("Id",width=50,anchor=CENTER)
    visitorTable5.column("First Name",width=150,anchor=CENTER)
    visitorTable5.column("Last Name",width=150,anchor=CENTER)
    visitorTable5.column("address",width=150,anchor=CENTER)
    visitorTable5.column("telephone",width=150,anchor=CENTER)
    visitorTable5.column("Prisoner Name",width=150,anchor=CENTER)
    visitorTable5.column("Current Date",width=150,anchor=CENTER)    

#la fonction de lajout des visitor
def add_data():
    global mycursor,con,fetched_data
    if  firstNameEntry.get()==''or lastNameEntry.get()==''or addressEntry.get()==''or telEntry.get()=='' or prisoneridEntry.get()=="" :
        messagebox.showerror("Error","All feilds are requied",parent=screen)
    else:
        newvisitor=visitor(firstNameEntry.get(),lastNameEntry.get(),addressEntry.get(),telEntry.get(),prisoneridEntry.get(),)
        newvisitor.addvisitor()
        show_visitor_data(visitorTable)
        
        if result_add_prisonner_id:
            firstNameEntry.delete(0,END)
            lastNameEntry.delete(0,END)
            addressEntry.delete(0,END)
            telEntry.delete(0,END)
            prisoneridEntry.delete(0,END)


#la fonction de la moudefication des donnes de la base de donne
def update_data():
    global firstNameEntry,lastNameEntry,addressEntry,telEntry,prisoneridEntry,id

    updatevisitor(firstNameEntry.get(),lastNameEntry.get(),addressEntry.get(),telEntry.get(),prisoneridEntry.get(),id,screen,visitorTable)

#la fonction de l'exportation des donnes d'un visitor
def profile_export_data(visitorTable):
    indexing=visitorTable.focus()
    if len(visitorTable.get_children())==1 :
        indexing=visitorTable.get_children()[0]
    elif visitorTable.focus()=="":
        export_data(visitorTable)
        return
    
    content=visitorTable.item(indexing)
    content_list=content["values"]
    url=filedialog.asksaveasfilename(defaultextension="pdf")
    print(url)
    if url!="":
        pdf=FPDF()
        x = (pdf.w - 60) / 2
        y = 30
        pdf.add_page()
        pdf.set_font('Arial', 'B', 26)
        pdf.set_text_color(255, 55, 0)
        pdf.cell(0, 10, f"Visitor N° {content_list[0]}", 0, 1, "C")

        pdf.cell(20, 80, txt="", ln=1)
        pdf.set_line_width(2)
        pdf.image("/Users/tayastudios/Desktop/project/seperatedprisonnier/images/Seal_of_the_Federal_Bureau_of_Prisons copy.svg.png", x, y, 60)

        pdf.set_text_color(255, 0, 0)
        pdf.set_font('Arial', 'B', 26)
        pdf.cell(95, 25, " The Full Name", border=1,align="C")
        pdf.set_text_color(0, 0, 0)
        pdf.set_font('Arial', 'B', 22)
        pdf.cell(95, 25, f"{content_list[1]} {content_list[2]}", border=1,align="C")
        pdf.ln()



        pdf.set_text_color(255, 0, 0)
        pdf.set_font('Arial', 'B', 26)
        pdf.cell(95, 25, "The address", border=1,align="C")
        pdf.set_text_color(0, 0, 0)
        pdf.set_font('Arial', 'B', 22)
        pdf.cell(95, 25, f"{content_list[3]}", border=1,align="C")
        pdf.ln()


        pdf.set_text_color(255, 0, 0)
        pdf.set_font('Arial', 'B', 26)
        pdf.cell(95, 25, "The Telephone N°", border=1,align="C")
        pdf.set_text_color(0, 0, 0)
        pdf.set_font('Arial', 'B', 22)
        pdf.cell(95, 25, f"{content_list[4]}", border=1,align="C")
        pdf.ln()


        pdf.set_text_color(255, 0, 0)
        pdf.set_font('Arial', 'B', 26)
        pdf.cell(95, 25, "The Prisoner's Name", border=1,align="C")
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
        pdf.set_xy(160, 250)  # adjust the x and y position to position the signature
        pdf.cell(30, 10, "The signature of the director and the seal of the prison institution ", align="R")

    


        pdf.output(url, 'F') 
        messagebox.showinfo("Enfo","file Saved successfully")


#la fonction de l'exportation des donnes
def export_data(visitorTable):
    url=filedialog.asksaveasfilename(defaultextension="pdf")
    if url!="":
        indexing=visitorTable.get_children()
        newlist=[]
        pdf=FPDF()
        x = (pdf.w - 50) / 2
        y = 5
        pdf.add_page()
        
        pdf.image("/Users/tayastudios/Desktop/project/seperatedprisonnier/images/Seal_of_the_Federal_Bureau_of_Prisons.svg.png", x, y, 50)
        pdf.set_text_color(255, 55, 0)
        pdf.set_font('Arial', 'B', 26)
        pdf.cell(20, 10, txt="", ln=1)
        pdf.cell(20, 10, txt="", ln=1)
        pdf.cell(20, 10, txt="", ln=1)
        pdf.cell(20, 10, txt="", ln=1)
        pdf.cell(20, 10, txt="", ln=1)
        pdf.set_font('Arial', 'B', 36)
        pdf.cell(0, 10, "Visitor List", 0, 1, "C")
        pdf.cell(20, 10, txt="", ln=1)
        pdf.set_font("Arial", "B", 12)
        pdf.cell(10, 10, " Id ", border=1,align="C")
        pdf.cell(45, 10, " The Full Name ", border=1,align="C")
        pdf.cell(45, 10, "The address", border=1,align="C")
        pdf.cell(45, 10, "The Telephone N°", border=1,align="C")
        pdf.cell(45, 10, "The Prisoner Name", border=1,align="C")
        pdf.ln()
        pdf.set_font('Arial', 'B', 8)
        pdf.set_text_color(0, 0, 0)
        for index in indexing:
            content =visitorTable.item(index)
            datalist=content["values"]
            pdf.cell(10, 10, f"{datalist[0]}", border=1,align="C")
            pdf.cell(45, 10, f"{datalist[1]} {datalist[2]}", border=1,align="C")
            pdf.cell(45, 10, f"{datalist[3]}", border=1,align="C")
            pdf.cell(45, 10, f"{datalist[4]}", border=1,align="C")
            pdf.cell(45, 10, f"{datalist[5]}", border=1,align="C")
            pdf.ln()


        pdf.set_font('Arial', 'B', 8)
        pdf.set_xy(160, 266)  # adjust the x and y position to position the signature
        pdf.cell(30, 10, "The signature of the director and the seal of the prison institution ", align="R")

        
        # pdf.cell(260, 10, "The signature of the director and the seal of the prison institution", 0, 0, "C")
        pdf.output(url, 'F') 
        messagebox.showinfo("Enfo","file Saved successfully")





#la fonction de la quittation des programe
def exit_programe():
    result=messagebox.askyesno("confirm","Do you want to exit?")
    if result:
        root.destroy()

        
    else:
        pass

#la fonction de lafichage des visitor
def visitorProfile():
    if visitorTable.focus()=="":
        messagebox.showerror("Error","You must select a visitour")
    else:
        screen=Toplevel(root)
        screen.state("zoomed")
        screen.config(background=gray)
        screen.geometry("2000x900+100+20")
        indexing=visitorTable.focus()
        content=visitorTable.item(indexing)
        content_list=content["values"]
        allFrame=Frame(screen,bg=move)
        allFrame.place(x=100,y=25,width=1250,height=800)
        profileidLabel=Label(allFrame,text="Id          :"+str(content_list[0]),font=font3,height=2,width=30,fg=move,bg=gray)
        profileidLabel.grid(row=1,column=0,pady=35,padx=40)
        profilefirstnameLabel=Label(allFrame,text="First Name  :"+content_list[1],font=font3,height=2,width=30,fg=move,bg=gray)
        profilefirstnameLabel.grid(row=1,column=1,pady=35,padx=40)
        profilelastnameLabel=Label(allFrame,text="Last Name   :"+content_list[2],font=font3,height=2,width=30,fg=move,bg=gray)
        profilelastnameLabel.grid(row=2,column=0,pady=35,padx=40)
        profileaddressLabel=Label(allFrame,text="address      :"+str(content_list[3]),font=font3,height=2,width=30,fg=move,bg=gray)
        profileaddressLabel.grid(row=2,column=1,pady=35,padx=40)

        profileshiftstartLabel=Label(allFrame,text="Telephone      :"+str(content_list[4]),font=font3,height=2,width=30,fg=move,bg=gray)
        profileshiftstartLabel.grid(row=3,column=0,pady=35,padx=40)


        profileprisoneridLabel=Label(allFrame,text="Prisoners Name :"+str(content_list[5]),font=font3,height=2,width=30,fg=move,bg=gray)
        profileprisoneridLabel.grid(row=3,column=1,pady=35,padx=40)


        profileAllLabel=Label(allFrame,text="mr(s)"+content_list[1]+" has visited mr(s) "+str(content_list[5]+" in "+content_list[6]),font=font3,height=2,width=60,fg=move,bg=gray)
        profileAllLabel.grid(row=4,columnspan=2,pady=35,padx=40)


        exit_button=Button(allFrame,text="Exit",font=font3,width=450,height=60,borderless=1,command=lambda:screen.destroy())
        exit_button.grid(row=5,column=1)
        Save_button=Button(allFrame,text="Save",font=font3,width=450,height=60,borderless=1,command=lambda:profile_export_data(visitorTable))
        Save_button.grid(row=5,column=0)


        screen.mainloop()





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

titleLabel=Label(root,text="visitors List",font=font1,bg=gray,borderwidth=0,fg="#ccc", relief="solid",padx=300)
titleLabel.place(x=300,y=5)

#################################################
#                  left frame                   #
#################################################
leftFrame=Frame(root,bg=gray)
leftFrame.place(x=50,y=80,width=300,height=800)
logo_image=PhotoImage(file="/Users/tayastudios/Desktop/project/seperatedprisonnier/images/meeting.png")
logo_Label=Label(leftFrame,image=logo_image,bg=gray)
logo_Label.grid(row=0,column=0)

#button d'ajout
addvisitorButton=Button(leftFrame,text="Add Visitor",width=250,height=50,fg=red,bg=move,font=font2,command=lambda:toplevel_data("Add Visitor","ADD",add_data),borderless=1,activebackground="red")
addvisitorButton.grid(row=1,column=0,pady=15)

#button de roucherche
searchvisitorButton=Button(leftFrame,text="search Visitor",width=250,height=50,fg=red,bg=move,font=font2,command=toplevel_search,borderless=1)
searchvisitorButton.grid(row=2,column=0,pady=15)

#button de supretion
deletevisitorButton=Button(leftFrame,text="Delete Visitor",width=250,height=50,fg=red,bg=move,font=font2,command=lambda:delete_visitor(visitorTable),borderless=1)
deletevisitorButton.grid(row=3,column=0,pady=15)

#button d'update
updatevisitorButton=Button(leftFrame,text="Update Visitor",width=250,height=50,fg=red,bg=move,font=font2,command=lambda:toplevel_data("Update Visitor","Update Visitor",update_data),borderless=1)
updatevisitorButton.grid(row=4,column=0,pady=15)

#button d'affichage
showvisitorButton=Button(leftFrame,text="Show Visitor",width=250,height=50,fg=red,font=font2,command=visitorProfile,bg=move, borderless=1)
showvisitorButton.grid(row=5,column=0,pady=15)

#button d'enregenstrement
exportvisitorButton=Button(leftFrame,text="Save File",width=250,height=50,fg=red,bg=move,font=font2,command=lambda:export_data(visitorTable),borderless=1)
exportvisitorButton.grid(row=6,column=0,pady=15)

#button de quittation
exitButton=Button(leftFrame,text="exit",width=250,height=50,fg=red,background=move,font=font2,command=exit_programe,borderless=1)
exitButton.grid(row=7,column=0,pady=15)


#################################################
#                  right frame                   #
#################################################
rightFrame=Frame(root,bg=red )
rightFrame.place(x=350,y=90,width=1010,height=757)
#la creation des tableaux de lafichage des visitor
ScrollbarX=Scrollbar(rightFrame,orient=HORIZONTAL)
ScrollbarY=Scrollbar(rightFrame,orient=VERTICAL)
ScrollbarX.pack(side=BOTTOM,fill=X)
ScrollbarY.pack(side=RIGHT,fill=Y)

visitorTable=ttk.Treeview(rightFrame,columns=("Id","First Name","Last Name","address","telephone","Prisoner Name","Current Date"),xscrollcommand=ScrollbarX.set,yscrollcommand=ScrollbarY.set)
visitorTable.pack(fill=BOTH,expand=1)

ScrollbarX.config(command=visitorTable.xview)
ScrollbarY.config(command=visitorTable.yview)

visitorTable.heading("Id",text="Id")
visitorTable.heading("First Name",text="First Name")
visitorTable.heading("Last Name",text="Last Name")
visitorTable.heading("address",text="address")
visitorTable.heading("telephone",text="telephone")
visitorTable.heading("Prisoner Name",text="Prisoner Name")
visitorTable.heading("Current Date",text="Current Date")
visitorTable.config(show="headings")

visitorTable.column("Id",width=50,anchor=CENTER)
visitorTable.column("First Name",width=150,anchor=CENTER)
visitorTable.column("Last Name",width=150,anchor=CENTER)
visitorTable.column("address",width=200,anchor=CENTER)
visitorTable.column("telephone",width=150,anchor=CENTER)
visitorTable.column("Prisoner Name",width=150,anchor=CENTER)
visitorTable.column("Current Date",width=150,anchor=CENTER)




style=ttk.Style()
style.configure("Treeview",rowheight=51,font=("arial",16,"bold"),foreground=gray,background="#ffce00",fieldbackground=move)
style.configure("Treeview.Heading",font=("arial",15,"bold"),foreground=red)




#la connection de la base des donnes
databaseconnect()
connectvisitor()
try:
    show_visitor_data(visitorTable)
except:
    pass


root.mainloop()