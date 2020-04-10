import os
import shutil
import tkinter as tk
from tkinter import PhotoImage
import os.path
import time
import sys
import win32api
import win32security
import datetime
import ctypes

def Original2k10():
    os.startfile(r"E:\Games\Playground\NBA 2K10\nba2k10.exe")
    sys.exit()

def Original2k11():
    os.startfile(r"E:\Games\Playground\NBA 2K11\nba2k11.exe")
    sys.exit()

def Original2k15():
    os.startfile(r"E:\Games\Playground\NBA 2K15\NBA2K15.lnk")
    sys.exit()

# def Original2k16():
#     os.startfile(r"E:\Games\Playground\NBA 2k16\NBA2K16.lnk")
#     sys.exit()

def Original2k17():
    os.startfile(r"E:\SteamLibrary\steamapps\common\NBA 2K17\NBA2K17.exe")
    sys.exit()

def Original2k18():
    os.startfile(r"E:\SteamLibrary\steamapps\common\NBA 2K18\NBA2K18.exe")
    sys.exit()


# def Original2k19():
#     os.startfile(r"E:\Games\Playground\NBA 2K19\nba2k19.exe")
#     sys.exit()

#!\\\\\\\\\\\\\\\\\\\\\ 
#!\\ - 2K12 Starts - \\
#!\\\\\\\\\\\\\\\\\\\\\

Folders2k11=["FIBA","Original"]
Founded=[]
Missing=[]
notFounded=[]
foundedSaves=[]
saves= os.listdir(r"C:\Users\The Mask Power\AppData\Roaming\2K Sports\NBA 2K12") 
modFolder = os.listdir(r"E:\Games\Playground\NBA 2K12\FIBA")#?Modificar a PC
originalFolder = os.listdir(r"E:\Games\Playground\NBA 2K12\Original")#?Modificar a PC
# os.chdir(r"E:\Games\Playground\NBA 2K12")#?Modificar a PC

#!Image
master=tk.Tk() 
master.title("NBA 2K Manager")

# photo1=PhotoImage(file=r"E:\Games\Playground\MODS Scripts\NBA 2K icons\nbacollection.gif") #This
photo2=PhotoImage(file=r"E:\Games\Playground\MODS Scripts\NBA 2K icons\2k10.png") #This
photo2k10=photo2.subsample(3, 3) 
photo3=PhotoImage(file=r"E:\Games\Playground\MODS Scripts\NBA 2K icons\2k11.png") #This
photo2k11=photo3.subsample(3, 3) 
photo4=PhotoImage(file=r"E:\Games\Playground\MODS Scripts\NBA 2K icons\2k12.png") #This
photo2k12=photo4.subsample(3, 3) 
photo5=PhotoImage(file=r"E:\Games\Playground\MODS Scripts\NBA 2K icons\2k13.png") #This
photo2k13=photo5.subsample(3, 3) 
photo6=PhotoImage(file=r"E:\Games\Playground\MODS Scripts\NBA 2K icons\2k14.png") #This
photo2k14=photo6.subsample(3, 3) 
photo7=PhotoImage(file=r"E:\Games\Playground\MODS Scripts\NBA 2K icons\2k15.png") #This
photo2k15=photo7.subsample(3, 3) 
photo8=PhotoImage(file=r"E:\Games\Playground\MODS Scripts\NBA 2K icons\2k16.png") #This
photo2k16=photo8.subsample(3, 3) 
photo9=PhotoImage(file=r"E:\Games\Playground\MODS Scripts\NBA 2K icons\2k17.png") #This
photo2k17=photo9.subsample(3, 3) 
photo10=PhotoImage(file=r"E:\Games\Playground\MODS Scripts\NBA 2K icons\2k18.png") #This
photo2k18=photo10.subsample(3, 3) 
photo11=PhotoImage(file=r"E:\Games\Playground\MODS Scripts\NBA 2K icons\2k19.png") #This
photo2k19=photo11.subsample(3, 3) 
photo12=PhotoImage(file=r"E:\Games\Playground\MODS Scripts\NBA 2K icons\2k20.png") #This
photo2k20=photo12.subsample(3, 3)
photo13=PhotoImage(file=r"E:\Games\Playground\MODS Scripts\NBA 2K icons\FIBA12.png") #This
photoFiba12=photo13.subsample(3, 3) 
photo14=PhotoImage(file=r"E:\Games\Playground\MODS Scripts\NBA 2K icons\Euroleague.png") #This
photoEuroleague=photo14.subsample(3, 3) 
photo15=PhotoImage(file=r"E:\Games\Playground\MODS Scripts\NBA 2K icons\March Madness.png") #This
photoCollege=photo15.subsample(3, 3)
photo16=PhotoImage(file=r"E:\Games\Playground\MODS Scripts\NBA 2K icons\2k20Retro.png") #This
photo2k20Retro=photo16.subsample(3, 3)
photo17=PhotoImage(file=r"E:\Games\Playground\MODS Scripts\NBA 2K icons\NBA Pro.png") #This
photo2k20Pro=photo17.subsample(3, 3)
photo18=PhotoImage(file=r"E:\Games\Playground\MODS Scripts\NBA 2K icons\fiba13.png") #This
photo2k13FIBA=photo18.subsample(3, 3)
photo19=PhotoImage(file=r"E:\Games\Playground\MODS Scripts\NBA 2K icons\ncaa13.png") #This
photo2k13College=photo19.subsample(3, 3)

photo20=PhotoImage(file=r"E:\Games\Playground\MODS Scripts\NBA 2K icons\FIBA14.png") #This
photo2k14FIBA=photo20.subsample(3, 3)
photo21=PhotoImage(file=r"E:\Games\Playground\MODS Scripts\NBA 2K icons\March-Madness-Odds.png") #This
photo2k20mm=photo21.subsample(3, 3)
photo22=PhotoImage(file=r"E:\Games\Playground\MODS Scripts\NBA 2K icons\ncaa14.png") #This
photo2k14College=photo22.subsample(3, 3)
photo23=PhotoImage(file=r"E:\Games\Playground\MODS Scripts\NBA 2K icons\ncaalogo.png") #This
photo2k1420=photo23.subsample(3, 3)
photo24=PhotoImage(file=r"E:\Games\Playground\MODS Scripts\NBA 2K icons\ncaa14.png") #This
photo2k14College=photo24.subsample(3, 3)
photo23=PhotoImage(file=r"E:\Games\Playground\MODS Scripts\NBA 2K icons\mbb.png") #This
photo2k14mbb=photo23.subsample(3, 3)
photo24=PhotoImage(file=r"E:\Games\Playground\MODS Scripts\NBA 2K icons\UltimateBase.png") #This
photo2k14CUBR=photo24.subsample(3, 3)

photo25=PhotoImage(file=r"E:\Games\Playground\MODS Scripts\NBA 2K icons\rio.png") #This
photo2k16Rio=photo25.subsample(3, 3)

photo26=PhotoImage(file=r"E:\Games\Playground\MODS Scripts\NBA 2K icons\FIBA2K19.png") #This
photo2k19FIBA=photo26.subsample(3, 3)
photo27=PhotoImage(file=r"E:\Games\Playground\MODS Scripts\NBA 2K icons\ncaa2k19.png") #This
photo2k19College=photo27.subsample(3, 3)


# tk.Label(master,image=photo1, bg="black").grid(row="0",column="0")
master.configure(bg="black")

def verify():

    for filename in os.listdir(r"C:\Users\The Mask Power\AppData\Roaming\2K Sports\NBA 2K12"): #This
        
        if(filename.startswith("Original")):
            Founded.append(filename)
                

        elif(filename.startswith("FIBA")):
            
            Founded.append(filename)

        elif(filename.startswith("NCAA")):

            Founded.append(filename)
                
verify()
# print("Founded",Founded)
def Missed(Founded, Folders2k11):
    return (list(set(Folders2k11) - set(Founded)))

Missing.append(Missed(Founded, Folders2k11)) 
# print("Activated save 2k12 1 -", Missing)
# print("Activated save 2k12 2-", Missing[0][0])


   #!\\-Lee la lista del mod-//
modText = open(r"E:\Games\Playground\NBA 2K12\FIBA\outputMod.txt", "r+") #?Modificar a PC
my_mod_data = modText.read().split()
modText.close()
my_mod_data.remove("outputMod.txt")
# print(my_mod_data, "Mod Data")

#!\\-Lee el Folder Del Juego-//
folderJuego = os.listdir(r"E:\Games\Playground\NBA 2K12")#?Modificar a PC
#! print(folderJuego,"folderJuego")
# print(len(modFolder),"modFolder")




