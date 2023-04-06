from tkinter import filedialog as fd 
from tkinter import tix
from tkinter.constants import RIDGE
from tkinter.tix import *
import tkinter as tk
from tkinter import ttk
import openpyxl as xl
from MainClasses import *
import WildAnimals
import TradeSecrets
import FourthAmendment
import os

#excluded due to data privacy concerns
#import NIHL 

#General Functionality and Menus
class Information():
    
    """
    info that is common between all classes which process the creation of an ADF
    """
    def __init__(self):
        
        self.name = None
        self.acceptance = []
        self.statement = []
        self.question = None
        self.adf = None
        self.multiFlag = False
        self.case = []
        self.node = None
        self.editFlag = False
        self.caseName = None
        self.caseList = {}

class UI(tix.Tk):
    
    def __init__(self,*args,**kwargs):
        
        tix.Tk.__init__(self,*args,**kwargs)
        tix.Tk.title(self,'ADF Tool')
        tix.Tk.geometry(self,"750x500")
        
        menubar = tk.Menu(self)
        filemenu = tk.Menu(menubar,tearoff=0)
        self.config(menu=menubar)
        
        filemenu.add_command(label="Menu",command=lambda:self.menu())
        filemenu.add_command(label="Exit", command=lambda:self.quit())
        menubar.add_cascade(label="File", menu=filemenu)
        menubar.add_command(label="Help", command=lambda:self.help())

        self.container = tk.Frame(self)
        self.container.pack(side="top",fill="both",expand=True)
        self.container.grid_rowconfigure(0,weight=1)
        self.container.grid_columnconfigure(0,weight=1)
        
        self.frames = {}
        frame = Welcome
        self.info = Information()
        self.frameCreation(frame,self.info)
        self.show_frame(frame)
        
        #styles
        s = ttk.Style()
        s.configure('my.TButton', font=('Helvetica', 15))
        
    def show_frame(self, page):
        frame = self.frames[page]
        frame.tkraise()
    
    def frameCreation(self, F, info):
        
        frame = F(self.container,self,info)
            
        self.frames[F] = frame
        frame.grid(row=0, column=0, sticky='nsew')
    
    def menu(self):
        self.frameCreation(MainMenu,self.info)
        self.show_frame(MainMenu)      

    def help(self):
        os.startfile('User_Manual.txt')

    def quit(self):
        exit()
    
class Background(tk.Frame):
    
    def __init__(self,parent):
        tk.Frame.__init__(self,parent,bg='#A7D0FF')
        self.acc = []

class Welcome(Background):
    
    def __init__(self, parent, controller, info):

        Background.__init__(self,parent)
        
        self.info = info
        self.controller = controller

        var = tk.StringVar()
        var.set("Welcome to the Legal Decision-Making Tool")
        label = tk.Label(self, textvariable=var,font="Verdana 20 underline",bg='#A7D0FF')
        label.pack(pady=10,padx=10)
        
        T = tk.Text(self, height = 11, width = 45, bg='#ddeded',font="Verdana 18" )
        
        message = """This is a tool to help assist in legal decision-making.\n\nThis tool will predict the outcome of a legal case, in a\nspecified legal domain, after asking the user a number\nof questions. You can also create new ADFs for legal\ndomains in this tool and edit existing ones in light\nof new precedents or domain knowledge.\n\nPress START to begin the tool or press MANUAL to\ncheck the user manual before you begin."""
                            
        T.place(relx=0.05,rely=0.13)
        
        T.insert(tk.END, message )
        
        button = ttk.Button(self, text = 'START',style='my.TButton',command=lambda: self.start())
        button.place(relheight= 0.1, relwidth = 0.15, relx=0.6, rely=0.85)
        
        button2 = ttk.Button(self, text = 'MANUAL',style='my.TButton',command=lambda: self.manual())
        button2.place(relheight= 0.1, relwidth = 0.15, relx=0.2, rely=0.85)
    
    def start(self):    
        self.controller.frameCreation(MainMenu, self.info)
        self.controller.show_frame(MainMenu)
    
    def manual(self):
        os.startfile('User_Manual.txt')

class MainMenu(Background):
    
    def __init__(self, parent, controller, info):

        Background.__init__(self,parent)

        self.controller = controller
        self.info = info
        self.info.case = []

        var = tk.StringVar()
        var.set("Main Menu")
        label = tk.Label(self, textvariable=var,font="Verdana 20 underline",bg='#A7D0FF')
        label.pack(pady=10,padx=10)
        button = ttk.Button(self, text = 'Existing domain',style='my.TButton',command=lambda: self.existingDomain())
        button.place(relheight= 0.25 , relwidth = 0.5, relx=0.25, rely=0.6)
        button2 = ttk.Button(self, text = 'Create a new domain',style='my.TButton',command=lambda: self.CreateDomain())
        button2.place(relheight= 0.25 , relwidth = 0.5, relx = 0.25, rely=0.2 )

    def CreateDomain(self):
        
        self.controller.frameCreation(CreateDomain, self.info)
        self.controller.show_frame(CreateDomain)
    
    def existingDomain(self):
        self.controller.frameCreation(ExistingDomain, self.info)
        self.controller.show_frame(ExistingDomain)

#Existing Domain Screens        
class ExistingDomain(Background):
   def __init__(self,parent,controller, info):
       
       Background.__init__(self,parent)
       
       self.controller = controller
       self.info = info
       self.adf = None
       
       var = tk.StringVar()
       var.set("Existing Domain")
       var2 = tk.StringVar()
       var2.set("Select Domain:")
       
       label = tk.Label(self, textvariable=var,bg='#A7D0FF',font="Verdana 20 underline")
       label.pack()
       label2 = tk.Label(self, textvariable=var2,bg='#A7D0FF',font="Verdana 12")
       label2.place(relx = 0.02,rely = 0.2)
       
       var3 = tk.StringVar()
       var3.set("Import Domain:")
       label3 = tk.Label(self, textvariable=var3,bg='#A7D0FF',font="Verdana 12")
       label3.place(relx = 0.02,rely = 0.45)
       
       button = ttk.Button(self, text = 'OK',style= 'my.TButton',command= lambda: self.OK())
       button.place(relheight= 0.1 , relwidth = 0.1, relx = 0.45, rely=0.8 )
       
       help = tk.StringVar()
       help.set('?')
       
       helpLabel = tk.Label(self, textvariable=help,bg='#A7D0FF',fg='#FF001F', relief=RIDGE,font="Verdana 12 bold")
       helpLabel.place(relx = 0.2,rely = 0.45)
       
       box = Balloon(self)
       
       box.bind_widget(helpLabel,balloonmsg="Please select a .xlsx file which has previously been created through this app")
       
       button1 = ttk.Button(self, text = 'BROWSE',style= 'my.TButton',command= lambda: self.browse())
       button1.place(relheight= 0.1 , relwidth = 0.2, relx = 0.4, rely=0.55 )
       
       n = tk.StringVar()
       self.combo = ttk.Combobox(self, width = 50, textvariable = n, state='readonly')
  
       # Adding combobox drop down list
       self.combo['values'] = ('Wild Animals','Trade Secrets','Automobile Exception to the 4th Amendment')#'Noise-Induced Hearing Loss')
       
       self.combo.place(relx = 0.3, rely=0.3)
    
   def OK(self):
       
        if self.adf != None:
            self.info.adf = self.adf
            self.info.caseList = {}
            self.controller.frameCreation(DomainMenu, self.info)
            self.controller.show_frame(DomainMenu)
            
        elif self.combo.get() == 'Wild Animals':
            self.info.adf = WildAnimals.adf()
            self.info.caseList = WildAnimals.cases()
            self.controller.frameCreation(DomainMenu, self.info)
            self.controller.show_frame(DomainMenu)
            
        elif self.combo.get() == 'Trade Secrets':
            self.info.adf = TradeSecrets.adf()
            self.info.caseList = TradeSecrets.cases()
            self.controller.frameCreation(DomainMenu, self.info)
            self.controller.show_frame(DomainMenu)
            
        elif self.combo.get() == 'Automobile Exception to the 4th Amendment':
            self.info.adf = FourthAmendment.adf()
            self.info.caseList = FourthAmendment.cases()
            self.controller.frameCreation(DomainMenu, self.info)
            self.controller.show_frame(DomainMenu)
            
        # elif self.combo.get() == 'Noise-Induced Hearing Loss':
        #     self.info.adf = NIHL.adf()
        #     self.info.caseList = NIHL.cases()
        #     self.controller.frameCreation(DomainMenu, self.info)
        #     self.controller.show_frame(DomainMenu)

        else:
            pass
            
   def browse(self):
       try:
        file = fd.askopenfilename(title='BROWSE',filetypes=[("Excel files", "*.xlsx")])
        name = os.path.basename(file)
        name = name.split('.')[0]
        self.adf = importADF(file,name)
        file.close()
       except:
           pass

