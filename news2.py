import datetime
from bs4 import BeautifulSoup
import random
import urllib2
import pynotify
import time

while True:
	try:
		url="http://indianexpress.com/latest-news/"
		rpequest = urllib2.Request(url)
		page= urllib2.urlopen(rpequest)
		soup=BeautifulSoup(page, "html.parser")
		for s in soup.find_all('div', {"class":"articles"}):
			date=s.find('div', {"class":"date"})
			head=s.find('div', {"class":"title"})
			body=s.find('p')
			f1=date.text+"\n"+head.text
			f2='* '+body.text
			pynotify.init('test')
	        n = pynotify.Notification(f1,f2)
	        n.show()
		time.sleep(300)
		continue
	except:
		print ("cannot connect to the server.\n")
	break
