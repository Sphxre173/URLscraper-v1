import os
import bs4
import pandas as pd
import time as t
import requests as rq
import webbrowser as web

class Scrape:
  def __init__(self):
    self.count = 1
    self.url = ""
    self.result = ""
    self.stage2 = ""
    self.e = ""
    self.lizt = []
    self.wait_anims = ["Loading. < ÓwÓ <", 
                       "Loading.. ~< -w- <", 
                       "Loading... > ÒwÒ =>", 
                       "loading.. > -w- >~"]
    
  def WelcomeAndCheck(self):
    print("Welcome to web scraper")
    t.sleep(5)
    while True:
      try:
        self.url = input("Your url ? : ")
        self.respond = rq.get(self.url)
        self.result = self.respond.status_code
        for i in self.wait_anims:
          os.system("clear")
          print(i)
          t.sleep(1.5)
        if self.result == 200:
          print("Success")
          t.sleep(1)
          self.processing()
          break
        else:
          raise Exception()
      except:
        print("cannot connect to server, try again or check your url")
        
  def processing(self):
    os.system("clear")
    print("stage 1 passed")
    self.stage2 = bs4.BeautifulSoup(self.respond.text, "html.parser")
    while True:
      try:
        self.stage3asktag = str(input("tag? : "))
        self.stage3askclassortag = str(input("class or tag : "))
        self.stage3askclassname = str(input("name of class/id? : "))
        
        self.stage3 = self.stage2.find_all(self.stage3asktag, {self.stage3askclassortag : self.stage3askclassname})
        
        if self.stage3:
          self.lizt = []
          for i in self.stage3:
            self.e = i.text
            self.lizt.append(self.e)
          print(f"Prewiew : {self.lizt}")
          self.check_save_xl()
        else:
          raise Exception()
      except:
        print("cannot scrape")
        t.sleep(2)
        os.system("clear")
    
  def check_save_xl(self):
    os.system("clear")
    print("do you want to save as xl?")
    while True:
      try:
        os.system("clear")
        self.save_check_xl = str(input("Excel [y/n]")).lower()
        
        if self.save_check_xl == "y":
          self.excel()
          break
        elif self.save_check_xl == "n":
          self.check_save_txt()
        else:
          raise Exception()
      except:
        print("only type y or n")

  def excel(self):
    os.system("clear")
    self.name_content = str(input("the name of column? : "))
    self.dataframe = pd.DataFrame({self.name_content : self.lizt})
    self.filename = str(input("file name? : "))
    self.dataframe.to_excel(f"{self.filename}.xlsx", index=False)
    self.check_save_txt()
    
  def check_save_txt(self):
    os.system("clear")
    print("do you want to save as xl or txt file?")
    while True:
      try:
        self.save_check_txt = input(".txt? [y/n]").lower()
        if self.save_check_txt == "y":
          self.text()
        elif self.save_check_txt == "n":
          pass
        else:
          raise Exception()
      except:
        print("only type y or n")
        
  def text(self):
    self.txt_filename = input("file name? : ")
    with open(f"{self.txt_filename}.txt", "w") as file:
      for i in self.stage3:
        self.e = i.text
        file.write(self.e + "\n")
      
  
  def start(self):
    self.WelcomeAndCheck()

test = Scrape()
test.start()
