
from tkinter import *
import time
from tkinter import ttk,messagebox,filedialog
import pymysql
from tkmacosx import *
import pandas

date=time.strftime("%d/%m/%Y")
currenttime=time.strftime("%H:%M:%S")


########################################################
#                 Prisoner Database                    #
########################################################



 

#connection alabase de donne
def databaseconnect():
    global mycursor,con
    try:
        con=pymysql.connect(host="localhost",user="root",password="roottaya") 
        mycursor=con.cursor()
    except:
        messagebox.showerror("Error","invalid Details")
        return 
    try:
        query="create database PrisonManagmentSysteme"
        mycursor.execute(query)
    except:
        query="use PrisonManagmentSysteme"
        mycursor.execute(query)

#creation de la table prisonner
def connectPrisonnier():
    try:
        query="""create table prisonnier( 
        id int not null primary key auto_increment,
        firstname varchar(30),
        lastname varchar(10),
        gender varchar(20),
        crime varchar(30),
        punishment varchar(40),
        currentdate varchar(50),
        image varchar(500));
        """
        mycursor.execute(query)
        
    except:
        query="use PrisonManagmentSysteme"
        mycursor.execute(query)
#lajout des prisoner a la base de donne
def addPrisonnierdata(firstname,lastName,Gender,Crime,punishment,image):
    query=" insert into prisonnier values(null,%s,%s,%s,%s,%s,%s,%s)"
    mycursor.execute(query,(firstname,lastName,Gender,Crime,punishment,date,image))
    con.commit()

#lafichage des donne de labase de donne
def show_data(prisonnierTable):
    global fetched_data
    query="select * from prisonnier"
    mycursor.execute(query)
    fetched_data=mycursor.fetchall()
    prisonnierTable.delete(*prisonnierTable.get_children())

    for data in fetched_data:
        datalist=list(data)
        prisonnierTable.insert("",END,values=datalist)

#la recherche dans labase de donne (id,gender,firstnamelasname,crime)
def search_data1(idRechercheEntry,prisonnierTablex):
    query="select * from prisonnier where id=%s"
    mycursor.execute(query,(idRechercheEntry))
    prisonnierTablex.delete(*prisonnierTablex.get_children())
    fetched_data=mycursor.fetchall()
    for data in fetched_data:
        prisonnierTablex.insert("",END,values=data)  

def search_data2(firstnameRechercheEntry,lastnameRechercheEntry,prisonnierTablex):
    if firstnameRechercheEntry!="" and lastnameRechercheEntry=="":
        query="select * from prisonnier where firstname=%s  "
        mycursor.execute(query,(firstnameRechercheEntry))
    elif firstnameRechercheEntry=="" and lastnameRechercheEntry!="":
        query="select * from prisonnier where  lastname=%s"
        mycursor.execute(query,(lastnameRechercheEntry))
    else:
        query="select * from prisonnier where firstname=%s and lastname=%s  "
        mycursor.execute(query,(firstnameRechercheEntry,lastnameRechercheEntry))
    prisonnierTablex.delete(*prisonnierTablex.get_children())
    fetched_data=mycursor.fetchall()
    for data in fetched_data:
        prisonnierTablex.insert("",END,values=data)

def search_data3(genderRechercheEntry,prisonnierTablex):
    query="select * from prisonnier where gender=%s"
    mycursor.execute(query,(genderRechercheEntry))
    prisonnierTablex.delete(*prisonnierTablex.get_children())
    fetched_data=mycursor.fetchall()
    for data in fetched_data:
        prisonnierTablex.insert("",END,values=data)

def search_data4(crimeRechercheEntry,prisonnierTablex):
    query="select * from prisonnier where crime=%s"
    mycursor.execute(query,(crimeRechercheEntry))
    prisonnierTablex.delete(*prisonnierTablex.get_children())
    fetched_data=mycursor.fetchall()
    for data in fetched_data:
        prisonnierTablex.insert("",END,values=data)

#la modefication des dtables de labase de donne 
def update(firstNameEntry,lastNameEntry,genderEntry,crimeEntry,punishmentEntry,imageUrl,id,screen,prisonnierTable):
    query="update prisonnier set firstname=%s,lastname=%s,gender=%s,crime=%s,punishment=%s,image=%s,currentdate=%s where id=%s"
    mycursor.execute(query,(firstNameEntry,lastNameEntry,genderEntry,crimeEntry,punishmentEntry,imageUrl,date,id))
    con.commit()
    messagebox.showinfo("Success",f"Id {id} is modified successfully",parent=screen)
    screen.destroy()
    show_data(prisonnierTable)

