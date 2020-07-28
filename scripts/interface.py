# main script for new check-in app
from tkinter import *
import tkinter.messagebox as tkm
import csv
import os
import smtplib, ssl
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from datetime import date
# frames
class CheckinApp:
    def __init__(self, master):
        self.master = master
        self.submitted
        self.response = False
        self.MasterContainer = Frame(self.master, borderwidth=4, relief='groove')
        self.MasterContainer.grid(pady=(2,10), padx=10)
        # will hold self.name, resident and reason entries
        frame1 = Frame(self.MasterContainer)
        frame1.grid(column=0, row=0, padx=30, pady=2)
        # will hold the Check boxes
        frame2 = Frame(self.MasterContainer)
        frame2.grid(column=0, row=1, padx=30, pady=2)
        # will hold self.temp and self.phone number entries
        frame3 = Frame(self.MasterContainer)
        frame3.grid(column=0, row=2, padx=30, pady=2)
        # will hold submit button and email entries
        frame4 = Frame(self.MasterContainer)
        frame4.grid(column=0, row=3, padx=30, pady=(2, 10))
        # Texts
        nm_txt = Label(frame1, text="Please enter your Name:", font="system").grid(column=0, row=1, padx=5, pady=2)
        who_txt = Label(frame1, text="Resident Visiting", font="system").grid(column=5, row=1, padx=5, pady=2)
        pur_txt = Label(frame1, text="Reason for Visit", font="system").grid(column=6, row=1, padx=5, pady=5)
        # Search Button
        Filler = Button(frame1, text='Find', command=self.DataSearch)
        Filler.grid(column=4, row=2, pady=5, padx=5, sticky='n'+'e'+'w'+'s')
        # Entry Boxes
        self.name = StringVar()
        self.who = StringVar()
        self.purp = StringVar()
        self.temp = StringVar()
        self.phone = StringVar()
        self.guard = StringVar()

        self.nm_entry = Entry(frame1, textvariable=self.name)
        self.nm_entry.grid(columnspan=4, row=2, padx=8, pady=8, sticky='n'+'e'+'w'+'s')
        self.who_entry = Entry(frame1, textvariable=self.who)
        self.who_entry.grid(column=5, row=2, padx=8, pady=8, sticky='n'+'e'+'w'+'s')
        self.pur_entry = Entry(frame1, textvariable=self.purp)
        self.pur_entry.grid(column=6, row=2, padx=8, pady=8, sticky='n'+'e'+'w'+'s')

        temp_txt = Label(frame3, text="Temperature", font="system").grid(column=0, row=0)
        self.temp_entry = Entry(frame3, textvariable=self.temp)
        self.temp_entry.grid(column=0, row=1, padx=5)

        ph_txt = Label(frame3, text="Phone Number", font="system").grid(column=1, row=0)
        self.ph_entry = Entry(frame3, textvariable=self.phone)
        self.ph_entry.grid(column=1, row=1, padx=5, pady=5)

        guard_txt = Label(frame3, text="Screener Name", font="system").grid(column=2, row=0)
        self.g_entry = Entry(frame3, textvariable=self.guard)
        self.g_entry.grid(column=2, row=1, pady=5, padx=5)
        # the questions frame starts here
        question1 = Label(frame2, text='Q1. Have you recently been in an airport or traveled out of state?', font="system")
        question1.grid(column=0, row=0, padx=2, pady=2, sticky=W)
        question2 = Label(frame2, text='Q2. In the last 24 Hours, have you had a fever, sneezing, coughing or loss of taste/smell?', font="system")
        question2.grid(column=0, row=1, padx=2, pady=2, sticky=W)
        question3 = Label(frame2, text='Q3. Have you had COVID-19 or have you had contact with someone who has or suspected to have?', font="system")
        question3.grid(column=0, row=2, padx=2, pady=2, sticky=N+S+E+W)
        # Checkboxes
        self.q1 = BooleanVar()
        self.q2 = BooleanVar()
        self.q3 = BooleanVar()
        q1a_box = Checkbutton(frame2, text="Yes", variable=self.q1, font="system")
        q1a_box.grid(column=2, row=0)
        q1b_box = Checkbutton(frame2, text="No", font="system")
        q1b_box.grid(column=3, row=0)
        q2a_box = Checkbutton(frame2, text="Yes", variable=self.q2, font="system")
        q2a_box.grid(column=2, row=1)
        q2b_box = Checkbutton(frame2, text="No", font="system")
        q2b_box.grid(column=3, row=1)
        q3a_box = Checkbutton(frame2, text="Yes", variable=self.q3, font="system")
        q3a_box.grid(column=2, row=2)
        q3b_box = Checkbutton(frame2, text="No", font="system")
        q3b_box.grid(column=3, row=2)

        submit = Button(frame3, text="Submit Entry!", command=lambda:[self.submitted(), self.trigger()], font="system")
        submit.grid(column=1, row=2, pady=5, padx=5)
        s_email = StringVar()
        s_pass = StringVar()
        r_email = StringVar()
        s_email.set("youremail@gmail.com")
        s_pass.set('passcode')
        sender_addy = Label(frame4, text="Sender Email", font="system").grid(column=0, row=0, pady=5, padx=5, sticky=W)
        sender_pass = Label(frame4, text="Sender password", font="system").grid(column=0, row=1, pady=5, padx=5, sticky=W)
        receiver_addy = Label(frame4, text='Receiver Email', font="system").grid(column=0, row=2, pady=5, padx=5, sticky=W)

        self.SenderEmail = Entry(frame4, textvariable=s_email, width=30)
        self.SenderEmail.grid(column=1, columnspan=3, row=0, pady=5, padx=5)
        self.SenderPass = Entry(frame4, textvariable=s_pass, width=15)
        self.SenderPass.grid(column=1, columnspan=2, row=1, pady=5, padx=5, sticky=W)
        self.ReceiverEmail = Entry(frame4, textvariable=r_email, width=30)
        self.ReceiverEmail.grid(column=1, columnspan=3, row=2, pady=5, padx=5, sticky=W)

        SendMail = Button(frame4, text='Send Email!', command= lambda:[self.SendEmail(), self.submitted(), self.trigger()], font="system")
        SendMail.grid(column = 1, row=3, pady=5, padx=5, sticky=W)

    def clear_entry(self):
        entries = [self.nm_entry, self.who_entry, self.who_entry, self.pur_entry, self.temp_entry, self.ph_entry]
        for entry in entries:
            entry.delete(0, END)
    def trigger(self):
        if self.response is True:
            self.clear_entry()
        else:
            pass

    def submitted(self):
        name = self.nm_entry.get()
        resident = self.who_entry.get()
        why = self.pur_entry.get()
        temp = self.temp_entry.get()
        phone = self.ph_entry.get()
        question1 = self.q1.get()
        question2 = self.q2.get()
        question3 = self.q3.get()
        guard = self.guard.get()
        info = {'Name': name, 'Visiting': resident, 'Purpose': why,
                'Temp': temp, 'Phone #': phone, 'Travel': question1,
                'Symptoms': question2,'Contact': question3, 'Screener':guard}
        today = date.today()
        DayMonth = today.strftime("%d/%m")
        info['Date'] = DayMonth
        # info = [self.name, resident, why, self.temp, self.phone, question1, question2, question3]
        full_path = "./Visitor_Log/check_log.csv"
        if os.path.exists(full_path) == True:
            with open(full_path, mode='a+') as log:
                data_col = ['Date', 'Name', 'Visiting', 'Purpose', 'Temp', 'Phone #', 'Travel', 'Symptoms', 'Contact', 'Screener']
                log_writer = csv.DictWriter(log, fieldnames = data_col)
                log_writer.writerow(info)
        else:
            with open(full_path, mode='a+') as log:
                data_col = ['Date', 'Name', 'Visiting', 'Purpose', 'Temp', 'Phone #', 'Travel', 'Symptoms', 'Contact', 'Screener']
                log_writer = csv.DictWriter(log, fieldnames = data_col)
                log_writer.writeheader()
                log_writer.writerow(info)
        self.response = True

    def DataSearch(self):
        try:
            ID = self.nm_entry.get()
            search_var = ID[0].upper() + ID[1:]
            self.mainframe = Toplevel(self.MasterContainer)
            self.mainframe.title('...')
            #
            text = Label(self.mainframe, text='Possible Matches', font="system").grid(column=0, row=0, pady=5, padx=5)
            self.area = Listbox(self.mainframe)
            self.area.grid(column=0, row=1)
            # making a select button
            button = Button(self.mainframe, text='Select', command=self.autofill)
            button.grid(column=0, row=2, pady=5, padx=5)

            f = open("./Visitor_Log/check_log.csv", 'r')
            with f:
                NameMatch = []
                reader = csv.DictReader(f)
                for items in reader:
                    if search_var in items['Name']:
                        if items['Name'] not in NameMatch:
                            NameMatch.append(items['Name'])
                        # self.area.insert(END, items['Name'])
                    else:
                        continue
            for names in NameMatch:
                self.area.insert(END, names)
        except IndexError:
            tkm.showerror('Error', 'Cannot search empty values!')
    def autofill(self):
        FullName = self.area.get(self.area.curselection())
        file = open("./Visitor_Log/check_log.csv", 'r')
        with file:
            reader = csv.DictReader(file)
            for person in reader:
                if person['Name'] == FullName:
                    self.name.set(person['Name'])
                    self.who.set(person['Visiting'])
                    self.purp.set(person['Purpose'])
                    self.temp.set(person['Temp'])
                    self.phone.set(person['Phone #'])
                else:
                    continue
        # print(FullName)
    def SendEmail(self):
        try:
            name = self.nm_entry.get()
            resident = self.who_entry.get()
            why = self.pur_entry.get()
            temp = self.temp_entry.get()
            phone = self.ph_entry.get()
            question1 = self.q1.get()
            question2 = self.q2.get()
            question3 = self.q3.get()
            guard = self.guard.get()
            # putting this all into a dictionary
            info = {'Name': name, 'Visiting': resident, 'Purpose': why,
                    'Temp': temp, 'Phone #': phone, 'Travel': question1,'Symptoms': question2,'Contact': question3, 'Screener':guard}

            sender = self.SenderEmail.get()
            sender_pass = self.SenderPass.get()
            receiver = self.ReceiverEmail.get()

            port = 465  # For SSL
            smtp_server = "smtp.gmail.com"
            sender_email = sender
            receiver_email = receiver
            password = sender_pass

            string = ''
            for key,value in info.items():
                string += (str(key) + ": " + str(value) + "\n")

            msg = MIMEMultipart('alternative')
            msg['Subject'] = 'Check-In'
            part1 = MIMEText(string, 'plain')
            msg.attach(part1)

            context = ssl.create_default_context()
            with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
                server.login(sender_email, password)
                server.sendmail(sender_email, receiver_email, msg.as_string())
            tkm.showinfo('Notice', 'Email Sent!')
            self.response = True
        except smtplib.SMTPAuthenticationError:
            tkm.showerror('Error', "Please check the Email and Password for the Sender again...")
            self.response = False
        except smtplib.SMTPServerDisconnected:
            tkm.showerror('Error', 'Please check your connection and try sending it again...')
            self.response = False
        finally:
            pass

def runtime():
    _path = '.\Visitor_Log'
    if not os.path.exists(_path):
        try:
            os.mkdir(_path)
        except OSError as e:
            print(e)
    root = Tk()
    root.title("Security Screening Form")
    App = CheckinApp(root)
    root.mainloop()
