import requests
from bs4 import BeautifulSoup
import pandas as pd 
import os.path

def extract(page):
    url = f'https://sg.indeed.com/jobs?q=oaktree&start={page}'
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.104 Safari/537.36'}
    r = requests.get(url, headers)
    soup = BeautifulSoup(r.content, 'html.parser')
    return soup

def transform(soup): 
    divs = soup.find_all('div', class_='jobsearch-SerpJobCard')
    for item in divs:
        title = item.find('a').text.strip()
        #wage = item.find('span', {'class':'salaryText'}).text.strip()
        description = item.find('div', class_ = 'summary').text.strip().replace('\n', '')
        job_link = item.find('a')['href']
        job_link = 'sg.Indeed.com/' + job_link
        
        
        job = {
            'title' : title,
            #'wage' : wage,
            'description' : description,
            'job_link' : job_link
            
        }
        joblist.append(job)
    return


joblist = []

for i in range(0,40,10):
    print(f'Getting page, {i}')
    c = extract(0)
    transform(c)

df = pd.DataFrame(data=joblist)
print(df.head())
df.to_csv('indeed.csv')