class DomainMenu(Background):
    
    def __init__(self,parent,controller, info):
       
       Background.__init__(self,parent)
       
       self.controller = controller
       self.info = info
       
       button = ttk.Button(self, text = 'Edit domain',style='my.TButton', command=lambda:self.editDomain())
       button.place(relheight= 0.2 , relwidth = 0.5, relx=0.25, rely=0.4)
       button2 = ttk.Button(self, text = 'Query domain',style='my.TButton',command=lambda: self.queryDomain())
       button2.place(relheight= 0.2 , relwidth = 0.5, relx = 0.25, rely=0.15 )
       button3 = ttk.Button(self, text = 'Visualise domain',style='my.TButton',command=lambda: self.visualise())
       button3.place(relheight= 0.2, relwidth = 0.5, relx = 0.25, rely=0.65 )
    
    def queryDomain(self):
        self.controller.frameCreation(CaseName, self.info)
        self.controller.show_frame(CaseName)
    
    def editDomain(self):
        self.controller.frameCreation(EditDomain, self.info)
        self.controller.show_frame(EditDomain)
    
    def visualise(self):
        self.graph = self.info.adf.visualiseNetwork()
       
        self.graph.write_png('{}.png'.format(self.info.adf.name))
            
        os.startfile('{}.png'.format(self.info.adf.name))

class CaseName(Background):
   def __init__(self,parent,controller, info):
       
       Background.__init__(self,parent)
       
       self.controller = controller
       self.info = info
       var = tk.StringVar()
       var.set("Query Domain")
       var2 = tk.StringVar()
       var2.set("Specify Case Name:")
       var3 = tk.StringVar()
       var3.set("Query a predefined case:")
       
       label = tk.Label(self, textvariable=var,bg='#A7D0FF',font="Verdana 20 underline")
       label.pack()
       label2 = tk.Label(self, textvariable=var2,bg='#A7D0FF',font="Verdana 12 underline")
       label2.place(relx = 0.02,rely = 0.2)
       label3 = tk.Label(self, textvariable=var3,bg='#A7D0FF',font="Verdana 12 underline")
       label3.place(relx = 0.02,rely = 0.5)
       
       n = tk.StringVar()
       self.combo = ttk.Combobox(self, width = 50, textvariable = n, state='readonly')
       if self.info.case != {}:
           self.combo['values'] = list(self.info.caseList.keys())
       self.combo.place(relx = 0.3 , rely = 0.62 )
       
       self.entry = tk.Entry(self,font='Verdana 12')
       self.entry.place(relx = 0.32,rely = 0.3,relheight=0.05,relwidth=0.35)
       button = ttk.Button(self, text = 'OK',style= 'my.TButton',command= lambda: self.OK())
       button.place(relheight= 0.1 , relwidth = 0.1, relx = 0.45, rely=0.8 )

   def OK(self):
       
        if self.entry.get() != '':
            self.info.caseName = self.entry.get()
            self.entry.delete(0,10000000)
            
            self.controller.frameCreation(QueryDomain, self.info)
            self.controller.show_frame(QueryDomain)
            
        elif self.combo.get() != '':
            self.info.caseName = self.combo.get()
            self.info.case = self.info.caseList[self.combo.get()]
            
            self.controller.frameCreation(Outcome, self.info)
            self.controller.show_frame(Outcome)
    
class QueryDomain(Background):
    def __init__(self,parent,controller, info):
       
       Background.__init__(self,parent)
       
       self.controller = controller
       self.info = info
       self.info.case = []
       
       self.number = 1
       
       self.stringDict = {}
       self.checkList = []
       
       self.nodes = self.info.adf.nodes.copy()
       
       self.questionOrder = self.info.adf.questionOrder.copy()
       self.orderFlag = False

       var = tk.StringVar()
       var.set("Domain Name:")
       
       var2 = tk.StringVar()
       var2.set(self.info.adf.name)
       
       self.var3 = tk.StringVar()
       self.var3.set("Question {}:".format(self.number))
       
       label = tk.Label(self, textvariable=var,bg='#A7D0FF',font="Verdana 20")
       label.pack(side = 'left',anchor='nw')

       label2 = tk.Label(self, textvariable=var2,bg='#A7D0FF',font="Verdana 20")
       label2.pack(side = 'left',anchor='nw')
       
       label3 = tk.Label(self, textvariable=self.var3,bg='#A7D0FF',font="Verdana 20")
       label3.place( relx = 0.05, rely=0.1)
       
       self.var4 = tk.StringVar()
       self.questionGen()
       
       label4 = tk.Label(self, textvariable=self.var4,bg='#A7D0FF',font="Verdana 20",wraplength=700)
       label4.place( relx = 0.05,rely=0.2)
       
       next = ttk.Button(self, text = 'NEXT',style= 'my.TButton',command= lambda: self.next())
       next.place(relheight= 0.1 , relwidth = 0.35, relx = 0.32, rely=0.85 )
       
       if self.multiFlag == False:
           self.trueFalse()
           
       else:
           self.multi()
        
    def next(self):
        if self.multiFlag == False:
            if self.i.get() == 'Yes':
                self.info.case.append(self.name)

            else:
                pass
        else:
            for key, value in self.stringDict.items():
      
                if value.get() == '1':
                    key = key.replace(' ','_')
                    self.info.case.append(key)

        self.forget()
            
        self.questionGen()
        
        if self.status == False:
            self.controller.frameCreation(Outcome, self.info)
            self.controller.show_frame(Outcome)
        else:
            pass
        
        if self.multiFlag:
            self.multi()
        else:
            self.trueFalse()
            
        self.number += 1
        self.var3.set("Question {}:".format(self.number))
    
    def questionGen(self):
        
        self.status = False
        self.multiFlag = False
        self.answers = []
        self.counter = 0
        
        if self.questionOrder != []:
            self.orderFlag = True
            
            for i in self.questionOrder:
                node = self.nodes[i]
                x = self.questionHelper(node)
                if x == 'Done':
                    break 
                
            self.questionOrder.remove(i)
            self.name = i
            return
                   
        elif self.orderFlag == False:
            for i in self.nodes.values():
                x = self.questionHelper(i)
                if x == 'Done':
                    break 
            self.nodes.pop(i.name)
            self.name = i.name
            return
        
        return

    def questionHelper(self,i):
        #multipe choice question 
        if i.answers != None:
            #prunes answers which are themselves non-leaf factors in the case of a multiple choice question
            for j in i.answers:
                
                try:
                    self.info.adf.nodes[j]
                    try:
                        #solves an issue in the fourth amendment domain with not_authorised sub-blf
                        if self.info.adf.nodes[j].question == '<>':
                            self.answers.append(j)     
                    except:
                        pass 
                except:
                    self.answers.append(j)
                
            question = i.question
            self.var4.set(question)
            self.multiFlag = True
            self.status = True
            return 'Done'
            
        #true/false question
        else:
            # '<>' is to fix a problem in the 4th amendment domain in which not_authorised was being prompted to set a question for it
            if i.question != None and i.question != '<>':
                self.question = i.question
                self.var4.set(self.question) 
                self.status = True
                return 'Done'
                
    def trueFalse(self):
       
        self.i = tk.StringVar()
        self.i.set("Yes")
           
        self.r1= tk.Radiobutton(self, text="Yes", value='Yes', variable =self.i)
        self.r1.place( relx = 0.45,rely=0.5)
        self.r2= tk.Radiobutton(self, text="No", value='No', variable=self.i)
        self.r2.place( relx = 0.45,rely=0.55)
    
    def multi(self):   
        
        x = 0.4
        y = 0.4
        
        counter = 0
        
        for i in self.answers:
            
            if len(self.answers)>5:
                x=0.2
            
                if len(self.checkList)>4:
                    x=0.6
                    y=0.4 + (0.05*counter)
                    counter+=1
            
            i = i.replace('_',' ')
            y += 0.05
            self.stringDict[i] = tk.StringVar()            
            c = tk.Checkbutton(self, text = i, variable=self.stringDict[i],tristatevalue=0)
            c.place(relx = x, rely = y)  
            self.checkList.append(c)
    
    def forget(self):
        
        #multi check boxes
        try:
            # remove previous StringVars
            self.stringDict.clear()

            # remove previous Checkboxes
            for cb in self.checkList:
                cb.destroy()
            self.checkList.clear() 
        
        except:
            pass
        
        try:
            self.r1.destroy()
            self.r2.destroy()
        except:
            pass
                            