#la suprission dee prisoner
def delete_prisonnier(prisonnierTable):
    if prisonnierTable.focus()=="":
        messagebox.showerror("Error","select a prisonnier")
    else:
        indexing=prisonnierTable.focus()
        content=prisonnierTable.item(indexing)
        content_id=content["values"][0]
        result=messagebox.askyesno("delete",f"are you sur that you want to delete Id {content_id} ?")
        if result:
            query="delete from prisonnier where id=%s"
            mycursor.execute(query,content_id)
            con.commit()
            show_data(prisonnierTable)
        else:
            pass



########################################################
#                 guardian Database                    #
########################################################








#creation de la table guardian
def connectguardian():
    try:
        query="""create table guard( 
        id int not null primary key auto_increment,
        firstname varchar(30),
        lastname varchar(10),
        gender varchar(20),
        shiftstarttime varchar(30),
        shiftendtime varchar(30),
        image varchar(500))  
        """
        mycursor.execute(query)
        
    except:
        query="use PrisonManagmentSysteme"
        mycursor.execute(query)

#lajout des guardian a la base de donne
def addgarddata(firstname,lastName,Gender,shiftstart,shiftend,image):
    query=" insert into guard values(id=%s,%s,%s,%s,%s,%s,%s)"
    mycursor.execute(query,(None,firstname,lastName,Gender,shiftstart,shiftend,image))
    con.commit()

#lafichage des donne de labase de donne 
def show_guardian_data(guardTable):
    global fetched_data
    query="select * from guard"
    mycursor.execute(query)
    fetched_data=mycursor.fetchall()
    guardTable.delete(*guardTable.get_children())

    for data in fetched_data:
        datalist=list(data)
        guardTable.insert("",END,values=datalist)

#la recherche dans labase de donne (id,gender,firstnamelasname,crime)
def search_guardian_data1(idRechercheEntry,guardTablex):
    query="select * from guard where id=%s"
    mycursor.execute(query,(idRechercheEntry))
    fetched_data=mycursor.fetchall()
    guardTablex.delete(*guardTablex.get_children())
    for data in fetched_data:
        guardTablex.insert("",END,values=data)

def search_guardian_data2(firstnameRechercheEntry,lastnameRechercheEntry,guardTablex):
    if firstnameRechercheEntry!="" and lastnameRechercheEntry=="":
        query="select * from guard where firstname=%s  "
        mycursor.execute(query,(firstnameRechercheEntry))
    elif firstnameRechercheEntry=="" and lastnameRechercheEntry!="":
        query="select * from guard where  lastname=%s"
        mycursor.execute(query,(lastnameRechercheEntry))
    else:
        query="select * from guard where firstname=%s and lastname=%s  "
        mycursor.execute(query,(firstnameRechercheEntry,lastnameRechercheEntry))
    fetched_data=mycursor.fetchall()
    guardTablex.delete(*guardTablex.get_children())
    for data in fetched_data:
        guardTablex.insert("",END,values=data)

def search_guardian_data3(genderRechercheEntry,guardTablex):
    query="select * from guard where gender=%s"
    mycursor.execute(query,(genderRechercheEntry))
    fetched_data=mycursor.fetchall()
    guardTablex.delete(*guardTablex.get_children())
    for data in fetched_data:
        guardTablex.insert("",END,values=data)

#la modefication des dtables de labase de donne 
def updateGuard(firstNameEntry,lastNameEntry,genderEntry,shiftstartingtimeEntry,shiftendEntry,imageUrl,id,screen,guardTable):
    query="update guard set firstname=%s,lastname=%s,gender=%s,shiftstarttime=%s ,shiftendtime=%s,image=%s where id=%s"
    mycursor.execute(query,(firstNameEntry,lastNameEntry,genderEntry,shiftstartingtimeEntry,shiftendEntry,imageUrl,id))
    con.commit()
    messagebox.showinfo("Success",f"Id {id} is modified successfully",parent=screen)
    screen.destroy()
    show_guardian_data(guardTable)

