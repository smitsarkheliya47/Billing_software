import random
import time
import datetime
import tkinter.messagebox
from tkinter import *
import mysql.connector
from tkinter import messagebox  

root=Tk()
root.geometry("1200x850+0+0")
root.title("BILLING SOFTWARE")
root.configure(background= 'powder blue')

def resturant ():
  p=CostofDrinks.get()
  q=CostofDishes.get()
  r=ServiceCharge.get()
  s=PaidTax.get()
  t=SubTotal.get()
  u=TotalCost.get()

  mydb=mysql.connector.connect(
       host="localhost",
       user="root",
       password="",
       database="resturant"
       )

  mycursor = mydb.cursor()

  sql="insert into details(cost_of_drink,cost_of_dish,service_charge,paid_tax,sub_total,total) values (%s,%s,%s,%s,%s,%s)"
  val=(p,q,r,s,t,u)
  mycursor.execute(sql,val)
  mydb.commit()
  messagebox.showinfo("record...","insert succesfully...!!!")

Tops= Frame(root, bg='Cadet Blue', bd=20, pady =5, relief=RIDGE)
Tops.pack(side=TOP)

lblTitle =Label(Tops, font=('arial',30,'bold'),width=48,text='BILLING SOFTWARE',bd=20,bg='Cadet Blue',fg='Cornsilk',justify=CENTER)
lblTitle.grid(row=0,column=0)

ReceiptCal_F= Frame(root, bg='Powder Blue', bd=10, relief=RIDGE)
ReceiptCal_F.pack(side=RIGHT)

Buttons_F=Frame(ReceiptCal_F, bg='Powder Blue', bd=3, relief=RIDGE)
Buttons_F.pack(side=BOTTOM)
Cal_F=Frame(ReceiptCal_F, bg='Powder Blue', bd=6, relief=RIDGE)
Cal_F.pack(side=TOP)
Receipt_F=Frame(ReceiptCal_F, bg='Powder Blue', bd=4, relief=RIDGE)
Receipt_F.pack(side=BOTTOM)

MenuFrame= Frame(root, bg='Cadet Blue', bd=10, relief=RIDGE)
MenuFrame.pack(side=LEFT)
Cost_F=Frame(MenuFrame, bg='Powder Blue', bd=4)
Cost_F.pack(side=BOTTOM)
Drinks_F=Frame(MenuFrame, bg='Cadet Blue', bd=10)
Drinks_F.pack(side=TOP)

Drinks_F=Frame(MenuFrame, bg='Powder Blue', bd=10, relief=RIDGE)
Drinks_F.pack(side=LEFT)

Drink_F=Frame(MenuFrame, bg='Cadet Blue', bd=10)
Drink_F.pack(side=TOP)

Drink_F=Frame(MenuFrame, bg='Powder Blue', bd=10, relief=RIDGE)
Drink_F.pack(side=LEFT)
Chickdish_F=Frame(MenuFrame, bg='Powder Blue', bd=10, relief=RIDGE)
Chickdish_F.pack(side=RIGHT)

#===========================================Variables==============================================

var1=IntVar()
var2=IntVar()
var3=IntVar()
var4=IntVar()
var5=IntVar()
var6=IntVar()
var7=IntVar()
var8=IntVar()
var9=IntVar()
var10=IntVar()
var11=IntVar()
var12=IntVar()
var13=IntVar()
var14=IntVar()
var15=IntVar()
var16=IntVar()
var17=IntVar()
var18=IntVar()
var19=IntVar()
var20=IntVar()
var21=IntVar()
var22=IntVar()
var23=IntVar()
var24=IntVar()

DateofOrder= StringVar()
Receipt_Ref= StringVar()
PaidTax= StringVar()
SubTotal= StringVar()
TotalCost= StringVar()
CostofDishes= StringVar()
CostofDrinks= StringVar()
ServiceCharge= StringVar()

text_Input= StringVar()
operator=""

E_Champagne=StringVar()
E_Irish=StringVar()
E_JackDaniel=StringVar()
E_Cocktail=StringVar()
E_RedWine=StringVar()
E_Scocth=StringVar()
E_JhonnyWalker=StringVar()
E_RedLabel=StringVar()

E_CocaCola=StringVar()
E_Sprite=StringVar()
E_Pepsi=StringVar()
E_MountainDew=StringVar()
E_Fanta=StringVar()
E_Mirinda=StringVar()
E_SevenUp=StringVar()
E_Maaza=StringVar()

E_PavBhaji=StringVar()
E_ButterBhaji=StringVar()
E_SpecialBhaji=StringVar()
E_CheeseBhaji=StringVar()
E_Hybiryani=StringVar()
E_SuratiLocho=StringVar()
E_JiraRice=StringVar()
E_Kajucurry=StringVar()

E_Champagne.set("0")
E_Irish.set("0")
E_JackDaniel.set("0")
E_Cocktail.set("0")
E_RedWine.set("0")
E_Scocth.set("0")
E_JhonnyWalker.set("0")
E_RedLabel.set("0")

E_CocaCola.set("0")
E_Sprite.set("0")
E_Pepsi.set("0")
E_MountainDew.set("0")
E_Fanta.set("0")
E_Mirinda.set("0")
E_SevenUp.set("0")
E_Maaza.set("0")

E_PavBhaji.set("0")
E_ButterBhaji.set("0")
E_SpecialBhaji.set("0")
E_CheeseBhaji.set("0")
E_Hybiryani.set("0")
E_SuratiLocho.set("0")
E_JiraRice.set("0")
E_Kajucurry.set("0")

