import os
from service import Service

s = Service()

fileList = []

results = []

counter = 1

fileList = s.getFolders()

for name in fileList:
    print str(counter) + ") " + name
    counter += 1

print "Choose a folder..."
input = raw_input()

print "Cleaning folder..."
s.beginCleanup(input)

results = s.getResults()
for a in results:
    print a