#la suprission dee guardian
def delete_guard(guardTable):
    if guardTable.focus()=="":
        messagebox.showerror("Error","select a guard")
    else:
        indexing=guardTable.focus()
        content=guardTable.item(indexing)
        content_id=content["values"][0]
        result=messagebox.askyesno("delete",f"are you sur that you want to delete Id {content_id} ?")
        if result:
            query="delete from guard where id=%s"
            mycursor.execute(query,content_id)
            con.commit()
            show_guardian_data(guardTable)
        else:
            pass



########################################################
#                  Visitor Database                    #
########################################################





#creation de la table visitor
def connectvisitor():
    try:
        query="""create table visitors( 
        id int primary key auto_increment,
        firstname varchar(30),
        lastname varchar(10),
        adress varchar(255),
        telephone varchar(30),
        prisonerid int,
        currentdate varchar(50),
        FOREIGN KEY (prisonerid) REFERENCES prisonnier(id)
        );
        """
        mycursor.execute(query)
        
    except:
        query="use PrisonManagmentSysteme"
        mycursor.execute(query)

#lajout des visitor a la base de donne
def addvisitordata(firstname,lastName,adress,tel,prisonnierid):
    global result_add_prisonner_id
    query="select id from prisonnier where id=%s"
    mycursor.execute(query,(prisonnierid))
    result=mycursor.fetchall()
    if result:
        query=" insert into visitors values(%s,%s,%s,%s,%s,%s,%s)"
        mycursor.execute(query,(None,firstname,lastName,adress,tel,prisonnierid,date))
        con.commit()

        result_add_prisonner_id=messagebox.askyesno("Confirm","Data addes successfully. Do you want to clean the form")
    else:
        messagebox.showerror("Error","prisonnier id dosn't exist")

#lafichage des donne de labase de donne 
def show_visitor_data(visitorsTable):
    global fetched_data
    query="""SELECT visitors.id,visitors.firstname,visitors.lastName,visitors.adress,(concat(visitors.telephone)),(concat(prisonnier.firstname," ",prisonnier.lastname) ),visitors.currentdate
    FROM prisonnier
    INNER JOIN visitors ON prisonnier.id = visitors.prisonerid;"""
    mycursor.execute(query)
    fetched_data=mycursor.fetchall()
    visitorsTable.delete(*visitorsTable.get_children())

    for data in fetched_data:
        visitorsTable.insert("",END,values=data)

#la recherche dans labase de donne (id,firstnamelasname,address)
def search_visitor_data1(idRechercheEntry,visitorsTablex):
    query="select id,firstname,lastname,adress,telephone,(concat(firstname,lastname)),currentdate from visitors where telephone=%s"
    mycursor.execute(query,(idRechercheEntry))
    fetched_data=mycursor.fetchall()
    visitorsTablex.delete(*visitorsTablex.get_children())
    for data in fetched_data:
        visitorsTablex.insert("",END,values=data)

def search_visitor_data2(firstnameRechercheEntry,lastnameRechercheEntry,visitorsTablex):
    if firstnameRechercheEntry!="" and lastnameRechercheEntry=="":
        query="select id,firstname,lastname,adress,telephone,(concat(firstname,lastname)),currentdate from visitors where firstname=%s  "
        mycursor.execute(query,(firstnameRechercheEntry))
    elif firstnameRechercheEntry=="" and lastnameRechercheEntry!="":
        query="select id,firstname,lastname,adress,telephone,(concat(firstname,lastname)),currentdate from visitors where  lastname=%s"
        mycursor.execute(query,(lastnameRechercheEntry))
    else:
        query="select id,firstname,lastname,adress,telephone,(concat(firstname,lastname)),currentdate from visitors where firstname=%s and lastname=%s  "
        mycursor.execute(query,(firstnameRechercheEntry,lastnameRechercheEntry))
    fetched_data=mycursor.fetchall()
    visitorsTablex.delete(*visitorsTablex.get_children())
    for data in fetched_data:
        visitorsTablex.insert("",END,values=data)

def search_visitor_data3(adressRechercheEntry,visitorsTablex):
    query="select id,firstname,lastname,adress,telephone,(concat(firstname,lastname)),currentdate from visitors where adress=%s"
    mycursor.execute(query,(adressRechercheEntry))
    fetched_data=mycursor.fetchall()
    visitorsTablex.delete(*visitorsTablex.get_children())
    for data in fetched_data:
        visitorsTablex.insert("",END,values=data)

