#!/usr/bin/env python3
from tkinter import Tk, Text, BOTH, W, N, E, S, PhotoImage
import tkinter as tk
from tkinter.constants import END, INSERT
from tkinter.ttk import Frame, Label
from PIL import Image, ImageTk
from nob_ecz_bilgi_getir import wet

class Example(Frame):
    def __init__(self):
        super().__init__()
        self.initUI()
    def initUI(self):
        self.master.title("Şule Eczanesi")
        self.pack(fill=BOTH, expand=True)
        self.columnconfigure(1, weight=1)
        self.columnconfigure(3, pad=7)
        self.rowconfigure(3, weight=1)
        self.rowconfigure(5, pad=7)

        lbl = Label(self, text="NÖBETÇİ ECZANELER",font="-family {Arial bold} -size 64",foreground="blue")
        lbl.grid(row=0,column=1, pady=4, padx=5,columnspan=2)
        
        # Animasyonlu Eczane Logosu
        frameCnt=12
        self.imagess=[PhotoImage(file='.\\resim\eczanelogo.gif',format = 'gif -index %i' %(i)) for i in range(frameCnt)]
        def update(ind):
            frame=self.imagess[ind]
            ind +=1
            if ind == frameCnt:
                ind=0
            self.panel.configure(image=frame)
            self.after(500,update,ind)
        self.panel=tk.Label(self) 
        self.panel.grid(row=0,column=0)
        self.after(0,update,0)

        #Google Resimi ekleme
        self.frameGoogle=Frame(self)
        self.frameGoogle.grid(row=1, column=1, columnspan=3, rowspan=4,padx=5, sticky=E+W+S+N)
        def on_resize(event):
            # resize the background image to the size of label
            image = bgimg.resize((event.width, event.height), Image.ANTIALIAS)
            # update the image of the label
            l.image = ImageTk.PhotoImage(image)
            l.config(image=l.image)
        bgimg = Image.open(".\\resim\googlegunluk.jpeg")
        l=tk.Label(self.frameGoogle)
        l.place(x=-20,y=-42,relwidth=1.05,relheight=1.05)
        l.bind('<Configure>', on_resize) # on_resize will be executed whenever label l is resized


        # Nönetçi Eczane Yazısı
        self.frameisim=Frame(self)
        self.frameisim.grid(row=1, column=0,pady=4,padx=4)
        abtn = Text(self.frameisim,width=30,height=3, font="-family {Arial bold} -size 16")
        abtn.insert(INSERT,wet.nob_olan_ecz)
        abtn.pack(fill="both",expand=True)
        abtn.configure(background="#d9d9d9")
        abtn.tag_configure("center",justify='center')
        abtn.tag_add("center",1.0,"end")


        # Nönetçi Eczane Adresi
        self.frame=Frame(self)
        self.frame.grid(row=2, column=0, pady=4,padx=4)
        self.Label2 = Text(self.frame,width=32,font="-family {Arial bold} -size 14")
        self.Label2.pack(side="left",fill="both",expand=True)
        self.Label2.insert(INSERT,"\U0001F3E0")
        #self.Label2.insert(END,"VANİ MEHMET MAH. ŞEHİT MUSTAFA KURT CAD. NO:20/A"+"\n")
        self.Label2.insert(END,wet.nob_olan_ecz_adres+wet.ek_adres_bilgisi+"\n")
        self.Label2.configure(background="#d9d9d9")
        self.Label2.configure(foreground="#000000")
        self.Label2.configure(highlightbackground="#f0f0f0f0f0f0")
        self.Label2.tag_add("ilk","1.0","1.1")
        self.Label2.tag_config("ilk",background="white",foreground="red")

        # Telefon numarası
        self.Label2.insert(END,"\n\U0000260E")
        #self.Label2.insert(END,"0224 373 07 77"+"\n")  
        self.Label2.insert(END,wet.nob_olan_ecz_telefon+"\n")       
        self.Label2.tag_add("ilk","3.0","3.1")

        # Nöbet tarihleri
        self.Label2.insert(END,"\n\U0001F551")
        #self.Label2.insert(END,"04.11.2021 18:00 / 05.11.2021 08:30 arası nöbetçidir."+"\n\n\n\n")    
        self.Label2.insert(END,wet.nob_olan_ecz_nobettarihleri+"\n\n\n\n")     
        self.Label2.tag_add("ilk","5.0","5.1")

        # Qr Codu ekleme
        load = Image.open(".\\resim\QrCode.png")
        load= load.resize((120,120))
        self.imageQr=ImageTk.PhotoImage(load)
        self.Label2.image_create(END,image=self.imageQr)
        self.Label2.tag_configure("center",justify='center')
        self.Label2.tag_add("center",6.0,"end")

def main():
    root = Tk()
    root.geometry("800x600+300+300")
    app = Example()
    root.mainloop()
if __name__ == '__main__':
    main()