DateofOrder.set(time.strftime("%d/%m/%Y"))

#===========================================Function Declaration======================================
def iExit():
    iExit = tkinter.messagebox.askyesno("Exit", "Are you sure?")
    if iExit>0:
        root.destroy()
        return

def Reset():
    E_Champagne.set("0")
    E_Irish.set("0")
    E_JackDaniel.set("0")
    E_Cocktail.set("0")
    E_RedWine.set("0")
    E_Scocth.set("0")
    E_JhonnyWalker.set("0")
    E_RedLabel.set("0")

    E_CocaCola.set("0")
    E_Sprite.set("0")
    E_Pepsi.set("0")
    E_MountainDew.set("0")
    E_Fanta.set("0")
    E_Mirinda.set("0")
    E_SevenUp.set("0")
    E_Maaza.set("0")

    E_PavBhaji.set("0")
    E_ButterBhaji.set("0")
    E_SpecialBhaji.set("0")
    E_CheeseBhaji.set("0")
    E_Hybiryani.set("0")
    E_SuratiLocho.set("0")
    E_JiraRice.set("0")
    E_Kajucurry.set("0")

    CostofDishes.set("0")
    CostofDrinks.set("0")
    ServiceCharge.set("0")
    SubTotal.set("0")
    PaidTax.set("0")
    TotalCost.set("0")

    var1.set(0)
    var2.set(0)
    var3.set(0)
    var4.set(0)
    var5.set(0)
    var6.set(0)
    var7.set(0)
    var8.set(0)
    var9.set(0)
    var10.set(0)
    var11.set(0)
    var12.set(0)
    var13.set(0)
    var14.set(0)
    var15.set(0)
    var16.set(0)
    var17.set(0)
    var18.set(0)
    var19.set(0)
    var20.set(0)
    var21.set(0)
    var22.set(0)
    var23.set(0)
    var24.set(0)

    txtChampagne.configure(state =DISABLED)
    txtIrish.configure(state=DISABLED)
    txtJackDaniel.configure(state=DISABLED)
    txtCocktail.configure(state=DISABLED)
    txtRedWine.configure(state=DISABLED)
    txtScocth.configure(state=DISABLED)
    txtJhonnyWalker.configure(state=DISABLED)
    txtRedLabel.configure(state=DISABLED)

    txtCocaCola.configure(state =DISABLED)
    txtSprite.configure(state=DISABLED)
    txtPepsi.configure(state=DISABLED)
    txtMountainDew.configure(state=DISABLED)
    txtFanta.configure(state=DISABLED)
    txtMirinda.configure(state=DISABLED)
    txtSevenUp.configure(state=DISABLED)
    txtMaaza.configure(state=DISABLED)
        
    txtPavBhaji.configure(state=DISABLED)
    txtButterBhaji.configure(state=DISABLED)
    txtSpecialBhaji.configure(state=DISABLED)
    txtCheeseBhaji.configure(state=DISABLED)
    txtHybiryani.configure(state=DISABLED)
    txtSuratiLocho.configure(state=DISABLED)
    txtJiraRice.configure(state=DISABLED)
    txtKajucurry.configure(state=DISABLED)

def CostofItem():
    Item1=float(E_Champagne.get())
    Item2=float(E_Irish.get())
    Item3=float(E_JackDaniel.get())
    Item4=float(E_Cocktail.get())
    Item5=float(E_RedWine.get())
    Item6=float(E_Scocth.get())
    Item7=float(E_JhonnyWalker.get())
    Item8=float(E_RedLabel.get())

    Item9=float(E_CocaCola.get())
    Item10=float(E_Sprite.get())
    Item11=float(E_Pepsi.get())
    Item12=float(E_MountainDew.get())
    Item13=float(E_Fanta.get())
    Item14=float(E_Mirinda.get())
    Item15=float(E_SevenUp.get())
    Item16=float(E_Maaza.get())

    Item17=float(E_PavBhaji.get())
    Item18=float(E_ButterBhaji.get())
    Item19=float(E_SpecialBhaji.get())
    Item20=float(E_CheeseBhaji.get())
    Item21=float(E_Hybiryani.get())
    Item22=float(E_SuratiLocho.get())
    Item23=float(E_JiraRice.get())
    Item24=float(E_Kajucurry.get())

    PriceofDrinks=((Item1 * 8000 ) + (Item2 * 6000) + (Item3 * 5500) + (Item4 * 2000)+ (Item5 * 4000) + (Item6 * 3500) + (Item7 * 5000) + (Item8 * 1500))+((Item9 * 30 ) + (Item10 * 30) + (Item11 * 30) + (Item12 * .80)+ (Item13 * 30) + (Item14 * 30) + (Item15 * 30) + (Item16 * 30))
    PriceofDishes=((Item17 * 150) + (Item18 * 250) + (Item19 * 230) + (Item20 * 200) + (Item21 * 300) + (Item22 * 280) + (Item23 * 200) + (Item24 * 400))


    DrinksPrice="Rs", str('%.2f'%(PriceofDrinks))
    DishesPrice="Rs", str('%.2f'%(PriceofDishes))
    CostofDishes.set(DishesPrice)
    CostofDrinks.set(DrinksPrice)
    SC="Rs", str('%.2f'%(20))
    ServiceCharge.set(SC)

    SubTotalofITEMS="Rs", str('%.2f'%(PriceofDrinks + PriceofDishes +2.5))
    SubTotal.set(SubTotalofITEMS)

    Tax="Rs", str('%.2f'%((PriceofDrinks + PriceofDishes + 2.5)*0.1))
    PaidTax.set(Tax)
    TT=((PriceofDrinks + PriceofDishes + 2.5) * 0.5)
    TC="Rs", str('%.2f'%(PriceofDishes + PriceofDrinks + 2.5 + TT))
        
    TotalCost.set(TC)
        


