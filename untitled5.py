from tkinter import *
import random

root=Tk()
root.geometry("600x600")
root.title("aaaaa")

profitslabel = Label(root)
profitslabel.place(relx=0.5,rely=0.4,anchor=CENTER)
monthlabel=Label(root)
monthlabel.place(relx=0.5,rely=0.45,anchor=CENTER)
profitlabel=Label(root)
profitlabel.place(relx=0.5,rely=0.25,anchor=CENTER)
profits = []
month = []
def addmonth():
    months = len(month)
    addprofit= random.randint(5000,50000)
    profits.append(addprofit)
    month.append(months)
    profitslabel["text"]=profits
    monthlabel["text"]=month
def highest():
    highest=max(profits)
    highestorder=profits.index(highest)
    highestmonth=month[highestorder]
    profitlabel["text"]="the highest profit was "+str(highest)+",in "+str(highestmonth)
addmonth = Button(root,text="add month",command=addmonth)
addmonth.place(relx=0.5,rely=0.5,anchor=CENTER)
high = Button(root,text="find highest",command=highest)
high.place(relx=0.5,rely=0.6,anchor=CENTER)
root.mainloop()