class Outcome(Background):
    
    def __init__(self,parent,controller, info):
       
       Background.__init__(self,parent)
       
       self.controller = controller
       self.info = info   

       output = self.info.adf.evaluateTree(self.info.case)
 
       var = tk.StringVar()
       var.set("Domain Name:")
       
       var2 = tk.StringVar()
       var2.set(self.info.adf.name)
       
       self.var3 = tk.StringVar()
       self.var3.set("Outcome in {}:".format(self.info.caseName))
       
       label = tk.Label(self, textvariable=var,bg='#A7D0FF',font="Verdana 20")
       label.pack(side = 'left',anchor='nw')

       label2 = tk.Label(self, textvariable=var2,bg='#A7D0FF',font="Verdana 20")
       label2.pack(side = 'left',anchor='nw')
       
       label3 = tk.Label(self, textvariable=self.var3,bg='#A7D0FF',font="Verdana 20")
       label3.place( relx = 0, rely=0.1)
       
       anotherCase = ttk.Button(self, text = 'NEXT CASE',style= 'my.TButton',command= lambda: self.anotherCase())
       anotherCase.place(relheight= 0.1 , relwidth = 0.2, relx = 0.2, rely=0.85 )
       
       menu = ttk.Button(self, text = 'MENU',style= 'my.TButton',command= lambda: self.menu())
       menu.place(relheight= 0.1 , relwidth = 0.2, relx = 0.4, rely=0.85 )
       
       report = ttk.Button(self, text = 'REPORT',style= 'my.TButton',command= lambda: self.report())
       report.place(relheight= 0.1 , relwidth = 0.2, relx = 0.6, rely=0.85 )
       
       outcome = tk.Text(self) 
       outcome.place(relheight=0.6,relwidth=0.8, relx = 0.1, rely=0.2)
       
       scrollbar = tk.Scrollbar(self)
       scrollbar.place(relheight=0.6,relwidth=0.02,relx=0.9,rely=0.2)
       scrollbar.config(command=outcome.yview)
       outcome.config(yscrollcommand=scrollbar.set)
       
       counter = 1
       
       for i in range(0,len(output)-1):
            x = output[i]
            
            outcome.insert(tk.END,"Reason {}: ".format(counter))            
            outcome.insert(tk.END,x+'\n' )
            counter += 1

       outcome.insert(tk.END,"Outcome: ")
       outcome.insert(tk.END,output[-1])
    
    def anotherCase(self):
        self.controller.frameCreation(CaseName, self.info)
        self.controller.show_frame(CaseName)
    
    def menu(self):
        self.controller.show_frame(MainMenu) 
        
    def report(self):
        self.controller.frameCreation(Report, self.info)
        self.controller.show_frame(Report)
            
class EditDomain(Background):
    def __init__(self,parent,controller, info):
       
       Background.__init__(self,parent)
       
       self.controller = controller
       self.info = info

       var = tk.StringVar()
       var.set("Domain Name:")
       
       var2 = tk.StringVar()
       var2.set(self.info.adf.name) 
       
       self.var3 = tk.StringVar()
       self.var3.set("Edit Node")
       
       label = tk.Label(self, textvariable=var,bg='#A7D0FF',font="Verdana 20")
       label.pack(side = 'left',anchor='nw')

       label2 = tk.Label(self, textvariable=var2,bg='#A7D0FF',font="Verdana 20")
       label2.pack(side = 'left',anchor='nw')
       
       label3 = tk.Label(self, textvariable=self.var3,bg='#A7D0FF',font="Verdana 20 underline")
       label3.place( relx = 0.05, rely=0.1)
       
       var4 = tk.StringVar()
       var4.set('Edit or delete a non-leaf node')
       
       name = tk.Label(self, textvariable=var4,bg='#A7D0FF',font="Verdana 20 ")
       name.place( relx = 0.05, rely=0.2 )
       
       var5 = tk.StringVar()
       var5.set('Edit the question of a leaf node')
       
       question = tk.Label(self, textvariable=var5,bg='#A7D0FF',font="Verdana 20 ")
       question.place( relx = 0.05, rely=0.4 )
       
       n = tk.StringVar()
       self.combo = ttk.Combobox(self, width = 50, textvariable = n, state='readonly')
       
       m = tk.StringVar()
       self.combo2 = ttk.Combobox(self, width = 50, textvariable = m, state='readonly')
       
       nodeList = []
       nodeList2 = []
       
       self.info.adf.nonLeafGen()
       
       # Adding combobox drop down list
       for key in self.info.adf.nonLeaf:
           nodeList.append(key)
           
       for name in self.info.adf.nodes:
           node = self.info.adf.nodes[name]
           if node.question != None:
                nodeList2.append(node.name)
                 
       self.combo['values'] = nodeList
       self.combo.place(relx = 0.3, rely=0.32)
       
       self.combo2['values'] = nodeList2
       self.combo2.place(relx = 0.3, rely=0.52)

       create = ttk.Button(self, text = 'CREATE NODE',style= 'my.TButton',command= lambda: self.createNode())
       create.place(relheight= 0.1 , relwidth = 0.4, relx = 0.1, rely=0.65 )

       search = ttk.Button(self, text = 'SEARCH',style= 'my.TButton',command= lambda: self.searchNode())
       search.place(relheight= 0.1 , relwidth = 0.4, relx = 0.3, rely=0.85 )
       
       save = ttk.Button(self, text = 'SAVE',style= 'my.TButton',command= lambda: self.saveNode())
       save.place(relheight= 0.1 , relwidth = 0.4, relx = 0.5, rely=0.75 )
       
       question = ttk.Button(self, text = 'CHANGE QUESTION ORDER',style= 'my.TButton',command= lambda: self.questionOrder())
       question.place(relheight= 0.1 , relwidth = 0.4, relx = 0.5, rely=0.65 )
       
       delete = ttk.Button(self, text = 'DELETE',style= 'my.TButton',command= lambda: self.delete())
       delete.place(relheight= 0.1 , relwidth = 0.4, relx = 0.1, rely=0.75 )
       
       
    def delete(self):
        
        if self.combo.get() != '':  
            
            self.info.adf.nodes.pop(self.combo.get())

            self.combo.set('')
            self.combo['values'] = []

            nodeList = []
            
            self.info.adf.nonLeafGen()
            
            # Adding combobox drop down list
            for key in self.info.adf.nonLeaf:
                nodeList.append(key)
                        
            self.combo['values'] = nodeList
                      
    def searchNode(self):
    
        if self.combo.get() != '':  
            node = self.info.adf.nodes[self.combo.get()]
            self.info.node = node
            self.controller.frameCreation(EditNode, self.info)
            self.controller.show_frame(EditNode)
        elif self.combo2.get() != '':
            node = self.info.adf.nodes[self.combo2.get()]
            self.info.node = node
            self.controller.frameCreation(EditQuestion, self.info)
            self.controller.show_frame(EditQuestion)

    def questionOrder(self):
        self.controller.frameCreation(QuestionOrder, self.info)
        self.controller.show_frame(QuestionOrder)

    def createNode(self):
        self.info.editFlag = True
        self.controller.frameCreation(NodeSelection, self.info)
        self.controller.show_frame(NodeSelection)
    
    def saveNode(self):
        self.controller.frameCreation(SaveScreen, self.info)
        self.controller.show_frame(SaveScreen)
        
