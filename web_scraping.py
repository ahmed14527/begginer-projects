import requests
from bs4 import BeautifulSoup
from itertools import zip_longest
import csv
job_titles=[]
company_names=[]
location_names=[]
job_skill=[]
result=requests.get('https://wuzzuf.net/search/jobs/?q=python&a=hpb')
src=result.content
#print(src)
soup=BeautifulSoup(src,'lxml')
print(soup)
job_title=soup.find_all("h2",{"class":"css-m604qf"})
print(job_title)
company_name=soup.find_all("a",{"class":"css-17s97q8"})
#print(company_name)
location_name=soup.find_all("span",{"class":"css-5wys0k"})
#print(location_name)
job_skills=soup.find_all("a",{"class":"css-o171k1"})
#print(job_skills)
for i in range(len(job_title)):
    job_titles.append(job_title[i].text)
    company_names.append(company_name[i].text)
    location_names.append(location_name[i].text)
    job_skill.append(job_skills[i].text)


print(job_titles)
print(company_names)



#with open("F:/database/web.csv","w")as myfile:

