#!/usr/bin/env python
# coding: utf-8

# In[1]:


##ANSWER (1.)


get_ipython().system('pip install bs4')
get_ipython().system('pip install requests')


# In[2]:


from bs4 import BeautifulSoup
import requests


# In[4]:


page = requests.get('https://en.wikipedia.org/wiki')


# In[5]:


page


# In[6]:


soup = BeautifulSoup(page.content)
soup


# In[7]:


bs = BeautifulSoup(page.content, "html.parser")


# In[8]:


titles = bs.find_all(['h1', 'h2','h3','h4','h5','h6'])


# In[9]:


print('Displaying all Header Tags :', *titles, sep='\n\n')


# In[10]:


## Answer (3.)

from bs4 import BeautifulSoup
import requests
import pandas as pd


# In[11]:


page3 = requests.get('https://www.imdb.com/list/ls056092300/')


# In[12]:


page3


# In[13]:


indian_movies = BeautifulSoup(page3.text, "html.parser")
indian_movies


# In[14]:


def get_indian_movies(indian_movies):
    selection_class = 'lister-item-header'
    movie_name_tags = indian_movies.find_all('h3', {'class':selection_class})
    names2 = []
    
    
    for i in movie_name_tags:
        a = i.find('a').text
        names2.append(a)
        
    return names2
    


# In[16]:


names2 = get_indian_movies(indian_movies)


# In[17]:


names2


# In[18]:


year2 = []
for i in indian_movies.find_all('span',class_="lister-item-year text-muted unbold"):
    year2.append(i.text)
    
year2


# In[19]:


rating2 = []
for i in indian_movies.find_all('div',class_="ipl-rating-star small"):
    rating2.append(i.text)
    
rating2


# In[20]:


rating2 = [i.split('\n')[8] for i in rating2]

rating2


# In[21]:


len(rating2)


# In[22]:


imdb_top100_indian = pd.DataFrame({'Name':names2, 'Rating':rating2, 'Year Of Release':year2})

imdb_top100_indian


# In[23]:


## Answer (4)

page4 = requests.get("https://presidentofindia.nic.in/former-presidents.htm")
page4


# In[24]:


pres = BeautifulSoup(page4.text)
pres


# In[25]:


pres_names = []
for i in pres.find_all('h3'):
    pres_names.append(i.text)
    
pres_names


# In[26]:


pres_terms = []
for i in pres.find_all('div', class_ = "presidentListing"):
    pres_terms.append(i.text)
    
pres_terms


# In[27]:


pres_term = [i.split('\n')[2] for i in pres_terms]

pres_term


# In[28]:


pres_term = [i.split(':')[1] for i in pres_term]

pres_term


# In[29]:


pres_list = pd.DataFrame({'President Names':pres_names,'Term of Office':pres_term})

pres_list


# In[2]:


## answer (7)

import pandas as pd
from bs4 import BeautifulSoup
import requests


# In[3]:


page7 = requests.get('https://www.cnbc.com/world/?region=world')
page7


# In[4]:


news = BeautifulSoup(page7.text)
news


# In[6]:


header = []
for i in news.find_all('div', class_ = "LatestNews-headlineWrapper"):
    header.append(i.text)
    
header


# In[7]:


headline = [i.split('Ago')[1] for i in header]
headline


# In[8]:


timestamp =  [i.split('Ago')[0] for i in header]
timestamp


# In[21]:


link = []
for i in news.find_all('a', href=True):
    link.append(i['href'])

link


# In[22]:


list =['link']


# In[23]:


len(list)


# In[24]:


len(headline)


# In[25]:


links = link[115:151]
links


# In[27]:


links.remove('/pro/')
links.remove('/pro/')
links.remove('/pro/')
links.remove('/pro/')
links.remove('/pro/')
links.remove('/investingclub/')

links


# In[28]:


len(links)


# In[30]:


import pandas as pd


# In[33]:


news_headlines = pd.DataFrame({'Headline':headline,'Timestamp':timestamp,'News Link':links})
news_headlines


# In[35]:


### Answer (8)

page8 = requests.get('https://www.journals.elsevier.com/artificial-intelligence/most-downloaded-articles')
page8


# In[36]:


art = BeautifulSoup(page8.content)
art


# In[37]:


article = []
for i in art.find_all('h2',class_="sc-1qrq3sd-1 gRGSUS sc-1nmom32-0 sc-1nmom32-1 btcbYu goSKRg"):
    article.append(i.text)
    
article


# In[39]:


author = []
for i in art.find_all('span',class_="sc-1w3fpd7-0 dnCnAO"):
    author.append(i.text)
    
author


# In[40]:


pdate = []
for i in art.find_all('span',class_="sc-1thf9ly-2 dvggWt"):
    pdate.append(i.text)
    
pdate


# In[41]:


artlink = []
for i in art.find_all('a',href=True):
    artlink.append(i['href'])
    
artlink


# In[42]:


artlink


# In[43]:


waste = [artlink]


# In[44]:


len(waste)


# In[45]:


len(article)


# In[46]:


len(artlink)


# In[47]:


artlinks = artlink[54:79]
artlinks


# In[48]:


Top_Downloaded_Articles = pd.DataFrame({'Article Name':article,'Authors':author,'Publishing Date':pdate,'Article Link':artlinks})

Top_Downloaded_Articles


# In[33]:


## ANSWER (9)

page9 = requests.get('https://www.dineout.co.in/delhi-restaurants/buffet-special')
page9


# In[34]:


dine = BeautifulSoup(page9.text)
dine


# In[35]:


rest_name = []
for i in dine.find_all('a', class_="restnt-name ellipsis"):
    rest_name.append(i.text)
rest_name    


# In[36]:


cuisine = []
for i in dine.find_all('span',class_="double-line-ellipsis"):
    cuisine.append(i.text)
    
cuisine


# In[37]:


cuisine = [i.split('|')[1] for i in cuisine]
cuisine


# In[38]:


location = []
for i in dine.find_all('div',class_="restnt-loc ellipsis"):
    location.append(i.text)
    
location


# In[39]:


rest_rating = []
for i in dine.find_all('div',class_="restnt-rating rating-4"):
    rest_rating.append(i.text)
    
rest_rating


# In[40]:


rest_images = []
for i in dine.find_all("img",class_="no-img"):
    rest_images.append(i.get('data-src'))
    
rest_images


# In[41]:


dineout_buffets = pd.DataFrame({'Restaurant':rest_name,'Cuisine':cuisine,'Location':location,'Rating':rest_rating,'Image Link':rest_images})

dineout_buffets


# In[43]:


## Answer (2)

page2 = requests.get('https://www.imdb.com/search/title/?groups=top_100&sort=user_rating,desc')
page2


# In[44]:


imdb1 = BeautifulSoup(page2.content)
imdb1


# In[45]:


def get_movie_names(imdb1):
    selection_class = 'lister-item-header'
    movie_name_tags = imdb1.find_all('h3',{'class':selection_class})
    names1 = []
    
    for i in movie_name_tags:
        a = i.find('a').text
        names1.append(a)
        
    return names1


# In[46]:


names1 = get_movie_names(imdb1)


# In[47]:


names1


# In[48]:


len(names1)


# In[49]:


page2_1 = requests.get('https://www.imdb.com/search/title/?groups=top_100&sort=user_rating,desc&start=51&ref_=adv_nxt')
page2_1


# In[50]:


imdb1_2 = BeautifulSoup(page2_1.text)
imdb1_2


# In[51]:


def get_movie_names2(imdb1_2):
    selection_class = 'lister-item-header'
    movie_name_tags = imdb1_2.find_all('h3',{'class':selection_class})
    names1_2 = []
    
    for i in movie_name_tags:
        a = i.find('a').text
        names1_2.append(a)
        
    return names1_2


# In[52]:


names1_2 = get_movie_names2(imdb1_2)


# In[53]:


names1_2


# In[54]:


names1 = names1+ names1_2


# In[55]:


names1


# In[56]:


year1 = []
for i in imdb1.find_all('span',class_="lister-item-year text-muted unbold"):
    year1.append(i.text)
    
year1


# In[57]:


year1_2 = []
for i in imdb1_2.find_all('span',class_="lister-item-year text-muted unbold"):
    year1_2.append(i.text)
    
year1_2


# In[58]:


year1 = year1 + year1_2
year1


# In[59]:


rating1 = []
for i in imdb1.find_all('strong'):
    rating1.append(i.text)
    
rating1


# In[60]:


rating1 = rating1[2:]

rating1


# In[61]:


rating1_2 = []
for i in imdb1_2.find_all('strong'):
    rating1_2.append(i.text)
    
rating1_2


# In[62]:


rating1_2 = rating1_2[2:]

rating1_2


# In[63]:


rating1 = rating1 + rating1_2

rating1


# In[64]:


len(rating1)


# In[65]:


len(names1)


# In[66]:


import pandas as pd
imdb_top100 = pd.DataFrame({'Name':names1, 'Rating':rating1, 'Year Of Release':year1})

imdb_top100


# In[17]:


import pandas as pd
from bs4 import BeautifulSoup
import requests


# In[18]:


## Answer (5.)

# (a) Top 10 ODI Teams

page5 = requests.get('https://www.icc-cricket.com/rankings/mens/team-rankings/odi')
page5


# In[19]:


team = BeautifulSoup(page5.text, "html.parser")
team


# In[20]:


team_name = []
for i in team.find_all ('span',class_="u-hide-phablet"):
    team_name.append(i.text)
    
team_name = team_name[0:10]
team_name


# In[21]:


team_matches = []
for i in team.find_all('td',class_="rankings-block__banner--matches"):
    team_matches.append(i.text)
    
team_matches = team_matches[0:10]
team_matches


# In[22]:


team_matches2 = []

for i in team.find_all('td',class_="table-body__cell u-center-text"):
    team_matches2.append(i.text)
    
team_matches = team_matches + team_matches2[0:18]
team_matches


# In[23]:


team_matches.remove('3,400')
team_matches.remove('3,572')
team_matches.remove('4,377')
team_matches.remove('2,584')
team_matches.remove('2,392')
team_matches.remove('3,129')
team_matches.remove('2,917')
team_matches.remove('1,419')
team_matches.remove('2,902')
team_matches


# In[24]:


team_points = []
for i in team.find_all('td',class_="rankings-block__banner--points"):
    team_points.append(i.text)
    
team_points


# In[28]:


team_points2 = []

for i in team.find_all('td',class_="table-body__cell u-center-text"):
    team_points2.append(i.text)
    
team_points2 = team_points2[1:18]
team_points2


# In[29]:


team_points2.remove('32')
team_points2.remove('40')
team_points2.remove('24')
team_points2.remove('24')
team_points2.remove('33')
team_points2.remove('33')
team_points2.remove('20')
team_points2.remove('41')

team_points = team_points + team_points2
team_points


# In[33]:


team_rating = []
for i in team.find_all('td',class_="rankings-block__banner--rating u-text-right"):
    team_rating.append(i.text)

team_rating


# In[34]:


team_rating = [i.split('\n')[1] for i in team_rating]
team_rating = [i.split('                            ')[1] for i in team_rating]

team_rating


# In[35]:


team_rating2 = []
for i in team.find_all('td',class_="table-body__cell u-text-right rating"):
    team_rating2.append(i.text)

team_rating = team_rating+team_rating2[0:9]
team_rating


# In[36]:


odi_team_ranking = pd.DataFrame({'TEAM':team_name,'MATCHES':team_matches,'POINTS':team_points,'RATING':team_rating})

odi_team_ranking


# In[37]:


# (b) TOP 10 ODI BATSMEN

page5_1 = requests.get('https://www.icc-cricket.com/rankings/mens/player-rankings/odi/batting')
page5_1


# In[39]:


bat = BeautifulSoup(page5_1.text)
bat


# In[40]:


bat_name = []
for i in bat.find_all('div',class_="rankings-block__banner--name-large"):
    bat_name.append(i.text)
    
bat_name


# In[41]:


bat_name2 = []
for i in bat.find_all('td',class_="table-body__cell rankings-table__name name"):
    bat_name2.append(i.text)
    
bat_name2 = bat_name2[0:9]
bat_name2


# In[42]:


bat_name2= [i.split('\n')[1] for i in bat_name2]

bat_name2
bat_name = bat_name + bat_name2
bat_name


# In[43]:


bat_team = []
for i in bat.find_all('div',class_="rankings-block__banner--nationality"):
    bat_team.append(i.text)
    
bat_team


# In[44]:


bat_team = [i.split('\n')[2] for i in bat_team]

bat_team


# In[45]:


bat_team2 = []
for i in bat.find_all('span',class_="table-body__logo-text"):
    bat_team2.append(i.text)
    
bat_team2 = bat_team2[0:9]
bat_team2


# In[46]:


bat_team = bat_team + bat_team2
bat_team


# In[47]:


bat_rating = []
for i in bat.find_all('div',class_="rankings-block__banner--rating"):
    bat_rating.append(i.text)
    
bat_rating


# In[48]:


bat_rating2 = []
for i in bat.find_all('td',class_="table-body__cell rating"):
    bat_rating2.append(i.text)
    
bat_rating2 = bat_rating2[0:9]
bat_rating2


# In[49]:


bat_rating = bat_rating + bat_rating2
bat_rating