class EditNode(Background):
    
    def __init__(self,parent,controller, info):
       
       Background.__init__(self,parent)
       
       self.controller = controller
       self.info = info
    
       var = tk.StringVar()
       var.set("Domain Name:")
       
       var2 = tk.StringVar()
       var2.set(self.info.adf.name) 
       
       self.var3 = tk.StringVar()
       self.var3.set("Node:")
       
       self.var4 = tk.StringVar()
       self.var4.set("{}".format(self.info.node.name))
       
       label = tk.Label(self, textvariable=var,bg='#A7D0FF',font="Verdana 20")
       label.pack(side = 'left',anchor='nw')

       label2 = tk.Label(self, textvariable=var2,bg='#A7D0FF',font="Verdana 20")
       label2.pack(side = 'left',anchor='nw')
       
       label3 = tk.Label(self, textvariable=self.var3,bg='#A7D0FF',font="Verdana 20 ")
       label3.place( relx = 0, rely=0.1)
       
       label4 = tk.Label(self, textvariable=self.var4,bg='#A7D0FF',font="Verdana 20 ")
       label4.place( relx = 0.15, rely=0.1)
     
       save = ttk.Button(self, text = 'SUBMIT',style= 'my.TButton',command= lambda: self.submit())
       save.place(relheight= 0.1 , relwidth = 0.3, relx = 0.35, rely=0.75 )
       
       done = ttk.Button(self, text = 'DONE',style= 'my.TButton',command= lambda: self.done())
       done.place(relheight= 0.1 , relwidth = 0.3, relx = 0.35, rely=0.85 )
       
       back = ttk.Button(self, text = 'BACK',style= 'my.TButton',command= lambda: self.back())
       back.place(relheight= 0.1 , relwidth = 0.3, relx = 0.02, rely=0.75 )

       addAcceptance = ttk.Button(self, text = 'ADD ACCEPTANCE',style= 'my.TButton',command= lambda: self.accept())
       addAcceptance.place(relheight= 0.1 , relwidth = 0.3, relx = 0.66, rely=0.75 )

       self.acceptDict = {}
       self.statementDict = {}
       self.acceptList = []
       self.statementList = []
       
       nameVar = tk.StringVar()
       nameVar.set("Name:")
       name = tk.Label(self, textvariable=nameVar,bg='#A7D0FF',font="Verdana 12 ")
       name.place(relx = 0, rely=0.2)
       
       self.nameEntry = tk.Entry(self,font='Verdana 12')
       self.nameEntry.place(relx = 0.2,rely = 0.2,relheight=0.05,relwidth=0.75)           
       self.nameEntry.insert(tk.END, self.info.node.name)
       
       self.y=0.2
       
       #ACCEPTANCE CONDITIONS
       counter = 1
       
       for i in self.info.node.acceptanceOriginal:
            self.y+=0.05
            
            self.acceptDict[i] = tk.StringVar() 
            self.acceptDict[i].set("Acceptance {}:".format(counter))
            
            labelAccept = tk.Label(self, textvariable=self.acceptDict[i],bg='#A7D0FF',font="Verdana 12")
            labelAccept.place(x=0.05, rely=self.y)
                        
            acceptance = tk.Entry(self,font='Verdana 12')
            acceptance.place(relx = 0.2,rely = self.y,relheight=0.05,relwidth=0.75)           
            acceptance.insert(tk.END, i)
            
            self.acceptList.append(acceptance)
            
            counter += 1
       
       #STATEMENTS
       counter = 1
       
       for j in self.info.node.statement:    
            self.y+=0.05
            
            self.statementDict[j] = tk.StringVar() 
            self.statementDict[j].set("Statement {}:".format(counter))
            
            labelStatement = tk.Label(self, textvariable=self.statementDict[j],bg='#A7D0FF',font="Verdana 12")
            labelStatement.place(x=0.05, rely=self.y)
            
            statement = tk.Entry(self,font='Verdana 12')
            statement.place(relx = 0.2,rely = self.y,relheight=0.05,relwidth=0.75)           
            statement.insert(tk.END, j)

            self.statementList.append(statement)
            
            counter+= 1     

    def accept(self):
        self.y+=0.05
        
        stringVar = tk.StringVar() 
        stringVar.set("Acceptance:")
        
        labelAccept = tk.Label(self, textvariable=stringVar,bg='#A7D0FF',font="Verdana 12")
        labelAccept.place(x=0.05, rely=self.y)
                    
        acceptance = tk.Entry(self,font='Verdana 12')
        acceptance.place(relx = 0.2,rely = self.y,relheight=0.05,relwidth=0.75)           
        
        #adds the entry box to the list of acceptance conditions
        self.acceptList.append(acceptance)

        self.y += 0.05
        
        stringVar2 = tk.StringVar() 
        stringVar2.set("Statement:")
        
        labelStatement = tk.Label(self, textvariable=stringVar2,bg='#A7D0FF',font="Verdana 12")
        labelStatement.place(x=0.05, rely=self.y)
        
        statement = tk.Entry(self,font='Verdana 12')
        statement.place(relx = 0.2,rely = self.y,relheight=0.05,relwidth=0.75)     
        self.statementList.append(statement)
        
    def submit(self):
        
        self.acceptance = []
        self.statements = []
        
        self.name = self.nameEntry.get()
        self.nameEntry.delete(0,10000000)
        
        for i in self.acceptList:
            self.acceptance.append(i.get())
            i.delete(0,10000000)
        
        for j in self.statementList:
            self.statements.append(j.get())
            j.delete(0,10000000)
            
        self.info.adf.nodes.pop(self.info.node.name)
        self.info.adf.addNodes(self.name, self.acceptance, self.statements)
           
    def back(self):
        
        self.controller.frameCreation(EditDomain, self.info)
        self.controller.show_frame(EditDomain)
    
    def done(self):
        
        questionGeneration = False
        
        for i in self.info.adf.nodes.values():
            
            if i.children == None and i.question == None:
                questionGeneration = True
                
        if questionGeneration == True:
            self.controller.frameCreation(QuestionCreation, self.info)
            self.controller.show_frame(QuestionCreation) 
        else:
            self.controller.frameCreation(EditDomain, self.info)
            self.controller.show_frame(EditDomain)    

class EditQuestion(Background):
    
    def __init__(self,parent,controller, info):
       
       Background.__init__(self,parent)
       
       self.controller = controller
       self.info = info
    
       var = tk.StringVar()
       var.set("Domain Name:")
       
       var2 = tk.StringVar()
       var2.set(self.info.adf.name) 
       
       self.var3 = tk.StringVar()
       self.var3.set("Node:")
       
       self.var4 = tk.StringVar()
       self.var4.set("{}".format(self.info.node.name))
       
       label = tk.Label(self, textvariable=var,bg='#A7D0FF',font="Verdana 20")
       label.pack(side = 'left',anchor='nw')

       label2 = tk.Label(self, textvariable=var2,bg='#A7D0FF',font="Verdana 20")
       label2.pack(side = 'left',anchor='nw')
       
       label3 = tk.Label(self, textvariable=self.var3,bg='#A7D0FF',font="Verdana 20 ")
       label3.place( relx = 0, rely=0.1)
       
       label4 = tk.Label(self, textvariable=self.var4,bg='#A7D0FF',font="Verdana 20 ")
       label4.place( relx = 0.15, rely=0.1)
     
       save = ttk.Button(self, text = 'SUBMIT',style= 'my.TButton',command= lambda: self.submit())
       save.place(relheight= 0.1 , relwidth = 0.35, relx = 0.32, rely=0.65 )
       
       done = ttk.Button(self, text = 'DONE',style= 'my.TButton',command= lambda: self.done())
       done.place(relheight= 0.1 , relwidth = 0.35, relx = 0.32, rely=0.75 )
       
       back = ttk.Button(self, text = 'BACK',style= 'my.TButton',command= lambda: self.back())
       back.place(relheight= 0.1 , relwidth = 0.35, relx = 0.32, rely=0.85 )
       
       questionVar = tk.StringVar()
       questionVar.set("Question:")
       question = tk.Label(self, textvariable=questionVar,bg='#A7D0FF',font="Verdana 12 ")
       question.place(relx=0.01,rely=0.2)
       
       self.questionEntry = tk.Entry(self,font='Verdana 12')
       self.questionEntry.place(relx=0.2,rely=0.2,relheight=0.05,relwidth=0.75)           
       try:
           self.questionEntry.insert(tk.END, self.info.node.question)
       except:
           pass

    def submit(self):
        
        self.question = self.questionEntry.get()
        self.info.adf.nodes[self.info.node.name].question = self.question
        self.questionEntry.delete(0,10000000)
    
    def back(self):
        
        self.controller.frameCreation(EditDomain, self.info)
        self.controller.show_frame(EditDomain)
    
    def done(self):
        self.controller.frameCreation(SaveScreen, self.info)
        self.controller.show_frame(SaveScreen)