def Champagne():
    if(var1.get()==1):
        txtChampagne.configure(state= NORMAL)
        txtChampagne.focus()
        txtChampagne.delete('0', END)
        E_Champagne.set("")
    elif(var1.get()==0):
        txtChampagne.configure(state= DISABLED)
        E_Champagne.set("0")
def Irish():
    if(var2.get()==1):
        txtIrish.configure(state= NORMAL)
        txtIrish.focus()
        txtIrish.delete('0', END)
        E_Irish.set("")
    elif(var2.get()==0):
        txtIrish.configure(state= DISABLED)
        E_Irish.set("0")
def JackDaniel():
    if(var3.get()==1):
        txtJackDaniel.configure(state= NORMAL)
        txtJackDaniel.focus()
        txtJackDaniel.delete('0', END)
        E_JackDaniel.set("")
    elif(var3.get()==0):
        txtJackDaniel.configure(state= DISABLED)
        E_JackDaniel.set("0")
def Cocktail():
    if(var4.get()==1):
        txtCocktail.configure(state= NORMAL)
        txtCocktail.focus()
        txtCocktail.delete('0', END)
        E_Cocktail.set("")
    elif(var4.get()==0):
        txtCocktail.configure(state= DISABLED)
        E_Cocktail.set("0")
def RedWine():
    if(var5.get()==1):
        txtRedWine.configure(state= NORMAL)
        txtRedWine.focus()
        txtRedWine.delete('0', END)
        E_RedWine.set("")
    elif(var5.get()==0):
        txtRedWine.configure(state= DISABLED)
        E_RedWine.set("0")
def Scocth():
    if(var6.get()==1):
        txtScocth.configure(state= NORMAL)
        txtScocth.focus()
        txtScocth.delete('0', END)
        E_Scocth.set("")
    elif(var6.get()==0):
        txtScocth.configure(state= DISABLED)
        E_Scocth.set("0")
def JhonnyWalker():
    if(var7.get()==1):
        txtJhonnyWalker.configure(state= NORMAL)
        txtJhonnyWalker.focus()
        txtJhonnyWalker.delete('0', END)
        E_JhonnyWalker.set("")
    elif(var7.get()==0):
        txtJhonnyWalker.configure(state= DISABLED)
        E_JhonnyWalker.set("0")
def RedLabel():
    if(var8.get()==1):
        txtRedLabel.configure(state= NORMAL)
        txtRedLabel.focus()
        txtRedLabel.delete('0', END)
        E_RedLabel.set("")
    elif(var8.get()==0):
        txtRedLabel.configure(state= DISABLED)
        E_RedLabel.set("0")

def CocaCola():
    if(var9.get()==1):
        txtCocaCola.configure(state= NORMAL)
        txtCocaCola.focus()
        txtCocaCola.delete('0', END)
        E_CocaCola.set("")
    elif(var9.get()==0):
        txtCocaCola.configure(state= DISABLED)
        E_CocaCola.set("0")
def Sprite():
    if(var10.get()==1):
        txtSprite.configure(state= NORMAL)
        txtSprite.focus()
        txtSprite.delete('0', END)
        E_Sprite.set("")
    elif(var1.get()==0):
        txtSprite.configure(state= DISABLED)
        E_Sprite.set("0")        
def Pepsi():
    if(var11.get()==1):
        txtPepsi.configure(state= NORMAL)
        txtPepsi.focus()
        txtPepsi.delete('0', END)
        E_Pepsi.set("")
    elif(var11.get()==0):
        txtPepsi.configure(state= DISABLED)
        E_Pepsi.set("0")
def MountainDew():
    if(var12.get()==1):
        txtMountainDew.configure(state= NORMAL)
        txtMountainDew.focus()
        txtMountainDew.delete('0', END)
        E_MountainDew.set("")
    elif(var12.get()==0):
        txtMountainDew.configure(state= DISABLED)
        E_MountainDew.set("0")
def Fanta():
    if(var13.get()==1):
        txtFanta.configure(state= NORMAL)
        txtFanta.focus()
        txtFanta.delete('0', END)
        E_Fanta.set("")
    elif(var13.get()==0):
        txtFanta.configure(state= DISABLED)
        E_Fanta.set("0")
def Mirinda():
    if(var14.get()==1):
        txtMirinda.configure(state= NORMAL)
        txtMirinda.focus()
        txtMirinda.delete('0', END)
        E_Mirinda.set("")
    elif(var14.get()==0):
        txtMirinda.configure(state= DISABLED)
        E_Mirinda.set("0")
def SevenUp():
    if(var15.get()==1):
        txtSevenUp.configure(state= NORMAL)
        txtSevenUp.focus()
        txtSevenUp.delete('0', END)
        E_SevenUp.set("")
    elif(var15.get()==0):
        txtSevenUp.configure(state= DISABLED)
        E_SevenUp.set("0")
def Maaza():
    if(var16.get()==1):
        txtMaaza.configure(state= NORMAL)
        txtMaaza.focus()
        txtMaaza.delete('0', END)
        E_Maaza.set("")
    elif(var16.get()==0):
        txtMaaza.configure(state= DISABLED)
        E_Maaza.set("0")
    
