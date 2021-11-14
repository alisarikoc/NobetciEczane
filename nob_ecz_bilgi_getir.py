from selenium import webdriver
import time 
from datetime import datetime
import qrcode

class nobet:
    def __init__(self):
        self.url="https://www.beo.org.tr/nobetci-eczaneler"
        self.browser=webdriver.Chrome(".\driver\chromedriver.exe")
        
    def nob_ecz_bul(self,an):
        self.browser.get(self.url)
        
        if an.day<10:
            gun = "0"+str(an.day)
        else:
            gun = str(an.day)
        if an.month<10:
            ay = "0"+str(an.month)
        else:
            ay = str(an.month)

        self.browser.find_element_by_xpath("/html/body/div[1]/div/div[2]/div/div[2]/div[2]/form/fieldset/div[1]/input").send_keys(gun+"-"+ay+"-"+str(an.year))
        self.browser.find_element_by_xpath("/html/body/div[1]/div/div[2]/div/div[2]/div[2]/form/fieldset/div[2]/select").send_keys("KESTEL")
        self.browser.find_element_by_xpath("/html/body/div[1]/div/div[2]/div/div[2]/div[2]/form/fieldset/div[3]/input").click()   
        self.nob_olan_ecz=self.browser.find_element_by_xpath("/html/body/div[1]/div/div[2]/div/div[3]/div/div/div[2]/h4").text
        self.nob_olan_ecz_bilgi=(self.browser.find_element_by_xpath("/html/body/div[1]/div/div[2]/div/div[3]/div/div/div[2]/p")).text.split("\n")        
        self.nob_olan_ecz_adres = self.nob_olan_ecz_bilgi[0]
        self.ek_adres_bilgisi = ""
        i = 1
        try:
            while type(self.nob_olan_ecz_bilgi[i].index("(")) == int:
                self.ek_adres_bilgisi += self.nob_olan_ecz_bilgi[i]
                i+=1
        except:
            self.nob_olan_ecz_telefon = self.nob_olan_ecz_bilgi[i]

        self.nob_olan_ecz_nobettarihleri = self.nob_olan_ecz_bilgi[-1].partition("arası nöbetçidir.")[0]
        nob_baslama_zaman=self.nob_olan_ecz_nobettarihleri.split("/")[0].strip()
        nob_bitirme_zaman=self.nob_olan_ecz_nobettarihleri.split("/")[1].strip()
        self.nob_bas_zmn = datetime.strptime(nob_baslama_zaman, '%d.%m.%Y %H:%M')
        self.nob_bit_zmn = datetime.strptime(nob_bitirme_zaman, '%d.%m.%Y %H:%M')
        
        time.sleep(1)
        self.browser.get("https://www.google.com/maps/dir/40.1984181,29.208069")
        self.browser.maximize_window()
        time.sleep(3)
        varis_noktasi=self.browser.find_element_by_class_name('tactile-searchbox-input')
        varis_noktasi.clear()
        varis_noktasi.send_keys(self.nob_olan_ecz_adres+" Kestel/Bursa")

        self.browser.find_element_by_xpath("//*[@id='omnibox-directions']/div/div[3]/div[2]/button/div").click()  
        
        baslangic_noktasi=self.browser.find_element_by_class_name('tactile-searchbox-input')
        baslangic_noktasi.clear()
        baslangic_noktasi.send_keys("Ahmet Vefik Paşa Mahallesi, Bursa Caddesi, No:45/2-A, Kestel/Bursa\n")    

        self.browser.find_element_by_xpath("//*[@id='omnibox-directions']/div/div[2]/div/div/div[1]/div[2]/button").click() # Adres tab'ında Araba buttonuna tıkla
        self.browser.find_element_by_xpath("//*[@id='pane']/div/div[3]/button").click() # Adres tab'ını kapat
        time.sleep(5) # Ekran oturana kadar 3 sn bekle
        self.browser.save_screenshot(".\\resim\googlegunluk.png")
        barkod_Icin_Url=self.browser.current_url
        imgg=qrcode.make(barkod_Icin_Url)
        type(imgg)
        imgg.save(".\\resim\QrCode.png")
        self.browser.quit()
