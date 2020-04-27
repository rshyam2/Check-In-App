from tkinter import *
import tkinter.messagebox as tkm
import json

root = Tk()
root.title("CheckIn")

# frames
frame1 = Frame(root)
frame1.pack(padx=2, pady=2)
frame2 = Frame(root)
frame2.pack(padx=2, pady=2)
frame3 = Frame(root)
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
nm_entry = Entry(frame1, textvariable=name)
nm_entry.grid(columnspan=4, row=2, padx=8, pady=2, sticky='n'+'e'+'w'+'s')
who_entry = Entry(frame1, textvariable=who)
who_entry.grid(column=4, row=2, padx=8, pady=2, sticky='n'+'e'+'w'+'s')
pur_entry = Entry(frame1, textvariable=purp)
pur_entry.grid(column=5, row=2, padx=8, pady=2, sticky='n'+'e'+'w'+'s')

temp_txt = Label(frame3, text="Temperature").grid(column=0, row=0)
temp_entry = Entry(frame3, textvariable=temp)
temp_entry.grid(column=0, row=1, padx=(1, 10))
ph_txt = Label(frame3, text="Phone Number").grid(column=2, row=0)
ph_entry = Entry(frame3, textvariable=phone)
ph_entry.grid(column=2, row=1, padx=(10, 5), pady=5)
# the questions frame starts here
question1 = Label(frame2, text='Q1. Have you recently been in an airport or traveled out of state?')
question1.grid(column=0, row=0, padx=2, pady=2, sticky=W)
question2 = Label(frame2, text='Q2. In the last 24 Hours, have you had a fever, sneezing or coughing?')
question2.grid(column=0, row=1, padx=2, pady=2, sticky=W)
question3 = Label(frame2, text='Q3. Have you had COVID-19 or have you had contact with someone who has?')
question3.grid(column=0, row=2, padx=2, pady=2, sticky=N+S+E+W)
# Checkboxes
q1 = BooleanVar()
q2 = BooleanVar()
q3 = BooleanVar()
q1a_box = Checkbutton(frame2, text="Yes", variable=q1)
q1a_box.grid(column=2, row=0)
q1b_box = Checkbutton(frame2, text="No")
q1b_box.grid(column=3, row=0)
q2a_box = Checkbutton(frame2, text="Yes", variable=q2)
q2a_box.grid(column=2, row=1)
q2b_box = Checkbutton(frame2, text="No")
q2b_box.grid(column=3, row=1)
q3a_box = Checkbutton(frame2, text="Yes", variable=q3)
q3a_box.grid(column=2, row=2)
q3b_box = Checkbutton(frame2, text="No")
q3b_box.grid(column=3, row=2)

class SaveInfo():
    def __init__(self):
        pass
    def submitted(self):
        tkm.showinfo('Notice', 'Your Entry was Saved!')
        log = open('check_log.txt', 'a')
        self.info = {'Name': nm_entry.get(), 'Visiting': who_entry.get(), 'Purpose': pur_entry.get(),
                'Temp': temp_entry.get(), 'Phone': ph_entry.get(), 'Questions': {'1': q1.get(),
                                                                                 '2': q2.get(),
                                                                                 '3': q3.get()}}
        log.write(json.dumps(self.info))
        log.write("\n")
        log.close()

s = SaveInfo()
mybutton = Button(frame3, text="Submit!", command=s.submitted)
mybutton.grid(column=1, row=2)

root.mainloop()