def FIBA():

    #!\\-Check if folder is empty for active-\\
    if(len(modFolder) <=1):
        # print(modFolder,"=1 Already Done")
        os.startfile(r"E:\Games\Playground\NBA 2K12\nba2k12.exe")
        sys.exit()

    else:
    #!\\-Compara las listas-//
        exist = set(my_mod_data).intersection(folderJuego)
        # print(exist,"duplicatedFiles")

    #!\\-Guarda archivos originales-//
        for filename in exist:
            # print(filename,"exist")
            shutil.move(r"E:\Games\Playground\NBA 2K12" + "\\"+ str(filename),r"E:\Games\Playground\NBA 2K12" + "\\"+"Original" + "\\" + str(filename))#?Modificar a PC

    #!\\-Mueve archivos del folder Mod al juego-//
        modFolder.remove("outputMod.txt")
        for filename in modFolder:
            shutil.move(r"E:\Games\Playground\NBA 2K12" + "\\"+ "FIBA" + "\\" + str(filename),r"E:\Games\Playground\NBA 2K12" + "\\" + str(filename))#?Modificar a PC
            # print(filename)

    os.chdir(r"C:\Users\The Mask Power\AppData\Roaming\2K Sports\NBA 2K12")
    for filename in saves:

        if(Missing[0][0] != "FIBA"):

            try:
                os.rename("Saves",Missing[0][0])
                time.sleep(0.1)
                os.rename("FIBA","Saves")       
                # print(Missing[0][0],"FIBA")     
                

            except:
                # print(filename,"Already Done")
                os.startfile(r"E:\Games\Playground\NBA 2K12\nba2k12.exe")
                
    os.startfile(r"E:\Games\Playground\NBA 2K12\nba2k12.exe")
    sys.exit()



def Original():

    #!\\-Check if folder is empty for active-\\
    if(len(originalFolder) <=1):
        # print(originalFolder,"Already Done")
        os.startfile(r"E:\Games\Playground\NBA 2K12\nba2k12.exe")
        sys.exit()
    else:    
        #!\\-Lee la Lista original-//
        modText2 = open(r"E:\Games\Playground\NBA 2K12\Original\outputMod.txt", "r+")#?Modificar a PC
        my_mod_data2 = modText2.read().split()
        modText2.close()
        my_mod_data2.remove("outputMod.txt")
        # print(my_mod_data2, "Mod Data2")

        #!\\-Compara las listas-//
        # exist2= set(my_mod_data2).intersection(folderJuego)
        # print(exist2,"duplicates files 2")

        #!\\-Guarda archivos Mod-//  ###################### lee lista
        for filename in my_mod_data:
            # print(filename,"exist")
            shutil.move(r"E:\Games\Playground\NBA 2K12" + "\\"+ str(filename),r"E:\Games\Playground\NBA 2K12" + "\\"+"FIBA" + "\\" + str(filename))#?Modificar a PC
        
        #!\\-Mueve archivos del folder Original al juego-//
        originalFolder.remove("outputMod.txt")
        
        for filename in originalFolder:
            shutil.move(r"E:\Games\Playground\NBA 2K12" + "\\"+ "Original" + "\\" + str(filename),r"E:\Games\Playground\NBA 2K12" + "\\" + str(filename))#?Modificar a PC
            # print(filename)
        
        os.chdir(r"C:\Users\The Mask Power\AppData\Roaming\2K Sports\NBA 2K12")
        for filename in saves:
            if(Missing[0][0] != "Original"):

                try:
                   os.rename("Saves",Missing[0][0])
                   time.sleep(0.1)
                   os.rename("Original","Saves")       
                #    print(Missing[0][0],"Original")     
                   

                except:
                    print(filename,"Already Done")
                    
                    

    os.startfile(r"E:\Games\Playground\NBA 2K12\nba2k12.exe")
    sys.exit()

#!\\\\\\\\\\\\\\\\\\\\\ 
#!\\ - 2K12 Ends - \\
#!\\\\\\\\\\\\\\\\\\\\\




#!\\\\\\\\\\\\\\\\\\\\\ 
#!\\ - 2K13 Starts - \\
#!\\\\\\\\\\\\\\\\\\\\\
Folders2k13=["FIBA","Original","College"]
Founded2k13=[]
Missing2k13=[]
Folders2k13Saves=["FIBA","Original","College"]
Founded2k13Save=[]
Missing2k13Save=[]
notFounded2k13=[]
foundedSaves2k13=[]
saves2k13= os.listdir(r"C:\Users\The Mask Power\AppData\Roaming\2K Sports\NBA 2K13")
modFolder2k13 = os.listdir(r"E:\Games\Playground\NBA 2K13\FIBA")#?Modificar a PC
College2k13 = os.listdir(r"E:\Games\Playground\NBA 2K13\College")#?Modificar a PC
originalFolder2k13 = os.listdir(r"E:\Games\Playground\NBA 2K13\Original")#?Modificar a PC





def verify2k13():
    os.chdir(r"E:\Games\Playground\NBA 2K13")#?Modificar a PC
    for filename in os.listdir(r"E:\Games\Playground\NBA 2K13"): #This
        
        if(filename.startswith("Original") and len(originalFolder2k13) == 1):
            # print("originalFolder2k13",originalFolder2k13,len(originalFolder2k13))
            Founded2k13.append(filename)
                

        if(filename.startswith("FIBA") and len(modFolder2k13) == 1):
            # print(filename,len(filename))
            Founded2k13.append(filename)

        if(filename.startswith("College") and len(College2k13) == 1):
            # print(filename,len(filename))
            Founded2k13.append(filename)
                
verify2k13()
Missing2k13=Founded2k13
# print("Founded",Founded2k13)

# def Missed2k13(Founded2k13, Folders2k13):
#     return (list(set(Folders2k13) - set(Founded2k13)))

# Missing2k13.append(Missed2k13(Founded2k13, Folders2k13)) 
# print("Activated save 2k12 1 -", Missing)
print("Activated 2k13", Missing2k13[0])



os.chdir(r"C:\Users\The Mask Power\AppData\Roaming\2K Sports\NBA 2K13")





def verify2k13Save():
    for filename in os.listdir(r"C:\Users\The Mask Power\AppData\Roaming\2K Sports\NBA 2K13"): #This
        
        if(filename.startswith("Original")):
           Founded2k13Save.append(filename)
                
        elif(filename.startswith("FIBA")):
           Founded2k13Save.append(filename)

        elif(filename.startswith("College")):
           Founded2k13Save.append(filename)
                
verify2k13Save()

def MissedSave(Founded2k13Save, Folders2k13):

    return (list(set(Folders2k13) - set(Founded2k13Save)))

Missing2k13Save.append(MissedSave(Founded2k13Save, Folders2k13)) 
print("2k13 save2",Missing2k13Save[0][0])
# print("Activated save 2k13 -", Missing2k13Save[0][0])




#!\\-Lee la lista del FIBA-//
modText2k13 = open(r"E:\Games\Playground\NBA 2K13\FIBA\outputMod.txt", "r+") #?Modificar a PC
my_mod_data2k13 = modText2k13.read().split()
modText2k13.close()
my_mod_data2k13.remove("outputMod.txt")
# print(my_mod_data2k13, "Mod Data")
activePath = open(r"E:\Games\Playground\NBA 2K13" + "\\"+ Missing2k13[0] + "\\" + "outputMod.txt")
active_folder2k13 = activePath.read().split()
active_folder2k13.remove("outputMod.txt")
activePath.close
# print(active_folder2k13, "Mod Data",my_mod_data2k13)


#!\\-Lee la Lista College-//
modText2k13c = open(r"E:\Games\Playground\NBA 2K13\College\outputMod.txt", "r+")#?Modificar a PC
my_mod_data2k13c = modText2k13c.read().split()
modText2k13c.close()
my_mod_data2k13c.remove("outputMod.txt")
# print(my_mod_data2k13c, "Mod Data")



 #!\\-Lee la Lista Original-//
modText2k13o = open(r"E:\Games\Playground\NBA 2K13\Original\outputMod.txt", "r+")#?Modificar a PC
my_mod_data2k13o = modText2k13o.read().split()
modText2k13o.close()
my_mod_data2k13o.remove("outputMod.txt")
# print(my_mod_data2k13, "Mod Data")



#!\\-Lee el Folder Del Juego-//
folderJuego2k13 = os.listdir(r"E:\Games\Playground\NBA 2K13")#?Modificar a PC
#! print(folderJuego2k13,"folderJuego2k13")
# print(len(modFolder2k13),"modFolder2k13")