#la modefication des dtables de labase de donne 
def updatevisitor(firstNameEntry,lastNameEntry,adressEntry,telEntry,prisoneridEntry,id,screen,visitorsTable):
    query="update visitors set firstname=%s,lastname=%s,adress=%s,telephone=%s ,prisonerid=%s where id=%s"
    mycursor.execute(query,(firstNameEntry,lastNameEntry,adressEntry,telEntry,prisoneridEntry,id))
    con.commit()
    messagebox.showinfo("Success",f"Id {id} is modified successfully",parent=screen)
    screen.destroy()
    show_visitor_data(visitorsTable)

#la suprission dee visitor
def delete_visitor(visitorTable):
    if visitorTable.focus()=="":
        messagebox.showerror("Error","select a visitor")
    else:
        indexing=visitorTable.focus()
        content=visitorTable.item(indexing)
        content_id=content["values"][0]
        result=messagebox.askyesno("delete",f"are you sur that you want to delete Id {content_id} ?")
        if result:
            query="delete from visitors where id=%s"
            mycursor.execute(query,content_id)
            con.commit()
            show_visitor_data(visitorTable)
        else:
            pass








#creation de la table utelisater
def connectuser():
    try:
        query="""create table user( 
        username varchar(30) primary key,
        firstname varchar(30),
        lastname varchar(10),
        gender varchar(20),
        Functionality varchar(90),
        Password varchar(30),
        image varchar(500))  
        """
        mycursor.execute(query)
        
    except:
        query="use PrisonManagmentSysteme"
        mycursor.execute(query)

#lajout des utelisater a la base de donne
def adduserdata(username,firstname,lastName,Gender,Functionality,password,image):
    query=" insert into user values(%s,%s,%s,%s,%s,%s,%s)"
    mycursor.execute(query,(username,firstname,lastName,Gender,Functionality,password,image))
    con.commit()

#lafichage des donne de labase de donne 
def show_user_data(userTable):
    global fetched_data
    query="select * from user"
    mycursor.execute(query)
    fetched_data=mycursor.fetchall()
    userTable.delete(*userTable.get_children())

    for data in fetched_data:
        datalist=list(data)
        userTable.insert("",END,values=datalist)

#la recherche dans labase de donne (id,gender,firstnamelasname,crime)
def search_user_data1(idRechercheEntry,userTablex):
    query="select * from user where username=%s"
    mycursor.execute(query,(idRechercheEntry))
    fetched_data=mycursor.fetchall()
    userTablex.delete(*userTablex.get_children())
    for data in fetched_data:
        userTablex.insert("",END,values=data)

def search_user_data2(firstnameRechercheEntry,lastnameRechercheEntry,userTablex):
    if firstnameRechercheEntry!="" and lastnameRechercheEntry=="":
        query="select * from user where firstname=%s  "
        mycursor.execute(query,(firstnameRechercheEntry))
    elif firstnameRechercheEntry=="" and lastnameRechercheEntry!="":
        query="select * from user where  lastname=%s"
        mycursor.execute(query,(lastnameRechercheEntry))
    else:
        query="select * from user where firstname=%s and lastname=%s  "
        mycursor.execute(query,(firstnameRechercheEntry,lastnameRechercheEntry))
    fetched_data=mycursor.fetchall()
    userTablex.delete(*userTablex.get_children())
    for data in fetched_data:
        userTablex.insert("",END,values=data)

def search_user_data3(genderRechercheEntry,userTablex):
    query="select * from user where gender=%s"
    mycursor.execute(query,(genderRechercheEntry))
    fetched_data=mycursor.fetchall()
    userTablex.delete(*userTablex.get_children())
    for data in fetched_data:
        userTablex.insert("",END,values=data)

#la suprission dee utelisater
def delete_user(userTablex):
    if userTablex.focus()=="":
        messagebox.showerror("Error","select user")
    else:
        indexing=userTablex.focus()
        content=userTablex.item(indexing)
        content_username=content["values"][0]
        result=messagebox.askyesno("delete",f"are you sur that you want to delete username: {content_username} ?")
        if result:
            query="delete from user where username=%s"
            mycursor.execute(query,content_username)
            con.commit()
            show_user_data(userTablex)
        else:
            pass

