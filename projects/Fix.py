from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import filedialog
import os
from tkinter import messagebox
import math
from statistics import stdev
from fractions import Fraction as fr



class Calculate_App:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1530x800+0+0")
        self.root.title("Calculate Software")

        # =================Varible===================

        self.Classroom=StringVar()
        self.room1=StringVar()
        self.room2=StringVar()
        self.Distance=IntVar()
        self.Times=IntVar()
        self.total_Distance=StringVar()
        self.total_Times=StringVar()
        self.SDWeekTim=StringVar()
        self.SDWeekDis=StringVar()
        self.SDDIS=StringVar()
        self.SDTIM=StringVar()
        self.sum=IntVar()


        #Building list
        self.Building_list = ['Select Building',
                            'A - ตึกเรียน',
                            'B - ตึกวิทยาศาสตร์',
                            'C - หอสมุดและแหล่งการเรียนรุ้',
                            'D - ห้องคุณธรรม ',
                            'E - ห้องเขียนแบบ',
                            'F - Stem - lab ',
                            'G - Machine Shop ',
                            'H - อาคารศิลป์',
                            'I - ศูนย์กีฬา']
        

        #Stair list
        self.Stair_list = ['1','2','3','4']
        self.A_Stair_list = ['1','2','3','4']
        self.B_Stair_list = ['1','2','3']
        self.C_Stair_list = ['1','2','3']
        self.D_Stair_list = ['1']
        self.E_Stair_list = ['1']
        self.F_Stair_list = ['1']
        self.G_Stair_list = ['1']
        self.H_Stair_list = ['1']
        self.I_Stair_list = ['1','2','3']


        #Room list
        self.Room_list = ['1','2','3','4','5','6','7','8','9']
        self.A_Room_list = ['1','2','3','4','5','6','7','8','9']
        self.B_Room_list = ['1','2','3','4','5','6','7','8','9']
        self.C_Room_list1 = ['1']
        self.C_Room_list2 = ['1','2','3']
        self.C_Room_list3 = ['1']
        self.D_Room_list = ['1']
        self.E_Room_list = ['1','2']
        self.F_Room_list = ['1']
        self.G_Room_list = ['1']
        self.H_Room_list = ['1','2','3','4']
        self.I_Room_list1 = ['1']
        self.I_Room_list2 = ['1','2','3','4']
        self.I_Room_list3 = ['1']

        #Class list
        self.Class_list = ['Select Grade',
                            'M.1-1','M.1-2','M.1-3','M.1-4','M.2-1','M.2-2','M.2-3','M.2-4','M.3-1','M.3-2','M.3-3','M.3-4',
                            'M.4-1','M.4-2','M.4-3','M.4-4','M.4-5','M.4-6','M.5-1','M.5-2','M.5-3','M.5-4','M.5-5','M.5-6',
                            'M.6-1','M.6-2','M.6-3','M.6-4','M.6-5','M.6-6']
        
        self.Day_list = ['Select Day',
                        'Monday','Tuesday','Wednesday','Thursday','Friday']
        
        

        #Maintitle
        Ibl_title=Label(self.root,text="CALCULATE DISTANCES AND TIMES",font=("Consolas",35,"bold"),bg="white",fg="black")
        Ibl_title.place(x=0,y=0,width=1530,height=45)


        #Maindframe
        Main_Frame=Frame(self.root,bd=5,relief=GROOVE,bg="white")
        Main_Frame.place(x=0,y=45,width=1530,height=680)

        
        #Image1
        
        #Image2

        #Image3


        #Place1 LabelFrame
        Place1_Frame=LabelFrame(Main_Frame,text="PLACE",font=("Consolas",12,"bold"),bg="white",fg="black")
        Place1_Frame.place(x=10,y=5,width=350,height=140)


        #Building
        self.Ibl_building1=Label(Place1_Frame,text="Building", font=("Consolas",12,),bg="white",fg="black", bd=4)
        self.Ibl_building1.grid(row=0, column=0, stick=W, padx=5, pady=2)

        self.Combo_building1=ttk.Combobox(Place1_Frame,value=self.Building_list, font=("Consolas",12), width=20, state="readonly")
        self.Combo_building1.current(0)
        self.Combo_building1.grid(row=0, column=1, sticky=W, padx=5, pady=2)
        self.Combo_building1.bind("<<ComboboxSelected>>", self.Buildings)



        #Stair
        self.Stair_label1 = Label(Place1_Frame, text="Stair",font=("Consolas",12,),bg="white",fg="black", bd=4)
        self.Stair_label1.grid(row=1, column=0, stick=W, padx=5, pady=2)

        self.Stair_Combo1 = ttk.Combobox(Place1_Frame, value=[""], font=('consolas',12), width=20, state="readonly")
        self.Stair_Combo1.grid(row=1, column=1, stick=W, padx=5, pady=2)
        self.Stair_Combo1.bind("<<ComboboxSelected>>", self.Stair)


        #Room
        self.Room_label1 = Label(Place1_Frame, text="Room",font=("Consolas",12,),bg="white",fg="black", bd=4)
        self.Room_label1.grid(row=2, column=0, stick=W, padx=5, pady=2)

        self.Room_Combo1 = ttk.Combobox(Place1_Frame, textvariable=self.room1, font=('consolas',12), width=20,state="readonly")
        self.Room_Combo1.grid(row=2, column=1, stick=W, padx=5, pady=2)


        #Place2 LabelFrame
        Place2_Frame=LabelFrame(Main_Frame,text="PLACE",font=("Consolas",12,"bold"),bg="white",fg="black")
        Place2_Frame.place(x=380,y=5,width=350,height=140)


        #Building
        self.Ibl_building2=Label(Place2_Frame,text="Building",font=("Consolas",12,),bg="white",fg="black", bd=4)
        self.Ibl_building2.grid(row=0, column=0, stick=W, padx=5, pady=2)

        self.Combo_building2=ttk.Combobox(Place2_Frame,value=self.Building_list, font=("Consolas",12), width=20, state="readonly")
        self.Combo_building2.current(0)
        self.Combo_building2.grid(row=0, column=1, sticky=W, padx=5, pady=2)
        self.Combo_building2.bind("<<ComboboxSelected>>", self.Buildings2)


        #Stair
        self.Stair_Combo2 = Label(Place2_Frame, text="Stair",font=("Consolas",12,),bg="white",fg="black", bd=4)
        self.Stair_Combo2.grid(row=1, column=0, stick=W, padx=5, pady=2)

        self.Stair_Combo2 = ttk.Combobox(Place2_Frame, values=[""], font=('consolas',12),width=20,state="readonly")
        self.Stair_Combo2.grid(row=1, column=1, stick=W, padx=5, pady=2)
        self.Stair_Combo2.bind("<<ComboboxSelected>>", self.Stair2)


        #Room
        self.Room_label2 = Label(Place2_Frame, text="Room",font=("Consolas",12),bg="white",fg="black", bd=4)
        self.Room_label2.grid(row=2, column=0, stick=W, padx=5, pady=2)

        self.Room_Combo2 = ttk.Combobox(Place2_Frame, textvariable=self.room2, font=('consolas',12), width=20, state="readonly")
        self.Room_Combo2.grid(row=2, column=1, stick=W, padx=5, pady=2)
        self.Room_Combo2.bind("<<ComboboxSelected>>", self.calculate)


        #Class Frame
        GradeClass_Frame=LabelFrame(Main_Frame,bg="white",fg="black")
        GradeClass_Frame.place(x=750,y=15,width=510,height=40)

        self.Class=Label(GradeClass_Frame,text="Grade", font=("Consolas",12,),bg="white",fg="black", bd=4)
        self.Class.grid(row=0, column=0, stick=W, padx=5, pady=2)

        self.Combo_Class=ttk.Combobox(GradeClass_Frame,value=self.Class_list, font=("Consolas",12), width=16, state="readonly")
        self.Combo_Class.grid(row=0, column=1, sticky=W, padx=5, pady=2)
        self.Combo_Class.current(0)

        self.Day=Label(GradeClass_Frame,text="Day", font=("Consolas",12,),bg="white",fg="black", bd=4)
        self.Day.grid(row=0, column=2, stick=W, padx=5, pady=2)

        self.Combo_Day=ttk.Combobox(GradeClass_Frame,value=self.Day_list, font=("Consolas",12), width=16, state="readonly")
        self.Combo_Day.grid(row=0, column=3, sticky=W, padx=5, pady=2)
        self.Combo_Day.current(0)

        #Right Frame show
        RightLabelFrame=LabelFrame(Main_Frame,text="SHOW CALCULATE", font=("Consolas",12,"bold"),bg="white",fg="black")
        RightLabelFrame.place(x=750,y=55,width=510,height=440)

        #Scrollbar
        Scroll_y=Scrollbar(RightLabelFrame,orient=VERTICAL)
        self.textarea=Text(RightLabelFrame,yscrollcommand=Scroll_y.set, bg="white", fg="blue",  font=("Consolas",12))
        Scroll_y.pack(side=RIGHT, fill=Y)
        Scroll_y.config(command=self.textarea.yview)
        self.textarea.pack(fill=BOTH, expand=1)

        #Middle_Frame
        MiddleFrame=Frame(Main_Frame)
        MiddleFrame.place(x=10,y=150,width=720,height=340)

        #image 1
        img12=Image.open("image/S__5193748.jpg")
        img12 = img12.resize((360, 340), resample=Image.LANCZOS)
        self.phoimg12=ImageTk.PhotoImage(img12)

        Ibl_img12=Label(MiddleFrame,image=self.phoimg12)
        Ibl_img12.place(x=0,y=0,width=360,height=340)

        #image 2
        img13=Image.open("image/S__5193747.jpg")
        img13 = img13.resize((360, 340), resample=Image.LANCZOS)
        self.phoimg13=ImageTk.PhotoImage(img13)

        Ibl_img13=Label(MiddleFrame,image=self.phoimg13)
        Ibl_img13.place(x=360,y=0,width=360,height=340)

        #AGGREGATE LabelFrame
        AGGREGATE_Frame=LabelFrame(Main_Frame,text="AGGREGATE",font=("Consolas",12,"bold"),bg="white",fg="black")
        AGGREGATE_Frame.place(x=10,y=495,width=720,height=147)

        #DISTANCE
        self.Dis=Label(AGGREGATE_Frame,text="DISTANCES (m)", font=("Consolas",10),bg="white",fg="black", bd=4)
        self.Dis.grid(row=0, column=0, stick=W, padx=5, pady=2)

        self.Dis_Enty=Entry(AGGREGATE_Frame,textvariable=self.Distance, font=("Consolas",12), width=12)
        self.Dis_Enty.grid(row=0, column=1, sticky=W, padx=5, pady=2)


        #TIMES
        self.Tim=Label(AGGREGATE_Frame,text="TIMES (s)", font=("Consolas",10),bg="white",fg="black", bd=4)
        self.Tim.grid(row=1, column=0, stick=W, padx=5, pady=2)

        self.Tim_Enty=Entry(AGGREGATE_Frame,textvariable=self.Times, font=("Consolas",12), width=12)
        self.Tim_Enty.grid(row=1, column=1, sticky=W, padx=5, pady=2)


        #SUM_DISTANCE
        self.IblTotalDIS=Label(AGGREGATE_Frame,text="TOTAL DISTANCES (m)", font=("Consolas",10),bg="white",fg="black",bd=4)
        self.IblTotalDIS.grid(row=2, column=0, sticky=W,padx=5, pady=2 )

        self.EntyTotalDIS = Entry(AGGREGATE_Frame,textvariable=self.total_Distance, font=('consolas',12),width=12)
        self.EntyTotalDIS.grid(row=2, column=1, stick=W, padx=5, pady=2)


        #SUM_TIMES
        self.IblTotalTIM=Label(AGGREGATE_Frame,text="TOTAL TIMES (s)", font=("Consolas",10),bg="white",fg="black",bd=4)
        self.IblTotalTIM.grid(row=3, column=0, sticky=W,padx=5, pady=2)

        self.EntyTotalTIM = Entry(AGGREGATE_Frame,textvariable=self.total_Times, font=('consolas',12),width=12)
        self.EntyTotalTIM.grid(row=3, column=1, stick=W, padx=5, pady=2)

        #Mathematical LabelFrame
        Mathematical_Frame=LabelFrame(Main_Frame,text="MATHEMATICAL",font=("Consolas",12,"bold"),bg="white",fg="black")
        Mathematical_Frame.place(x=750,y=495,width=510,height=147)

        #SUM_DISTANCE_WEEK
        self.IblweekDIS=Label(Mathematical_Frame,text="TOTAL DISTANCES (m)", font=("Consolas",10),bg="white",fg="black",bd=4)
        self.IblweekDIS.grid(row=0, column=0, sticky=W,padx=5, pady=2 )

        self.EntyweekDIS = Entry(Mathematical_Frame,textvariable=self.SDWeekDis, font=('consolas',12),width=12)
        self.EntyweekDIS.grid(row=0, column=1, stick=W, padx=5, pady=2)

        #SUM_TIMES_WEEK
        self.IblweekTIM=Label(Mathematical_Frame,text="TOTAL TIMES (s)", font=("Consolas",10),bg="white",fg="black",bd=4)
        self.IblweekTIM.grid(row=1, column=0, sticky=W,padx=5, pady=2)

        self.EntyweekTIM = Entry(Mathematical_Frame,textvariable=self.SDWeekTim, font=('consolas',12),width=12)
        self.EntyweekTIM.grid(row=1, column=1, stick=W, padx=5, pady=2)
        

        #SD_DISTANCE
        self.IblSDDis=Label(Mathematical_Frame,text="SD Distances", font=("Consolas",10),bg="white",fg="black",bd=4)
        self.IblSDDis.grid(row=2, column=0, sticky=W,padx=5, pady=2)

        self.EntySDDis = Entry(Mathematical_Frame,textvariable=self.SDDIS, font=('consolas',12),width=12)
        self.EntySDDis.grid(row=2, column=1, stick=W, padx=5, pady=2)


        #SD_TIMES
        self.IblSDTim=Label(Mathematical_Frame,text="SD Times", font=("Consolas",10),bg="white",fg="black",bd=4)
        self.IblSDTim.grid(row=3, column=0, sticky=W,padx=5, pady=2)

        self.EntySDTim = Entry(Mathematical_Frame,textvariable=self.SDTIM, font=('consolas',12),width=12)
        self.EntySDTim.grid(row=3, column=1, stick=W, padx=5, pady=2)


        self.EnterSDDIS=Button(Mathematical_Frame,height=1,text="Enter",command=self.enterSDdis,font=("Consolas",9),bg="white",fg="black",width=8,cursor="hand2")
        self.EnterSDDIS.grid(row=0,column=2,padx=5, pady=3)

        self.EnterSDTIM=Button(Mathematical_Frame,height=1,text="Enter",command=self.enterSDtim,font=("Consolas",9),bg="white",fg="black",width=8,cursor="hand2")
        self.EnterSDTIM.grid(row=1,column=2,padx=5, pady=3)

        self.EnterCALDIS=Button(Mathematical_Frame,height=1,text="Calculate",command=self.calculateSD_DISTANCE,font=("Consolas",9),bg="white",fg="black",width=11,cursor="hand2")
        self.EnterCALDIS.grid(row=0,column=3,padx=5, pady=3)

        self.EnterCALTIM=Button(Mathematical_Frame,height=1,text="Calculate",command=self.calculateSD_TIMES,font=("Consolas",9),bg="white",fg="black",width=11,cursor="hand2")
        self.EnterCALTIM.grid(row=1,column=3,padx=5, pady=3)

        self.ClearCALDIS=Button(Mathematical_Frame,height=1,text="Clear",command=self.clearSD,font=("Consolas",9),bg="white",fg="black",width=8,cursor="hand2")
        self.ClearCALDIS.grid(row=2,column=2,padx=5, pady=3)

        self.ClearCALTIM=Button(Mathematical_Frame,height=1,text="Clear",command=self.clearSD,font=("Consolas",9),bg="white",fg="black",width=8,cursor="hand2")
        self.ClearCALTIM.grid(row=3,column=2,padx=5, pady=3)


        #Button Frame
        Btn_Frame=Frame(AGGREGATE_Frame,bd=2,bg="white")
        Btn_Frame.place(x=330,y=5)
        

        #Enter_Button
        self.BtnEnter=Button(Btn_Frame,height=2,text="Enter",command=self.enter_data,font=("Consolas",12),bg="white",fg="black",width=9,cursor="hand2")
        self.BtnEnter.grid(row=0,column=0)


        #Delete_Button
        self.BtnDelete=Button(Btn_Frame,height=2,text="Delete",command=self.delete,font=("Consolas",12),bg="white",fg="black",width=9,cursor="hand2")
        self.BtnDelete.grid(row=0,column=1)


        #Clear_Button
        self.BtnClear=Button(Btn_Frame,height=2,text="Clear",command=self.clear,font=("Consolas",12),bg="white",fg="black",width=9,cursor="hand2")
        self.BtnClear.grid(row=0,column=2)


        #Generate_Button
        self.BtnExit=Button(Btn_Frame,height=2,text="Create",command=self.create,font=("Consolas",12),bg="white",fg="black",width=9,cursor="hand2")
        self.BtnExit.grid(row=0,column=3)


        #Save_Button
        self.BtnExit=Button(Btn_Frame,height=2,text="Save",command=self.save,font=("Consolas",12),bg="white",fg="black",width=9,cursor="hand2")
        self.BtnExit.grid(row=1,column=0)


        #Open_Button
        self.BtnExit=Button(Btn_Frame,height=2,text="Open",command=self.open,font=("Consolas",12),bg="white",fg="black",width=9,cursor="hand2")
        self.BtnExit.grid(row=1,column=1)

        #Break_Button
        self.BtnExit=Button(Btn_Frame,height=2,text="Break",command=self.Stop,font=("Consolas",12),bg="white",fg="black",width=9,cursor="hand2")
        self.BtnExit.grid(row=1,column=2)

        #Exit_Button
        self.BtnExit=Button(Btn_Frame,height=2,text="Exit",command=self.root.destroy,font=("Consolas",12),bg="white",fg="black",width=9,cursor="hand2")
        self.BtnExit.grid(row=1,column=3)



        self.welcome()
        self.i=[]
        self.l=[]
        self.a=[]
        self.b=[]
        

# ========================================= Fuction Declaration ===================================================================

    def welcome(self):
            self.textarea.delete(1.0,END)
            self.textarea.insert(END,"\t Welcome CALCULATE DISTANCES AND TIMES ")
            self.textarea.insert(END,"\n ====================================================")
            self.textarea.insert(END,f"\n Classroom\t\t\t\tDistance\t\tTimes")
            self.textarea.insert(END,"\n ====================================================\n")


    #config 
    def Buildings(self,event=""):
            if self.Combo_building1.get()=="A - ตึกเรียน" :
                self.Stair_Combo1.config(value=self.A_Stair_list) 
                self.Stair_Combo1.current(0)

            if self.Combo_building1.get()=="B - ตึกวิทยาศาสตร์" :
                self.Stair_Combo1.config(value=self.B_Stair_list)
                self.Stair_Combo1.current(0)

            if self.Combo_building1.get()=="C - หอสมุดและแหล่งการเรียนรุ้" :
                self.Stair_Combo1.config(value=self.C_Stair_list)
                self.Stair_Combo1.current(0)

            if self.Combo_building1.get()=="D - ห้องคุณธรรม" :
                self.Stair_Combo1.config(value=self.D_Stair_list)
                self.Stair_Combo1.current(0)
            
            if self.Combo_building1.get()=="E - ห้องเขียนแบบ" :
                self.Stair_Combo1.config(value=self.E_Stair_list)
                self.Stair_Combo1.current(0)

            if self.Combo_building1.get()=="F - Stem - lab " :
                self.Stair_Combo1.config(value=self.F_Stair_list)
                self.Stair_Combo1.current(0)

            if self.Combo_building1.get()=="G - Machine Shop" :
                self.Stair_Combo1.config(value=self.G_Stair_list)
                self.Stair_Combo1.current(0)

            if self.Combo_building1.get()=="H - อาคารศิลป์" :
                self.Stair_Combo1.config(value=self.H_Stair_list)
                self.Stair_Combo1.current(0)

            if self.Combo_building1.get()=="I - ศูนย์กีฬา" :
                self.Stair_Combo1.config(value=self.I_Stair_list)
                self.Stair_Combo1.current(0)
            

    # Place 2
    def Buildings2(self,event=""):
            if self.Combo_building2.get()=="A - ตึกเรียน" :
                self.Stair_Combo2.config(value=self.A_Stair_list) 
                self.Stair_Combo2.current(0)

            if self.Combo_building2.get()=="B - ตึกวิทยาศาสตร์"  :
                self.Stair_Combo2.config(value=self.B_Stair_list)
                self.Stair_Combo2.current(0)

            if self.Combo_building2.get()=="C - หอสมุดและแหล่งการเรียนรุ้" :
                self.Stair_Combo2.config(value=self.C_Stair_list)
                self.Stair_Combo2.current(0)

            if self.Combo_building2.get()=="D - ห้องคุณธรรม" :
                self.Stair_Combo2.config(value=self.D_Stair_list)
                self.Stair_Combo2.current(0)
            
            if self.Combo_building2.get()=="E - ห้องเขียนแบบ" :
                self.Stair_Combo2.config(value=self.E_Stair_list)
                self.Stair_Combo2.current(0)

            if self.Combo_building2.get()=="F - Stem - lab" :
                self.Stair_Combo2.config(value=self.F_Stair_list)
                self.Stair_Combo2.current(0)

            if self.Combo_building2.get()=="G - Machine Shop" :
                self.Stair_Combo2.config(value=self.G_Stair_list)
                self.Stair_Combo2.current(0)

            if self.Combo_building2.get()=="H - อาคารศิลป์" :
                self.Stair_Combo2.config(value=self.H_Stair_list)
                self.Stair_Combo2.current(0)

            if self.Combo_building2.get()=="I - ศูนย์กีฬา" :
                self.Stair_Combo2.config(value=self.I_Stair_list)
                self.Stair_Combo2.current(0)

    def Stair(self,event=""):
            if self.Combo_building1.get()=="A - ตึกเรียน" and self.Stair_Combo1.get()=="1" or "2" or "3" or "4" :
                self.Room_Combo1.config(value=self.A_Room_list)
                self.Room_Combo1.current(0)

            if self.Combo_building1.get()=="B - ตึกวิทยาศาสตร์" and self.Stair_Combo1.get()=="1" or "2" or "3"  :
                self.Room_Combo1.config(value=self.B_Room_list)
                self.Room_Combo1.current(0)

            if self.Combo_building1.get()=="C - หอสมุดและแหล่งการเรียนรุ้" and self.Stair_Combo1.get()=="1" :
                self.Room_Combo1.config(value=self.C_Room_list1)
                self.Room_Combo1.current(0)

            if self.Combo_building1.get()=="C - หอสมุดและแหล่งการเรียนรุ้" and self.Stair_Combo1.get()=="2" :
                self.Room_Combo1.config(value=self.C_Room_list2)
                self.Room_Combo1.current(0)

            if self.Combo_building1.get()=="C - หอสมุดและแหล่งการเรียนรุ้" and self.Stair_Combo1.get()=="3" :
                self.Room_Combo1.config(value=self.C_Room_list3)
                self.Room_Combo1.current(0)

            if self.Combo_building1.get()=="D - ห้องคุณธรรม" and self.Stair_Combo1.get()=="1"  :
                self.Room_Combo1.config(value=self.D_Room_list)
                self.Room_Combo1.current(0)

            if self.Combo_building1.get()=="E - ห้องเขียนแบบ" and self.Stair_Combo1.get()=="1" :
                self.Room_Combo1.config(value=self.E_Room_list)
                self.Room_Combo1.current(0)

            if self.Combo_building1.get()=="F - Stem - lab" and self.Stair_Combo1.get()=="1" :
                self.Room_Combo1.config(value=self.F_Room_list)
                self.Room_Combo1.current(0)

            if self.Combo_building1.get()=="G - Machine Shop" and self.Stair_Combo1.get()=="1" :
                self.Room_Combo1.config(value=self.G_Room_list)
                self.Room_Combo1.current(0)

            if self.Combo_building1.get()=="H - อาคารศิลป์" and self.Stair_Combo1.get()=="1" :
                self.Room_Combo1.config(value=self.H_Room_list)
                self.Room_Combo1.current(0)

            if self.Combo_building1.get()=="I - ศูนย์กีฬา" and self.Stair_Combo1.get()=="1" :
                self.Room_Combo1.config(value=self.I_Room_list1)
                self.Room_Combo1.current(0)

            if self.Combo_building1.get()=="I - ศูนย์กีฬา" and self.Stair_Combo1.get()=="2" :
                self.Room_Combo1.config(value=self.I_Room_list2)
                self.Room_Combo1.current(0)

            if self.Combo_building1.get()=="I - ศูนย์กีฬา" and self.Stair_Combo1.get()=="3" :
                self.Room_Combo1.config(value=self.I_Room_list3)
                self.Room_Combo1.current(0)


            # Place 2
    def Stair2(self,event=""):
            if self.Combo_building2.get()=="A - ตึกเรียน" and self.Stair_Combo2.get()=="1" or "2" or "3" or "4" :
                self.Room_Combo2.config(value=self.A_Room_list)
                self.Room_Combo2.current(0)

            if self.Combo_building2.get()=="B - ตึกวิทยาศาสตร์" and self.Stair_Combo2.get()=="1" or "2" or "3"  :
                self.Room_Combo2.config(value=self.B_Room_list)
                self.Room_Combo2.current(0)

            if self.Combo_building2.get()=="C - หอสมุดและแหล่งการเรียนรุ้" and self.Stair_Combo2.get()=="1" :
                self.Room_Combo2.config(value=self.C_Room_list1)
                self.Room_Combo2.current(0)

            if self.Combo_building2.get()=="C - หอสมุดและแหล่งการเรียนรุ้" and self.Stair_Combo2.get()=="2" :
                self.Room_Combo2.config(value=self.C_Room_list2)
                self.Room_Combo2.current(0)

            if self.Combo_building2.get()=="C - หอสมุดและแหล่งการเรียนรุ้" and self.Stair_Combo2.get()=="3" :
                self.Room_Combo2.config(value=self.C_Room_list3)
                self.Room_Combo2.current(0)

            if self.Combo_building2.get()=="D - ห้องคุณธรรม" and self.Stair_Combo2.get()=="1"  :
                self.Room_Combo2.config(value=self.D_Room_list)
                self.Room_Combo2.current(0)

            if self.Combo_building2.get()=="E - ห้องเขียนแบบ" and self.Stair_Combo2.get()=="1" :
                self.Room_Combo2.config(value=self.E_Room_list)
                self.Room_Combo2.current(0)

            if self.Combo_building2.get()=="F - Stem - lab" and self.Stair_Combo2.get()=="1" :
                self.Room_Combo2.config(value=self.F_Room_list)
                self.Room_Combo2.current(0)

            if self.Combo_building2.get()=="G - Machine Shop" and self.Stair_Combo2.get()=="1" :
                self.Room_Combo2.config(value=self.G_Room_list)
                self.Room_Combo2.current(0)

            if self.Combo_building2.get()=="H - อาคารศิลป์" and self.Stair_Combo2.get()=="1" :
                self.Room_Combo2.config(value=self.H_Room_list)
                self.Room_Combo2.current(0)

            if self.Combo_building2.get()=="I - ศูนย์กีฬา" and self.Stair_Combo2.get()=="1" :
                self.Room_Combo2.config(value=self.I_Room_list1)
                self.Room_Combo2.current(0)

            if self.Combo_building2.get()=="I - ศูนย์กีฬา" and self.Stair_Combo2.get()=="2" :
                self.Room_Combo2.config(value=self.I_Room_list2)
                self.Room_Combo2.current(0)

            if self.Combo_building2.get()=="I - ศูนย์กีฬา" and self.Stair_Combo2.get()=="3" :
                self.Room_Combo2.config(value=self.I_Room_list3)
                self.Room_Combo2.current(0)

    def calculate(self,event="") :
            # Place

            if self.Combo_building1.get()== "A - ตึกเรียน" and self.Combo_building2.get()=="A - ตึกเรียน" :
                S_buiding = 0
                T_buiding = 0
            if self.Combo_building1.get()== "A - ตึกเรียน" and self.Combo_building2.get()=="B - ตึกวิทยาศาสตร์" :
                S_buiding = 28
                T_buiding = 39.32
            if self.Combo_building1.get()== "A - ตึกเรียน" and self.Combo_building2.get()=="C - หอสมุดและแหล่งการเรียนรุ้" :
                S_buiding = 118.8
                T_buiding = 40
            if self.Combo_building1.get()== "A - ตึกเรียน" and self.Combo_building2.get()== "D - ห้องคุณธรรม" :
                S_buiding = 123.9
                T_buiding = 40
            if self.Combo_building1.get() == "A - ตึกเรียน" and self.Combo_building2.get()== "E - ห้องเขียนแบบ" :
                S_buiding = 142.7
                T_buiding = 50
            if self.Combo_building1.get()== "A - ตึกเรียน" and self.Combo_building2.get()== "F - Stem - lab" :
                S_buiding = 157.3
                T_buiding = 55
            if self.Combo_building1.get()== "A - ตึกเรียน" and self.Combo_building2.get()== "G - Machine Shop" :
                S_buiding = 181.6
                T_buiding = 65
            if self.Combo_building1.get()== "A - ตึกเรียน" and self.Combo_building2.get() == "H - อาคารศิลป์" :
                S_buiding = 245.6
                T_buiding = 50
            if self.Combo_building1.get()== "A - ตึกเรียน" and self.Combo_building2.get()== "I - ศูนย์กีฬา" :
                S_buiding = 399
                T_buiding = 58
            if self.Combo_building1.get()== "B - ตึกวิทยาศาสตร์" and self.Combo_building2.get()== "A - ตึกเรียน" :
                S_buiding = 95
                T_buiding = 65
            if self.Combo_building1.get()== "B - ตึกวิทยาศาสตร์" and self.Combo_building2.get()== "B - ตึกวิทยาศาสตร์" :
                S_buiding = 0
                T_buiding = 0
            if self.Combo_building1.get()== "B - ตึกวิทยาศาสตร์" and self.Combo_building2.get()== "C - หอสมุดและแหล่งการเรียนรุ้" :
                S_buiding = 95
                T_buiding = 65
            if self.Combo_building1.get()== "B - ตึกวิทยาศาสตร์" and self.Combo_building2.get()== "D - ห้องคุณธรรม" :
                S_buiding = 87.9
                T_buiding = 54
            if self.Combo_building1.get()== "B - ตึกวิทยาศาสตร์" and self.Combo_building2.get()== "E - ห้องเขียนแบบ" :
                S_buiding = 35
                T_buiding = 12
            if self.Combo_building1.get()== "B - ตึกวิทยาศาสตร์" and self.Combo_building2.get()== "F - Stem - lab" :
                S_buiding = 61
                T_buiding = 54
            if self.Combo_building1.get()== "B - ตึกวิทยาศาสตร์" and self.Combo_building2.get()== "G - Machine Shop" :
                S_buiding = 64
                T_buiding = 84
            if self.Combo_building1.get()== "B - ตึกวิทยาศาสตร์" and self.Combo_building2.get()== "H - อาคารศิลป์" :
                S_buiding = 64
                T_buiding = 21
            if self.Combo_building1.get()== "B - ตึกวิทยาศาสตร์" and self.Combo_building2.get()== "I - ศูนย์กีฬา" :
                S_buiding = 365
                T_buiding = 32
            if self.Combo_building1.get()== "C - หอสมุดและแหล่งการเรียนรุ้" and self.Combo_building2.get()== "A - ตึกเรียน" :
                S_buiding = 123
                T_buiding = 32
            if self.Combo_building1.get()== "C - หอสมุดและแหล่งการเรียนรุ้" and self.Combo_building2.get()== "B - ตึกวิทยาศาสตร์" :
                S_buiding = 123
                T_buiding = 32
            if self.Combo_building1.get()== "C - หอสมุดและแหล่งการเรียนรุ้" and self.Combo_building2.get()== "C - หอสมุดและแหล่งการเรียนรุ้" :
                S_buiding = 0
                T_buiding = 0
            if self.Combo_building1.get()== "C - หอสมุดและแหล่งการเรียนรุ้" and self.Combo_building2.get()== "D - ห้องคุณธรรม" :
                S_buiding = 123
                T_buiding = 32
            if self.Combo_building1.get()== "C - หอสมุดและแหล่งการเรียนรุ้" and self.Combo_building2.get()== "E - ห้องเขียนแบบ" :
                S_buiding = 234
                T_buiding = 21
            if self.Combo_building1.get()== "C - หอสมุดและแหล่งการเรียนรุ้" and self.Combo_building2.get()== "F - Stem - lab" :
                S_buiding = 465
                T_buiding = 22
            if self.Combo_building1.get()== "C - หอสมุดและแหล่งการเรียนรุ้" and self.Combo_building2.get()== "G - Machine Shop" :
                S_buiding = 134
                T_buiding = 67
            if self.Combo_building1.get()== "C - หอสมุดและแหล่งการเรียนรุ้" and self.Combo_building2.get()== "H - อาคารศิลป์" :
                S_buiding = 100
                T_buiding = 50
            if self.Combo_building1.get()== "C - หอสมุดและแหล่งการเรียนรุ้" and self.Combo_building2.get()== "I - ศูนย์กีฬา" :
                S_buiding = 100
                T_buiding = 50
            if self.Combo_building1.get()== "D - ห้องคุณธรรม" and self.Combo_building2.get()== "A - ตึกเรียน" :
                S_buiding = 100
                T_buiding = 50
            if self.Combo_building1.get()== "D - ห้องคุณธรรม" and self.Combo_building2.get()== "B - ตึกวิทยาศาสตร์" :
                S_buiding = 100
                T_buiding = 50
            if self.Combo_building1.get()== "D - ห้องคุณธรรม" and self.Combo_building2.get()== "C - หอสมุดและแหล่งการเรียนรุ้" :
                S_buiding = 100
                T_buiding = 50
            if self.Combo_building1.get()== "D - ห้องคุณธรรม" and self.Combo_building2.get()== "D - ห้องคุณธรรม" :
                S_buiding = 0
                T_buiding = 0
            if self.Combo_building1.get()== "D - ห้องคุณธรรม" and self.Combo_building2.get()== "E - ห้องเขียนแบบ" :
                S_buiding = 100
                T_buiding = 50
            if self.Combo_building1.get()== "D - ห้องคุณธรรม" and self.Combo_building2.get()== "F - Stem - lab" :
                S_buiding = 100
                T_buiding = 50
            if self.Combo_building1.get()== "D - ห้องคุณธรรม" and self.Combo_building2.get()== "G - Machine Shop" :
                S_buiding = 100
                T_buiding = 50
            if self.Combo_building1.get()== "D - ห้องคุณธรรม" and self.Combo_building2.get()== "H - อาคารศิลป์" :
                S_buiding = 100
                T_buiding = 50
            if self.Combo_building1.get()== "D - ห้องคุณธรรม" and self.Combo_building2.get()== "I - ศูนย์กีฬา" :
                S_buiding = 100
                T_buiding = 50
            if self.Combo_building1.get()== "E - ห้องเขียนแบบ" and self.Combo_building2.get()== "A - ตึกเรียน" :
                S_buiding = 100
                T_buiding = 50
            if self.Combo_building1.get()== "E - ห้องเขียนแบบ" and self.Combo_building2.get()== "B - ตึกวิทยาศาสตร์" :
                S_buiding = 100
                T_buiding = 50
            if self.Combo_building1.get()== "E - ห้องเขียนแบบ" and self.Combo_building2.get()== "C - หอสมุดและแหล่งการเรียนรุ้" :
                S_buiding = 100
                T_buiding = 50
            if self.Combo_building1.get()== "E - ห้องเขียนแบบ" and self.Combo_building2.get()== "D - ห้องคุณธรรม" :
                S_buiding = 100
                T_buiding = 50
            if self.Combo_building1.get()== "E - ห้องเขียนแบบ" and self.Combo_building1.get()== "E - ห้องเขียนแบบ" :
                S_buiding = 0
                T_buiding = 0
            if self.Combo_building1.get()== "E - ห้องเขียนแบบ" and self.Combo_building2.get()== "F - Stem - lab" :
                S_buiding = 100
                T_buiding = 50
            if self.Combo_building1.get()== "E - ห้องเขียนแบบ" and self.Combo_building2.get()== "G - Machine Shop" :
                S_buiding = 100
                T_buiding = 50
            if self.Combo_building1.get()== "E - ห้องเขียนแบบ" and self.Combo_building2.get()== "H - อาคารศิลป์" :
                S_buiding = 100
                T_buiding = 50
            if self.Combo_building1.get()== "E - ห้องเขียนแบบ" and self.Combo_building2.get()== "I - ศูนย์กีฬา" :
                S_buiding = 100
                T_buiding = 50
            if self.Combo_building1.get()== "F - Stem - lab" and self.Combo_building2.get()== "A - ตึกเรียน" :
                S_buiding = 254
                T_buiding = 68
            if self.Combo_building1.get()== "F - Stem - lab" and self.Combo_building2.get()== "B - ตึกวิทยาศาสตร์" :
                S_buiding = 254
                T_buiding = 68
            if self.Combo_building1.get()== "F - Stem - lab" and self.Combo_building2.get()== "C - หอสมุดและแหล่งการเรียนรุ้" :
                S_buiding = 254
                T_buiding = 68
            if self.Combo_building1.get()== "F - Stem - lab" and self.Combo_building2.get()== "D - ห้องคุณธรรม" :
                S_buiding = 254
                T_buiding = 68
            if self.Combo_building1.get()== "F - Stem - lab" and self.Combo_building2.get()== "E - ห้องเขียนแบบ" :
                S_buiding = 254
                T_buiding = 68
            if self.Combo_building1.get()== "F - Stem - lab" and self.Combo_building2.get()== "F - Stem - lab" :
                S_buiding = 0
                T_buiding = 0
            if self.Combo_building1.get()== "F - Stem - lab" and self.Combo_building2.get()== "G - Machine Shop" :
                S_buiding = 254
                T_buiding = 68
            if self.Combo_building1.get()== "F - Stem - lab" and self.Combo_building2.get()== "H - อาคารศิลป์" :
                S_buiding = 54
                T_buiding = 51
            if self.Combo_building1.get()== "F - Stem - lab" and self.Combo_building2.get()== "I - ศูนย์กีฬา" :
                S_buiding = 236
                T_buiding = 54
            if self.Combo_building1.get()== "G - Machine Shop" and self.Combo_building2.get()== "A - ตึกเรียน" :
                S_buiding = 84
                T_buiding = 65
            if self.Combo_building1.get()== "G - Machine Shop" and self.Combo_building2.get()== "B - ตึกวิทยาศาสตร์" :
                S_buiding = 84
                T_buiding = 65
            if self.Combo_building1.get()== "G - Machine Shop" and self.Combo_building2.get()== "C - หอสมุดและแหล่งการเรียนรุ้" :
                S_buiding = 84
                T_buiding = 65
            if self.Combo_building1.get()== "G - Machine Shop" and self.Combo_building2.get()== "D - ห้องคุณธรรม" :
                S_buiding = 84
                T_buiding = 65
            if self.Combo_building1.get()== "G - Machine Shop" and self.Combo_building2.get()== "E - ห้องเขียนแบบ" :
                S_buiding = 84
                T_buiding = 65
            if self.Combo_building1.get()== "G - Machine Shop" and self.Combo_building2.get()== "F - Stem - lab" :
                S_buiding = 84
                T_buiding = 65
            if self.Combo_building1.get()== "G - Machine Shop" and self.Combo_building2.get()== "G - Machine Shop" :
                S_buiding = 0
                T_buiding = 0
            if self.Combo_building1.get()== "G - Machine Shop" and self.Combo_building2.get()== "H - อาคารศิลป์" :
                S_buiding = 84
                T_buiding = 65
            if self.Combo_building1.get()== "G - Machine Shop" and self.Combo_building2.get()== "I - ศูนย์กีฬา" :
                S_buiding = 20
                T_buiding = 50
            if self.Combo_building1.get()== "H - อาคารศิลป์" and self.Combo_building2.get()== "A - ตึกเรียน" :
                S_buiding = 50
                T_buiding = 40
            if self.Combo_building1.get()== "H - อาคารศิลป์" and self.Combo_building2.get()== "B - ตึกวิทยาศาสตร์" :
                S_buiding = 50
                T_buiding = 40
            if self.Combo_building1.get()== "H - อาคารศิลป์" and self.Combo_building2.get()== "C - หอสมุดและแหล่งการเรียนรุ้" :
                S_buiding = 50
                T_buiding = 40
            if self.Combo_building1.get()== "H - อาคารศิลป์" and self.Combo_building1.get()== "D - ห้องคุณธรรม" :
                S_buiding = 50
                T_buiding = 40
            if self.Combo_building1.get()== "H - อาคารศิลป์" and self.Combo_building1.get()== "E - ห้องเขียนแบบ" :
                S_buiding = 50
                T_buiding = 40
            if self.Combo_building1.get()== "H - อาคารศิลป์" and self.Combo_building2.get()== "F - Stem - lab" :
                S_buiding = 50
                T_buiding = 40
            if self.Combo_building1.get()== "H - อาคารศิลป์" and self.Combo_building2.get()== "G - Machine Shop" :
                S_buiding = 50
                T_buiding = 40
            if self.Combo_building1.get()== "H - อาคารศิลป์" and self.Combo_building2.get()== "H - อาคารศิลป์" :
                S_buiding = 0
                T_buiding = 0
            if self.Combo_building1.get()== "H - อาคารศิลป์" and self.Combo_building2.get()== "I - ศูนย์กีฬา" :
                S_buiding = 50
                T_buiding = 40
            if self.Combo_building1.get()== "I - ศูนย์กีฬา" and self.Combo_building2.get()== "A - ตึกเรียน" :
                S_buiding = 50
                T_buiding = 40
            if self.Combo_building1.get()== "I - ศูนย์กีฬา" and self.Combo_building2.get()== "B - ตึกวิทยาศาสตร์" :
                S_buiding = 50
                T_buiding = 40
            if self.Combo_building1.get()== "I - ศูนย์กีฬา" and self.Combo_building2.get()== "C - หอสมุดและแหล่งการเรียนรุ้" :
                S_buiding = 50
                T_buiding = 40
            if self.Combo_building1.get()== "I - ศูนย์กีฬา" and self.Combo_building2.get()== "D - ห้องคุณธรรม" :
                S_buiding = 50
                T_buiding = 40
            if self.Combo_building1.get()== "I - ศูนย์กีฬา" and self.Combo_building2.get()== "E - ห้องเขียนแบบ" :
                S_buiding = 50
                T_buiding = 40
            if self.Combo_building1.get()== "I - ศูนย์กีฬา" and self.Combo_building2.get()== "F - Stem - lab" :
                S_buiding = 50
                T_buiding = 40
            if self.Combo_building1.get()== "I - ศูนย์กีฬา" and self.Combo_building2.get()== "G - Machine Shop" :
                S_buiding = 50
                T_buiding = 40
            if self.Combo_building1.get()== "I - ศูนย์กีฬา" and self.Combo_building2.get()== "H - อาคารศิลป์" :
                S_buiding = 0
                T_buiding = 0
            
            if self.Combo_building1.get()== "I - ศูนย์กีฬา" and self.Combo_building2.get()== "I - ศูนย์กีฬา" :
                S_buiding = 0
                T_buiding = 0

            print("S_buiding :" ,  S_buiding , "m")
            print("T_buiding : " , T_buiding , "s")


            t_Stair = 42.3
            MS_Stair = 20
            if str(self.Combo_building1.get()) == str(self.Combo_building1.get()) :
                S_Stair = math.fabs((int(self.Stair_Combo1.get())-1) - (int(self.Stair_Combo2.get())-1))
                T_Stair = S_Stair * t_Stair
                SS_Stair = MS_Stair * S_Stair
            else :
                S_Stair = math.fabs((int(self.Stair_Combo1.get())-1) + (int(self.Stair_Combo2.get())-1))
                T_Stair = S_Stair * t_Stair
                SS_Stair = MS_Stair * S_Stair

            print("SS_Stair : " , SS_Stair ,"m")
            print("T_Stair : " ,  T_Stair ,"s")


            t_Room = 10.06
            MS_Room = 8
            if str(self.Combo_building1.get()) == str(self.Combo_building1.get()) :
                S_Room = math.fabs(int(self.Room_Combo1.get()) - int(self.Room_Combo2.get()))
                T_Room = S_Room * t_Room
                SS_Room = MS_Room * S_Room
            else :
                S_Room = math.fabs(int(self.Room_Combo1.get()) + int(self.Room_Combo2.get()))
                T_Room = S_Room * t_Room
                SS_Room = MS_Room * S_Room

            print("SS_Room : " , SS_Room , "m")
            print("T_Room : " , T_Room , "s")

            sum_distance = S_buiding + SS_Stair + SS_Room
            sum_time = T_buiding + T_Stair + T_Room

            print("sum_distance : " , "{:.2f}".format(sum_distance) , "m" )
            print("sum_time : " , "{:.2f}".format(sum_time) , "s" )
            self.Tim_Enty.insert(0,sum_time)
            self.Dis_Enty.insert(0,sum_distance)

    def enter_data(self):
            self.m=self.Distance.get()
            self.n=self.Times.get() 
            self.l.append(self.m)
            self.i.append(self.n)
            

            if self.room1.get()== "" or self.room2.get()== "" :
                messagebox.showerror("Error", "Plaese Select Classroom")

            elif self.room1.get()== "1"or"2"or'3'or'4'or'5'or'6'or'7'or'8'or'9' and self.room2.get()=='1'or'2'or'3'or'4'or'5'or'6'or'7'or'8'or'9' :
                self.textarea.insert(END,f"\n {self.Combo_building1.get()}\t{self.Stair_Combo1.get()}\t{self.Room_Combo1.get()}")
                self.textarea.insert(END,f"\n {self.Combo_building2.get()}\t{self.Stair_Combo2.get()}\t{self.Room_Combo2.get()}\t\t{self.m}\t\t{self.n}")
                self.Combo_building1.set(self.Combo_building2.get())
                self.Stair_Combo1.set(self.Stair_Combo2.get())
                self.Room_Combo1.set(self.Room_Combo2.get())
                self.total_Distance.set(str(sum(self.l)))
                self.total_Times.set(str(sum(self.i)))
                self.Distance.set(0)
                self.Times.set(0)

    def Stop(self):
            self.textarea.insert(END,"\n\n ====================== Break =======================")
            self.textarea.insert(END,"\n")
    
    def save(self):
            op=messagebox.askyesno("Save Result", "Do you want to save the Result")
            if op>0:
                self.Result_data=self.textarea.get(1.0,END)
                f1=open('calculate/'+ (self.Combo_Class.get()) +"_"+ (self.Combo_Day.get()) + ".txt",'w')
                f1.write(self.Result_data)
                op=messagebox.showinfo("Saved",f"Result : {self.Combo_Class.get()} {self.Combo_Day.get()} saved successfully")
                f1.close()

    def create(self):

            if self.total_Distance.get()=="" and self.total_Times.get()=="":
                messagebox.showerror("Error", "Plaese Select Classroom")
            else :
                text=self.textarea.get(10.0,(10.0+float(len(self.l))))
                self.textarea.insert(END,"\n ===============================================")
                self.textarea.insert(END,f"\n Total Distance (m) : \t\t\t\t{sum(self.l)}")
                self.textarea.insert(END,f"\n Total Times (s) : \t\t\t\t{sum(self.i)}")
                self.textarea.insert(END,f"\n ==============================================")



    def open(self):
            filepath = filedialog.askopenfilename(initialdir="C:\\Users\\Lenovo\\Desktop\\Programmer\\Sum_Distance_time\\calculate")
            file = open(filepath,'r')
            self.textarea.delete(0.0,END)
            self.textarea.insert(END,f" {file.read()}")
            self.m=self.Distance.get()
            self.n=self.Times.get() 
            self.l.append(self.m)
            self.i.append(self.n)
            self.x=(sum(self.l))
            self.y=(sum(self.i))
            self.total_Distance.set('Rs.%.2f' % float(self.x))
            self.total_Times.set('Rs.%.2f' % float(self.y))
            for i in os.listdir("calculate/"):
                    if  i.split('_')[0]==("M.1-1"):
                        self.Combo_Class.set("M.1-1")
                    if i.split('_')[0]==("M.1-2"):
                        self.Combo_Class.set("M.1-2")
                    if i.split('_')[0]==("M.1-3"):
                        self.Combo_Class.set("M.1-3")
                    if i.split('_')[0]==("M.1-4"):
                        self.Combo_Class.set("M.1-4")
                    if i.split('_')[0]==("M.2-1"):
                        self.Combo_Class.set("M.2-1")
                    if i.split('_')[0]==("M.2-2"):
                        self.Combo_Class.set("M.2-2")
                    if i.split('_')[0]==("M.2-3"):
                        self.Combo_Class.set("M.2-3")
                    if i.split('_')[0]==("M.2-4"):
                        self.Combo_Class.set("M.2-4")
                    if i.split('_')[0]==("M.3-1"):
                        self.Combo_Class.set("M.3-1")
                    if i.split('_')[0]==("M.3-2"):
                        self.Combo_Class.set("M.3-2")
                    if i.split('_')[0]==("M.3-3"):
                        self.Combo_Class.set("M.3-3")
                    if i.split('_')[0]==("M.3-4"):
                        self.Combo_Class.set("M.3-4")
                    if i.split('_')[0]==("M.4-1"):
                        self.Combo_Class.set("M.4-1")
                    if i.split('_')[0]==("M.4-2"):
                        self.Combo_Class.set("M.4-2")
                    if i.split('_')[0]==("M.4-3"):
                        self.Combo_Class.set("M.4-3")
                    if i.split('_')[0]==("M.4-4"):
                        self.Combo_Class.set("M.4-4")
                    if i.split('_')[0]==("M.4-5"):
                        self.Combo_Class.set("M.4-5")
                    if i.split('_')[0]==("M.4-6"):
                        self.Combo_Class.set("M.4-6")
                    if i.split('_')[0]==("M.5-1"):
                        self.Combo_Class.set("M.5-1")
                    if i.split('_')[0]==("M.5-2"):
                        self.Combo_Class.set("M.5-2")
                    if i.split('_')[0]==("M.5-3"):
                        self.Combo_Class.set("M.5-3")
                    if i.split('_')[0]==("M.5-4"):
                        self.Combo_Class.set("M.5-4")
                    if i.split('_')[0]==("M.5-5"):
                        self.Combo_Class.set("M.5-5")
                    if i.split('_')[0]==("M.5-6"):
                        self.Combo_Class.set("M.5-6")
                    if i.split('_')[0]==("M.6-1"):
                        self.Combo_Class.set("M.6-1")
                    if i.split('_')[0]==("M.6-2"):
                        self.Combo_Class.set("M.6-2")
                    if i.split('_')[0]==("M.6-3"):
                        self.Combo_Class.set("M.6-3")
                    if i.split('_')[0]==("M.6-4"):
                        self.Combo_Class.set("M.6-4")
                    if i.split('_')[0]==("M.6-5"):
                        self.Combo_Class.set("M.6-5")
                    if i.split('_')[0]==("M.6-6"):
                        self.Combo_Class.set("M.6-6")

            for i in os.listdir("calculate/"):
                    if i.split('_')[1]==("Monday"):
                        self.Combo_Day.set("Monday")
                    if i.split('_')[1]==("Tuesday"):
                        self.Combo_Day.set("Tuesday")
                    if i.split('_')[1]==(" Wednesday"):
                        self.Combo_Day.set(" Wednesday")
                    if i.split('_')[1]==("Thursday"):
                        self.Combo_Day.set("Thursday")
                    if i.split('_')[1]==("Friday"):
                        self.Combo_Day.set("Friday")


    def delete(self):
            self.textarea.delete(1.0,END)
            self.Combo_building1.current(0)
            self.Stair_Combo1.set("")
            self.Room_Combo1.set("")
            self.Combo_building2.current(0)
            self.Stair_Combo2.set("")
            self.Room_Combo2.set("")
            self.Distance.set(0)
            self.Times.set(0)
            self.welcome()

    def clear(self):
            self.textarea.delete(1.0,END)
            self.l.clear()
            self.i.clear()
            self.total_Distance.set(0)
            self.total_Times.set(0)
            self.Combo_building1.current(0)
            self.Stair_Combo1.set("")
            self.Room_Combo1.set("")
            self.Combo_building2.current(0)
            self.Stair_Combo2.set("")
            self.Room_Combo2.set("")
            self.Distance.set(0)
            self.Times.set(0)
            self.welcome()

    def enterSDdis(self):
            self.x = self.SDWeekDis.get()
            self.a.append(self.x)
            self.EntySDDis.insert(0, f",{self.x}")
            self.EntyweekDIS.delete(0,END)


    def enterSDtim(self):
            self.y = self.SDWeekTim.get()
            self.b.append(self.y)
            self.EntySDTim.insert(0, f",{self.y}")
            self.EntyweekTIM.delete(0,END)


    def calculateSD_DISTANCE(self):
            SD_DISTANCE = [float(value) for value in self.a]
            self.SDDIS = stdev(SD_DISTANCE)
            self.EntySDDis.insert(0,self.SDDIS)

    def calculateSD_TIMES(self):
            SD_TIMES = [float(value) for value in self.b]
            self.SDTIM = stdev(SD_TIMES)
            self.EntySDTim.insert(0,self.SDTIM)

    def clearSD(self):
            self.EntySDDis.delete(0,END)
            self.EntySDTim.delete(0,END)

    

    
            

    


            
















if __name__ == '__main__':
    root=Tk()
    obj=Calculate_App(root)
    root.mainloop()