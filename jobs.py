from selenium import webdriver
import pandas as pd
from bs4 import BeautifulSoup
import selenium
df = pd.DataFrame(columns=["Title","Location","Company","Salary","Sponsored","Description"])
driver=webdriver.Chrome(r"C:\\Users\\Brunda\\Downloads\\chromedriver\\chromedriver.exe")
driver.get("https://www.indeed.co.in/jobs?q=software+developer&l=india")
all_jobs=driver.find_elements_by_class_name('result')
for job in all_jobs:
	result_html=job.get_attribute('innerHTML')
	soup=BeautifulSoup(result_html,'html.parser')
	try:

		title=soup.find('a',class_='jobtitle').text
	except:
		title="None"
	try:
		location = soup.find(class_="location").text
	except:
		location = 'None'

	try:
		company = soup.find(class_="company").text.replace("\n","").strip()
	except:
		company = 'None'

	try:
		salary = soup.find(class_="salary").text.replace("\n","").strip()
	except:
		salary = 'None'
	

	df = df.append({'Title':title,'Location':location,"Company":company,"Salary":salary,
						},ignore_index=True)
	df.to_csv('jobs.csv')