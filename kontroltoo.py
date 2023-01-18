from tkinter import *
#aken
aken = Tk()
aken.title("porgandit")
aken.geometry("300x200")

#funktsioon
def porgandit():
    ringid = int(sisestus.get())
    count = 0
    b = 2
    while(ringid>1):
        ringid-=2
        count+=b
        b+=2
    valjund.config(text="porgandite arv:" +str(count))

#sildid
silt = Label(aken, text="Ringide arv: ")
silt.grid(row=0,column=0)
valjund = Label(aken, text="Siia tuleb porgandite arv")
valjund.grid(row=1,column=1)

#sisestusvali
sisestus = Entry(aken)
sisestus.grid(row=0,column=1)

#nupp
nupp = Button(aken, text="arvuta", width=10, command=porgandit)
nupp.grid(row=2, column=1)





aken.mainloop()