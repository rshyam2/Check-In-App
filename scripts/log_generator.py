# daily csv maker
from datetime import date
import time, os

class FileGenerator:
    def __init__(self):
        self._date = date.today()
    def timeloop(self):
        t = 60
        while True:
            self.makefile()
            time.sleep(t)

    def makefile(self):
        today = self._date.strftime("%m-%d-%y")
        prefix = 'Entry_Log-'
        filename = prefix + today + '.csv'
        if os.path.exists('./Visitor_Log/'+filename) == False:
            f = open('./'+filename, 'w+')
            f.close()
        else:
            pass

def port():
    f = FileGenerator()
    f.timeloop()