def PavBhaji():
    if(var17.get()==1):
        txtPavBhaji.configure(state= NORMAL)
        txtPavBhaji.focus()
        txtPavBhaji.delete('0', END)
        E_PavBhaji.set("")
    elif(var17.get()==0):
        txtPavBhaji.configure(state= DISABLED)
        E_PavBhaji.set("0")
def ButterBhaji():
    if(var18.get()==1):
        txtButterBhaji.configure(state= NORMAL)
        txtButterBhaji.focus()
        txtButterBhaji.delete('0', END)
        E_ButterBhaji.set("")
    elif(var18.get()==0):
        txtButterBhaji.configure(state= DISABLED)
        E_ButterBhaji.set("0")
def SpecialBhaji():
    if(var19.get()==1):
        txtSpecialBhaji.configure(state= NORMAL)
        txtSpecialBhaji.focus()
        txtSpecialBhaji.delete('0', END)
        E_SpecialBhaji.set("")
    elif(var19.get()==0):
        txtSpecialBhaji.configure(state= DISABLED)
        E_SpecialBhaji.set("0")
def CheeseBhaji():
    if(var20.get()==1):
        txtCheeseBhaji.configure(state= NORMAL)
        txtCheeseBhaji.focus()
        txtCheeseBhaji.delete('0', END)
        E_CheeseBhaji.set("")
    elif(var20.get()==0):
        txtCheeseBhaji.configure(state= DISABLED)
        E_CheeseBhaji.set("0")
def Hybiryani():
    if(var21.get()==1):
        txtHybiryani.configure(state= NORMAL)
        txtHybiryani.focus()
        txtHybiryani.delete('0', END)
        E_Hybiryani.set("")
    elif(var21.get()==0):
        txtHybiryani.configure(state= DISABLED)
        E_Hybiryani.set("0")
def SuratiLocho():
    if(var22.get()==1):
        txtSuratiLocho.configure(state= NORMAL)
        txtSuratiLocho.focus()
        txtSuratiLocho.delete('0', END)
        E_SuratiLocho.set("")
    elif(var22.get()==0):
        txtSuratiLocho.configure(state= DISABLED)
        E_SuratiLocho.set("0")
def JiraRice():
    if(var23.get()==1):
        txtJiraRice.configure(state= NORMAL)
        txtJiraRice.focus()
        txtJiraRice.delete('0', END)
        E_JiraRice.set("")
    elif(var23.get()==0):
        txtJiraRice.configure(state= DISABLED)
        E_JiraRice.set("0")
def Kajucurry():
    if(var24.get()==1):
        txtKajucurry.configure(state= NORMAL)
        txtKajucurry.focus()
        txtKajucurry.delete('0', END)
        E_Kajucurry.set("")
    elif(var24.get()==0):
        txtKajucurry.configure(state= DISABLED)
        E_Kajucurry.set("0")
            
def Receipt():
    txtReceipt.delete("1.0",END)
    x= random.randint(10903, 609235)
    randomRef= str(x)
    Receipt_Ref.set("BILL" + randomRef)

def menu():
    new=Toplevel(root)
    new.geometry("500x250")
    new.title("New Window")

    
    listbox = Listbox(new, height = 10,
                  width = 25,
                  activestyle = 'dotbox',
                  font = "bold",
                  fg = "black")
    label = Label(new, text = " FOOD ITEMS")
    listbox.insert(1, " Champagne - ₹8000 ")
    listbox.insert(2, "Irish")
    listbox.insert(3, "Jack Daniel")
    listbox.insert(4, "Cocktail")
    listbox.insert(5, "Red Wine")
    label.pack()
    listbox.pack()
    new.mainloop()

    txtReceipt.insert(END, 'Receipt Ref:\t\t\t' + Receipt_Ref.get() + "\t" + DateofOrder.get() + "\n")
    txtReceipt.insert(END, 'Item:\t\t\t' + "No of Items\n")
    txtReceipt.insert(END, 'Champagne: \t\t\t\t' + E_Champagne.get() + "\n")
    txtReceipt.insert(END, 'Irish: \t\t\t\t' + E_Irish.get() + "\n")
    txtReceipt.insert(END, 'Jack Daniel: \t\t\t\t' + E_JackDaniel.get() + "\n")
    txtReceipt.insert(END, 'Cocktail: \t\t\t\t' + E_Cocktail.get() + "\n")
    txtReceipt.insert(END, 'Red Wine: \t\t\t\t' + E_RedWine.get() + "\n")
    txtReceipt.insert(END, 'Scocth: \t\t\t\t' + E_Scocth.get() + "\n")
    txtReceipt.insert(END, 'Jhonny Walker: \t\t\t\t' + E_JhonnyWalker.get() + "\n")
    txtReceipt.insert(END, 'Red Label: \t\t\t\t' + E_RedLabel.get() + "\n")

    txtReceipt.insert(END, 'CocaCola: \t\t\t\t' + E_CocaCola.get() + "\n")
    txtReceipt.insert(END, 'Sprite: \t\t\t\t' + E_Sprite.get() + "\n")
    txtReceipt.insert(END, 'Pepsi: \t\t\t\t' + E_Pepsi.get() + "\n")
    txtReceipt.insert(END, 'Mountain Dew: \t\t\t\t' + E_MountainDew.get() + "\n")
    txtReceipt.insert(END, 'Fanta: \t\t\t\t' + E_Fanta.get() + "\n")
    txtReceipt.insert(END, 'Mirinda: \t\t\t\t' + E_Mirinda.get() + "\n")
    txtReceipt.insert(END, '7 Up: \t\t\t\t' + E_SevenUp.get() + "\n")
    txtReceipt.insert(END, 'Maaza: \t\t\t\t' + E_Maaza.get() + "\n")
        
    txtReceipt.insert(END, 'Pav-Bhaji: \t\t\t\t' + E_PavBhaji.get() + "\n")
    txtReceipt.insert(END, 'Butter Bhaji: \t\t\t\t' + E_ButterBhaji.get() + "\n")
    txtReceipt.insert(END, 'Special Bhaji: \t\t\t\t' + E_SpecialBhaji.get() + "\n")
    txtReceipt.insert(END, 'Cheese Bhaji: \t\t\t\t' + E_CheeseBhaji.get() + "\n")
    txtReceipt.insert(END, 'Hydera Biryani: \t\t\t\t' + E_Hybiryani.get() + "\n")
    txtReceipt.insert(END, 'Surati Locho: \t\t\t\t' + E_SuratiLocho.get() + "\n")
    txtReceipt.insert(END, 'Jira-Rice: \t\t\t\t' + E_JiraRice.get() + "\n")
    txtReceipt.insert(END, 'Kaju-curry: \t\t\t\t' + E_Kajucurry.get() + "\n")
    txtReceipt.insert(END, 'Final Total: \t\t\t' + TotalCost.get() + "\n")



