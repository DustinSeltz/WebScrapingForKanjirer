#!/usr/bin/env python
# coding: utf-8

# In[38]:


import numpy as np
import pandas as pd
from bs4 import BeautifulSoup
from requests import get
from time import sleep
from random import randint


# In[164]:


df = pd.read_csv('wikitionary_wordlist.csv')
sr = df['word']

kamei_list = list("あいうえおかきくけこさしすせそたちつてとなにぬねのはひふへほまみむめもやゆよらりるれろわをんがぎぐげござじずぜぞだぢづでどばびぶべぼパピプペポアイウエロカキクケコサシスセソタチツテトナニヌネノハヒフヘホマミムメモヤユヨラリルレロワヲンガギグゲゴザジズゼゾダヂヅデドバビブベボパピプペポャュョー")

# In[208]:


def get_furigana(soup):
    furi = soup.find('span',class_='furigana')
    #print(list(furi.children))
    txt = furi.next_sibling.next_sibling
    text_cont = list(str(txt.get_text()).strip())
    furistring = ""
    txtstring = ""
    text_loc = 0
    for f1 in furi.children:
        #print(f1)
        if ((f1 != '\n') & (f1 is not None)):
            t1 = text_cont[text_loc]
            txtstring += t1
            if (f1.get_text() == '') & (t1 in kamei_list):
                furistring += t1
            else:
                furistring += f1.get_text().strip()
            text_loc += 1
    return (furistring, txtstring)


# In[209]:


def get_meanings(soup):
    meanings = ""
    raw_meanings = soup.findAll('div', class_='meaning-wrapper')
    for x in raw_meanings:
        flag = x.findAll('span', class_='meaning-definition-section_divider')
        if ((flag is not None) & (flag != [])):
            #print(flag)
            tag = flag[0]
            #print(tag)
            #print(tag.next_sibling)
            meanings += tag.get_text() + tag.next_sibling.get_text() + '$'
    return meanings

# Temporary Save
def save_temp(wlist, flist, mlist,k):
    pd.DataFrame({
        'word': wlist,
        'reading': flist,
        'meaning': mlist
        }).to_csv('wikiword_table_{}_new.csv'.format(k))
    return

# In[211]:


wordlist = []
furigana = []
meanings = []

url_base = 'https://jisho.org/word/'

requests = 0
i = 0

for k in np.arange(len(sr)):
    i = 0
    word = sr[k]
#word = '一つ一つ'
#if (True):
    while (True):
        if (i == 0):
            url = url_base+word
        else:
            url = url_base+word+'-'+str(i)
            
        #print(url)
        
        response = get(url)
        requests += 1
        print("Requests Made: {}, status {}".format(requests, response.status_code))
        sleep(0.1)
        
        i += 1

        if (requests % 100 == 0):
            save_temp(wordlist, furigana, meanings, k)
        
        if (response.status_code != 200):
            if (response.status_code == 408):
                # Timed Out
                i -= 1
                continue
            if (response.status_code != 404):
                print("Error: code {} at word {}, i={}".format(response.status_code, word, i-1))
            break
        else:
            soup = BeautifulSoup(response.text, 'html.parser')
            furi, txt = get_furigana(soup)
            mean = get_meanings(soup)
            print(txt+' / '+furi+' / '+mean)
            wordlist.append(txt)
            furigana.append(furi)
            meanings.append(mean)
    
   
    


# In[145]:

pd.DataFrame({
        'word': wordlist,
        'reading': furigana,
        'meaning': meanings
        }).to_csv('wikiword_table_new.csv')



# In[ ]:




