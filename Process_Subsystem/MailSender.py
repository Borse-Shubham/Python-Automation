
import os
from sys import *
import smtplib,ssl
import urllib.error
import urllib.request

def is_connected():
    try:
        urllib.request.urlopen('http://www.gmail.com')
        return True
    except urllib.error.URLError as err:
        return False

def MailSender(mailid):
    try:
        fromadd = "shubhamborse0911@gmail.com"
        toadd = mailid

        Message = """
        Hello %s,
        Harshal Kadam - 9 Vishay back
        """%(toadd)

        s = smtplib.SMTP('smtp.gmail.com',587)

        s.starttls()

        s.login(fromadd,"efji yhju wtee opdr")

        s.sendmail(fromadd,toadd,Message)

        s.quit()
        
        print("Mail Successfully Send")

    except Exception as E:
        print("Unable to send mail.",E)       

def main():

    if(len(argv) == 2):
        if (argv[1] == "-h") or (argv[1] == "-H"):
            print("This Script is used to send mail")
            exit()

        if (argv[1] == "-u") or (argv[1] == "-U"):
            print("usage : ApplicationName")
            exit()

    try:
        MailSender("harshalkadam3604@gmail.com")

    except ValueError:
        print("Error : Invalid datatype of input")

    except Exception as E:
        print("Error : Invalid input",E)

if __name__ == "__main__":
    main()