#===========================================Drinks===================================================

Champagne=Checkbutton(Drinks_F, text='Champagne', variable=var1, onvalue=1, offvalue=0, font=('arial',16,'bold')
                  ,bg= "Powder Blue", command=Champagne).grid(row=0,sticky=W)
Irish=Checkbutton(Drinks_F, text='Irish', variable=var2, onvalue=1, offvalue=0, font=('arial',16,'bold')
                  ,bg= "Powder Blue", command=Irish).grid(row=1,sticky=W)
JackDaniel=Checkbutton(Drinks_F, text='Jack Daniel', variable=var3, onvalue=1, offvalue=0, font=('arial',16,'bold')
                  ,bg= "Powder Blue", command=JackDaniel).grid(row=2,sticky=W)
Cocktail=Checkbutton(Drinks_F, text='Cocktail', variable=var4, onvalue=1, offvalue=0, font=('arial',16,'bold')
                  ,bg= "Powder Blue", command=Cocktail).grid(row=3,sticky=W)
RedWine=Checkbutton(Drinks_F, text='Red Wine', variable=var5, onvalue=1, offvalue=0, font=('arial',16,'bold')
                  ,bg= "Powder Blue", command=RedWine).grid(row=4,sticky=W)
Scocth=Checkbutton(Drinks_F, text='Scoth', variable=var6, onvalue=1, offvalue=0, font=('arial',16,'bold')
                  ,bg= "Powder Blue", command=Scocth).grid(row=5,sticky=W)
JhonnyWalker=Checkbutton(Drinks_F, text='Jhonny W', variable=var7, onvalue=1, offvalue=0, font=('arial',16,'bold')
                  ,bg= "Powder Blue", command=JhonnyWalker).grid(row=6,sticky=W)
RedLabel=Checkbutton(Drinks_F, text='Red Label', variable=var8, onvalue=1, offvalue=0, font=('arial',16,'bold')
                  ,bg= "Powder Blue", command=RedLabel).grid(row=7,sticky=W)


#===========================================Entry Box for Drinks===========================================================

txtChampagne= Entry(Drinks_F,font=('arial',16,'bold'),bd=8, width=6, justify=LEFT, state= DISABLED, textvariable=E_Champagne)
txtChampagne.grid(row=0,column=1)

txtIrish= Entry(Drinks_F,font=('arial',16,'bold'),bd=8, width=6, justify=LEFT, state= DISABLED, textvariable=E_Irish)
txtIrish.grid(row=1,column=1)

txtJackDaniel= Entry(Drinks_F,font=('arial',16,'bold'),bd=8, width=6, justify=LEFT, state= DISABLED, textvariable=E_JackDaniel)
txtJackDaniel.grid(row=2,column=1)

txtCocktail= Entry(Drinks_F,font=('arial',16,'bold'),bd=8, width=6, justify=LEFT, state= DISABLED, textvariable=E_Cocktail)
txtCocktail.grid(row=3,column=1)

txtRedWine= Entry(Drinks_F,font=('arial',16,'bold'),bd=8, width=6, justify=LEFT, state= DISABLED, textvariable=E_RedWine)
txtRedWine.grid(row=4,column=1)

txtScocth= Entry(Drinks_F,font=('arial',16,'bold'),bd=8, width=6, justify=LEFT, state= DISABLED, textvariable=E_Scocth)
txtScocth.grid(row=5,column=1)

txtJhonnyWalker= Entry(Drinks_F,font=('arial',16,'bold'),bd=8, width=6, justify=LEFT, state= DISABLED, textvariable=E_JhonnyWalker)
txtJhonnyWalker.grid(row=6,column=1)

txtRedLabel= Entry(Drinks_F,font=('arial',16,'bold'),bd=8, width=6, justify=LEFT, state= DISABLED, textvariable=E_RedLabel)
txtRedLabel.grid(row=7,column=1)


#===========================================Drinks2===================================================

CocaCola=Checkbutton(Drink_F, text='CocaCola', variable=var9, onvalue=1, offvalue=0, font=('arial',16,'bold')
                  ,bg= "Powder Blue", command=CocaCola).grid(row=0,column=2,sticky=W)
Sprite=Checkbutton(Drink_F, text='Sprite', variable=var10, onvalue=1, offvalue=0, font=('arial',16,'bold')
                  ,bg= "Powder Blue", command=Sprite).grid(row=1,column=2,sticky=W)
