import argparse,os,time
import urlparse, random
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup

def getPeopleLinks(page):
	links=[]
	for link in page.find_all('a'):
		url= link.get("href")
		if url:
			if 'profile/view?id' in url:
				links.append(url)

	return links

def getJobLinks(page):
	jobs=[]
	for link in  page.find_all('a'):
		url =link.get("href")
		if "/jobs" in url:
			jobs.append(url)

	return jobs

def getID(url):
	pUrl = urlparse.urlparse(url)
	return urlparse.parse_qs(pUrl.query['id'][0])

def ViewBot(browser):
	visited = {}
	plist= []
	count = 0
	while True:
		#sleep to male sure everything loads.
		#add random to make us  look main
		time.sleep(random.uniform(3.5,6.9))
		page= BeautifulSoup(browser.page_source)
		people =getPeopleLinks(page)
		# if people:
		# 	for person in people:
		# 		ID=getID(person)
		# 		if ID not in visited:
		# 			pList.append(person) 
		# 			#people to visit
		# 			visited[ID]=1
		# if pList:
		# 		person = pList.pop()
		# 		browser.get(person)
		# 		count +=1
		if 1: 
			jobs=getJobLinks(page)
			if jobs:
				job=random.choice(jobs)
				root= "http://www.linkedin.com"
				roots= 'http://www.linkedin.com'
				if root not in job  or roots not in job:
					job='https://www.linkedin.com'+job
					browser.get(job)
				print("$$")
			else: 
			 	print("I'm Lost")
			 	break 

	# print("[+]"+browser.title+"VISITED! \n"+"("\"+str(count)+"/"+"str(len(plist))+") Visited/Queue")


def Main():
	parser= argparse.ArgumentParser()
	parser.add_argument("email",help="Linkedin Email")
	parser.add_argument("password",help="Linkedin Password")
	
	args= parser.parse_args()
	browser=webdriver.Chrome()
	browser.get("https://www.linkedin.com/uas/login")
	
	emailElement=browser.find_element_by_id("session_key-login")
	emailElement.send_keys(args.email)
	
	passElement=browser.find_element_by_id("session_key-password")
	emailElement.send_keys(args.paasword)
	passElement.submit()
	
	os.system('clear')
	print "[+] Sucess! Logged In, Bot Starting!"
	ViewBot(browser)
	browser.close()

if __name__ =="__main__":
	Main()
