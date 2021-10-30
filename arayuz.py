
from tkinter import *
from typing import Literal
from selenium import webdriver
import time

class nobet:
    def __init__(self):
        self.url="https://www.beo.org.tr/nobetci-eczaneler"
        self.browser=webdriver.Chrome("D:\dev\seleniumdene\driver\chromedriver.exe")
    def nob_ecz_bul(self):
        self.browser.get(self.url)
        day=time.localtime
        print(day)
        self.browser.find_element_by_xpath("/html/body/div[1]/div/div[2]/div/div[2]/div[2]/form/fieldset/div[2]/select").send_keys("KESTEL")
        self.browser.find_element_by_xpath("/html/body/div[1]/div/div[2]/div/div[2]/div[2]/form/fieldset/div[3]/input").click()
        
        #time.sleep(2)

    def google(self):
        self.browser.get("https://www.google.com/maps/dir/40.1984865,29.208209/40.199426,29.213213/@40.1987671,29.2099889,18z")
        #time.sleep(10)




master = Tk()
canvas=Canvas(master,height=520,width=800)
canvas.pack()

frame_ust=Frame(master,bg='#add8e6')
frame_ust.place(relx=0.005,rely=0.005,relwidth=0.99,relheight=0.07)

frame_alt_sol=Frame(master,bg='#add8e6')
frame_alt_sol.place(relx=0.005,rely=0.08,relwidth=0.23,relheight=0.915)

frame_alt_sag=Frame(master,bg='#add8e6')
frame_alt_sag.place(relx=0.240,rely=0.08,relwidth=0.755,relheight=0.915)

hatırlatma_tipi_etiket=Label(frame_ust,bg='#add8e6',text="NÖBETÇİ ECZANELER",font="Verdana 14 bold")
hatırlatma_tipi_etiket.pack(padx=10,pady=10,side=BOTTOM)

hatırlatma_tipi_opsiyon=StringVar(frame_ust)
hatırlatma_tipi_opsiyon.set("\t")

hatırlatma_tipi_acilirmenu=OptionMenu(
    frame_ust,
    hatırlatma_tipi_opsiyon,
    "doğumdünü",
    "alışveriş"
)
hatırlatma_tipi_acilirmenu.pack(padx=10,pady=10,side="right")

nob_ecz_adi=Label(frame_alt_sol,bg='#add8e6',text="ŞİFA ECZANESİ",font="Verdana 14 bold",)
nob_ecz_adi.pack(padx=10,pady=10,side=TOP)
nob_ecz_adres=Label(frame_alt_sol,bg='#add8e6',text="VANİ MEHMET MAH. HAKİM AYTEKİN BAYSAL SOK. NO:3/A",font="Verdana 12 bold",)
nob_ecz_adres.pack(padx=10,pady=20,side=TOP)






master.mainloop()

wet=nobet()
#wet.nob_ecz_bul()
wet.google()