Pepsi=Checkbutton(Drink_F, text='Pepsi', variable=var11, onvalue=1, offvalue=0, font=('arial',16,'bold')
                  ,bg= "Powder Blue", command=Pepsi).grid(row=2,column=2,sticky=W)
MountainDew=Checkbutton(Drink_F, text='Mountain Dew', variable=var12, onvalue=1, offvalue=0, font=('arial',16,'bold')
                  ,bg= "Powder Blue", command=MountainDew).grid(row=3,column=2,sticky=W)
Fanta=Checkbutton(Drink_F, text='Fanta', variable=var13, onvalue=1, offvalue=0, font=('arial',16,'bold')
                  ,bg= "Powder Blue", command=Fanta).grid(row=4,column=2,sticky=W)
Mirinda=Checkbutton(Drink_F, text='Mirinda', variable=var14, onvalue=1, offvalue=0, font=('arial',16,'bold')
                  ,bg= "Powder Blue", command=Mirinda).grid(row=5,column=2,sticky=W)
SevenUp=Checkbutton(Drink_F, text='7 Up', variable=var15, onvalue=1, offvalue=0, font=('arial',16,'bold')
                  ,bg= "Powder Blue", command=SevenUp).grid(row=6,column=2,sticky=W)
Maaza=Checkbutton(Drink_F, text='Maaza', variable=var16, onvalue=1, offvalue=0, font=('arial',16,'bold')
                  ,bg= "Powder Blue", command=Maaza).grid(row=7,column=2,sticky=W)


#===========================================Entry Box for Drinks2===========================================================

txtCocaCola= Entry(Drink_F,font=('arial',16,'bold'),bd=8, width=6, justify=LEFT, state= DISABLED, textvariable=E_CocaCola)
txtCocaCola.grid(row=0,column=3)

txtSprite= Entry(Drink_F,font=('arial',16,'bold'),bd=8, width=6, justify=LEFT, state= DISABLED, textvariable=E_Sprite)
txtSprite.grid(row=1,column=3)

txtPepsi= Entry(Drink_F,font=('arial',16,'bold'),bd=8, width=6, justify=LEFT, state= DISABLED, textvariable=E_Pepsi)
txtPepsi.grid(row=2,column=3)

txtMountainDew= Entry(Drink_F,font=('arial',16,'bold'),bd=8, width=6, justify=LEFT, state= DISABLED, textvariable=E_MountainDew)
txtMountainDew.grid(row=3,column=3)

txtFanta= Entry(Drink_F,font=('arial',16,'bold'),bd=8, width=6, justify=LEFT, state= DISABLED, textvariable=E_Fanta)
txtFanta.grid(row=4,column=3)

txtMirinda= Entry(Drink_F,font=('arial',16,'bold'),bd=8, width=6, justify=LEFT, state= DISABLED, textvariable=E_Mirinda)
txtMirinda.grid(row=5,column=3)

txtSevenUp= Entry(Drink_F,font=('arial',16,'bold'),bd=8, width=6, justify=LEFT, state= DISABLED, textvariable=E_SevenUp)
txtSevenUp.grid(row=6,column=3)

txtMaaza= Entry(Drink_F,font=('arial',16,'bold'),bd=8, width=6, justify=LEFT, state= DISABLED, textvariable=E_Maaza)
txtMaaza.grid(row=7,column=3)



#===========================================Dishes=================================================================

PavBhaji=Checkbutton(Chickdish_F, text='Pav-Bhaji', variable=var17, onvalue=1, offvalue=0, font=('arial',16,'bold')
                  ,bg= "Powder Blue", command=PavBhaji).grid(row=0,sticky=W)
ButterBhaji=Checkbutton(Chickdish_F, text='Butter Bhaji', variable=var18, onvalue=1, offvalue=0, font=('arial',16,'bold')
                  ,bg= "Powder Blue", command=ButterBhaji).grid(row=1,sticky=W)
SpecialBhaji=Checkbutton(Chickdish_F, text='Special Bhaji', variable=var19, onvalue=1, offvalue=0, font=('arial',16,'bold')
                  ,bg= "Powder Blue",command=SpecialBhaji).grid(row=2,sticky=W)
CheeseBhaji=Checkbutton(Chickdish_F, text='Cheese Bhaji', variable=var20, onvalue=1, offvalue=0, font=('arial',16,'bold')
                  ,bg= "Powder Blue", command=CheeseBhaji).grid(row=3,sticky=W)
Hybiryani=Checkbutton(Chickdish_F, text='Hydera Biryani', variable=var21, onvalue=1, offvalue=0, font=('arial',16,'bold')
                  ,bg= "Powder Blue", command=Hybiryani).grid(row=4,sticky=W)
SuratiLocho=Checkbutton(Chickdish_F, text='Surati Locho', variable=var22, onvalue=1, offvalue=0, font=('arial',16,'bold')
                  ,bg= "Powder Blue", command=SuratiLocho).grid(row=5,sticky=W)
JiraRice=Checkbutton(Chickdish_F, text='Jira-Rice', variable=var23, onvalue=1, offvalue=0, font=('arial',16,'bold')
                  ,bg= "Powder Blue", command=JiraRice).grid(row=6,sticky=W)
Kajucurry=Checkbutton(Chickdish_F, text='Kaju-curry', variable=var24, onvalue=1, offvalue=0, font=('arial',16,'bold')
                  ,bg= "Powder Blue", command=Kajucurry).grid(row=7,sticky=W)


#===========================================Entry Box for Dishes===================================================

