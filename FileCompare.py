import os
import re
import tkinter as tk
from tkinter import *
from tkinter.messagebox import *
from tkinter.filedialog import askdirectory

class Functions:
    def openFolder1(self, fileNames1, T1):
        dir1 = askdirectory()
        dirs1 = os.listdir(dir1)
        fileNames1.append(dirs1)
        T1.configure(state="normal")
        T1.insert(END, dir1 + " selected. \n")
        #for name in fileNames1:
         #   T1.insert(END, "\n".join(name))
        #T1.insert(END,"\n".join(fileNames) )
        T1.configure(state="disabled")

    def openFolder2(self, fileNames2, T2):
        dir2 = askdirectory()
        dirs2 = os.listdir(dir2)
        fileNames2.append(dirs2)
        T2.configure(state="normal")
        T1.insert(END, dir2 + " selected. \n")
        #for name in fileNames2:
        #    T2.insert(END, "\n".join(name))
        # T1.insert(END,"\n".join(fileNames) )
        T2.configure(state="disabled")

    def compare(self, dirs1, dirs2, T1, T2, T3):
        T1.configure(state="normal")
        T1.insert(END, "Comparing directories! \n")
        T1.configure(state="disabled")
        compWindow = tk.Toplevel()

        r2TextFrame1 = Frame(compWindow, bd=2)
        r2TextFrame1.grid(in_=compWindow, row=0, column=0, columnspan=4, sticky="NEW")
        compWindow.columnconfigure(0, weight=1)
        compWindow.rowconfigure(1, weight=1)

        r2T1 = Text(compWindow, width=100, height=15, bg="green")
        r2scrollbar1 = Scrollbar(compWindow)
        r2scrollbar1.config(command=r2T1.yview)
        r2T1.config(yscrollcommand=r2scrollbar1.set, state="disabled")
        r2T1.bind("<1>", lambda event: r2T1.focus_set())
        r2scrollbar1.pack(in_=r2TextFrame1, side=RIGHT, fill=Y)
        r2T1.pack(in_=r2TextFrame1, side=LEFT, fill=BOTH, expand=1)

        r2TextFrame2 = Frame(compWindow, bd=2)
        r2TextFrame2.grid(in_=compWindow, row = 1, column = 0, columnspan=4, sticky="NEW")

        r2T2 = Text(compWindow, bg="#7ef7ff")
        r2scrollbar2 = Scrollbar(compWindow)
        r2scrollbar2.config(command=r2T2.yview)
        r2T2.config(yscrollcommand=r2scrollbar2.set, state="disabled")
        r2T2.bind("<1>", lambda event: r2T2.focus_set())
        r2T2.pack(in_=r2TextFrame2, side=LEFT, fill=BOTH, expand=1)
        r2scrollbar2.pack(in_=r2TextFrame2, side=LEFT, fill=BOTH, expand=1)


        r2T3= Text(compWindow, bg="#f47eff")
        r2scrollbar3 = Scrollbar(compWindow)
        r2scrollbar3.config(command=r2T3.yview)
        r2T3.config(yscrollcommand=r2scrollbar3.set, state="disabled")
        r2T3.bind("<1>", lambda event: r2T3.focus_set())
        r2scrollbar3.pack(in_=r2TextFrame2, side=RIGHT, fill=BOTH, expand=1)
        r2T3.pack(in_=r2TextFrame2, side=RIGHT, fill=BOTH, expand=1)

        # r2T1.config(state="normal")
        # r2T1.insert(END, quote)
        # r2T1.config(state="disabled")
        #
        # r2T2.config(state="normal")
        # r2T2.insert(END, quote)
        # r2T2.config(state="disabled")
        #
        # r2T3.config(state="normal")
        # r2T3.insert(END, quote)
        # r2T3.config(state="disabled")


        r2T1.config(state="normal")
        r2T2.config(state="normal")
        r2T3.config(state="normal")
        r2T1.delete(1.0, END)
        r2T2.delete(1.0, END)
        r2T3.delete(1.0, END)
        r2T1.insert(END, "Files that appear in both directories: \n \n")
        r2T2.insert(END, "Files that only appear in directory 1: \n \n")
        r2T3.insert(END, "Files that only appear in directory 2: \n \n")
        for inArray in dirs1:
            for file in inArray:
                flag = 0
                for inArray2 in dirs2:

                    for fileComp in inArray2:
                        if(file == fileComp):
                            #print(file + " equals " + fileComp)
                            r2T1.insert(END, file + "\n")
                            flag = 1
                            print(repr(file) + " is in both directories")
                if(flag == 0):
                    r2T2.insert(END, file + "\n")

        for inArray in dirs2:
            for file in inArray:
                flag = 0
                for inArray2 in dirs1:

                    for fileComp in inArray2:
                        if (file == fileComp):
                            # print(file + " equals " + fileComp)
                            #r2T1.insert(END, file + "\n")
                            flag = 1
                            print(repr(file) + " is in both directories")
                if (flag == 0):
                    r2T3.insert(END, file + "\n")

        r2T1.config(state="disabled")
        r2T2.config(state="disabled")
        r2T3.config(state="disabled")
        buttonComp2 = Button(root, text='Compare', command=lambda: func.compare(dirs1, dirs2, T1, T2, T3))
        buttonComp.grid(row=0, column=3, sticky=E)

func = Functions()

root = tk.Tk()
root.title("Comparing 2 folders")
#root.configure(background='black')

dirs1 = []
dirs2 = []

textFrame1=Frame(root)
textFrame1.grid(in_=root, row=1, column=0, columnspan=4, sticky=NSEW)
root.columnconfigure(0, weight=1)
root.rowconfigure(1, weight=1)

T1 = Text(root, width = 35, height=15)
scrollbar1 = Scrollbar(root)
scrollbar1.config(command=T1.yview)
T1.config(yscrollcommand=scrollbar1.set, state="disabled")
T1.bind("<1>", lambda event: T1.focus_set())
scrollbar1.pack(in_=textFrame1, side=RIGHT, fill=Y)
T1.pack(in_=textFrame1, side=LEFT, fill=BOTH, expand=1)

textFrame2=Frame(root)
textFrame2.grid(in_=root, row=2, column=0, columnspan=4, sticky=NSEW)


T2 = Text(root, width = 35, height=15)
scrollbar2 = Scrollbar(root)
scrollbar2.config(command=T2.yview)
T2.config(yscrollcommand=scrollbar2.set, state='disabled')
T2.bind("<1>", lambda event: T2.focus_set())
scrollbar2.pack(in_=textFrame2, side=RIGHT, fill=Y)
T2.pack(in_=textFrame2, side=LEFT, fill=BOTH, expand=1)

textFrame3=Frame(root)
textFrame3.grid(in_=root, row=3, column=0, columnspan=4, sticky=NSEW)


T3 = Text(root, width = 35, height=15)
scrollbar3 = Scrollbar(root)
scrollbar3.config(command=T3.yview)
T3.config(yscrollcommand=scrollbar3.set, state='disabled')
T3.bind("<1>", lambda event: T3.focus_set())
scrollbar3.pack(in_=textFrame3, side=RIGHT, fill=Y)
T3.pack(in_=textFrame3, side=LEFT, fill=BOTH, expand=1)

buttonFold1 = Button(root, text='Choose Folder 1', command=lambda: func.openFolder1(dirs1, T1))
buttonFold2 = Button(root, text='Choose folder 2', command=lambda: func.openFolder2(dirs2, T1))
buttonComp = Button(root, text='Compare', command=lambda: func.compare(dirs1, dirs2, T1, T2, T3))

buttonFold1.grid(row=0, column=0, sticky=W)
buttonFold2.grid(row=0, column=1, sticky=W)
buttonComp.grid(row=0, column=3, sticky=W)

root.mainloop()

