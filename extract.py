from bs4 import BeautifulSoup
import requests
from googlesearch import search
import pandas as pd
import re

df = pd.read_csv('nameloc.csv')
df_name = df['name'].to_list()
df_location = df['location'].to_list()


my_results_list = []
nf = "not found
Email_list=[]
Phone_no=[]
Address_list=[]
current_loc = None

for i in range(len(df.name)):
    query = df_name[i]+" "+df_location[i]
    current_loc = df_location[i]
    for j in search(query,
               tld = 'com',
               lang = 'en',
               num = 10,
               start = 0,
               stop = 1,
               pause = 2.0):
        my_results_list.append(j)


    for k in my_results_list:
        urls = str(k)
        page = requests.get(urls)
        soup = BeautifulSoup(page.content, 'html.parser')

    #FOR EMAIL **********************
    my_list = []
    for link in soup.find_all('a'):
        my_list.append(link.get('href'))

    emailregex = re.compile(r'''(
        [a-zA-Z0-9._%+-:]+
        @
        [a-zA-Z0-9.-]+
        \.[a-zA-Z]{2,4}
        )''', re.VERBOSE)

    my_list = list(map(str, my_list))
    newlist = list(filter(emailregex.search, my_list))
    if newlist:
        email = newlist.pop(0)
        email = email[7:]
        Email_list.append(email)

    else:
        Email_list.append(nf)

    #FOR PHONE **********************
    div = soup.div
    p = div.find_all('p')
    t = []
    for i in p:
        t.append(i.get_text()) 
    re1 = re.compile("(\+)?(91)? (\d){3} (\d){3} (\d){4}")
    re2 = re.compile("(\+)?(91)?-(\d){3}-(\d){3}-(\d){4}")
    re3 = re.compile("(\d){3} (\d){2} (\d){3} (\d){3}")
    re4 = re.compile("(\d){10}")
    re5 = re.compile("\+91(\d){10}" )
    reList = [re1, re2, re3, re4, re5]

    match = False
    for regex in reList:
        new = list(filter(regex.search, t))
        if len(new)>=1:
            match = True
            break
    if match:
        phone = new.pop(0)
        Phone_no.append(phone)

    #2
    else:
        span = div.find_all('span')
        t2 = []
        for i in span:
            t2.append(i.get_text())
            
        gotMatch = False
        for regex in reList:
            new2 = list(filter(regex.search, t2))
            if len(new2)>=1:
                gotMatch = True
                break
        if gotMatch:
            phone2 = new2.pop(0)
            Phone_no.append(phone2)
        else:
            Phone_no.append(nf)

"""
    #FOR ADDRESS *******************
    a_list = []
    for ad in soup.findAll('div'):
        a_list.append(ad.get('p'))

    word = current_loc
    word = str(word)
    my_re = r"^.*" + re.escape(word) + r".*$"
    #add_temp = re.search(my_re, a_list, re.IGNORECASE)
    add_temp = re.search(rf"^.*%s.*$" % word,a_list,re.IGNORECASE)
    
    if add_temp:
        address = add_temp.group()
        Address_list.append(address)
    else:
        Address_list.append(nf)
        """

#print('\n',Email_list,'\n')
#print('\n',Phone_no,'\n')
#print('\n',Address_list,'\n')

dict = {'email': Email_list, 'phone': Phone_no}
df = pd.DataFrame(dict)
df.to_csv('file1.csv') 

    
    

    