txtPavBhaji= Entry(Chickdish_F,font=('arial',16,'bold'),bd=8, width=6, justify=LEFT, state= DISABLED, textvariable=E_PavBhaji)
txtPavBhaji.grid(row=0,column=1)
txtButterBhaji= Entry(Chickdish_F,font=('arial',16,'bold'),bd=8, width=6, justify=LEFT, state= DISABLED, textvariable=E_ButterBhaji)
txtButterBhaji.grid(row=1,column=1)
txtSpecialBhaji= Entry(Chickdish_F,font=('arial',16,'bold'),bd=8, width=6, justify=LEFT, state= DISABLED, textvariable=E_SpecialBhaji)
txtSpecialBhaji.grid(row=2,column=1)
txtCheeseBhaji= Entry(Chickdish_F,font=('arial',16,'bold'),bd=8, width=6, justify=LEFT, state= DISABLED, textvariable=E_CheeseBhaji)
txtCheeseBhaji.grid(row=3,column=1)
txtHybiryani= Entry(Chickdish_F,font=('arial',16,'bold'),bd=8, width=6, justify=LEFT, state= DISABLED, textvariable=E_Hybiryani)
txtHybiryani.grid(row=4,column=1)
txtSuratiLocho= Entry(Chickdish_F,font=('arial',16,'bold'),bd=8, width=6, justify=LEFT, state= DISABLED, textvariable=E_SuratiLocho)
txtSuratiLocho.grid(row=5,column=1)
txtJiraRice= Entry(Chickdish_F,font=('arial',16,'bold'),bd=8, width=6, justify=LEFT, state= DISABLED, textvariable=E_JiraRice)
txtJiraRice.grid(row=6,column=1)
txtKajucurry= Entry(Chickdish_F,font=('arial',16,'bold'),bd=8, width=6, justify=LEFT, state= DISABLED, textvariable=E_Kajucurry)
txtKajucurry.grid(row=7,column=1)

#=======================================================Total Cost=========================================================
lblCostofDrinks =Label(Cost_F, font=('arial',14,'bold'),text='Cost of Drinks\t',bg='Powder Blue',fg='black')
lblCostofDrinks.grid(row=0,column=0, sticky=W)
txtCostofDrinks= Entry(Cost_F, width=28, bg='white', bd=7, font=('arial',10,'bold'), justify=RIGHT, textvariable=CostofDrinks)
txtCostofDrinks.grid(row=0, column=1)

lblCostofDishes =Label(Cost_F, font=('arial',14,'bold'),text='Cost of Dishes\t',bg='Powder Blue',fg='black')
lblCostofDishes.grid(row=1,column=0, sticky=W)
txtCostofDishes= Entry(Cost_F, width=28, bg='white', bd=7, font=('arial',10,'bold'), justify=RIGHT, textvariable=CostofDishes)
txtCostofDishes.grid(row=1, column=1)

lblServiceCharge =Label(Cost_F, font=('arial',14,'bold'),text='Service Charge\t',bg='Powder Blue',fg='black')
lblServiceCharge.grid(row=2,column=0, sticky=W)
lblServiceCharge= Entry(Cost_F, bg='white',width=28, bd=7, font=('arial',10,'bold'), justify=RIGHT, textvariable=ServiceCharge)
lblServiceCharge.grid(row=2, column=1)

#=======================================================Payment Information================================================
lblPaidTax =Label(Cost_F, font=('arial',14,'bold'),text='\tPaid Tax',bg='Powder Blue',fg='black')
lblPaidTax.grid(row=0,column=2, sticky=W)
txtPaidTax= Entry(Cost_F, width=27, bg='white', bd=7, font=('arial',10,'bold'), justify=RIGHT, textvariable=PaidTax)
txtPaidTax.grid(row=0, column=3)

lblSubTotal =Label(Cost_F, font=('arial',14,'bold'),text='\tSub Total',bg='Powder Blue',fg='black')
lblSubTotal.grid(row=1,column=2, sticky=W)
txtSubTotal= Entry(Cost_F, width=27, bg='white', bd=7, font=('arial',10,'bold'), justify=RIGHT, textvariable=SubTotal)
txtSubTotal.grid(row=1, column=3)

lblTotalCost =Label(Cost_F, font=('arial',14,'bold'),text='\tTotal Cost',bg='Powder Blue',fg='black')
lblTotalCost.grid(row=2,column=2, sticky=W)
txtTotalCost= Entry(Cost_F, width=27, bg='white', bd=7, font=('arial',10,'bold'), justify=RIGHT, textvariable=TotalCost)
txtTotalCost.grid(row=2, column=3)


#=======================================================Receipt============================================================

txtReceipt= Text(Receipt_F, width=40, height=6.7, bg='white', bd=4, font=('arial',12,'bold'))
txtReceipt.grid(row=0, column=0)

#=======================================================Buttons============================================================

btnTotal=Button(Buttons_F, padx=16, pady=1, bd=7, fg='black', font=('arial',16,'bold'),
                width=3, text="Total", bg="Powder Blue", command=CostofItem).grid(row=0,column=0)
btnReceipt=Button(Buttons_F, padx=16, pady=1, bd=7, fg='black', font=('arial',16,'bold'),
                width=4, text="Receipt", bg="Powder Blue", command=Receipt).grid(row=0,column=1)
btnReset=Button(Buttons_F, padx=16, pady=1, bd=7, fg='black', font=('arial',16,'bold'),
                width=3, text="Reset", bg="Powder Blue", command=Reset).grid(row=0,column=2)