def FIBA2k13():

    #!\\-Check if folder is empty for active-\\
    if(len(modFolder2k13) ==1):
        print(modFolder2k13,"=1 Already Done")
        # os.startfile(r"E:\Games\Playground\NBA 2K13\nba2k13.exe")
        sys.exit()

    else:
    #!\\-Compara las listas-//

        exist2k13o = set(active_folder2k13).intersection(folderJuego2k13)
        # print(exist2k13o,"duplicatedFiles")

    #!\\-Guarda archivos originales-//
        for filename in exist2k13o:
            # print(filename,"exist2k13o")
            shutil.move(r"E:\Games\Playground\NBA 2K13" + "\\"+ str(filename),r"E:\Games\Playground\NBA 2K13" + "\\"+ Missing2k13[0] + "\\" + str(filename))#?Modificar a PC

    #!\\-Mueve archivos del folder Mod al juego-//
        modFolder2k13.remove("outputMod.txt")
        for filename in modFolder2k13:
            shutil.move(r"E:\Games\Playground\NBA 2K13" + "\\"+ "FIBA" + "\\" + str(filename),r"E:\Games\Playground\NBA 2K13" + "\\" + str(filename))#?Modificar a PC
            # print(filename)

    os.chdir(r"C:\Users\The Mask Power\AppData\Roaming\2K Sports\NBA 2K13")
    for filename in saves2k13:
        
        if(Missing2k13Save[0][0] != "FIBA"):
            print(Missing2k13Save[0][0])
            
            try:
                os.rename("Saves",Missing2k13Save[0][0])
                time.sleep(0.1)
                os.rename("FIBA","Saves")       
            #    print(Missing[0][0],"Original")     
                   

            except:
                print(filename,"Already Done")
                # os.startfile(r"E:\Games\Playground\NBA 2K13\nba2k13.exe")
                
    # os.startfile(r"E:\Games\Playground\NBA 2K13\nba2k13.exe")
    sys.exit()



def Original2k13():

    #!\\-Check if folder is empty for active-\\
    if(len(originalFolder2k13) <=1):
        print(originalFolder2k13,"Already Done")
        # os.startfile(r"E:\Games\Playground\NBA 2K13\nba2k13.exe")
        sys.exit()
    else:    
       

        #!\\-Compara las listas-//
        exist2k13o= set(active_folder2k13).intersection(folderJuego2k13)
        print(exist2k13o,"duplicates files 2")

        #!\\-Guarda archivos Mod-//  ###################### lee lista
        for filename in exist2k13o:
            # print(filename,"exist")
            shutil.move(r"E:\Games\Playground\NBA 2K13" + "\\"+ str(filename),r"E:\Games\Playground\NBA 2K13" + "\\"+ Missing2k13[0] + "\\" + str(filename))#?Modificar a PC
        
        #!\\-Mueve archivos del folder Original al juego-//
        originalFolder2k13.remove("outputMod.txt")
        
        for filename in originalFolder2k13:
            shutil.move(r"E:\Games\Playground\NBA 2K13" + "\\"+ "Original" + "\\" + str(filename),r"E:\Games\Playground\NBA 2K13" + "\\" + str(filename))#?Modificar a PC
            print(filename)
        
        os.chdir(r"C:\Users\The Mask Power\AppData\Roaming\2K Sports\NBA 2K13")
        for filename in saves2k13:
            if(Missing2k13Save[0][0] != "Original"):

                try:
                   os.rename("Saves",Missing2k13Save[0][0])
                   time.sleep(0.1)
                   os.rename("Original","Saves")       
                #    print(Missing2k13Save[0][0],"Original")
                   break     
                   

                except:
                    print(filename,"Already Done")
                    break
                    

    # os.startfile(r"E:\Games\Playground\NBA 2K13\nba2k13.exe")
    sys.exit()

def NCAA2k13():
    #!\\-Check if folder is empty for active-\\
    if(len(College2k13) <=1):
        print(College2k13,"Already Done")
        # os.startfile(r"E:\Games\Playground\NBA 2K13\nba2k13.exe")
        sys.exit()
    else:    
       

        #!\\-Compara las listas-//
        exist2k13c= set(active_folder2k13).intersection(folderJuego2k13)
        # print(exist2k13c,"duplicates files 2")

        #!\\-Guarda archivos Mod-//  ###################### lee lista
        for filename in exist2k13c:
            # print(filename,"exist")
            shutil.move(r"E:\Games\Playground\NBA 2K13" + "\\"+ str(filename),r"E:\Games\Playground\NBA 2K13" + "\\"+ Missing2k13[0] + "\\" + str(filename))#?Modificar a PC
        
        #!\\-Mueve archivos del folder College al juego-//
        College2k13.remove("outputMod.txt")
        
        for filename in College2k13:
            shutil.move(r"E:\Games\Playground\NBA 2K13" + "\\"+ "College" + "\\" + str(filename),r"E:\Games\Playground\NBA 2K13" + "\\" + str(filename))#?Modificar a PC
            print(filename)
        
        os.chdir(r"C:\Users\The Mask Power\AppData\Roaming\2K Sports\NBA 2K13")
        for filename in saves2k13:
            if(Missing2k13Save[0][0] != "College"):
                     
                try:
                    os.rename("Saves",Missing2k13Save[0][0])
                    time.sleep(0.1)
                    os.rename("College","Saves")       
                #    print(Missing[0][0],"Original")     
                    

                except:
                    print(filename,"Already Done")
                    # os.startfile(r"E:\Games\Playground\NBA 2K13\nba2k13.exe")
                
    # os.startfile(r"E:\Games\Playground\NBA 2K13\nba2k13.exe")
    sys.exit()
                            
#!\\\\\\\\\\\\\\\\\\\\\ 
#!\\ - 2K13 Ends -   \\
#!\\\\\\\\\\\\\\\\\\\\\





#!\\\\\\\\\\\\\\\\\\\\\ 
#!\\ - 2K14 Starts - \\
#!\\\\\\\\\\\\\\\\\\\\\
Folders2k14=["FIBA","MarchMadness 15","College 2k20","Original","NCAA 14","NCAA MBB 17-18","Ultimate Base Roster 14"]
Founded2k14=[]
Missing2k14=[]
Folders2k14Saves=["FIBA","MarchMadness 15","College 2k20","Original","NCAA 14","NCAA MBB 17-18","Ultimate Base Roster 14"]
Founded2k14Save=[]
Missing2k14Save=[]
notFounded2k14=[]
foundedSaves2k14=[]
saves2k14= os.listdir(r"C:\Users\The Mask Power\AppData\Roaming\2K Sports\NBA 2K14")
modFolder2k14 = os.listdir(r"E:\Games\Playground\NBA 2K14\FIBA")#?Modificar a PC
College2k14_20 = os.listdir(r"E:\Games\Playground\NBA 2K14\College 2k20")#?Modificar a PC
MarchMadness15 = os.listdir(r"E:\Games\Playground\NBA 2K14\MarchMadness 15")#?Modificar a PC
NCAA14 = os.listdir(r"E:\Games\Playground\NBA 2K14\NCAA 14")#?Modificar a PC
NCAAMBB = os.listdir(r"E:\Games\Playground\NBA 2K14\NCAA MBB 17-18")#?Modificar a PC
ultimateBase = os.listdir(r"E:\Games\Playground\NBA 2K14\Ultimate Base Roster 14")#?Modificar a PC
originalFolder2k14 = os.listdir(r"E:\Games\Playground\NBA 2K14\Original")#?Modificar a PC





def verify2k14():
    os.chdir(r"E:\Games\Playground\NBA 2K14")#?Modificar a PC
    for filename in os.listdir(r"E:\Games\Playground\NBA 2K14"): #This
        
        if(filename.startswith("Original") and len(originalFolder2k14) == 1):
            # print("originalFolder2k13",originalFolder2k13,len(originalFolder2k13))
            Founded2k14.append(filename)
                
        if(filename.startswith("FIBA") and len(modFolder2k14) == 1):
            # print(filename,len(filename))
            Founded2k14.append(filename)

        if(filename.startswith("College 2k20") and len(College2k14_20) == 1):
            # print(filename,len(filename))
            Founded2k14.append(filename)

        if(filename.startswith("MarchMadness 15") and len(MarchMadness15) == 1):
            # print(filename,len(filename))
            Founded2k14.append(filename)
        
        if(filename.startswith("NCAA 14") and len(NCAA14) == 1):
            # print(filename,len(filename))
            Founded2k14.append(filename)

        if(filename.startswith("NCAA MBB 17-18") and len(NCAAMBB) == 1):
            # print(filename,len(filename))
            Founded2k14.append(filename)

        if(filename.startswith("Ultimate Base Roster 14") and len(ultimateBase) == 1):
            # print(filename,len(filename))
            Founded2k14.append(filename)
                
verify2k14()
Missing2k14=Founded2k14
# print("Founded",Founded2k14)

# def Missed2k13(Founded2k14, Folders2k13):
#     return (list(set(Folders2k13) - set(Founded2k14)))

# Missing2k14.append(Missed2k13(Founded2k14, Folders2k13)) 
# print("Activated save 2k12 1 -", Missing)
print("Activated 2k14", Missing2k14[0])



os.chdir(r"C:\Users\The Mask Power\AppData\Roaming\2K Sports\NBA 2K14")





def verify2k14Save():
    for filename in os.listdir(r"C:\Users\The Mask Power\AppData\Roaming\2K Sports\NBA 2K14"): #This
        
        if(filename.startswith("Original")):
           Founded2k14Save.append(filename)
                
        if(filename.startswith("FIBA")):
            # print(filename,len(filename))
            Founded2k14Save.append(filename)

        if(filename.startswith("College 2k20")):
            # print(filename,len(filename))
            Founded2k14Save.append(filename)

        if(filename.startswith("MarchMadness 15")):
            # print(filename,len(filename))
            Founded2k14Save.append(filename)
        
        if(filename.startswith("NCAA 14")):
            # print(filename,len(filename))
            Founded2k14Save.append(filename)

        if(filename.startswith("NCAA MBB 17-18")):
            # print(filename,len(filename))
            Founded2k14Save.append(filename)

        if(filename.startswith("Ultimate Base Roster 14")):
            # print(filename,len(filename))
            Founded2k14Save.append(filename)
                
verify2k14Save()

def MissedSave2k14(Founded2k14Save, Folders2k14):
    return (list(set(Folders2k14) - set(Founded2k14Save)))

Missing2k14Save.append(MissedSave2k14(Founded2k14Save, Folders2k14)) 
print("2k14 save2",Missing2k14Save[0][0])
# print("Activated save 2k13 -", Missing2k14Save[0][0])




#!\\-Lee la lista del FIBA-//
modText2k14 = open(r"E:\Games\Playground\NBA 2K14\FIBA\outputMod.txt", "r+") #?Modificar a PC
my_mod_data2k14 = modText2k14.read().split()
modText2k14.close()
my_mod_data2k14.remove("outputMod.txt")
# print(my_mod_data2k14, "Mod Data")
activePath2k14 = open(r"E:\Games\Playground\NBA 2K14" + "\\"+ Missing2k14[0] + "\\" + "outputMod.txt")
active_folder2k14 = activePath2k14.read().split()
active_folder2k14.remove("outputMod.txt")
activePath2k14.close
# print(active_folder2k14, "Mod Data",my_mod_data2k14)


#!\\-Lee la Lista College2k20-//
modText2k14c = open(r"E:\Games\Playground\NBA 2K14\College 2k20\outputMod.txt", "r+")#?Modificar a PC
my_mod_data2k14c = modText2k14c.read().split()
modText2k14c.close()
my_mod_data2k14c.remove("outputMod.txt")
# print(my_mod_data2k13c, "Mod Data")



#!\\-Lee la Lista Original-//
modText2k14o = open(r"E:\Games\Playground\NBA 2K14\Original\outputMod.txt", "r+")#?Modificar a PC
my_mod_data2k14o = modText2k14o.read().split()
modText2k14o.close()
my_mod_data2k14o.remove("outputMod.txt")
# print(my_mod_data2k14o, "Mod Data")

#!\\-Lee la Lista MarchMadness 15-//
modText2k14mm = open(r"E:\Games\Playground\NBA 2K14\MarchMadness 15\outputMod.txt", "r+")#?Modificar a PC
my_mod_data2k14mm = modText2k14mm.read().split()
modText2k14mm.close()
my_mod_data2k14mm.remove("outputMod.txt")
# print(my_mod_data2k13mm, "Mod Data")

#!\\-Lee la Lista NCAA 14-//
modText2k14n = open(r"E:\Games\Playground\NBA 2K14\NCAA 14\outputMod.txt", "r+")#?Modificar a PC
my_mod_data2k14n = modText2k14n.read().split()
modText2k14n.close()
my_mod_data2k14n.remove("outputMod.txt")
# print(my_mod_data2k13n, "Mod Data")

#!\\-Lee la Lista NCAA MBB 17-18-//
modText2k14mbb = open(r"E:\Games\Playground\NBA 2K14\NCAA MBB 17-18\outputMod.txt", "r+")#?Modificar a PC
my_mod_data2k14mbb = modText2k14mbb.read().split()
modText2k14mbb.close()
my_mod_data2k14mbb.remove("outputMod.txt")
# print(my_mod_data2k13mbb, "Mod Data")

#!\\-Lee la Lista Ultimate Base Roster 14-//
modText2k14ub = open(r"E:\Games\Playground\NBA 2K14\Ultimate Base Roster 14\outputMod.txt", "r+")#?Modificar a PC
my_mod_data2k14ub = modText2k14ub.read().split()
modText2k14ub.close()
my_mod_data2k14ub.remove("outputMod.txt")
# print(my_mod_data2k13ub, "Mod Data")

#!\\-Lee el Folder Del Juego-//
folderJuego2k14 = os.listdir(r"E:\Games\Playground\NBA 2K14")#?Modificar a PC
#! print(folderJuego2k13,"folderJuego2k13")
# print(len(modFolder2k13),"modFolder2k13")




def FIBA2k14():

    #!\\-Check if folder is empty for active-\\
    if(len(modFolder2k14) ==1):
        print(modFolder2k14,"=1 Already Done")
        # os.startfile(r"E:\Games\Playground\NBA 2K14\nba2k13.exe")
        sys.exit()

    else:
    #!\\-Compara las listas-//

        exist2k14o = set(active_folder2k14).intersection(folderJuego2k14)
        # print(exist2k13o,"duplicatedFiles")

    #!\\-Guarda archivos originales-//
        for filename in exist2k14o:
            # print(filename,"exist2k13o")
            shutil.move(r"E:\Games\Playground\NBA 2K14" + "\\"+ str(filename),r"E:\Games\Playground\NBA 2K14" + "\\"+ Missing2k14[0] + "\\" + str(filename))#?Modificar a PC

    #!\\-Mueve archivos del folder Mod al juego-//
        modFolder2k14.remove("outputMod.txt")
        for filename in modFolder2k14:
            shutil.move(r"E:\Games\Playground\NBA 2K14" + "\\"+ "FIBA" + "\\" + str(filename),r"E:\Games\Playground\NBA 2K14" + "\\" + str(filename))#?Modificar a PC
            # print(filename)

    os.chdir(r"C:\Users\The Mask Power\AppData\Roaming\2K Sports\NBA 2K14")
    for filename in saves2k14:
        
        if(Missing2k14Save[0][0] != "FIBA"):
            print(Missing2k14Save[0][0])
            
            try:
                os.rename("Saves",Missing2k14Save[0][0])
                time.sleep(0.1)
                os.rename("FIBA","Saves")       
            #    print(Missing[0][0],"Original")     
                   

            except:
                print(filename,"Already Done")
                # os.startfile(r"E:\Games\Playground\NBA 2K14\nba2k13.exe")
                
    # os.startfile(r"E:\Games\Playground\NBA 2K14\nba2k13.exe")
    sys.exit()



def Original2k14():

    #!\\-Check if folder is empty for active-\\
    if(len(originalFolder2k14) <=1):
        print(originalFolder2k14,"Already Done")
        # os.startfile(r"E:\Games\Playground\NBA 2K14\nba2k14.exe")
        sys.exit()
    else:    
       

        #!\\-Compara las listas-//
        exist2k14o= set(active_folder2k14).intersection(folderJuego2k14)
        print(exist2k14o,"duplicates files 2")

        #!\\-Guarda archivos Mod-//  ###################### lee lista
        for filename in exist2k14o:
            # print(filename,"exist")
            shutil.move(r"E:\Games\Playground\NBA 2K14" + "\\"+ str(filename),r"E:\Games\Playground\NBA 2K14" + "\\"+ Missing2k14[0] + "\\" + str(filename))#?Modificar a PC
        
        #!\\-Mueve archivos del folder Original al juego-//
        originalFolder2k14.remove("outputMod.txt")
        
        for filename in originalFolder2k14:
            shutil.move(r"E:\Games\Playground\NBA 2K14" + "\\"+ "Original" + "\\" + str(filename),r"E:\Games\Playground\NBA 2K14" + "\\" + str(filename))#?Modificar a PC
            print(filename)
        
        os.chdir(r"C:\Users\The Mask Power\AppData\Roaming\2K Sports\NBA 2K14")
        for filename in saves2k14:
            if(Missing2k14Save[0][0] != "Original"):

                try:
                   os.rename("Saves",Missing2k14Save[0][0])
                   time.sleep(0.1)
                   os.rename("Original","Saves")       
                #    print(Missing2k14Save[0][0],"Original")
                   break     
                   

                except:
                    print(filename,"Already Done")
                    break
                    

    # os.startfile(r"E:\Games\Playground\NBA 2K14\nba2k13.exe")
    sys.exit()