# In[50]:


batsmen_ranking = pd.DataFrame({'Player Name':bat_name,'Team':bat_team,'Rating':bat_rating})
batsmen_ranking


# In[54]:


# (c) TOP 10 ODI BOWLERS

page5_3 = requests.get('https://www.icc-cricket.com/rankings/mens/player-rankings/odi/bowling')
page5_3


# In[56]:


bowl = BeautifulSoup(page5_3.content)
bowl


# In[57]:


bowl_name = []
for i in bowl.find_all('div',class_="rankings-block__banner--name-large"):
    bowl_name.append(i.text)
    
bowl_name


# In[58]:


bowl_name2 = []
for i in bowl.find_all('td',class_="table-body__cell rankings-table__name name"):
    bowl_name2.append(i.text)
    
bowl_name2 = bowl_name2[0:9]
bowl_name2


# In[59]:


bowl_name2= [i.split('\n')[1] for i in bowl_name2]
bowl_name = bowl_name + bowl_name2

bowl_name


# In[60]:


bowl_team = []
for i in bowl.find_all('div',class_="rankings-block__banner--nationality"):
    bowl_team.append(i.text)
    
bowl_team = [i.split('\n')[2] for i in bowl_team]

bowl_team


# In[61]:


bowl_team2 = []
for i in bowl.find_all('span',class_="table-body__logo-text"):
    bowl_team2.append(i.text)
    
bowl_team2 = bowl_team2[0:9]
bowl_team = bowl_team + bowl_team2
bowl_team


# In[62]:


bowl_rating = []
for i in bowl.find_all('div',class_="rankings-block__banner--rating"):
    bowl_rating.append(i.text)
    
bowl_rating


# In[63]:


for i in bowl.find_all('td',class_="table-body__cell rating"):
    bowl_rating.append(i.text)
    
bowl_rating = bowl_rating[0:10]
bowl_rating


# In[64]:


bowler_ranking = pd.DataFrame({'Bowler Name':bowl_name,'Team':bowl_team,'Rating':bowl_rating})
bowler_ranking


# In[65]:


## Answer (6)

# (a) WOMEN'S ODI TEAM RANKING

page6_1 = requests.get('https://www.icc-cricket.com/rankings/womens/team-rankings/odi')
page6_1


# In[66]:


wteam = BeautifulSoup(page6_1.content)
wteam


# In[67]:


wteam_name = []
for i in wteam.find_all ('span',class_="u-hide-phablet"):
    wteam_name.append(i.text)
    
wteam_name = wteam_name[0:10]
wteam_name


# In[68]:


wteam_matches = []
for i in wteam.find_all('td',class_="rankings-block__banner--matches"):
    wteam_matches.append(i.text)
    
wteam_matches = wteam_matches[0:10]
wteam_matches


# In[69]:


wteam_matches2 = []

for i in wteam.find_all('td',class_="table-body__cell u-center-text"):
    wteam_matches2.append(i.text)
    
wteam_matches = wteam_matches + wteam_matches2[0:17]
wteam_matches


# In[70]:


wteam_matches.remove('3,342')
wteam_matches.remove('3,098')
wteam_matches.remove('2,820')
wteam_matches.remove('2,553')
wteam_matches.remove('2,535')
wteam_matches.remove('983')
wteam_matches.remove('572')
wteam_matches.remove('1,519')
wteam_matches


# In[71]:


wteam_points = []
for i in wteam.find_all('td',class_="rankings-block__banner--points"):
    wteam_points.append(i.text)
    
wteam_points


# In[72]:


wteam_points2 = []

for i in wteam.find_all('td',class_="table-body__cell u-center-text"):
    wteam_points2.append(i.text)
    
wteam_points2 = wteam_points2[1:18]
wteam_points2


# In[73]:


wteam_points2.remove('26')
wteam_points2.remove('27')
wteam_points2.remove('25')
wteam_points2.remove('27')
wteam_points2.remove('13')
wteam_points2.remove('8')
wteam_points2.remove('24')
wteam_points2.remove('8')

wteam_points = wteam_points + wteam_points2
wteam_points


# In[74]:


wteam_rating = []
for i in wteam.find_all('td',class_="rankings-block__banner--rating u-text-right"):
    wteam_rating.append(i.text)

wteam_rating


# In[75]:


wteam_rating = [i.split('\n')[1] for i in wteam_rating]
wteam_rating = [i.split('                            ')[1] for i in wteam_rating]

wteam_rating


# In[76]:


wteam_rating2 = []
for i in wteam.find_all('td',class_="table-body__cell u-text-right rating"):
    wteam_rating2.append(i.text)

wteam_rating = wteam_rating+wteam_rating2[0:9]
wteam_rating


# In[77]:


women_team_ranking = pd.DataFrame({'TEAM':wteam_name,'MATCHES':wteam_matches,'POINTS':wteam_points,'RATING':wteam_rating})

women_team_ranking


# In[78]:


## (b.) TOP 10 ODI WOMEN'S BATTING

page6_2 = requests.get('https://www.icc-cricket.com/rankings/womens/player-rankings/odi/batting')
page6_2


# In[79]:


wbat = BeautifulSoup(page6_2.content)
wbat


# In[86]:


wbat_name = []
for i in wbat.find_all('div',class_="rankings-block__banner--name-large"):
    wbat_name.append(i.text)
    
wbat_name


# In[87]:


wbat_name2 = []
for i in wbat.find_all('td',class_="table-body__cell rankings-table__name name"):
    wbat_name2.append(i.text)
    
wbat_name2 = wbat_name2[0:9]
wbat_name2


# In[88]:


wbat_name2= [i.split('\n')[1] for i in wbat_name2]

wbat_name = wbat_name + wbat_name2


# In[89]:


wbat_name


# In[90]:


wbat_team = []
for i in wbat.find_all('div',class_="rankings-block__banner--nationality"):
    wbat_team.append(i.text)
    
wbat_team


# In[91]:


wbat_team = [i.split('\n')[2] for i in wbat_team]

wbat_team


# In[92]:


wbat_team2 = []
for i in wbat.find_all('span',class_="table-body__logo-text"):
    wbat_team2.append(i.text)
    
wbat_team2 = wbat_team2[0:9]
wbat_team = wbat_team + wbat_team2
wbat_team


# In[93]:


wbat_rating = []
for i in wbat.find_all('div',class_="rankings-block__banner--rating"):
    wbat_rating.append(i.text)
    
wbat_rating


# In[94]:


wbat_rating2 = []
for i in wbat.find_all('td',class_="table-body__cell rating"):
    wbat_rating2.append(i.text)
    
wbat_rating2 = wbat_rating2[0:9]
wbat_rating2


# In[95]:


wbat_rating = wbat_rating + wbat_rating2
wbat_rating


# In[96]:


women_batsmen_ranking = pd.DataFrame({'Player Name':wbat_name,'Team':wbat_team,'Rating':wbat_rating})
women_batsmen_ranking


# In[97]:


##(C.)  TOP 10 ODI WOMEN'S BOWLERS

page6_3 = requests.get('https://www.icc-cricket.com/rankings/womens/player-rankings/odi/bowling')
page6_3


# In[98]:


wbowl = BeautifulSoup(page6_3.content)
wbowl


# In[99]:


wbowl_name = []
for i in wbowl.find_all('div',class_="rankings-block__banner--name-large"):
    wbowl_name.append(i.text)
    
wbowl_name


# In[100]:


wbowl_name2 = []
for i in wbowl.find_all('td',class_="table-body__cell rankings-table__name name"):
    wbowl_name2.append(i.text)
    
wbowl_name2 = wbowl_name2[0:9]
wbowl_name2


# In[101]:


wbowl_name2= [i.split('\n')[1] for i in wbowl_name2]
wbowl_name = wbowl_name + wbowl_name2

wbowl_name


# In[102]:


wbowl_team = []
for i in wbowl.find_all('div',class_="rankings-block__banner--nationality"):
    wbowl_team.append(i.text)
    
wbowl_team = [i.split('\n')[2] for i in wbowl_team]

wbowl_team


# In[103]:


wbowl_team2 = []
for i in wbowl.find_all('span',class_="table-body__logo-text"):
    wbowl_team2.append(i.text)
    
wbowl_team2 = wbowl_team2[0:9]
wbowl_team = wbowl_team + wbowl_team2
wbowl_team


# In[105]:


wbowl_rating = []
for i in wbowl.find_all('div',class_="rankings-block__banner--rating"):
    wbowl_rating.append(i.text)
    
wbowl_rating


# In[106]:


for i in wbowl.find_all('td',class_="table-body__cell rating"):
    wbowl_rating.append(i.text)
    
wbowl_rating = wbowl_rating[0:10]
wbowl_rating


# In[107]:


women_bowler_ranking = pd.DataFrame({'Bowler Name':wbowl_name,'Team':wbowl_team,'Rating':wbowl_rating})
women_bowler_ranking


# In[ ]:




