import tkinter
import tkinter.messagebox #for message dialogue boxes
from tkinter import *

import emsBLLWithDataBase
from emsBLLWithDataBase import *

class Form(Frame):  # creating a frame class which inherits from built-in Frame class
    def __init__(self,master=None):

        super().__init__(master)
        self.pack(expand=True)
        self.createWidget()

    def addBtn_click(self):
        try:
            if(self.type.get()==1):
                self.dir=Director()
                self.dir.id=self.varId.get()
                self.dir.name=self.varName.get()
                self.dir.type="d"
                self.dir.special=self.varDirSpecial.get()
                self.dir.sal=self.varDirSalary.get()
                self.dir.add()

            elif(self.type.get()==2):
                self.mgr=Manager()
                self.mgr.id=self.varId.get()
                self.mgr.name=self.varName.get()
                self.mgr.type="m"
                self.mgr.special=self.varMgrSpecial.get()
                self.mgr.sal=self.varMgrSalary.get()
                self.mgr.add()

            else:
                self.tt = TT()
                self.tt.id = self.varId.get()
                self.tt.name = self.varName.get()
                self.tt.type = "t"
                self.tt.special = self.varTTSpecial.get()
                self.tt.sal = self.varTTSalary.get()
                self.tt.add()

            print(tkinter.messagebox.showinfo("Action Info","Employee added successfully!!"))


        except Exception as ex:
            tkinter.messagebox.showerror("Error",ex)

    def btn_click_topSearch(self):
        try:
            self.obj=Employee.checkId(self.searchId.get())
            if(self.obj==-1):
                raise Exception("Id not found!")
            self.obj.search(self.searchId.get())
            self.top=Toplevel(self)
            self.top.title("Details Page")
            self.top.geometry("200x100")
            self.top.text=Text(self.top)
            self.top.text.insert(END,"Id found with\n\tName: "+self.obj.name+"\n\tType: "+self.obj.type+"\n\tSpecial: "+self.obj.special+"\n\tSalary: %s"%self.obj.sal)
            self.top.text.grid()
            self.top.mainloop()
        except Exception as ex:
            tkinter.messagebox.showerror("Error",ex)

    def searchBtn_click(self):
        try:
            self.topSearch=Toplevel(self)
            self.topSearch.labelIdSearch=Label(self.topSearch,text="Enter Id to be searched:")
            self.topSearch.labelIdSearch.grid(row=0,column=0,columnspan=4)
            self.topSearch.varIdSearch=IntVar()
            self.topSearch.varIdSearch.set("0")
            self.searchId=self.topSearch.varIdSearch
            self.topSearch.entryIdSearch=Entry(self.topSearch,textvariable=self.topSearch.varIdSearch)
            self.topSearch.entryIdSearch.grid(row=0,column=4,columnspan=4)
            Button(self.topSearch,text="Search",command=self.btn_click_topSearch).grid(row=2,column=3,columnspan=2)

        except Exception as ex:
            tkinter.messagebox.showerror("Error",ex)

    def btn_click_topUpdate(self):
        try:
            self.obj=Employee.checkId(self.updateId.get())
            if(self.obj==-1):
                raise Exception("Id not found!")
            self.obNew = Employee.checkId(self.updateId.get())
            self.obNew.search(self.updateId.get())
            if(len(self.sel)==3):
                self.obj.name=self.NewName.get()
                self.obj.sal=self.NewSal.get()
                self.obj.special=self.NewSpecial.get()

            elif(len(self.sel)==2):
                if(self.sel==(0,1)):
                    self.obj.name=self.NewName.get()
                    self.obj.sal=self.NewSal.get()
                    self.obj.special=self.obNew.special

                elif(self.sel==(0,2)):
                    self.obj.name=self.NewName.get()
                    self.obj.sal=self.obNew.sal
                    self.obj.special=self.NewSpecial.get()

                else:
                    self.obj.name=self.obNew.name
                    self.obj.sal=self.NewSal.get()
                    self.obj.special=self.NewSpecial.get()

            else:
                if(self.sel==(0,)):
                    self.obj.name=self.NewName.get()
                    self.obj.special=self.obNew.special
                    self.obj.sal=self.obNew.sal

                elif(self.sel==(1,)):
                    self.obj.name=self.obNew.name
                    self.obj.special=self.NewSpecial.get()
                    self.obj.sal=self.obNew.sal

                else:
                    self.obj.name=self.obNew.name
                    self.obj.special=self.obNew.special
                    self.obj.sal=self.NewSal.get()

            self.obj.update(self.updateId.get())

            tkinter.messagebox.showinfo("Action Info","Employee updated successfully!!")

        except Exception as ex:

            tkinter.messagebox.showerror("Error",ex)



    def topUpdateFunc(self,event):
        self.sel=[]
        self.sel=self.lbUpdate.curselection()
        if (len(self.sel )==3):
            Label(self.topUpdate, text="Enter new name:").grid(row=2, column=0, columnspan=4)
            self.NewName=StringVar()
            Entry(self.topUpdate,textvariable=self.NewName).grid(row=2,column=4,columnspan=4)
            Label(self.topUpdate, text="Enter new salary:").grid(row=3, column=0, columnspan=4)
            self.NewSal = IntVar()
            Entry(self.topUpdate, textvariable=self.NewSal).grid(row=3, column=4, columnspan=4)
            Label(self.topUpdate, text="Enter new special:").grid(row=4, column=0, columnspan=4)
            self.NewSpecial = StringVar()
            Entry(self.topUpdate, textvariable=self.NewSpecial).grid(row=4, column=4, columnspan=4)

        elif(len(self.sel)==2):
            if(self.sel==(0,1)):
                Label(self.topUpdate, text="Enter new name:").grid(row=2, column=0, columnspan=4)
                self.NewName = StringVar()
                Entry(self.topUpdate, textvariable=self.NewName).grid(row=2, column=4, columnspan=4)
                Label(self.topUpdate, text="Enter new salary:").grid(row=3, column=0, columnspan=4)
                self.NewSal = IntVar()
                Entry(self.topUpdate, textvariable=self.NewSal).grid(row=3, column=4, columnspan=4)
            elif(self.sel==(1,2)):
                Label(self.topUpdate, text="Enter new salary:").grid(row=2, column=0, columnspan=4)
                self.NewSal = IntVar()
                Entry(self.topUpdate, textvariable=self.NewSal).grid(row=2, column=4, columnspan=4)
                Label(self.topUpdate, text="Enter new special:").grid(row=3, column=0, columnspan=4)
                self.NewSpecial = StringVar()
                Entry(self.topUpdate, textvariable=self.NewSpecial).grid(row=3, column=4, columnspan=4)
            else:
                Label(self.topUpdate, text="Enter new name:").grid(row=2, column=0, columnspan=4)
                self.NewName = StringVar()
                Entry(self.topUpdate, textvariable=self.NewName).grid(row=2, column=4, columnspan=4)
                Label(self.topUpdate, text="Enter new special:").grid(row=3, column=0, columnspan=4)
                self.NewSpecial = StringVar()
                Entry(self.topUpdate, textvariable=self.NewSpecial).grid(row=3, column=4, columnspan=4)

        else:
            if(self.sel==(0,)):
                Label(self.topUpdate, text="Enter new name:").grid(row=2, column=0, columnspan=4)
                self.NewName = StringVar()
                Entry(self.topUpdate, textvariable=self.NewName).grid(row=2, column=4, columnspan=4)
            elif(self.sel==(1,)):
                Label(self.topUpdate, text="Enter new salary:").grid(row=2, column=0, columnspan=4)
                self.NewSal = IntVar()
                Entry(self.topUpdate, textvariable=self.NewSal).grid(row=2, column=4, columnspan=4)
            else:
                Label(self.topUpdate, text="Enter new special:").grid(row=2, column=0, columnspan=4)
                self.NewSpecial = StringVar()
                Entry(self.topUpdate, textvariable=self.NewSpecial).grid(row=2, column=4, columnspan=4)

    def updateBtn_click(self):
        try:
            self.topUpdate=Toplevel(self)
            self.topUpdate.labelIdUpdate=Label(self.topUpdate,text="Enter Id to be updated:")
            self.topUpdate.labelIdUpdate.grid(row=0,column=0,columnspan=4)
            self.topUpdate.varIdUpdate=IntVar()
            self.topUpdate.varIdUpdate.set("0")
            self.updateId=self.topUpdate.varIdUpdate
            self.topUpdate.entryIdUpdate=Entry(self.topUpdate,textvariable=self.topUpdate.varIdUpdate)
            self.topUpdate.entryIdUpdate.grid(row=0,column=4,columnspan=4)
            Label(self.topUpdate,text="Select fields to be updated:").grid(row=1,column=0,columnspan=4)
            self.OptionsUp=StringVar()
            self.OptionsUp.set("Name")
            self.lbUpdate=Listbox(self.topUpdate,listvariable=self.OptionsUp,selectmode=EXTENDED)
            self.lbUpdate.insert(END,"Salary")
            self.lbUpdate.insert(END, "Special")
            self.lbUpdate.bind("<Double-Button-1>",self.topUpdateFunc)
            self.lbUpdate.grid(row=1,column=4,columnspan=4)

            Button(self.topUpdate,text="Update",command=self.btn_click_topUpdate).grid(row=5,column=3,columnspan=2)

        except Exception as ex:
            tkinter.messagebox.showerror("Error",ex)

    def func_del(self):
        try:
            self.obj=Employee.checkId(self.delId.get())
            if(self.obj==-1):
                raise Exception("Id not found!")
            self.obj.delete(self.delId.get())
            tkinter.messagebox.showinfo("Action Info","Employee deleted successfully!!")

        except Exception as ex:
            tkinter.messagebox.showerror("Error",ex)

    def deleteBtn_click(self):
        self.topDel=Toplevel(self)
        Label(self.topDel,text="Enter Id to be deleted:").grid(row=0,column=0,columnspan=4)
        self.delId=IntVar()
        Entry(self.topDel,textvariable=self.delId).grid(row=0,column=4,columnspan=4)
        Button(self.topDel,text="Delete",command=self.func_del).grid(row=1,column=3,columnspan=2)

    def firstBtn_click(self):
        try:
            query="Select * from employee_info where id = (select min(id) from employee_info)"
            myCursor.execute(query)
            row=myCursor.fetchone()
            self.varId.set(row[0])
            self.varName.set(row[1])
            if(row[2]=="d"):
                self.type.set(1)
                self.radioFunc()
                query="select * from director where id = %s"
                myCursor.execute(query,(row[0]))
                row_dir=myCursor.fetchone()
                self.varDirSpecial.set(row_dir[1])
                self.varDirSalary.set(row_dir[2])
            elif(row[2]=="m"):
                self.type.set(2)
                self.radioFunc()
                query = "select * from manager where id = %s"
                myCursor.execute(query, (row[0]))
                row_mgr = myCursor.fetchone()
                self.varMgrSpecial.set(row_mgr[1])
                self.varMgrSalary.set(row_mgr[2])
            else:
                self.type.set(3)
                self.radioFunc()
                query = "select * from tt where id = %s"
                myCursor.execute(query, (row[0]))
                row_tt = myCursor.fetchone()
                self.varTTSpecial.set(row_tt[1])
                self.varTTSalary.set(row_tt[2])

        except Exception as ex:
            tkinter.messagebox.showerror("Error",ex)


    def lastBtn_click(self):
        try:
            query="Select * from employee_info where id = (select max(id) from employee_info)"
            myCursor.execute(query)
            row=myCursor.fetchone()
            self.varId.set(row[0])
            self.varName.set(row[1])
            if(row[2]=="d"):
                self.type.set(1)
                self.radioFunc()
                query="select * from director where id = %s"
                myCursor.execute(query,(row[0]))
                row_dir=myCursor.fetchone()
                self.varDirSpecial.set(row_dir[1])
                self.varDirSalary.set(row_dir[2])
            elif(row[2]=="m"):
                self.type.set(2)
                self.radioFunc()
                query = "select * from manager where id = %s"
                myCursor.execute(query, (row[0]))
                row_mgr = myCursor.fetchone()
                self.varMgrSpecial.set(row_mgr[1])
                self.varMgrSalary.set(row_mgr[2])
            else:
                self.type.set(3)
                self.radioFunc()
                query = "select * from tt where id = %s"
                myCursor.execute(query, (row[0]))
                row_tt = myCursor.fetchone()
                self.varTTSpecial.set(row_tt[1])
                self.varTTSalary.set(row_tt[2])

        except Exception as ex:
            tkinter.messagebox.showerror("Error",ex)

    def prevBtn_click(self):
        try:
            if(self.varId.get()==0):
                raise Exception("Please enter something!")
            self.obj=Employee.checkId(self.varId.get()-1)
            if(self.obj==-1):
                raise Exception("Id not found!")
            self.obj.search(self.varId.get()-1)
            self.varId.set(self.varId.get()-1)
            self.varName.set(self.obj.name)
            if(self.obj.type=="d"):
                self.type.set(1)
                self.radioFunc()
                self.varDirSpecial.set(self.obj.special)
                self.varDirSalary.set(self.obj.sal)
            elif(self.obj.type=="m"):
                self.type.set(2)
                self.radioFunc()
                self.varMgrSpecial.set(self.obj.special)
                self.varMgrSalary.set(self.obj.sal)
            else:
                self.type.set(3)
                self.radioFunc()
                self.varTTSpecial.set(self.obj.special)
                self.varTTSalary.set(self.obj.sal)

        except Exception as ex:
            tkinter.messagebox.showerror("Error",ex)

    def nextBtn_click(self):
        try:
            if(self.varId.get()==0):
                raise Exception("Please enter something!")
            self.obj=Employee.checkId(self.varId.get()+1)
            if(self.obj==-1):
                raise Exception("Id not found!")
            self.obj.search(self.varId.get()+1)
            self.varId.set(self.varId.get()+1)
            self.varName.set(self.obj.name)
            if(self.obj.type=="d"):
                self.type.set(1)
                self.radioFunc()
                self.varDirSpecial.set(self.obj.special)
                self.varDirSalary.set(self.obj.sal)
            elif(self.obj.type=="m"):
                self.type.set(2)
                self.radioFunc()
                self.varMgrSpecial.set(self.obj.special)
                self.varMgrSalary.set(self.obj.sal)
            else:
                self.type.set(3)
                self.radioFunc()
                self.varTTSpecial.set(self.obj.special)
                self.varTTSalary.set(self.obj.sal)

        except Exception as ex:
            tkinter.messagebox.showerror("Error",ex)


    def radioFunc(self):

        if(self.type.get()==1):

            self.dirSpecialLabel=Label(self,text="Enter Director Special:")
            self.dirSpecialLabel.grid(row=3,column=0,columnspan=4)

            self.varDirSpecial=StringVar()
            self.varDirSpecial.set("Enter_director_Special")
            self.dirSpecialEntry=Entry(self,textvariable=self.varDirSpecial)
            self.dirSpecialEntry.grid(row=3,column=4,columnspan=4)

            self.dirSalaryLabel = Label(self, text="Enter Director Salary:")
            self.dirSalaryLabel.grid(row=4, column=0, columnspan=4)

            self.varDirSalary = IntVar()
            self.varDirSalary.set(0)
            self.dirSalaryEntry = Entry(self, textvariable=self.varDirSalary)
            self.dirSalaryEntry.grid(row=4, column=4, columnspan=4)

        elif(self.type.get()==2):

                self.mgrSpecialLabel=Label(self,text="Enter Manager Special:")
                self.mgrSpecialLabel.grid(row=3,column=0,columnspan=4)

                self.varMgrSpecial=StringVar()
                self.varMgrSpecial.set("Enter_manager_Special")
                self.mgrSpecialEntry=Entry(self,textvariable=self.varMgrSpecial)
                self.mgrSpecialEntry.grid(row=3,column=4,columnspan=4)

                self.mgrSalaryLabel = Label(self, text="Enter Manager Salary:")
                self.mgrSalaryLabel.grid(row=4, column=0, columnspan=4)

                self.varMgrSalary = IntVar()
                self.varMgrSalary.set(0)
                self.mgrSalaryEntry = Entry(self, textvariable=self.varMgrSalary)
                self.mgrSalaryEntry.grid(row=4, column=4, columnspan=4)
        else:

            self.ttSpecialLabel = Label(self, text="Enter Trainee Special:")
            self.ttSpecialLabel.grid(row=3, column=0, columnspan=4)

            self.varTTSpecial = StringVar()
            self.varTTSpecial.set("Enter_tt_Special")
            self.ttSpecialEntry = Entry(self, textvariable=self.varTTSpecial)
            self.ttSpecialEntry.grid(row=3, column=4, columnspan=4)

            self.ttSalaryLabel = Label(self, text="Enter Trainee Salary:")
            self.ttSalaryLabel.grid(row=4, column=0, columnspan=4)

            self.varTTSalary = IntVar()
            self.varTTSalary.set(0)
            self.ttSalaryEntry = Entry(self, textvariable=self.varTTSalary)
            self.ttSalaryEntry.grid(row=4, column=4, columnspan=4)

    def createWidget(self):

        self.idLabel = Label(self, text="Employee Id:")
        self.idLabel.grid(row=0, column=0,columnspan=3)
        self.varId = IntVar()
        self.varId.set(0)
        self.idEntry = Entry(self, textvariable=self.varId)
        self.idEntry.grid(row=0, column=3,columnspan=3)

        self.nameLabel = Label(self, text="Employee Name:")
        self.nameLabel.grid(row=1, column=0, columnspan=3)
        self.varName = StringVar()
        self.varName.set("Enter Name")
        self.nameEntry = Entry(self, textvariable=self.varName)
        self.nameEntry.grid(row=1, column=3, columnspan=3)

        self.type=IntVar()
        self.Type1=Radiobutton(self,text="Director", variable=self.type, value=1,command=self.radioFunc)
        self.Type1.grid(row=2,column=0,columnspan=2)
        self.Type2=Radiobutton(self, text="Manager", variable=self.type, value=2,command=self.radioFunc)
        self.Type2.grid(row=2,column=2,columnspan=2)
        self.Type3=Radiobutton(self, text="TT", variable=self.type, value=3,command=self.radioFunc)
        self.Type3.grid(row=2,column=4,columnspan=2)

        self.addBtn=Button(self,text="Add",command=self.addBtn_click)
        self.addBtn.grid(row=5,column=0,columnspan=2)

        self.searchBtn = Button(self, text="Search",command=self.searchBtn_click)
        self.searchBtn.grid(row=5, column=2,columnspan=2)

        self.updateBtn = Button(self, text="Update",command=self.updateBtn_click)
        self.updateBtn.grid(row=5, column=4,columnspan=2)

        self.deleteBtn = Button(self, text="Delete",command=self.deleteBtn_click)
        self.deleteBtn.grid(row=5, column=6,columnspan=2)

        self.firstBtn = Button(self, text="First",command=self.firstBtn_click)
        self.firstBtn.grid(row=6, column=0,columnspan=2)

        self.lastBtn = Button(self, text="  Last  ",command=self.lastBtn_click)
        self.lastBtn.grid(row=6, column=2,columnspan=2)

        self.prevBtn = Button(self, text="  Prev  ",command=self.prevBtn_click)
        self.prevBtn.grid(row=6, column=4,columnspan=2)

        self.nextBtn = Button(self, text=" Next  ",command=self.nextBtn_click)
        self.nextBtn.grid(row=6, column=6,columnspan=2)


root=Tk()
root.title("Ems with Tkinter")
root.resizable(0,0)
f=Form(root)
root.mainloop()