def MM15():
    #!\\-Check if folder is empty for active-\\
    if(len(MarchMadness15) <=1):
        print(MarchMadness15,"Already Done")
        # os.startfile(r"E:\Games\Playground\NBA 2K14\nba2k14.exe")
        sys.exit()
    else:    
       

        #!\\-Compara las listas-//
        exist2k14c= set(active_folder2k14).intersection(folderJuego2k14)
        # print(exist2k14c,"duplicates files 2")

        #!\\-Guarda archivos Mod-//  ###################### lee lista
        for filename in exist2k14c:
            # print(filename,"exist")
            shutil.move(r"E:\Games\Playground\NBA 2K14" + "\\"+ str(filename),r"E:\Games\Playground\NBA 2K14" + "\\"+ Missing2k14[0] + "\\" + str(filename))#?Modificar a PC
        
        #!\\-Mueve archivos del folder MarchMadness15 al juego-//
        MarchMadness15.remove("outputMod.txt")
        
        for filename in MarchMadness15:
            shutil.move(r"E:\Games\Playground\NBA 2K14" + "\\"+ "MarchMadness 15" + "\\" + str(filename),r"E:\Games\Playground\NBA 2K14" + "\\" + str(filename))#?Modificar a PC
            print(filename)
        
        os.chdir(r"C:\Users\The Mask Power\AppData\Roaming\2K Sports\NBA 2K14")
        for filename in saves2k14:
            if(Missing2k14Save[0][0] != "MarchMadness 15"):
                     
                try:
                    os.rename("Saves",Missing2k14Save[0][0])
                    time.sleep(0.1)
                    os.rename("MarchMadness 15","Saves")       
                #    print(Missing[0][0],"Original")     
                    

                except:
                    print(filename,"Already Done")
                    # os.startfile(r"E:\Games\Playground\NBA 2K14\nba2k13.exe")
                
    # os.startfile(r"E:\Games\Playground\NBA 2K14\nba2k13.exe")
    sys.exit()


def College2k1420():

    #!\\-Check if folder is empty for active-\\
    if(len(College2k14_20) ==1):
        print(College2k14_20,"=1 Already Done")
        # os.startfile(r"E:\Games\Playground\NBA 2K14\nba2k13.exe")
        sys.exit()

    else:
    #!\\-Compara las listas-//

        exist2k14o = set(active_folder2k14).intersection(folderJuego2k14)
        # print(exist2k13o,"duplicatedFiles")

    #!\\-Guarda archivos originales-//
        for filename in exist2k14o:
            # print(filename,"exist2k13o")
            shutil.move(r"E:\Games\Playground\NBA 2K14" + "\\"+ str(filename),r"E:\Games\Playground\NBA 2K14" + "\\"+ Missing2k14[0] + "\\" + str(filename))#?Modificar a PC

    #!\\-Mueve archivos del folder Mod al juego-//
        College2k14_20.remove("outputMod.txt")
        for filename in College2k14_20:
            shutil.move(r"E:\Games\Playground\NBA 2K14" + "\\"+ "College 2k20" + "\\" + str(filename),r"E:\Games\Playground\NBA 2K14" + "\\" + str(filename))#?Modificar a PC
            # print(filename)

    os.chdir(r"C:\Users\The Mask Power\AppData\Roaming\2K Sports\NBA 2K14")
    for filename in saves2k14:
        
        if(Missing2k14Save[0][0] != "College 2k20"):
            print(Missing2k14Save[0][0])
            
            try:
                os.rename("Saves",Missing2k14Save[0][0])
                time.sleep(0.1)
                os.rename("College 2k20","Saves")       
            #    print(Missing[0][0],"Original")     
                   

            except:
                print(filename,"Already Done")
                # os.startfile(r"E:\Games\Playground\NBA 2K14\nba2k13.exe")
                
    # os.startfile(r"E:\Games\Playground\NBA 2K14\nba2k13.exe")
    sys.exit()



def NCAA2k14():

    #!\\-Check if folder is empty for active-\\
    if(len(NCAA14) <=1):
        print(NCAA14,"Already Done")
        # os.startfile(r"E:\Games\Playground\NBA 2K14\nba2k14.exe")
        sys.exit()
    else:    
       

        #!\\-Compara las listas-//
        exist2k14o= set(active_folder2k14).intersection(folderJuego2k14)
        print(exist2k14o,"duplicates files 2")

        #!\\-Guarda archivos Mod-//  ###################### lee lista
        for filename in exist2k14o:
            # print(filename,"exist")
            shutil.move(r"E:\Games\Playground\NBA 2K14" + "\\"+ str(filename),r"E:\Games\Playground\NBA 2K14" + "\\"+ Missing2k14[0] + "\\" + str(filename))#?Modificar a PC
        
        #!\\-Mueve archivos del folder Original al juego-//
        NCAA14.remove("outputMod.txt")
        
        for filename in NCAA14:
            shutil.move(r"E:\Games\Playground\NBA 2K14" + "\\"+ "NCAA 14" + "\\" + str(filename),r"E:\Games\Playground\NBA 2K14" + "\\" + str(filename))#?Modificar a PC
            print(filename)
        
        os.chdir(r"C:\Users\The Mask Power\AppData\Roaming\2K Sports\NBA 2K14")
        for filename in saves2k14:
            if(Missing2k14Save[0][0] != "Original"):

                try:
                   os.rename("Saves",Missing2k14Save[0][0])
                   time.sleep(0.1)
                   os.rename("NCAA 14","Saves")       
                #    print(Missing2k14Save[0][0],"Original")
                   break     
                   

                except:
                    print(filename,"Already Done")
                    break
                    

    # os.startfile(r"E:\Games\Playground\NBA 2K14\nba2k13.exe")
    sys.exit()

def NCAAMBB2k14():
    #!\\-Check if folder is empty for active-\\
    if(len(NCAAMBB) <=1):
        print(NCAAMBB,"Already Done")
        # os.startfile(r"E:\Games\Playground\NBA 2K14\nba2k14.exe")
        sys.exit()
    else:    
       

        #!\\-Compara las listas-//
        exist2k14c= set(active_folder2k14).intersection(folderJuego2k14)
        # print(exist2k14c,"duplicates files 2")

        #!\\-Guarda archivos Mod-//  ###################### lee lista
        for filename in exist2k14c:
            # print(filename,"exist")
            shutil.move(r"E:\Games\Playground\NBA 2K14" + "\\"+ str(filename),r"E:\Games\Playground\NBA 2K14" + "\\"+ Missing2k14[0] + "\\" + str(filename))#?Modificar a PC
        
        #!\\-Mueve archivos del folder NCAAMBB al juego-//
        NCAAMBB.remove("outputMod.txt")
        
        for filename in NCAAMBB:
            shutil.move(r"E:\Games\Playground\NBA 2K14" + "\\"+ "NCAA MBB 17-18" + "\\" + str(filename),r"E:\Games\Playground\NBA 2K14" + "\\" + str(filename))#?Modificar a PC
            print(filename)
        
        os.chdir(r"C:\Users\The Mask Power\AppData\Roaming\2K Sports\NBA 2K14")
        for filename in saves2k14:
            if(Missing2k14Save[0][0] != "NCAA MBB 17-18"):
                     
                try:
                    os.rename("Saves",Missing2k14Save[0][0])
                    time.sleep(0.1)
                    os.rename("NCAA MBB 17-18","Saves")       
                #    print(Missing[0][0],"Original")     
                    

                except:
                    print(filename,"Already Done")
                    # os.startfile(r"E:\Games\Playground\NBA 2K14\nba2k13.exe")
                
    # os.startfile(r"E:\Games\Playground\NBA 2K14\nba2k13.exe")
    sys.exit()          


