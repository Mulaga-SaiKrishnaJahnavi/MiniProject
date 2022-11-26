from tkinter import *
from functools import partial
#from pro import *
import imaplib
import smtplib
import email
import os
from datetime import datetime
import mimetypes
import smtplib
from getpass import getpass
#window
tkWindow = Tk() 
tkWindow.geometry('400x400') 
tkWindow.title('Login Form ')
tkWindow['background']='cyan'
#Title
titleLabel = Label(tkWindow, text=" Placement Messenger ",bg='lawn 
green').grid(row=0, column=1 ,columnspan=2)
def validateLogin():
 chWindow = Toplevel(tkWindow)
 chWindow.geometry('400x400')
 chWindow.title('Choice Form')
 chWindow['background']='cyan'
 chTitle=Label(chWindow,text="Choose your choice",bg="peach 
puff").grid(row=0,column=1)
 chLabel3 = Label(chWindow,text="Filter through Sender : 
").grid(row=2,column=0)
 chButton3 = Button(chWindow,text="Filter through 
Sender",command=SendEmails).grid(row=2,column=1)
 chLabel4 = Label(chWindow,text="Filter throuht both Sender and Date : 
").grid(row=4,column=0)
 chButton4 = Button(chWindow,text="Filter throuht both Sender and 
Date",command=SDEmails).grid(row=4,column=1)
def AllEmails():
 global Folder
 allWindow = Tk()
 allWindow.geometry('400x400')
 allWindow.title('AllEmails Form')
 alltitle = Label(allWindow, text=" Placement Messenger ").grid(row=0, 
column=1 ,columnspan=2)
 allFolder = Label(allWindow, text=" Folder :").grid(row=1, column=0)
 #Folder = StringVar()
 
 Folder = Entry(allWindow)
 Folder.grid(row=1, column=1)
 allLabel = Label(allWindow, text=" All mails are been sent 
").grid(row=2, column=1)
 #allButton = Button(allWindow, text="submit", 
command=lambda:button(Folder.get())).grid(row=5, 
column=1,columnspan=2)
 allButton = Button(allWindow, text="submit", 
command=sddt).grid(row=5, column=1,columnspan=2)
def button(e):
 print(e)
def DateEmails():
 global Folder
 global Year
 global Month
 global Date
 dateWindow = Tk()
 dateWindow.geometry('400x400')
 dateWindow.title('Emails Filtering Through Date Form')
 datetitle = Label(dateWindow, text=" Filtering through Date 
").grid(row=0, column=1 ,columnspan=2)
 dateFolderLabel = Label(dateWindow, text=" Folder :").grid(row=1, 
column=0)
 #Folder = StringVar()
 Folder = Entry(dateWindow)
 Folder.grid(row=1, column=1)
 dateYearLabel= Label(dateWindow, text=" Year :").grid(row=2, 
column=0)
 #Year = StringVar()
 Year = Entry(dateWindow)
 Year.grid(row=2, column=1)
 dateMonthLabel = Label(dateWindow, text=" Month(numbers only) 
:").grid(row=3, column=0)
 #Month= StringVar()
 Month = Entry(dateWindow)
 Month.grid(row=3, column=1)
 dateDateLabel = Label(dateWindow, text=" Date :").grid(row=4, 
column=0)
 #Date= StringVar()
 Date= Entry(dateWindow)
 Date.grid(row=4, column=1)
 dateloginButton = Button(dateWindow, text="submit").grid(row=5, 
column=1,columnspan=2)
def SendEmails():
 global Folder
 global Sender
 sendWindow = Tk()
 sendWindow.geometry('400x400')
 sendWindow.title('Emails Filtering Through Sender Form')
 sendWindow['background']='cyan'
 sendtitle = Label(sendWindow, text=" Filtering through Sender Email 
",bg="bisque2").grid(row=0, column=1 ,columnspan=2)
 sendFolderLabel = Label(sendWindow, text=" Folder :").grid(row=1, 
column=0)
 #Folder = StringVar()
 Folder= Entry(sendWindow)
 Folder.grid(row=1, column=1)
 SenderLabel = Label(sendWindow, text=" Sender(emailId) 
:").grid(row=2, column=0)
 #Sender = StringVar()
 Sender = Entry(sendWindow)
 Sender.grid(row=2, column=1)
 sendloginButton = Button(sendWindow, 
text="submit",bg="yellow",command=dt).grid(row=5, 
column=1,columnspan=2)
def SDEmails():
 global Folder
 global Year
 global Month
 global Date
 global Sender
 sdWindow = Tk()
 sdWindow.geometry('400x400')
 sdWindow.title('Emails Filtering Through Date and Sender Form')
 sdWindow['background']='cyan'
 titleLabel = Label(sdWindow, text=" Filtering through Sender & Date 
",bg='LemonChiffon2').grid(row=0, column=1 ,columnspan=2)
 #username label and text entry box
 sdFolderLabel = Label(sdWindow, text=" Folder :").grid(row=2, 
column=0)
 #global Folder
 #Folder = StringVar()
 #global sdFolderEntry
 Folder = Entry(sdWindow)
 Folder.grid(row=2, column=1)
 #print(Folder.get())
 
 sdYearLabel = Label(sdWindow, text=" Year :").grid(row=4, column=0)
 #global Year
 #Year = StringVar()
 Year= Entry(sdWindow)
 Year.grid(row=4, column=1)
 sdMonthLabel = Label(sdWindow, text=" Month(numbers only) 
:").grid(row=6, column=0)
 #global Month
 #Month= StringVar()
 Month= Entry(sdWindow)
 Month.grid(row=6, column=1)
 sdDateLabel = Label(sdWindow, text=" Date :").grid(row=8, column=0)
 #global Date
 #Date= StringVar()
 Date= Entry(sdWindow)
 Date.grid(row=8, column=1)
 sdSenderLabel = Label(sdWindow, text=" Sender(emailId) 
:").grid(row=10, column=0)
 #global Sender
 #Sender = StringVar()
 Sender = Entry(sdWindow)
 Sender.grid(row=10, column=1)
 sdloginButton = Button(sdWindow, text="click on 
me!",bg="yellow",command=sddt).grid(row=12, 
column=1,columnspan=2)
 
def sddt():
 global Folder
 Username=username.get()
 Password=password.get()
 
 folder=Folder.get()
 year=Year.get()
 month=Month.get()
 date=Date.get()
 sender=Sender.get()
 
 #print(username,password)
 
 #print(Folder,Year,Month,Date,Sender)
 #print(sdFolderEntry.get())
 year=int(year)
 month=int(month)
 date=int(date)
 #print(type(folder))
 ##print(type(date))
 #print(type(sender))
 #print(Username,Password,year,month,date,sender,folder)
 
getMailsUsingDateAndSender(Username,Password,year,month,date,send
er,folder)
 print("Mail has been send to students based on date given",date,"-
",month,"-",year,"and sender is",sender)
def getMailsUsingDateAndSender(Username, Password, year, month, 
date, fromEmail, folderName):
 #print(Username,Password,year,month,date,fromEmail,folderName)
 mail = imaplib.IMAP4_SSL("imap.gmail.com")
 #print("into the function")
 mail.login(Username, Password)
 print("Login success..........")
 
 mail.select("inbox")
 #year=int(year)
 #date=int(date)
 #month=int(month)
 # querying through search method to filter emails based on date we 
provided.
 x1 = datetime(year, month, date)
 startDate = x1.strftime("%d-%b-%Y")
 result, data = mail.search(None, '(SENTSINCE {0})'.format(startDate))
 inbox_item_list_date = data[0].split() 
 
 # querying through search method to filter emails based on sender mail 
we provided.
 result, data = mail.search(None, 'FROM', '"{}"'.format(fromEmail))
 inbox_item_list_sender = data[0].split() 
 
 #We take intersection of these sets so that we have UIDs of only those 
which satify both criteria. 
 inbox_item_list = list(set(inbox_item_list_date) & 
set(inbox_item_list_sender))
 
 counter = 0
 for item in inbox_item_list:
 counter+=1
 result2, email_data = mail.fetch(item,'(RFC822)')
 raw_email = email_data[0][1].decode("utf-8")
 email_message = email.message_from_string(raw_email)
 to_ = email_message['To']
 from_ = email_message['From']
 subject_ = email_message['Subject']
 date_ = email_message['date']
 sub1 = subject_
 d = date_
 to_ = "to: " + to_ + str("\n")
 from_ = "from: " + from_ + str("\n")
 date_ = "date: " + date_ + str("\n")
 subject__ = "subject: " + subject_ + str("\n")
 lenOfSubject = len(subject_)
 if (lenOfSubject > 30):
 subject_ = "exceed"+str(counter)
 for part in email_message.walk():
 if part.get_content_maintype == 'multipart':
 continue
 content_type = part.get_content_type()
 content_disposition = str(part.get("Content-Disposition"))
 filename = part.get_filename()
 
 ext = mimetypes.guess_extension(part.get_content_type())
 if ext == '.pdf' or ext == '.jpe' or ext == '.png' or ext == '.docx':
 if filename:
 save_path = os.path.join(os.getcwd(), folderName, subject_)
 if not os.path.exists(save_path):
 os.makedirs(save_path)
 with open(os.path.join(save_path, filename), 'wb') as fp:
 fp.write(part.get_payload(decode=True))
 fp.close()
 try:
 body = part.get_payload(decode=True).decode()
 except:
 pass
 if content_type == "text/plain" and "attachment" not in 
content_disposition:
 save_path = os.path.join(os.getcwd(), folderName, subject_)
 if not os.path.exists(save_path):
 os.makedirs(save_path)
 
 filename = "textfile.txt"
 with open(os.path.join(save_path, filename), 'w+', 
encoding='utf-8') as fp:
 fp.writelines(to_)
 fp.writelines(from_)
 fp.writelines(date_)
 fp.writelines(subject__)
 fp.writelines(body)
 fp.close()
 server = smtplib.SMTP_SSL("smtp.gmail.com",465)
 server.login(Username,Password)
 msg=subject__ +"\n"+body
 
to=['jahnavimulaga123@gmail.com','jaswanthimulaga121@gmail.com','v
ennelaranikuna@gmail.com']
 server.sendmail(Username,to,msg)
 server.quit()
 mail.close()
 mail.logout()
def dt():
 Username=username.get()
 Password=password.get()
 folder=Folder.get()
 sender=Sender.get()
 getMailsUsingSender(Username, Password, sender, folder)
 print("All filtered mails based sender",sender,"has been sent to 
students")
def getMailsUsingSender(username, password, fromEmail, folderName):
 mail = imaplib.IMAP4_SSL("imap.gmail.com")
 mail.login(username, password)
 print("Login success..........")
 
 mail.select("inbox")
 # querying through search method to filter emails based on sender mail 
we provided.
 result, data = mail.search(None, 'FROM', '"{}"'.format(fromEmail))
 inbox_item_list = data[0].split()
 counter = 0
 for item in inbox_item_list:
 counter+=1
 result2, email_data = mail.fetch(item,'(RFC822)')
 raw_email = email_data[0][1].decode("utf-8")
 email_message = email.message_from_string(raw_email)
 to_ = email_message['To']
 from_ = email_message['From']
 subject_ = email_message['Subject']
 date_ = email_message['date']
 to_ = "to: " + to_ + str("\n")
 from_ = "from: " + from_ + str("\n")
 date_ = "date: " + date_ + str("\n")
 subject__ = "subject: " + subject_ + str("\n")
 lenOfSubject = len(subject_)
 if (lenOfSubject > 30):
 subject_ = "exceed"+str(counter)
 print(subject_)
 for part in email_message.walk():
 if part.get_content_maintype == 'multipart':
 continue
 content_type = part.get_content_type()
 content_disposition = str(part.get("Content-Disposition"))
 filename = part.get_filename()
 
 ext = mimetypes.guess_extension(part.get_content_type())
 if ext == '.pdf' or ext == '.jpe' or ext == '.png' or ext == '.docx':
 if filename:
 save_path = os.path.join(os.getcwd(), folderName, subject_)
 if not os.path.exists(save_path):
 os.makedirs(save_path)
 with open(os.path.join(save_path, filename), 'wb') as fp:
 fp.write(part.get_payload(decode=True))
 fp.close()
 try:
 body = part.get_payload(decode=True).decode()
 except:
 pass
 if content_type == "text/plain" and "attachment" not in 
content_disposition:
 save_path = os.path.join(os.getcwd(), folderName, subject_)
 if not os.path.exists(save_path):
 os.makedirs(save_path)
 filename = "textfile.txt"
 with open(os.path.join(save_path, filename), 'w+', 
encoding='utf-8') as fp:
 fp.writelines(to_)
 fp.writelines(from_)
 fp.writelines(date_)
 fp.writelines(subject__)
 fp.writelines(body)
 fp.close()
 server = smtplib.SMTP_SSL("smtp.gmail.com",465)
 server.login(username,password)
 msg=subject__ +"\n"+body
 
to=['jahnavimulaga123@gmail.com','jaswanthimulaga121@gmail.com']
 server.sendmail(username,to,msg)
 server.quit()
 mail.close()
 mail.logout()
def getAllEmails(username, password, folderName):
 # used to make an connection over imap4 server over an SSL encrypted 
socket
 # in our case that server is gmail
 # If port is omitted, the standard IMAP4-over-SSL port (993) is used
 mail = imaplib.IMAP4_SSL("imap.gmail.com") 
 # login is used to identify client
 mail.login(username, password)
 print("Login success..........")
 
 # we can select any directory using mail.list(), in our case we have 
selected inbox.
 mail.select("inbox")
 
 # mails are identified by UID number
 result, data = mail.uid('search',None,'ALL')
 
 #This is a list containing UID number for each mail present in Inbox 
mail.
 inbox_item_list = data[0].split() 
 
 counter = 0
 # iterating over UIDs
 for item in inbox_item_list:
 counter+=1
 #result2 contains confirmation in the form of "OK" and email_data 
contains information regarding the mail.
 result2, email_data = mail.uid('fetch',item,'(RFC822)')
 
 raw_email = email_data[0][1].decode("utf-8") 
 
 #Return a message object structure from a string.
 email_message = email.message_from_string(raw_email)
 #getting information about the mail like to, from,subject, date.
 to_ = email_message['To'] 
 from_ = email_message['From']
 subject_ = email_message['Subject']
 date_ = email_message['date']
 
 # setting the format to save in text file. 
 to_ = "to: " + to_ + str("\n")
 from_ = "from: " + from_ + str("\n")
 date_ = "date: " + date_ + str("\n")
 subject__ = "subject: " + subject_ + str("\n")
 
 
 # if path length exceeds a certain limit, then changing the name of 
mail folder.
 lenOfSubject = len(subject_)
 if (lenOfSubject > 30):
 #Setting subject equals to exceed + counter if len of subject is more 
than 30.
 subject_ = "exceed"+str(counter) 
 
 # accessing the subparts of email_message
 for part in email_message.walk():
 if part.get_content_maintype == 'multipart':
 continue
 content_type = part.get_content_type()
 content_disposition = str(part.get("Content-Disposition"))
 
 filename = part.get_filename()
 # using mimetype to know the extension of attachment
 # comment below 2 lines to allow all types of format to download
in all functions. 
 ext = mimetypes.guess_extension(part.get_content_type())
 # allowing pdf, jpg, png and doc format only
 if ext == '.pdf' or ext == '.jpe' or ext == '.png' or ext == '.docx':
 if filename:
 save_path = os.path.join(os.getcwd(), folderName, subject_)
 if not os.path.exists(save_path):
 os.makedirs(save_path)
 with open(os.path.join(save_path, filename), 'wb') as fp:
 fp.write(part.get_payload(decode=True))
 fp.close()
 # getting the body part of the mail.
 try:
 body = part.get_payload(decode=True).decode() 
 except:
 pass
 
 # saving the required information in a file named as "textfile.txt".
 if content_type == "text/plain" and "attachment" not in 
content_disposition:
 save_path = os.path.join(os.getcwd(), folderName, subject_)
 if not os.path.exists(save_path):
 os.makedirs(save_path)
 filename = "textfile.txt"
 with open(os.path.join(save_path, filename), 'w+', 
encoding='utf-8') as fp:
 fp.writelines(to_)
 fp.writelines(from_)
 fp.writelines(date_)
 fp.writelines(subject__)
 fp.writelines(body) #Add here if any other information you 
want to add in text file.
 fp.close()
 server = smtplib.SMTP_SSL("smtp.gmail.com",465)
 server.login(username,password)
 msg=subject__ +"\n"+body
 to=['miniproject296@gmail.com']
 server.sendmail(username,to,msg)
 server.quit()
 mail.close()
 mail.logout()
def getMailsUsingDate(username, password, year, month, date, 
folderName):
 mail = imaplib.IMAP4_SSL("imap.gmail.com")
 mail.login(username, password)
 print("Login success..........")
 
 mail.select("inbox")
 
 # seeting the year, month, date in strftime format.
 x1 = datetime(year, month, date)
 startDate = x1.strftime("%d-%b-%Y")
 # querying through search method to filter emails based on date we 
provided.
 result, data = mail.search(None, '(SENTSINCE {0})'.format(startDate)) 
 inbox_item_list = data[0].split() 
 counter = 0
 for item in inbox_item_list:
 counter+=1
 result2, email_data = mail.fetch(item,'(RFC822)')
 raw_email = email_data[0][1].decode("utf-8")
 email_message = email.message_from_string(raw_email)
 to_ = email_message['To']
 from_ = email_message['From']
 subject_ = email_message['Subject']
 date_ = email_message['date']
 to_ = "to: " + to_ + str("\n")
 from_ = "from: " + from_ + str("\n")
 date_ = "date: " + date_ + str("\n")
 subject__ = "subject: " + subject_ + str("\n")
 lenOfSubject = len(subject_)
 if (lenOfSubject > 30):
 subject_ = "exceed"+str(counter)
 for part in email_message.walk():
 if part.get_content_maintype == 'multipart':
 continue
 content_type = part.get_content_type()
 content_disposition = str(part.get("Content-Disposition"))
 filename = part.get_filename()
 
 ext = mimetypes.guess_extension(part.get_content_type())
 if ext == '.pdf' or ext == '.jpe' or ext == '.png' or ext == '.docx':
 
 if filename:
 save_path = os.path.join(os.getcwd(), folderName, subject_)
 if not os.path.exists(save_path):
 os.makedirs(save_path)
 with open(os.path.join(save_path, filename), 'wb') as fp:
 fp.write(part.get_payload(decode=True))
 fp.close()
 try:
 body = part.get_payload(decode=True).decode()
 except:
 pass
 if content_type == "text/plain" and "attachment" not in 
content_disposition:
 save_path = os.path.join(os.getcwd(), folderName, subject_)
 if not os.path.exists(save_path):
 os.makedirs(save_path)
 filename = "textfile.txt"
 with open(os.path.join(save_path, filename), 'w+', 
encoding='utf-8') as fp:
 fp.writelines(to_)
 fp.writelines(from_)
 fp.writelines(date_)
 fp.writelines(subject__)
 fp.writelines(body)
 fp.close()
 server = smtplib.SMTP_SSL("smtp.gmail.com",465)
 server.login(username,password)
 msg=subject__ +"\n"+body
 
to=['jahnavimulaga123@gmail.com','jaswanthimulaga121@gmail.com']
 server.sendmail(username,to,msg)
 server.quit()
 mail.close()
 mail.logout()
 
 
#username label and text entry box
usernameLabel = Label(tkWindow, text=" User Name :").grid(row=1, 
column=0)
#username=StringVar()
#username
username = Entry(tkWindow)
username.grid(row=1, column=1)
#password label and password entry box
passwordLabel = Label(tkWindow,text=" Password :").grid(row=4, 
column=0) 
#password = StringVar()
#global password
password = Entry(tkWindow, show='*')
password.grid(row=4, column=1)
global Folder
global Year
global Month
global Date
global Sender
#validateLogin = partial(validateLogin, username, password)
#login button
loginButton = Button(tkWindow, text="Login",bg="yellow" 
,command=validateLogin).grid(row=5, column=1,columnspan=2)
#page2
tkWindow.mainloop()
