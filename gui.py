import os
import sys
import time
from service import Service

class Menu:
    
    s = Service()

    fileList = []

    results = []

    fileList = s.getFolders()

    def __init__(self):
        pass

    def spinning_cursor(self):
        while True:
           for cursor in '|/-\\':
              yield cursor

    def mainMenu(self):
        #Start commanding
        os.system('cls' if os.name == 'nt' else 'clear') #Clear terminal

        print "Choose a command to start"
        print "1) Proccess email addresses"
        print "2) Setup email columns"

        startInput = raw_input() #Startup command

        #Procces command===============
        if startInput == "1":
            self.proccesEmails()
        elif startInput == "2":
            self.setupEmails()
        else:
            print "Not proper command..."
        #Process command---------------      

    def proccesEmails(self):

        os.system('cls' if os.name == 'nt' else 'clear') #Clear terminal
        
        counter = 1

        print "Choose a folder to procces..."

        for name in self.fileList:
            print str(counter) + ") " + name
            counter += 1

        input = raw_input()

        print "Cleaning folder..."
        self.s.beginCleanup(input)

        #Spinning circle============================
        spinner = self.spinning_cursor()
        for _ in range(50):
        	sys.stdout.write(spinner.next())
        	sys.stdout.flush()
        	time.sleep(0.1)
        	sys.stdout.write('\b')
        #Spinning circle----------------------------

        print "--------------------------------"

        results = self.s.getResults()
        for a in results:
            print a
        print "--------------------------------"

        print "Press ENTER to exit..."
        raw_input()

m = Menu()
m.mainMenu()