def ultimateBase2k14():

    #!\\-Check if folder is empty for active-\\
    if(len(ultimateBase) <=1):
        print(ultimateBase,"Already Done")
        # os.startfile(r"E:\Games\Playground\NBA 2K14\nba2k14.exe")
        sys.exit()
    else:    
       

        #!\\-Compara las listas-//
        exist2k14o= set(active_folder2k14).intersection(folderJuego2k14)
        print(exist2k14o,"duplicates files 2")

        #!\\-Guarda archivos Mod-//  ###################### lee lista
        for filename in exist2k14o:
            # print(filename,"exist")
            shutil.move(r"E:\Games\Playground\NBA 2K14" + "\\"+ str(filename),r"E:\Games\Playground\NBA 2K14" + "\\"+ Missing2k14[0] + "\\" + str(filename))#?Modificar a PC
        
        #!\\-Mueve archivos del folder Original al juego-//
        ultimateBase.remove("outputMod.txt")
        
        for filename in ultimateBase:
            shutil.move(r"E:\Games\Playground\NBA 2K14" + "\\"+ "Ultimate Base Roster 14" + "\\" + str(filename),r"E:\Games\Playground\NBA 2K14" + "\\" + str(filename))#?Modificar a PC
            print(filename)
        
        os.chdir(r"C:\Users\The Mask Power\AppData\Roaming\2K Sports\NBA 2K14")
        for filename in saves2k14:
            if(Missing2k14Save[0][0] != "Ultimate Base Roster 14"):

                try:
                   os.rename("Saves",Missing2k14Save[0][0])
                   time.sleep(0.1)
                   os.rename("Ultimate Base Roster 14","Saves")       
                #    print(Missing2k14Save[0][0],"Original")
                   break     
                   

                except:
                    print(filename,"Already Done")
                    break
                    

    # os.startfile(r"E:\Games\Playground\NBA 2K14\nba2k13.exe")
    sys.exit()
               
#!\\\\\\\\\\\\\\\\\\\\\ 
#!\\ - 2K14 Ends -   \\
#!\\\\\\\\\\\\\\\\\\\\\



#!\\\\\\\\\\\\\\\\\\\\\ 
#!\\ - 2K16 Starts - \\
#!\\\\\\\\\\\\\\\\\\\\\


Folders2k16=["FIBA","Original"]
Founded2k16=[]
Missing2k16=[]
Folders2k16Saves=["FIBA","Original"]
Founded2k16Save=[]
Missing2k16Save=[]
notFounded2k16=[]
foundedSaves2k16=[]
saves2k16= os.listdir(r"C:\Users\The Mask Power\AppData\Roaming\2K Sports\NBA 2K16")
modFolder2k16 = os.listdir(r"E:\Games\Playground\NBA 2K16\FIBA")#?Modificar a PC
originalFolder2k16 = os.listdir(r"E:\Games\Playground\NBA 2K16\Original")#?Modificar a PC





def verify2k16():
    os.chdir(r"E:\Games\Playground\NBA 2K16")#?Modificar a PC
    for filename in os.listdir(r"E:\Games\Playground\NBA 2K16"): #This
        
        if(filename.startswith("Original") and len(originalFolder2k16) == 1):
            # print("originalFolder2k16",originalFolder2k16,len(originalFolder2k16))
            Founded2k16.append(filename)
                

        if(filename.startswith("FIBA") and len(modFolder2k16) == 1):
            # print(filename,len(filename))
            Founded2k16.append(filename)

                
verify2k16()
Missing2k16=Founded2k16
# print("Founded",Founded2k16)

# def Missed2k16(Founded2k16, Folders2k16):
#     return (list(set(Folders2k16) - set(Founded2k16)))

# Missing2k16.append(Missed2k16(Founded2k16, Folders2k16)) 
# print("Activated save 2k12 1 -", Missing)
print("Activated 2k16", Missing2k16[0])



os.chdir(r"C:\Users\The Mask Power\AppData\Roaming\2K Sports\NBA 2K16")





def verify2k16Save():
    for filename in os.listdir(r"C:\Users\The Mask Power\AppData\Roaming\2K Sports\NBA 2K16"): #This
        
        if(filename.startswith("Original")):
           Founded2k16Save.append(filename)
                
        elif(filename.startswith("FIBA")):
           Founded2k16Save.append(filename)

                
verify2k16Save()

def MissedSave2k16(Founded2k16Save, Folders2k16):

    return (list(set(Folders2k16) - set(Founded2k16Save)))

Missing2k16Save.append(MissedSave2k16(Founded2k16Save, Folders2k16)) 
print("2k16 save2",Missing2k16Save[0][0])
# print("Activated save 2k16 -", Missing2k16Save[0][0])




#!\\-Lee la lista del FIBA-//
modText2k16 = open(r"E:\Games\Playground\NBA 2K16\FIBA\outputMod.txt", "r+") #?Modificar a PC
my_mod_data2k16 = modText2k16.read().split()
modText2k16.close()
my_mod_data2k16.remove("outputMod.txt")
# print(my_mod_data2k16, "Mod Data")
activePath = open(r"E:\Games\Playground\NBA 2K16" + "\\"+ Missing2k16[0] + "\\" + "outputMod.txt")
active_folder2k16 = activePath.read().split()
active_folder2k16.remove("outputMod.txt")
activePath.close
# print(active_folder2k16, "Mod Data",my_mod_data2k16)



 #!\\-Lee la Lista Original-//
modText2k16o = open(r"E:\Games\Playground\NBA 2K16\Original\outputMod.txt", "r+")#?Modificar a PC
my_mod_data2k16o = modText2k16o.read().split()
modText2k16o.close()
my_mod_data2k16o.remove("outputMod.txt")
# print(my_mod_data2k16, "Mod Data")



#!\\-Lee el Folder Del Juego-//
folderJuego2k16 = os.listdir(r"E:\Games\Playground\NBA 2K16")#?Modificar a PC
#! print(folderJuego2k16,"folderJuego2k16")
# print(len(modFolder2k16),"modFolder2k16")




def FIBA2k16():

    #!\\-Check if folder is empty for active-\\
    if(len(modFolder2k16) ==1):
        print(modFolder2k16,"=1 Already Done")
        # os.startfile(r"E:\Games\Playground\NBA 2K16\nba2k16.exe")
        sys.exit()

    else:
    #!\\-Compara las listas-//

        exist2k16o = set(active_folder2k16).intersection(folderJuego2k16)
        # print(exist2k16o,"duplicatedFiles")

    #!\\-Guarda archivos originales-//
        for filename in exist2k16o:
            # print(filename,"exist2k16o")
            shutil.move(r"E:\Games\Playground\NBA 2K16" + "\\"+ str(filename),r"E:\Games\Playground\NBA 2K16" + "\\"+ Missing2k16[0] + "\\" + str(filename))#?Modificar a PC

    #!\\-Mueve archivos del folder Mod al juego-//
        modFolder2k16.remove("outputMod.txt")
        for filename in modFolder2k16:
            shutil.move(r"E:\Games\Playground\NBA 2K16" + "\\"+ "FIBA" + "\\" + str(filename),r"E:\Games\Playground\NBA 2K16" + "\\" + str(filename))#?Modificar a PC
            # print(filename)

    os.chdir(r"C:\Users\The Mask Power\AppData\Roaming\2K Sports\NBA 2K16")
    for filename in saves2k16:
        
        if(Missing2k16Save[0][0] != "FIBA"):
            print(Missing2k16Save[0][0])
            
            try:
                os.rename("Saves",Missing2k16Save[0][0])
                time.sleep(0.1)
                os.rename("FIBA","Saves")       
                print(Missing[0][0],"Original")     
                   

            except:
                print(filename,"Already Done")
                # os.startfile(r"E:\Games\Playground\NBA 2K16\nba2k16.exe")
                
    # os.startfile(r"E:\Games\Playground\NBA 2K16\nba2k16.exe")
    sys.exit()



