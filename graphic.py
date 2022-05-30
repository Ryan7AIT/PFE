# -*- coding: utf-8 -*-
"""
Created on Thu May 19 17:21:52 2022

@author: micro
"""

from tkinter import *
from tkinter import font as tkfont
from aggregation import aggregation




class MyWindow:
    
    def __init__(self, win):
        
        self.lbl0=Label(win, text='Bienvenu ')
        #self.lbl0.config(width=200)
        self.lbl0.place(x=350, y=10)
        
        self.lbl1=Label(win, text='La 1er fonction objective ')
        self.lbl2=Label(win, text='La 2eme fonction objective')
        
        self.lbl4=Label(win, text=' donner le vecteur de votre contraint')
        
        self.lbl5=Label(win, text=' donner Le poid maximum de sac :')
        
        
        #self.lbl7=Label(win, text='la valeur otimal de f :')
        
        self.lbl6=Label(win, text='les valeur de xi :')
        
        self.lbl8=Label(win, text='la valeur optimal de f apres la premier iteration :')
        self.lbl9=Label(win, text='la valeur optimal de f apres la 2eme iteration :')
        self.lbl10=Label(win, text='la valeur optimal de f apres la 3ene iteration :')
        self.lbl11=Label(win, text='la valeur optimal de f apres la 4eme iteration :')
        self.lbl12=Label(win, text='le poid de le sac utiliser  :')




        
 
        self.t1=Entry()
        self.t2=Entry()
        self.t4=Entry()
        self.t5=Entry()
        
        self.t6=Entry(bd=3)  #xi
        #self.t7=Entry() #f
        self.t8=Entry(bd=3) #f1
        self.t9=Entry(bd=3) #f2
        self.t10=Entry(bd=3) #f3
        self.t11=Entry(bd=3) #f4
        self.t12=Entry(bd=4) #f4


        
        #self.btn1 = Button(win, text='Add')
        
        self.btn2=Button(win, text='solver')
        
        self.lbl0.place(x=350, y=50)
        
        
        self.lbl1.place(x=100, y=100)
        self.t1.place(x=320, y=100)
        
        self.lbl2.place(x=100, y=150)
        self.t2.place(x=320, y=150)
        
        #self.b1=Button(win, text='Add', command=self.add)

        self.b2=Button(win, text='solver')
        self.b2.bind('<Button-1>', self.solve)
        
        #self.b1.place(x=100, y=150)
        self.b2.place(x=340, y=300)
        self.t5.place(x=320, y=450)
        
        
        self.lbl4.place(x=100, y=200)
        self.t4.place(x=320, y=200)
        
        self.lbl5.place(x=100, y=250)
        self.t5.place(x=320, y=250)
        
        self.lbl6.place(x=100, y=500)
        self.t6.place(x=320, y=500)
        
        #self.lbl7.place(x=100, y=550)
        #self.t7.place(x=320, y=550)
        
        self.lbl8.place(x=100, y=600)
        self.t8.place(x=420, y=600)
        
        self.lbl9.place(x=100, y=650)
        self.t9.place(x=420, y=650)
        
        self.lbl10.place(x=100, y=700)
        self.t10.place(x=420, y=700)
        
        self.lbl11.place(x=100, y=750)
        self.t11.place(x=420, y=750)
        
        self.lbl12.place(x=100, y=800)
        self.t12.place(x=420, y=800)
        

    def solve(self, event):
        data = {}
        #self.t3.delete(0, 'end')
        num1= self.t1.get()
        num2= self.t2.get()
        num4= self.t4.get()
        
        v1 = num1.split()
        v2 = num2.split()
        vecContraint = num4.split()
        lmda = 0.0001
        p=0.3
        poid= int(self.t5.get())
        
        #data[weights] = weight
        
        (optimalvalue,pmax,v1all,v2all,xi,alloptimal)= aggregation(vecContraint, v1, v2, lmda, p, poid)
        
        
        self.t6.insert(END, str(xi[0])  + ' , '  + str(xi[1]) + ' , '  + str(xi[2]) + ' , '  + str(xi[3]) + ' , '  + str(xi[4])   )
        
        self.t8.insert(END, str( alloptimal[0]) )


        self.t9.insert(END, str(alloptimal[1]))


        self.t10.insert(END, str(alloptimal[2]))
        
        self.t11.insert(END, str(alloptimal[3]))
        
        self.t12.insert(END, str(pmax))




        
        #self.t7.insert(END, str(optimalvalue))

window=Tk()
mywin=MyWindow(window)
window.title('Sac a Dos')
window.geometry("900x600")
window.mainloop()