#Create Domain Screens           
class CreateDomain(Background):
   def __init__(self,parent,controller, info):
       
       Background.__init__(self,parent)
       
       self.controller = controller
       self.info = info
       var = tk.StringVar()
       var.set("Create Domain")
       var2 = tk.StringVar()
       var2.set("Specify Domain Name:")
       label = tk.Label(self, textvariable=var,bg='#A7D0FF',font="Verdana 20 underline")
       label.pack()
       label2 = tk.Label(self, textvariable=var2,bg='#A7D0FF',font="Verdana 12 underline")
       label2.place(relx = 0.02,rely = 0.2)
       
       help = tk.StringVar()
       help.set('?')
       
       helpLabel = tk.Label(self, textvariable=help,bg='#A7D0FF',fg='#FF001F',relief=RIDGE,font="Verdana 12 bold")
       helpLabel.place(relx = 0.3,rely = 0.2)
       
       box = Balloon(self)
       
       box.bind_widget(helpLabel,balloonmsg="Please ensure your domain name has no spaces between words")
       
       
       self.entry = tk.Entry(self,font='Calibri 20')
       self.entry.place(relx = 0.32,rely = 0.35,relheight=0.1,relwidth=0.35)
       button = ttk.Button(self, text = 'OK',style= 'my.TButton',command= lambda: self.OK())
       button.place(relheight= 0.1 , relwidth = 0.1, relx = 0.45, rely=0.8 )

   def OK(self):
       
        self.info.adf = ADF(self.entry.get())
        self.entry.delete(0,10000000)
        
        self.controller.frameCreation(NodeSelection, self.info)
        self.controller.show_frame(NodeSelection)

class NodeSelection(Background):
    
    def __init__(self,parent,controller, info):
       
        Background.__init__(self,parent)
        
        self.controller = controller
        self.info = info
        
        var = tk.StringVar()
        var.set("Node Creation")
        label = tk.Label(self, textvariable=var,font="Verdana 20 underline",bg='#A7D0FF')
        label.pack(pady=10,padx=10)
        
        help = tk.StringVar()
        help.set('?')
        
        helpLabel = tk.Label(self, textvariable=help,bg='#A7D0FF',fg='#FF001F',relief=RIDGE,font="Verdana 20 bold")
        helpLabel.place(relx = 0.8,rely = 0.3)
       
        helpLabel1 = tk.Label(self, textvariable=help,bg='#A7D0FF',fg='#FF001F',relief=RIDGE,font="Verdana 20 bold")
        helpLabel1.place(relx = 0.8,rely = 0.7)
        
        box = Balloon(self)
       
        box.bind_widget(helpLabel,balloonmsg="Create this type of node if you are creating non-leaf nodes")
        box.bind_widget(helpLabel1,balloonmsg="Create this type of node if you are creating a base level factor with multiple sub-factors")
        
        button = ttk.Button(self, text = 'Create a T/F Node',style='my.TButton',command = lambda: self.standardNode() )
        button.place(relheight= 0.25 , relwidth = 0.5, relx=0.25, rely=0.2 )
        button2 = ttk.Button(self, text = 'Create a Multiple Choice Node',style='my.TButton',command=lambda: self.multiNode())
        button2.place(relheight= 0.25 , relwidth = 0.5, relx = 0.25, rely=0.6 )

        
    def standardNode(self):
        self.controller.frameCreation(NodeCreation, self.info)
        self.controller.show_frame(NodeCreation) 
    
    def multiNode(self):
        self.controller.frameCreation(MultiCreation, self.info)
        self.controller.show_frame(MultiCreation) 
    
class NodeCreation(Background):
    
    def __init__(self,parent,controller, info):
       
        Background.__init__(self,parent)
        
        self.name = ''
        self.acceptance = []
        self.statement = []
        
        self.controller = controller
        self.info = info
        
        var = tk.StringVar()
        var.set("Domain Name:")
       
        var2 = tk.StringVar()
        var2.set(self.info.adf.name)
        
        var3 = tk.StringVar()
        var3.set('Create Node')
        
        var4 = tk.StringVar()
        var4.set('Name:')
        
        var5 = tk.StringVar()
        var5.set('Acceptance:')
        
        var6 = tk.StringVar()
        var6.set('Statement:')
        
        label = tk.Label(self, textvariable=var,bg='#A7D0FF',font="Verdana 20")
        label.pack(side = 'left',anchor='nw')
        
        label2 = tk.Label(self, textvariable=var2,bg='#A7D0FF',font="Verdana 20")
        label2.pack(side = 'left',anchor='nw')
        
        label3 = tk.Label(self, textvariable=var3,bg='#A7D0FF',font="Verdana 20 underline")
        label3.place( relx = 0, rely=0.1 )
        
        name = tk.Label(self, textvariable=var4,bg='#A7D0FF',font="Verdana 20 ")
        name.place( relx = 0, rely=0.2 )
        
        help = tk.StringVar()
        help.set('?')
       
        helpLabel = tk.Label(self, textvariable=help,bg='#A7D0FF',fg='#FF001F',relief=RIDGE,font="Verdana 20 bold")
        helpLabel.place(relx = 0.8,rely = 0.2)
        
        helpLabel1 = tk.Label(self, textvariable=help, bg='#A7D0FF',fg='#FF001F',relief=RIDGE,font="Verdana 20 bold")
        helpLabel1.place(relx = 0.8,rely = 0.3)
        
        helpLabel2 = tk.Label(self, textvariable=help,bg='#A7D0FF',fg='#FF001F',relief=RIDGE,font="Verdana 20 bold")
        helpLabel2.place(relx = 0.8,rely = 0.4)
       
        box = Balloon(self)
       
        box.bind_widget(helpLabel,balloonmsg="Please ensure your node name has no spaces")
        box.bind_widget(helpLabel1,balloonmsg="Please use the logical operators and, or, not\nYou can use brackets but there must be a space before and after them \nIf you want to create a reject condition use the keyword reject at the beginning ")
        box.bind_widget(helpLabel2,balloonmsg="This statement will be printed when the node is accepted")
      
        acceptance = tk.Label(self, textvariable=var5,bg='#A7D0FF',font="Verdana 20 ")
        acceptance.place( relx = 0, rely=0.3)
        
        statement = tk.Label(self, textvariable=var6,bg='#A7D0FF',font="Verdana 20 ")
        statement.place( relx = 0, rely=0.4)
        
        self.nameEntry = tk.Entry(self,font='Calibri 20')
        self.nameEntry.place(relx = 0.25,rely = 0.2,relheight=0.1,relwidth=0.5)
        
        self.acceptanceEntry = tk.Entry(self,font='Calibri 20')
        self.acceptanceEntry.place(relx = 0.25,rely = 0.3,relheight=0.1,relwidth=0.5)
        
        self.statementEntry = tk.Entry(self,font='Calibri 20')
        self.statementEntry.place(relx = 0.25,rely = 0.4,relheight=0.1,relwidth=0.5)
        
        addDefault = ttk.Button(self, text = 'NEXT',style= 'my.TButton',command= lambda: self.addDefault())
        addDefault.place(relheight= 0.1 , relwidth = 0.35, relx = 0.32, rely=0.85 )

        addCondition = ttk.Button(self, text = 'ADD CONDITION',style= 'my.TButton',command= lambda: self.addCondition())
        addCondition.place(relheight= 0.1 , relwidth = 0.35, relx = 0.32, rely=0.75 )

    def addDefault(self):
        
        self.info.name = self.name
        self.info.acceptance = self.acceptance
        self.info.statement = self.statement
        
        self.acceptanceEntry.delete(0,10000000)
        self.statementEntry.delete(0,10000000)
        self.nameEntry.delete(0,10000000)
                    
        self.controller.frameCreation(DefaultCreation, self.info)
        self.controller.show_frame(DefaultCreation)     
               
    def addCondition(self):
        
        if self.nameEntry.get() != '':
            self.name = self.nameEntry.get()
        acceptance = self.acceptanceEntry.get()
        statement = self.statementEntry.get()
        
        if acceptance != '':
            self.acceptance.append(acceptance)
            self.statement.append(statement)
        
        self.acceptanceEntry.delete(0,10000000)
        self.statementEntry.delete(0,10000000)
        