def Original2k16():

    #!\\-Check if folder is empty for active-\\
    if(len(originalFolder2k16) <=1):
        print(originalFolder2k16,"Already Done")
        # os.startfile(r"E:\Games\Playground\NBA 2K16\nba2k16.exe")
        sys.exit()
    else:    
       

        #!\\-Compara las listas-//
        exist2k16o= set(active_folder2k16).intersection(folderJuego2k16)
        print(exist2k16o,"duplicates files 2")

        #!\\-Guarda archivos Mod-//  ###################### lee lista
        for filename in exist2k16o:
            # print(filename,"exist")
            shutil.move(r"E:\Games\Playground\NBA 2K16" + "\\"+ str(filename),r"E:\Games\Playground\NBA 2K16" + "\\"+ Missing2k16[0] + "\\" + str(filename))#?Modificar a PC
        
        #!\\-Mueve archivos del folder Original al juego-//
        originalFolder2k16.remove("outputMod.txt")
        
        for filename in originalFolder2k16:
            shutil.move(r"E:\Games\Playground\NBA 2K16" + "\\"+ "Original" + "\\" + str(filename),r"E:\Games\Playground\NBA 2K16" + "\\" + str(filename))#?Modificar a PC
            print(filename)
        
        os.chdir(r"C:\Users\The Mask Power\AppData\Roaming\2K Sports\NBA 2K16")
        for filename in saves2k16:
            if(Missing2k16Save[0][0] != "Original"):

                try:
                   os.rename("Saves",Missing2k16Save[0][0])
                   time.sleep(0.1)
                   os.rename("Original","Saves")       
                #    print(Missing2k16Save[0][0],"Original")
                   break     
                   

                except:
                    print(filename,"Already Done")
                    break
                    

    # os.startfile(r"E:\Games\Playground\NBA 2K16\nba2k16.exe")
    sys.exit()





#!\\\\\\\\\\\\\\\\\\\\\ 
#!\\ - 2K16 Ends -   \\
#!\\\\\\\\\\\\\\\\\\\\\




#!\\\\\\\\\\\\\\\\\\\\\ 
#!\\ - 2K19 Starts - \\
#!\\\\\\\\\\\\\\\\\\\\\


def Original2k19():
    print("2k19")

def FIBA2k19():
    print("FIBA2k19")

def College2k19():
    print("College2k19")


#!\\\\\\\\\\\\\\\\\\\\\ 
#!\\ - 2K19 Ends -   \\
#!\\\\\\\\\\\\\\\\\\\\\



#!\\\\\\\\\\\\\\\\\\\\\ 
#!\\ - 2K20 Starts - \\
#!\\\\\\\\\\\\\\\\\\\\\


Folders2k20=["Euroleague","NCAA","NBAPro", "Retro"] #This
Founded2k20=[]
Missing2k20=[]
os.chdir(r"E:\SteamLibrary\steamapps\common\NBA 2K20")

def verify2k20():
    for filename in os.listdir(r"E:\SteamLibrary\steamapps\common\NBA 2K20"): #This

        if(filename.startswith("Euroleague")):
            Founded2k20.append(filename)
            
        elif(filename.startswith("NCAA")):
            Founded2k20.append(filename)

        elif(filename.startswith("NBAPro")):
            Founded2k20.append(filename)
         
        elif(filename.startswith("Retro")):
            Founded2k20.append(filename)

verify2k20()



def Missed2k20(Founded2k20, Folders2k20):
    return (list(set(Folders2k20) - set(Founded2k20)))


Missing2k20.append(Missed2k20(Founded2k20, Folders2k20)) 
# print("Activated -",Missing2k20[0][0])

print()

def Euroleague():
    for filename in os.listdir(r"E:\SteamLibrary\steamapps\common\NBA 2K20"): #This

        if(os.path.exists(r"E:\SteamLibrary\steamapps\common\NBA 2K20\waigua") == False):
            os.rename("Euroleague","waigua")
            break

        if(filename.startswith("waigua") and Missing2k20[0][0] == "Euroleague"):
            print("Already done", filename)
            print("Missing2k20 -",Missing2k20[0][0])
            break

        
     
             
        if(Missing2k20[0][0] != "Euroleague"):
            try:
                os.rename("NBA2K_Hook", "NBA2K_HookRetro")
                time.sleep(1)
                os.rename("NBA2K_HookOriginal", "NBA2K_Hook")
            except:
                print("already rename to original")

            os.rename("waigua",Missing2k20[0][0])
            time.sleep(0.1)
            os.rename("Euroleague","waigua")
            break

        


        # elif(os.path.exists(r"E:\SteamLibrary\steamapps\common\NBA 2K20\Euroleague") and os.path.exists(r"E:\SteamLibrary\steamapps\common\NBA 2K20\Euroleague")):
        #     os.rename("Euroleague", "waigua")
        #     # os.rename("NBA2K20.exe","NBA2K20Normal.exe")
        #     # os.rename("NBA2K20Mod.exe","NBA2K20.exe")
        #     break

       

    os.startfile(r"E:\SteamLibrary\steamapps\common\NBA 2K20\NBA2K20.exe")
    sys.exit()
    


    
def NCAA():
    for filename in os.listdir(r"E:\SteamLibrary\steamapps\common\NBA 2K20"): #This

        if(os.path.exists(r"E:\SteamLibrary\steamapps\common\NBA 2K20\waigua") == False):
            os.rename("NCAA","waigua")
            break

        if(filename.startswith("waigua") and Missing2k20[0][0] == "NCAA"):
            print("Already done", filename)
            print("Missing2k20 -",Missing2k20[0][0])
            break

       
            
        if(Missing2k20[0][0] != "NCAA"):
            try:
                os.rename("NBA2K_Hook", "NBA2K_HookRetro")
                time.sleep(1)
                os.rename("NBA2K_HookOriginal", "NBA2K_Hook")
            except:
                print("already rename to original")
                
            os.rename("waigua",Missing2k20[0][0])
            time.sleep(0.1)
            os.rename("NCAA","waigua")
            break

        
        

        # elif(os.path.exists(r"E:\SteamLibrary\steamapps\common\NBA 2K20\NCAA") and os.path.exists(r"E:\SteamLibrary\steamapps\common\NBA 2K20\Euroleague") and os.path.exists(r"E:\SteamLibrary\steamapps\common\NBA 2K20\NBAPro")):
        #     os.rename("NCAA", "waigua")
        #     print(filename)
        #     # os.rename("NBA2K20.exe","NBA2K20Normal.exe")
        #     # os.rename("NBA2K20Mod.exe","NBA2K20.exe")
        #     break
       
    

    os.startfile(r"E:\SteamLibrary\steamapps\common\NBA 2K20\NBA2K20.exe")
    sys.exit()
        
def NBAPro():
    for filename in os.listdir(r"E:\SteamLibrary\steamapps\common\NBA 2K20"): #This

        if(filename.startswith("NBA2K_HookOriginal")):
                    print(filename,"founded2k20")
                    os.rename("NBA2K_Hook", "NBA2K_HookRetro")
                    time.sleep(0.1)
                    os.rename("NBA2K_HookOriginal", "NBA2K_Hook")
                    time.sleep(0.1)

        if(os.path.exists(r"E:\SteamLibrary\steamapps\common\NBA 2K20\waigua") == False):
            os.rename("NBAPro","waigua")
            break

        if(filename.startswith("waigua") and Missing2k20[0][0] == "NBAPro"):
            print("Already done", filename)
            print("Missing2k20 -",Missing2k20[0][0])
            break

        
       
        

        if(Missing2k20[0][0] != "NBAPro"):
            try:
                os.rename("NBA2K_Hook", "NBA2K_HookRetro")
                time.sleep(0.1)
                os.rename("NBA2K_HookOriginal", "NBA2K_Hook")
            except:
                print("already rename to original")

            os.rename("waigua",Missing2k20[0][0])
            time.sleep(0.1)
            os.rename("NBAPro","waigua")
            break

            
        
        

        # elif(os.path.exists(r"E:\SteamLibrary\steamapps\common\NBA 2K20\Euroleague") and os.path.exists(r"E:\SteamLibrary\steamapps\common\NBA 2K20\NCAA")):
        #     os.rename("NBAPro", "waigua")
        #     print(filename)
        #     # os.rename("NBA2K20.exe","NBA2K20Normal.exe")
        #     # os.rename("NBA2K20Mod.exe","NBA2K20.exe")
        #     break
        
    

    os.startfile(r"E:\SteamLibrary\steamapps\common\NBA 2K20\NBA2K20.exe")
    sys.exit()


 
def Retro():
    for filename in os.listdir(r"E:\SteamLibrary\steamapps\common\NBA 2K20"): #This

        if(os.path.exists(r"E:\SteamLibrary\steamapps\common\NBA 2K20\waigua") == False):
            os.rename("Retro","waigua")
            break

        if(filename.startswith("waigua") and Missing2k20[0][0] == "Retro"):
            print("Already done", filename)
            print("Missing2k20 -",Missing2k20[0][0])
            break
        try:
            if(Missing2k20[0][0] != "Retro"):
                os.rename("waigua",Missing2k20[0][0])
                os.rename("NBA2K_Hook", "NBA2K_HookOriginal")
                time.sleep(0.1)
                os.rename("Retro","waigua")
                os.rename("NBA2K_HookRetro", "NBA2K_Hook")
                break
        except:
            print("2K hook ready")

        

        # elif(os.path.exists(r"E:\SteamLibrary\steamapps\common\NBA 2K20\Euroleague") and os.path.exists(r"E:\SteamLibrary\steamapps\common\NBA 2K20\NCAA")):
        #     os.rename("NBAPro", "waigua")
        #     print(filename)
        #     # os.rename("NBA2K20.exe","NBA2K20Normal.exe")
        #     # os.rename("NBA2K20Mod.exe","NBA2K20.exe")
        #     break
        
    

    os.startfile(r"E:\SteamLibrary\steamapps\common\NBA 2K20\NBA2K20.exe")
    sys.exit()


