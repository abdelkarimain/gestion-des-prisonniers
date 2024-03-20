from database import *


#####################################################################################
#                           la creation des classes                                 #
#####################################################################################


###################################################
#                 Class prisoner                  #
###################################################
class Prisoner:
    cpt=0
    def __init__(self,firstName,lastName,Gender,Crime,punishment,image):
        self.firstname=firstName
        self.lastName=lastName
        self.Gender=Gender
        self.Crime=Crime
        self.punishment=punishment
        self.image=image
    def addPrisonnier(self):
        addPrisonnierdata(self.firstname,self.lastName,self.Gender,self.Crime,self.punishment,self.image)

###################################################
#                 Class Guard                     #
###################################################
class guard:
    cpt=0
    def __init__(self,firstName,lastName,Gender,shiftstart,shiftend,image):
        self.firstname=firstName
        self.lastName=lastName
        self.Gender=Gender
        self.shiftstart=shiftstart
        self.shiftend=shiftend
        self.image=image
    def addguard(self):
        addgarddata(self.firstname,self.lastName,self.Gender,self.shiftstart,self.shiftend,self.image)



###################################################
#                Class Visitor                    #
###################################################
class visitor:
    cpt=0
    def __init__(self,firstName,lastName,adress,tel,prisonnierid):
        self.firstname=firstName
        self.lastName=lastName
        self.adress=adress
        self.tel=tel
        self.prisonnierid=prisonnierid
                
    def addvisitor(self):
        addvisitordata(self.firstname,self.lastName,self.adress,self.tel,self.prisonnierid)



###################################################
#                 Class User                     #
###################################################
class user:
    def __init__(self,username,firstName,lastName,Gender,Functionality,password,image):
        self.username=username
        self.firstname=firstName
        self.lastName=lastName
        self.Gender=Gender
        self.Functionality=Functionality
        self.password=password
        self.image=image
    def adduser(self):
        adduserdata(self.username,self.firstname,self.lastName,self.Gender,self.Functionality,self.password,self.image)