class MultiCreation(Background):
    
    def __init__(self,parent,controller, info):
       
        Background.__init__(self,parent)
        
        self.name = ''
        self.acceptance = []
        self.statement = []
        self.question = ''
        
        self.controller = controller
        self.info = info
        
        var = tk.StringVar()
        var.set("Domain Name:")
       
        var2 = tk.StringVar()
        var2.set(self.info.adf.name)
        
        var3 = tk.StringVar()
        var3.set('Create Node')
        
        var4 = tk.StringVar()
        var4.set('Name:')
        
        var5 = tk.StringVar()
        var5.set('Acceptance:')
        
        var6 = tk.StringVar()
        var6.set('Statement:')
        
        var7 = tk.StringVar()
        var7.set('Question:')
        
        help = tk.StringVar()
        help.set('?')
       
        helpLabel = tk.Label(self, textvariable=help,bg='#A7D0FF',fg='#FF001F',relief=RIDGE,font="Verdana 20 bold")
        helpLabel.place(relx = 0.8,rely = 0.2)
        
        helpLabel1 = tk.Label(self, textvariable=help,bg='#A7D0FF',fg='#FF001F',relief=RIDGE,font="Verdana 20 bold")
        helpLabel1.place(relx = 0.8,rely = 0.3)
        
        helpLabel2 = tk.Label(self, textvariable=help,bg='#A7D0FF',fg='#FF001F',relief=RIDGE,font="Verdana 20 bold")
        helpLabel2.place(relx = 0.8,rely = 0.4)
        
        helpLabel3 = tk.Label(self, textvariable=help,bg='#A7D0FF',fg='#FF001F',relief=RIDGE,font="Verdana 20 bold")
        helpLabel3.place(relx = 0.8,rely = 0.5)
       
        box = Balloon(self)
       
        box.bind_widget(helpLabel,balloonmsg="Please ensure your node name has no spaces")
        box.bind_widget(helpLabel1,balloonmsg="Please use the logical operators and, or, not\nYou can use brackets but there must be a space before and after them \nIf you want to create a reject condition use the keyword reject at the beginning ")
        box.bind_widget(helpLabel2,balloonmsg="This statement will be printed when the node is accepted")
        box.bind_widget(helpLabel3,balloonmsg="Set the question which will be asked to determine this acceptance condition\nThe possible answers will be taken from the acceptance conditions")
      
        
        label = tk.Label(self, textvariable=var,bg='#A7D0FF',font="Verdana 20")
        label.pack(side = 'left',anchor='nw')
        
        label2 = tk.Label(self, textvariable=var2,bg='#A7D0FF',font="Verdana 20")
        label2.pack(side = 'left',anchor='nw')
        
        label3 = tk.Label(self, textvariable=var3,bg='#A7D0FF',font="Verdana 20 underline")
        label3.place( relx = 0, rely=0.1 )
        
        name = tk.Label(self, textvariable=var4,bg='#A7D0FF',font="Verdana 20 ")
        name.place( relx = 0, rely=0.2 )
        
        acceptance = tk.Label(self, textvariable=var5,bg='#A7D0FF',font="Verdana 20 ")
        acceptance.place( relx = 0, rely=0.3)
        
        statement = tk.Label(self, textvariable=var6,bg='#A7D0FF',font="Verdana 20 ")
        statement.place( relx = 0, rely=0.4)
        
        question = tk.Label(self, textvariable=var7,bg='#A7D0FF',font="Verdana 20 ")
        question.place( relx = 0, rely=0.5)
       
        self.nameEntry = tk.Entry(self,font='Calibri 20')
        self.nameEntry.place(relx = 0.25,rely = 0.2,relheight=0.1,relwidth=0.5)
        
        self.acceptanceEntry = tk.Entry(self,font='Calibri 20')
        self.acceptanceEntry.place(relx = 0.25,rely = 0.3,relheight=0.1,relwidth=0.5)
        
        self.statementEntry = tk.Entry(self,font='Calibri 20')
        self.statementEntry.place(relx = 0.25,rely = 0.4,relheight=0.1,relwidth=0.5)
        
        self.questionEntry = tk.Entry(self,font='Calibri 20')
        self.questionEntry.place(relx = 0.25,rely = 0.5,relheight=0.1,relwidth=0.5)
        
        addDefault = ttk.Button(self, text = 'NEXT',style= 'my.TButton',command= lambda: self.addDefault())
        addDefault.place(relheight= 0.1 , relwidth = 0.35, relx = 0.32, rely=0.85 )

        addCondition = ttk.Button(self, text = 'ADD CONDITION',style= 'my.TButton',command= lambda: self.addCondition())
        addCondition.place(relheight= 0.1 , relwidth = 0.35, relx = 0.32, rely=0.65 )
        
        addQuestion = ttk.Button(self, text = 'ADD QUESTION',style= 'my.TButton',command= lambda: self.addQuestion())
        addQuestion.place(relheight= 0.1 , relwidth = 0.35, relx = 0.32, rely=0.75 )       
    
    def addQuestion(self):
        
        if self.questionEntry.get() != '':
            self.question = self.questionEntry.get()
            
            if self.info.editFlag:
                self.info.adf.questionOrder.append(self.nameEntry.get())
        
        self.questionEntry.delete(0,10000000)
    
    def addDefault(self):
                                 
        self.info.name = self.name
        self.info.acceptance = self.acceptance
        self.info.statement = self.statement
        self.info.question = self.question
        self.info.multiFlag = True
        
        self.acceptanceEntry.delete(0,10000000)
        self.statementEntry.delete(0,10000000)
        self.nameEntry.delete(0,10000000)
        self.questionEntry.delete(0,10000000)
                    
        self.controller.frameCreation(DefaultCreation, self.info)
        self.controller.show_frame(DefaultCreation)     
    
    def addCondition(self):
        
        if self.nameEntry.get() != '':
            self.name = self.nameEntry.get()
        acceptance = self.acceptanceEntry.get()
        statement = self.statementEntry.get()
        
        if acceptance != '':
            self.acceptance.append(acceptance)
            self.statement.append(statement)
        
        self.acceptanceEntry.delete(0,10000000)
        self.statementEntry.delete(0,10000000)
    
