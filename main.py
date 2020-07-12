from tkinter import *
import tkinter.messagebox as tkm
import json
import os
import smtplib, ssl

# frames
class CheckinApp:
    def __init__(self, master):
        self.submitted
        self.sendemail
        frame1 = Frame(master)
        frame1.pack(padx=2, pady=2)
        frame2 = Frame(master)
        frame2.pack(padx=2, pady=2)
        frame3 = Frame(master)
        frame3.pack(padx=2, pady=(2, 20)) 
        # Texts
        nm_txt = Label(frame1, text="Please enter your Name:", font="Bold").grid(column=0, row=1, padx=5, pady=2)
        who_txt = Label(frame1, text="Resident Visiting", font="Bold").grid(column=4, row=1, padx=5, pady=2)
        pur_txt = Label(frame1, text="Reason for Visit", font="Bold").grid(column=5, row=1, padx=5, pady=5)
        # Entry Boxes
        name = StringVar()
        who = StringVar()
        purp = StringVar()
        temp = StringVar()
        phone = StringVar()
        self.nm_entry = Entry(frame1, textvariable=name)
        self.nm_entry.grid(columnspan=4, row=2, padx=8, pady=2, sticky='n'+'e'+'w'+'s')
        self.who_entry = Entry(frame1, textvariable=who)
        self.who_entry.grid(column=4, row=2, padx=8, pady=2, sticky='n'+'e'+'w'+'s')
        self.pur_entry = Entry(frame1, textvariable=purp)
        self.pur_entry.grid(column=5, row=2, padx=8, pady=2, sticky='n'+'e'+'w'+'s')
        
        temp_txt = Label(frame3, text="Temperature").grid(column=0, row=0)
        self.temp_entry = Entry(frame3, textvariable=temp)
        self.temp_entry.grid(column=0, row=1, padx=(1, 10))
        ph_txt = Label(frame3, text="Phone Number").grid(column=2, row=0)
        self.ph_entry = Entry(frame3, textvariable=phone)
        self.ph_entry.grid(column=2, row=1, padx=(10, 5), pady=5)
        # the questions frame starts here
        question1 = Label(frame2, text='Q1. Have you recently been in an airport or traveled out of state?')
        question1.grid(column=0, row=0, padx=2, pady=2, sticky=W)
        question2 = Label(frame2, text='Q2. In the last 24 Hours, have you had a fever, sneezing or coughing?')
        question2.grid(column=0, row=1, padx=2, pady=2, sticky=W)
        question3 = Label(frame2, text='Q3. Have you had COVID-19 or have you had contact with someone who has?')
        question3.grid(column=0, row=2, padx=2, pady=2, sticky=N+S+E+W)
        # Checkboxes
        self.q1 = BooleanVar()
        self.q2 = BooleanVar()
        self.q3 = BooleanVar()
        q1a_box = Checkbutton(frame2, text="Yes", variable=self.q1)
        q1a_box.grid(column=2, row=0)
        q1b_box = Checkbutton(frame2, text="No")
        q1b_box.grid(column=3, row=0)
        q2a_box = Checkbutton(frame2, text="Yes", variable=self.q2)
        q2a_box.grid(column=2, row=1)
        q2b_box = Checkbutton(frame2, text="No")
        q2b_box.grid(column=3, row=1)
        q3a_box = Checkbutton(frame2, text="Yes", variable=self.q3)
        q3a_box.grid(column=2, row=2)
        q3b_box = Checkbutton(frame2, text="No")
        q3b_box.grid(column=3, row=2)
        
        mybutton = Button(frame3, text="Submit!", command=lambda:[self.sendemail(), self.submitted()])
        mybutton.grid(column=1, row=2)  
        
    def submitted(self):
        tkm.showinfo('Notice', 'Your Entry was Saved!')
        full_path = "./check_log.txt"
        log = open(full_path, 'a+')
        info = {'Name': self.nm_entry.get(), 'Visiting': self.who_entry.get(), 'Purpose': self.pur_entry.get(),
                'Temp': self.temp_entry.get(), 'Phone': self.ph_entry.get(), 'Questions': {'1': self.q1.get(),
                                                                                         '2': self.q2.get(),
                                                                                         '3': self.q3.get()}}
        log.write(json.dumps(info))
        log.write("\n")
        log.close()
    def sendemail(self):
        name = self.nm_entry.get()
        resident = self.who_entry.get()
        why = self.pur_entry.get()
        temp = self.temp_entry.get()
        phone = self.ph_entry.get()
        question1 = self.q1.get()
        question2 = self.q2.get()
        question3 = self.q3.get()
        port = 465  # For SSL
        smtp_server = "smtp.gmail.com"
        sender_email = "hermescheckin@gmail.com"  # Enter your address
        receiver_email = "rshyampokhrel@gmail.com"  # Enter receiver address
        password = "admin108"
        message = ()
        context = ssl.create_default_context()
        with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
            server.login(sender_email, password)
            server.sendmail(sender_email, receiver_email, message)
           
root = Tk()
root.title("CheckIn")
App = CheckinApp(root)
root.mainloop()