btnExit=Button(Buttons_F, padx=16, pady=1, bd=7, fg='black', font=('arial',16,'bold'),
                width=3, text="Exit", bg="Powder Blue", command=iExit).grid(row=0,column=3)

#=======================================================Calculator Display=================================================

def btnClick(numbers):
    global operator
    operator= operator + str(numbers)
    text_Input.set(operator)

def btnClear():
    global operator
    operator = ""
    text_Input.set("")

def btnEquals():
    global operator
    sumup = str(eval(operator))
    text_Input.set(sumup)
    operator = ""

    txtDisplay= Entry(Cal_F, width=40, bg='white', bd=4, font=('arial',12,'bold'), justify=RIGHT, textvariable= text_Input)
    txtDisplay.grid(row=0, column=0, columnspan=4, pady=1)
    txtDisplay.insert(0,"0")



#=======================================================Calculator Buttons=================================================

btn7=Button(Cal_F, padx=16, pady=1, bd=7, fg='black', font=('arial',16,'bold'),
                width=3, text="7", bg="Powder Blue", command=lambda:btnClick(7)).grid(row=2,column=0)
btn8=Button(Cal_F, padx=16, pady=1, bd=7, fg='black', font=('arial',16,'bold'),
                width=3, text="8", bg="Powder Blue", command=lambda:btnClick(8)).grid(row=2,column=1)
btn9=Button(Cal_F, padx=16, pady=1, bd=7, fg='black', font=('arial',16,'bold'),
                width=3, text="9", bg="Powder Blue", command=lambda:btnClick(9)).grid(row=2,column=2)
btnAdd=Button(Cal_F, padx=16, pady=1, bd=7, fg='black', font=('arial',16,'bold'),
                width=3, text="+", bg="Powder Blue", command=lambda:btnClick("+")).grid(row=2,column=3)

#=======================================================Calculator Buttons=================================================

btn4=Button(Cal_F, padx=16, pady=1, bd=7, fg='black', font=('arial',16,'bold'),
                width=3, text="4", bg="Powder Blue", command=lambda:btnClick(4)).grid(row=3,column=0)
btn5=Button(Cal_F, padx=16, pady=1, bd=7, fg='black', font=('arial',16,'bold'),
                width=3, text="5", bg="Powder Blue", command=lambda:btnClick(5)).grid(row=3,column=1)
btn6=Button(Cal_F, padx=16, pady=1, bd=7, fg='black', font=('arial',16,'bold'),
                width=3, text="6", bg="Powder Blue", command=lambda:btnClick(6)).grid(row=3,column=2)
btnSub=Button(Cal_F, padx=16, pady=1, bd=7, fg='black', font=('arial',16,'bold'),
                width=3, text="-", bg="Powder Blue", command=lambda:btnClick("-")).grid(row=3,column=3)

#=======================================================Calculator Buttons=================================================

btn1=Button(Cal_F, padx=16, pady=1, bd=7, fg='black', font=('arial',16,'bold'),
                width=3, text="1", bg="Powder Blue", command=lambda:btnClick(1)).grid(row=4,column=0)
btn2=Button(Cal_F, padx=16, pady=1, bd=7, fg='black', font=('arial',16,'bold'),
                width=3, text="2", bg="Powder Blue", command=lambda:btnClick(2)).grid(row=4,column=1)
btn3=Button(Cal_F, padx=16, pady=1, bd=7, fg='black', font=('arial',16,'bold'),
                width=3, text="3", bg="Powder Blue", command=lambda:btnClick(3)).grid(row=4,column=2)
btnMulti=Button(Cal_F, padx=16, pady=1, bd=7, fg='black', font=('arial',16,'bold'),
                width=3, text="*", bg="Powder Blue", command=lambda:btnClick("*")).grid(row=4,column=3)

#=======================================================Calculator Buttons=================================================

btn0=Button(Cal_F, padx=16, pady=1, bd=7, fg='black', font=('arial',16,'bold'),
                width=3, text="0", bg="Powder Blue", command=lambda:btnClick(0)).grid(row=5,column=0)
btnClear=Button(Cal_F, padx=16, pady=1, bd=7, fg='black', font=('arial',16,'bold'),
                width=3, text="C", bg="Powder Blue", command=btnClear).grid(row=5,column=1)
btnEquals=Button(Cal_F, padx=16, pady=1, bd=7, fg='black', font=('arial',16,'bold'),
                width=3, text="=", bg="Powder Blue", command=btnEquals).grid(row=5,column=2)
btnDiv=Button(Cal_F, padx=16, pady=1, bd=7, fg='black', font=('arial',16,'bold'),
                width=3, text="/", bg="Powder Blue", command=lambda:btnClick("/")).grid(row=5,column=3)

btnMenu=Button(Buttons_F, padx=16, pady=1, bd=7, fg='black', font=('arial',16,'bold'),
                width=3, text="Menu", bg="Powder Blue", command=menu).grid(row=1,column=0)

btnInsert=Button(Buttons_F, padx=16, pady=1, bd=7, fg='black', font=('arial',16,'bold'),
                width=3, text="Insert", bg="Powder Blue", command=resturant).grid(row=1,column=1)

nDelete=Button(Buttons_F, padx=16, pady=1, bd=7, fg='black', font=('arial',16,'bold'),
                width=3, text="Delete", bg="Powder Blue", command=lambda:btnClick("Show Menu")).grid(row=1,column=2)
nUpdate=Button(Buttons_F, padx=16, pady=1, bd=7, fg='black', font=('arial',16,'bold'),
                width=3, text="Update", bg="Powder Blue", command=lambda:btnClick("Show Menu")).grid(row=1,column=3)


root.mainloop()