class DefaultCreation(Background):
    
    def __init__(self,parent,controller, info):
       
        Background.__init__(self,parent)
        
        self.info = info
        
        self.name = self.info.name
        self.acceptance = self.info.acceptance
        self.statement = self.info.statement
        self.question = self.info.question
        self.controller = controller
        
        var = tk.StringVar()
        var.set("Domain Name:")
       
        var2 = tk.StringVar()
        var2.set(self.info.adf.name)
        
        var3 = tk.StringVar()
        var3.set('Create Node')
        
        var6 = tk.StringVar()
        var6.set('Default Statement:')
        
        help = tk.StringVar()
        help.set('?')
       
        helpLabel = tk.Label(self, textvariable=help,bg='#A7D0FF',fg='#FF001F',relief=RIDGE,font="Verdana 20 bold")
        helpLabel.place(relx = 0.8,rely = 0.3)
        
        box = Balloon(self)
       
        box.bind_widget(helpLabel,balloonmsg="This statement will print if the node is not accepted")
        
        label = tk.Label(self, textvariable=var,bg='#A7D0FF',font="Verdana 20")
        label.pack(side = 'left',anchor='nw')

        label2 = tk.Label(self, textvariable=var2,bg='#A7D0FF',font="Verdana 20")
        label2.pack(side = 'left',anchor='nw')
        
        label3 = tk.Label(self, textvariable=var3,bg='#A7D0FF',font="Verdana 20 underline")
        label3.place( relx = 0, rely=0.1 )
        
        default = tk.Label(self, textvariable=var6,bg='#A7D0FF',font="Verdana 20 ")
        default.place( relx = 0, rely=0.2)

        self.defaultEntry = tk.Entry(self,font='Calibri 20')
        self.defaultEntry.place(relx = 0.25,rely = 0.3,relheight=0.1,relwidth=0.5)
       
        end = ttk.Button(self, text = 'END',style= 'my.TButton',command= lambda: self.end())
        end.place(relheight= 0.1 , relwidth = 0.1, relx = 0.46, rely=0.8 )
        
        addStatement = ttk.Button(self, text = 'ADD STATEMENT',style= 'my.TButton',command= lambda: self.addStatement())
        addStatement.place(relheight= 0.1 , relwidth = 0.35, relx = 0.32, rely=0.5 )
        
        addNode = ttk.Button(self, text = 'ADD T/F NODE',style= 'my.TButton',command= lambda: self.standardNode())
        addNode.place(relheight= 0.1 , relwidth = 0.35, relx = 0.32, rely=0.6 )
        
        addMulti = ttk.Button(self, text = 'ADD MULTI NODE',style= 'my.TButton',command= lambda: self.multiNode())
        addMulti.place(relheight= 0.1 , relwidth = 0.35, relx = 0.32, rely=0.7 )
    
    def addStatement(self):
        
        statement = self.defaultEntry.get()
        
        if statement != '':
            self.statement.append(statement)
        
        self.defaultEntry.delete(0,10000000)
        
    def end(self):
        
        self.addNodeADF()
        
        self.info.multiFlag = False
        
        questionGeneration = False
        
        for i in self.info.adf.nodes.values():
            
            if i.children == None and i.question == None:
                questionGeneration = True
                
        if questionGeneration == True:
            self.controller.frameCreation(QuestionCreation, self.info)
            self.controller.show_frame(QuestionCreation) 
        
        elif self.info.editFlag:
            self.controller.frameCreation(EditDomain, self.info)
            self.controller.show_frame(EditDomain)
            self.info.editFlag = False
        
        else:
            self.controller.frameCreation(SaveScreen, self.info)
            self.controller.show_frame(SaveScreen)                 

    def standardNode(self):
        
        self.addNodeADF()
        
        self.controller.frameCreation(NodeCreation, self.info)
        self.controller.show_frame(NodeCreation) 
        
        self.info.multiFlag = False
        
    def multiNode(self):

        self.addNodeADF()
        
        self.controller.frameCreation(MultiCreation, self.info)
        self.controller.show_frame(MultiCreation) 
            
    def addNodeADF(self):
        
        if self.info.multiFlag == True:
            self.info.adf.addMulti(self.name, self.acceptance, self.statement, self.question)
        else:
            self.info.adf.addNodes(self.name, self.acceptance, self.statement)

class QuestionCreation(Background):
    
    def __init__(self,parent,controller, info):
       
        Background.__init__(self,parent)
        
        self.info = info
        self.controller = controller
        
        name = self.info.adf.questionAssignment()
        
        self.nameVar = tk.StringVar()
        self.nameVar.set(name)
        self.name = name

        self.nameLabel = tk.Label(self, textvariable=self.nameVar,bg='#A7D0FF',font="Verdana 20 ")
        self.nameLabel.place( relx = 0.25, rely=0.2)

        var = tk.StringVar()
        var.set("Domain Name:")
       
        var2 = tk.StringVar()
        var2.set(self.info.adf.name)
        
        var3 = tk.StringVar()
        var3.set('Set Questions for Base-Level Factors')
        
        var4 = tk.StringVar()
        var4.set('Name:')
        
        var7 = tk.StringVar()
        var7.set('Question:')
        
        label = tk.Label(self, textvariable=var,bg='#A7D0FF',font="Verdana 20")
        label.pack(side = 'left',anchor='nw')
        
        label2 = tk.Label(self, textvariable=var2,bg='#A7D0FF',font="Verdana 20")
        label2.pack(side = 'left',anchor='nw')
        
        label3 = tk.Label(self, textvariable=var3,bg='#A7D0FF',font="Verdana 20 underline")
        label3.place( relx = 0, rely=0.1 )
        
        name = tk.Label(self, textvariable=var4,bg='#A7D0FF',font="Verdana 20 ")
        name.place( relx = 0, rely=0.2 )
        
        question = tk.Label(self, textvariable=var7,bg='#A7D0FF',font="Verdana 20 ")
        question.place( relx = 0, rely=0.3)

        self.questionEntry = tk.Entry(self,font='Calibri 20')
        self.questionEntry.place(relx = 0.25,rely = 0.3,relheight=0.1,relwidth=0.5)
        
        next = ttk.Button(self, text = 'NEXT',style= 'my.TButton',command= lambda: self.next())
        next.place(relheight= 0.1 , relwidth = 0.35, relx = 0.32, rely=0.85 )

        addQuestionEntry = ttk.Button(self, text = 'ADD QUESTION',style= 'my.TButton',command= lambda: self.addQuestion())
        addQuestionEntry.place(relheight= 0.1 , relwidth = 0.35, relx = 0.32, rely=0.75 )       
    
    def addQuestion(self):
        node = self.info.adf.nodes[self.name]
        
        if self.questionEntry != '':
            node.question = self.questionEntry.get()

            if self.info.editFlag:
                self.info.adf.questionOrder.append(node.name)
        
        self.questionEntry.delete(0,10000000)
        
    def next(self):
         
        if self.info.adf.questionAssignment() == None:
            
            if self.info.editFlag == True:
                self.controller.frameCreation(EditDomain, self.info)
                self.controller.show_frame(EditDomain)
                self.info.editFlag = False
            else:
                self.controller.frameCreation(QuestionOrder, self.info)
                self.controller.show_frame(QuestionOrder)
                
        else:
            name = self.info.adf.questionAssignment()
            self.nameVar.set(name)
            self.name = name

class QuestionOrder(Background):
    def __init__(self,parent,controller, info):
       
        Background.__init__(self,parent)
        
        self.info = info
        self.controller = controller

        var = tk.StringVar()
        var.set("Domain Name:")
       
        var2 = tk.StringVar()
        var2.set(self.info.adf.name)
        
        var3 = tk.StringVar()
        var3.set('Set Question Order')
        
        label = tk.Label(self, textvariable=var,bg='#A7D0FF',font="Verdana 20")
        label.pack(side = 'left',anchor='nw')
        
        label2 = tk.Label(self, textvariable=var2,bg='#A7D0FF',font="Verdana 20")
        label2.pack(side = 'left',anchor='nw')
        
        label3 = tk.Label(self, textvariable=var3,bg='#A7D0FF',font="Verdana 20 underline")
        label3.place( relx = 0, rely=0.1 )

        next = ttk.Button(self, text = 'DONE',style= 'my.TButton',command= lambda: self.done())
        next.place(relheight= 0.1 , relwidth = 0.3, relx = 0.65, rely=0.65 )

        up = ttk.Button(self, text = 'UP',style= 'my.TButton',command= lambda: self.up())
        up.place(relheight= 0.1 , relwidth = 0.3, relx = 0.65, rely=0.45 )

        down = ttk.Button(self, text = 'DOWN',style= 'my.TButton',command= lambda: self.down())
        down.place(relheight= 0.1 , relwidth = 0.3, relx = 0.65, rely=0.55 )
        
        self.nodeDict = {}
        
        self.questionList = []
        
        #CHANGE
        if self.info.adf.questionOrder == []:

            for node in self.info.adf.nodes.values():
                if node.question != None:
                    self.questionList.append(node.question)
                    self.nodeDict[node.question] = node
        
        else:
    
            for name in self.info.adf.questionOrder:
                node = self.info.adf.nodes[name]
                if node.question != None:
                    self.questionList.append(node.question)
                    self.nodeDict[node.question] = node
                         
            for node in self.info.adf.nodes.values():
                if node.question != None and node.question not in self.questionList:
                    self.questionList.append(node.question)
                    self.nodeDict[node.question] = node
        
        n = tk.StringVar(value=self.questionList)
        self.list = tk.Listbox(self, height=20, width = 70, listvariable = n)
        self.list.place(relx = 0.05, rely=0.25)

    def done(self):
        
        newOrder = []
        for i in self.questionList:
            
            x = self.nodeDict[i]
            newOrder.append(x.name)
        
        self.info.adf.questionOrder = newOrder
        
        self.controller.frameCreation(EditDomain, self.info)
        self.controller.show_frame(EditDomain)

    def up(self):
        
       try:
            index = self.list.curselection()[0]

            if index == 0:
                pass
            else:
                text=self.list.get(index)
                self.list.delete(index)
 
                self.list.insert(index-1, text)
                self.questionList.pop(index)
                self.questionList.insert(index-1, text)
                self.list.selection_set(index-1)
            
       except:
            pass

    def down(self):
        
        try:
            index = self.list.curselection()[0]
   

            text=self.list.get(index)
            self.list.delete(index)
        
            self.list.insert(index+1, text)
            self.questionList.pop(index)
            self.questionList.insert(index+1, text)
            self.list.selection_set(index+1)
            
        except:
            pass
    
class SaveScreen(Background):
    
    def __init__(self,parent,controller, info):
       
        Background.__init__(self,parent)
        
        self.info = info
        self.controller = controller
        
        name = self.info.adf.questionAssignment()
        
        self.name = name

        var = tk.StringVar()
        var.set("Domain Name:")
       
        var2 = tk.StringVar()
        var2.set(self.info.adf.name)
        
        var3 = tk.StringVar()
        var3.set('Save ADF as .xlsx file')
        
        var4 = tk.StringVar()
        var4.set('Filename:')
        
        help = tk.StringVar()
        help.set('?')
       
        helpLabel = tk.Label(self, textvariable=help,bg='#A7D0FF',fg='#FF001F',relief=RIDGE,font="Verdana 20 bold")
        helpLabel.place(relx = 0.8,rely = 0.2)
        
        box = Balloon(self)
       
        box.bind_widget(helpLabel,balloonmsg="Please ensure your filename has no spaces")
        
        label = tk.Label(self, textvariable=var,bg='#A7D0FF',font="Verdana 20")
        label.pack(side = 'left',anchor='nw')
        
        label2 = tk.Label(self, textvariable=var2,bg='#A7D0FF',font="Verdana 20")
        label2.pack(side = 'left',anchor='nw')
        
        label3 = tk.Label(self, textvariable=var3,bg='#A7D0FF',font="Verdana 20 underline")
        label3.place( relx = 0, rely=0.1 )
        
        name = tk.Label(self, textvariable=var4,bg='#A7D0FF',font="Verdana 20 ")
        name.place( relx = 0, rely=0.2 )
        
        self.fileName = tk.Entry(self,font='Calibri 20')
        self.fileName.place(relx = 0.25,rely = 0.2,relheight=0.1,relwidth=0.5)
        
        save = ttk.Button(self, text = 'SAVE',style= 'my.TButton',command= lambda: self.save())
        save.place(relheight= 0.1 , relwidth = 0.35, relx = 0.32, rely=0.75 ) 
        menu = ttk.Button(self, text = 'MENU',style= 'my.TButton',command= lambda: self.menu())
        menu.place(relheight= 0.1 , relwidth = 0.35, relx = 0.32, rely=0.85 ) 
        
    def save(self):
        
        if self.fileName.get() != '':
            filename = self.fileName.get()
            self.info.adf.saveNew(filename)
            
            varDone = tk.StringVar()
            varDone.set('DONE')
        
            self.done = tk.Label(self, textvariable=varDone,bg='#A7D0FF',font="Verdana 20")
            self.done.place( relx = 0.42, rely=0.4 )
        
        else:
            pass
            
    def menu(self):
        
        self.controller.show_frame(MainMenu)    

class Report(Background):
    
    def __init__(self,parent,controller, info):
       
       Background.__init__(self,parent)
       
       self.controller = controller
       self.info = info   
       
       self.graph = self.info.adf.visualiseNetwork(self.info.adf.case)
       
       var = tk.StringVar()
       var.set("Domain Name:")
       
       var2 = tk.StringVar()
       var2.set(self.info.adf.name)
       
       self.var3 = tk.StringVar()
       self.var3.set("Report for {}:".format(self.info.caseName))
       
       label = tk.Label(self, textvariable=var,bg='#A7D0FF',font="Verdana 20 underline")
       label.pack(side = 'left',anchor='nw')

       label2 = tk.Label(self, textvariable=var2,bg='#A7D0FF',font="Verdana 20")
       label2.pack(side = 'left',anchor='nw')
       
       label3 = tk.Label(self, textvariable=self.var3,bg='#A7D0FF',font="Verdana 20")
       label3.place( relx = 0.05, rely=0.1)
       
       nodeNames = set()
       for i in self.graph.get_node_list():
           nodeNames.add(i.get_name())
       
       #make a set so it only counts unique nodes
       numNodes = len(nodeNames)
       
       
       var4 = tk.StringVar()
       var4.set("{} nodes in this domain".format(numNodes))
       
       label4 = tk.Label(self, textvariable=var4,bg='#A7D0FF',font="Verdana 16")
       label4.place( relx = 0.05, rely=0.2)
       
       numAccepted = len(self.info.adf.case)
       
       var5 = tk.StringVar()
       var5.set("{} nodes accepted in this case".format(numAccepted))
       
       label5 = tk.Label(self, textvariable=var5,bg='#A7D0FF',font="Verdana 16")
       label5.place( relx = 0.05, rely=0.3)
       
       var6 = tk.StringVar()
       var6.set("Factors in this case: ")
       
       label6 = tk.Label(self, textvariable=var6,bg='#A7D0FF',font="Verdana 16")
       label6.place( relx = 0.05, rely=0.4)
       
       n = tk.StringVar()
       self.combo = ttk.Combobox(self, width = 50, textvariable = n, state='readonly')
  
       self.combo['values'] = self.info.case
       self.combo.place(relx = 0.45, rely=0.41)
       
       outcome = self.info.adf.statements[-1]
       var7 = tk.StringVar()
       var7.set("Outcome: {}".format(outcome))
       
       label7 = tk.Label(self, textvariable=var7,bg='#A7D0FF',font="Verdana 16")
       label7.place( relx = 0.05, rely=0.5)
       
       visualise = ttk.Button(self, text = 'VISUALISE',style= 'my.TButton',command= lambda: self.visualise())
       visualise.place(relheight= 0.1 , relwidth = 0.2, relx = 0.42, rely=0.75 )
        
       back = ttk.Button(self, text = 'BACK',style= 'my.TButton',command= lambda: self.back())
       back.place(relheight= 0.1 , relwidth = 0.2, relx = 0.42, rely=0.85 )
       
       self.fileName = tk.Entry(self,font='Calibri 16')
       self.fileName.place(relx = 0.3,rely = 0.65,relheight=0.07,relwidth=0.5)
        
       var4 = tk.StringVar()
       var4.set('Filename:')
       
       filename = tk.Label(self, textvariable=var4,bg='#A7D0FF',font="Verdana 16 ")
       filename.place( relx = 0.05, rely=0.65 )    

    def visualise(self):
        
        if self.fileName.get() != '':
            
            filename = self.fileName.get()
            
            self.graph.write_png('{}.png'.format(filename))
            
            os.startfile('{}.png'.format(filename))

    def back(self):
        self.controller.show_frame(Outcome)
            
app = UI()

app.mainloop()  