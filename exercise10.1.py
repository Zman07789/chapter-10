#!/usr/bin/env python3

"""
Exercise  10.1: Revise a previous program as follows: Read and parse the "From"
lines and pull out the addresses from the line. Count the number of messages
from each person using a dictionary.
After all the data has been read, print the person with the most commits by
creating a list of (count, email) tuples from the dictionary. Then sort the
list in the reverse order and print out the person who has the most commits.
Sample line:
From stephen.marquard@uct.ac.az Sat Jan 05 09:14:16 2008
Enter a file name: mbox-short.txt
cwen@iupui.edu 5
Enter a file name: mbox.txt
zqian@umich.edu 195
Python for Everybody: Exploring Data Using Python 3

By Zackary Paulson
"""


thisisthedict = dict()          
lst = list()

fname = input('Enter file name: ')
try:
	fhand = open(fname)
except FileNotFoundError:
	print('File cannot be opened:', fname)
	quit()
	
for line in fhand:
	words = line.split()
	if len(words) < 2 or words[0] != 'From':
		continue
	else:
		if words[1] not in thisisthedict:
			thisisthedict[words[1]] = 1       
		else:
			thisisthedict[words[1]] += 1      
			
for key, val in list(thisisthedict.items()):
	lst.append((val, key))              
	
lst.sort(reverse=True)                 
for count, email in lst[:1]:            
	print(email, count)