# Como identificar que lo quiero default

def Normal():
    for filename in os.listdir(r"E:\SteamLibrary\steamapps\common\NBA 2K20"): #This

        if(filename.startswith("waigua")):
            print(Missing2k20[0][0])
            os.rename("waigua",Missing2k20[0][0])
            # os.rename("NBA2K20.exe", "NBA2K20Mod.exe")
            # os.rename("NBA2K20Normal.exe", "NBA2K20.exe")
            break
        
            
    
    os.startfile(r"E:\SteamLibrary\steamapps\common\NBA 2K20\NBA2K20.exe")
    sys.exit()



#!\\\\\\\\\\\\\\\\\\\\\ 
#!\\ - 2K20 Ends - \\
#!\\\\\\\\\\\\\\\\\\\\\




main=tk.IntVar()
tk.Label(master, text="""NBA 2K10""", fg="white", bg="black").grid(row="0", column="1")
tk.Button(master,text="NBA 2K10", command=Original2k10, fg="white", bg="black", image=photo2k10).grid(row="1", column="1")
tk.Label(master, text="""NBA 2K11""", fg="white",  bg="black").grid(row="0", column="2")
tk.Button(master,text="NBA 2K11     ", command=Original2k11, fg="white", bg="black" ,image=photo2k11).grid(row="1", column="2")
tk.Label(master, text="""NBA 2K12""", fg="white",  bg="black").grid(row="0", column="3")
tk.Button(master,text="Original", command=Original, fg="white", bg="black", image=photo2k12).grid(row="1", column="3")
tk.Label(master, text="""NBA 2K13""", fg="white",  bg="black").grid(row="0", column="4")
tk.Button(master,text="Original     ", command=Original2k13, fg="white", bg="black" ,image=photo2k13).grid(row="1", column="4")
tk.Label(master, text="""NBA 2K14""", fg="white", bg="black").grid(row="0", column="5")
tk.Button(master,text="NBA 2K14", command=Original2k14, fg="white", bg="black", image=photo2k14).grid(row="1", column="5")
tk.Label(master, text="""NBA 2K15""", fg="white",  bg="black").grid(row="0", column="6")
tk.Button(master,text="Original", command=Original2k15, fg="white", bg="black", image=photo2k15).grid(row="1", column="6")
tk.Label(master, text="""NBA 2K16""", fg="white",  bg="black").grid(row="0", column="7")
tk.Button(master,text="Original", command=Original2k16, fg="white", bg="black", image=photo2k16).grid(row="1", column="7")

tk.Label(master, text="""NBA 2K17""", fg="white",  bg="black").grid(row="2", column="1")
tk.Button(master,text="Original", command=Original2k17, fg="white", bg="black", image=photo2k17).grid(row="3", column="1")
tk.Label(master, text="""NBA 2K18""", fg="white",  bg="black").grid(row="2", column="2")
tk.Button(master,text="NBA 2K18", command=Original2k18, fg="white", bg="black", image=photo2k18).grid(row="3", column="2")
tk.Label(master, text="""NBA 2K19""", fg="white", bg="black").grid(row="2", column="3")
tk.Button(master,text="NBA 2K19", command=Original2k19, fg="white", bg="black", image=photo2k19).grid(row="3", column="3")
tk.Label(master, text="""NBA 2K20""", fg="white",  bg="black").grid(row="2", column="4")
tk.Button(master,text="Original", command=Normal, fg="white", bg="black", image=photo2k20).grid(row="3", column="4")

tk.Label(master, text="""NBA 2K12- FIBA""", fg="white",  bg="black").grid(row="2", column="5")
tk.Button(master,text="FIBA2k12     ", command=FIBA, fg="white", bg="black" ,image=photoFiba12).grid(row="3", column="5")
tk.Label(master, text="""NBA 2K12- FIBA""", fg="white",  bg="black").grid(row="2", column="6")
tk.Button(master,text="FIBA 2k13", command=FIBA2k13, fg="white", bg="black" ,image=photo2k13FIBA).grid(row="3", column="6")
tk.Label(master, text="""NBA 2K13- FIBA""", fg="white",  bg="black").grid(row="2", column="7")
tk.Button(master,text="FIBA2k13     ", command=FIBA, fg="white", bg="black" ,image=photoFiba12).grid(row="3", column="7")
tk.Label(master, text="""NBA 2K14- FIBA""", fg="white", bg="black").grid(row="4", column="1")
tk.Button(master,text="NBA 2K14 FIBA", command=FIBA2k14, fg="white", bg="black", image=photo2k14FIBA).grid(row="5", column="1")
tk.Label(master, text="""NBA 2K16- FIBA""", fg="white", bg="black").grid(row="4", column="2")
tk.Button(master,text="NBA 2K16 FIBA", command=FIBA2k16, fg="white", bg="black", image=photo2k16Rio).grid(row="5", column="2")
tk.Label(master, text="""NBA 2K19- FIBA""", fg="white", bg="black").grid(row="4", column="3")
tk.Button(master,text="NBA 2K19 FIBA", command=FIBA2k19, fg="white", bg="black", image=photo2k19FIBA).grid(row="5", column="3")

tk.Label(master, text="""NBA 2K13- College""", fg="white",  bg="black").grid(row="4", column="4")
tk.Button(master,text="College     ", command=NCAA2k13, fg="white", bg="black" ,image=photo2k13College).grid(row="5", column="4")
tk.Label(master, text="""NBA 2K14- MarchMadness 15""", fg="white", bg="black").grid(row="4", column="5")
tk.Button(master,text="NBA 2K14 MarchMadness 15", command=MM15, fg="white", bg="black", image=photoCollege).grid(row="5", column="5")
tk.Label(master, text="""NBA 2k14- College 2k20""", fg="white", bg="black").grid(row="4", column="6")
tk.Button(master,text="NBA 2k4 College 2k20", command=College2k1420, fg="white", bg="black", image=photo2k1420).grid(row="5", column="6")
tk.Label(master, text="""NBA 2K14- NCAA 14""", fg="white", bg="black").grid(row="4", column="7")
tk.Button(master,text="NBA 2K14 NCAA 14", command=NCAA2k14, fg="white", bg="black", image=photo2k14College).grid(row="5", column="7")
tk.Label(master, text="""NBA 2K14- NCAA MBB 17/18""", fg="white", bg="black").grid(row="6", column="1")
tk.Button(master,text="NBA 2K14- NCAA MBB 17-18", command=NCAAMBB2k14, fg="white", bg="black", image=photo2k14mbb).grid(row="7", column="1")
tk.Label(master, text="""NBA 2K14- Ultimate Base Roster 14""", fg="white", bg="black").grid(row="6", column="2")
tk.Button(master,text="NBA 2K14 Ultimate Base Roster 14", command=ultimateBase2k14, fg="white", bg="black", image=photo2k14CUBR).grid(row="7", column="2")
tk.Label(master, text="""NBA 2K20- NCAA""", fg="white",  bg="black").grid(row="6", column="3")
tk.Button(master,text="NBA 2K20- NCAA", command=NCAA, fg="white", bg="black", image=photo2k20mm).grid(row="7", column="3")

tk.Label(master, text="""NBA 2K20- Retro""", fg="white",  bg="black").grid(row="6", column="4")
tk.Button(master,text="NBA 2K20- Retro", command=Retro, fg="white", bg="black", image=photo2k20Retro).grid(row="7", column="4")
tk.Label(master, text="""NBA 2K20- Euroleague""", fg="white",  bg="black").grid(row="6", column="5")
tk.Button(master,text="NBA 2K20- Euroleague", command=Euroleague, fg="white", bg="black", image=photoEuroleague).grid(row="7", column="5")
tk.Label(master, text="""NBA 2K20- Pro""", fg="white",  bg="black").grid(row="6", column="6")
tk.Button(master,text="2K20 Pro", command=NBAPro, fg="white", bg="black", image=photo2k20Pro).grid(row="7", column="6")



master.geometry("1485x585")
master.mainloop() 

