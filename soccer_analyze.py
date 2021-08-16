# Importing the relevant liabraries.
from bs4 import BeautifulSoup
import requests
import warnings
from requests.packages.urllib3.exceptions import InsecureRequestWarning
import matplotlib.pyplot as plt
import pandas as pd

# Requesting permission to use the site for web scraping (Italy Seria-A).
warnings.simplefilter('ignore',InsecureRequestWarning)
source5 = requests.get("https://www.worldfootball.net/winner/ita-serie-a/", verify=False).text
soup5 = BeautifulSoup(source5, 'lxml')

# Creating empty list to store the data from site.
table_information_serie_A=[]

# Runnig with a loop through the content of the relevant spot in the site.
for td in soup5.find_all("td"):
# Appending the data into the empty list.
    table_information_serie_A.append(td.text)
# Start working on the strings in order to remove unnecessary characters and separate the data into teams, years and nationality.
years_seria_A=table_information_serie_A[0::5]
years_seria_A=[i.replace('\n',"").replace('\t',"") for i in years_seria_A]
del years_seria_A[119:]
winners_seria_A=table_information_serie_A[2::5]
del winners_seria_A[119:]
nationality_seria_A=table_information_serie_A[4::5]
del nationality_seria_A[119:]

# Requesting permission to use the site for web scraping (Spanish League).
warnings.simplefilter('ignore',InsecureRequestWarning)
source1 = requests.get("https://www.worldfootball.net/winner/esp-primera-division/", verify=False).text
soup1 = BeautifulSoup(source1, 'lxml')

# Creating empty list to store the data from site.
table_information_spanish_league=[]

# Runnig with a loop through the content of the relevant spot in the site.
for td in soup1.find_all("td"):
    table_information_spanish_league.append(td.text.encode(encoding='ascii',errors="replace"))

# Replacing all the data into string data type
str_spanish_league=[]
for i in table_information_spanish_league:
    x=str(i)
    str_spanish_league.append(x)

# Start working on the strings in order to remove unnecessary characters and separate the data into teams, years and nationality.
years_spanish_league=str_spanish_league[0::5]
years_spanish_league=[v.replace("b'","").replace("\\n","").replace("'","") for v in years_spanish_league]
del years_spanish_league[89:]
winners_spanish_league=str_spanish_league[2::5]
winners_spanish_league=[f.replace("b'","").replace("'","").replace("??","e") for f in winners_spanish_league]

# Function to swap between the first and second charcter in a string.
def replace_second(string,e,n):
    return string.replace("e","n",2).replace("n","e",1)
winners_spanish_league[20]=replace_second(winners_spanish_league[20],"e","n")
del winners_spanish_league[89:]
nationality_spanish_league=str_spanish_league[4::5]
nationality_spanish_league=[g.replace("b'","").replace("'","") for g in nationality_spanish_league]
del nationality_spanish_league[89:]

# Requesting permission to use the site for web scraping (Premier League).
warnings.simplefilter('ignore',InsecureRequestWarning)
source2 = requests.get("https://www.worldfootball.net/winner/eng-premier-league/", verify=False).text
soup2 = BeautifulSoup(source2, 'lxml')

# Creating empty list to store the data from site.
table_information_premier_league=[]

# Runnig with a loop through the content of the relevant spot in the site.
for td in soup2.find_all("td"):
    table_information_premier_league.append(td.text)

# Start working on the strings in order to remove unnecessary characters and separate the data into teams, years and nationality.
years_premier_league=table_information_premier_league[0::5]
winners_premier_league=table_information_premier_league[2::5]
nationality_premier_league=table_information_premier_league[4::5]
del years_premier_league[121:]
years_premier_league=[x.replace("\n","") for x in years_premier_league]
del winners_premier_league[121:]
del nationality_premier_league[121:]

# Requesting permission to use the site for web scraping (Bundes Liga).
warnings.simplefilter('ignore',InsecureRequestWarning)
source3 = requests.get("https://www.worldfootball.net/winner/bundesliga/", verify=False).text
soup3 = BeautifulSoup(source3, 'lxml')

# Creating empty list to store the data from site.
table_information_bundesliga=[]

# Runnig with a loop through the content of the relevant spot in the site.
for td in soup3.find_all("td"):
    table_information_bundesliga.append(td.text.encode(encoding='ascii',errors="replace"))

# Replacing all the data into string data type
str_table_information_bundesliga=[]
for i in table_information_bundesliga:
    x=str(i)
    str_table_information_bundesliga.append(x)

# Start working on the strings in order to remove unnecessary characters and separate the data into teams, years and nationality.
years_bundesliga=str_table_information_bundesliga[0::5]
years_bundesliga=[y.replace("b'","").replace("\\n","").replace("'","") for y in years_bundesliga]
del years_bundesliga[109:]
winners_bundesliga=str_table_information_bundesliga[2::5]
winners_bundesliga=[w.replace("b'","").replace("'","") for w in winners_bundesliga]
del winners_bundesliga[109:]
winners_bundesliga=[t.replace("??","u") for t in winners_bundesliga]
winners_bundesliga=[o.replace("?","u") for o in winners_bundesliga]
nationality_bundesliga=str_table_information_bundesliga[4::5]
nationality_bundesliga=[l.replace("b'","").replace("'","") for l in nationality_bundesliga]
del nationality_bundesliga[109:]

# Requesting permission to use the site for web scraping (French League).
warnings.simplefilter('ignore',InsecureRequestWarning)
source4 = requests.get("https://www.worldfootball.net/winner/fra-ligue-1/", verify=False).text
soup4 = BeautifulSoup(source4, 'lxml')

# Creating empty list to store the data from site.
table_information_french_league=[]

# Runnig with a loop through the content of the relevant spot in the site.
for td in soup4.find_all("td"):
    table_information_french_league.append(td.text.encode(encoding='ascii',errors="replace"))

# Replacing all the data into string data type
str_table_information_french_league=[]
for i in table_information_french_league:
    x=str(i)
    str_table_information_french_league.append(x)

# Start working on the strings in order to remove unnecessary characters and separate the data into teams, years and nationality.
years_french_league=str_table_information_french_league[0::5]
years_french_league=[n.replace("b'","").replace("\\n","").replace("'","").replace("\\t","") for n in years_french_league]
del years_french_league[123:]
winners_french_league=str_table_information_french_league[2::5]
winners_french_league=[r.replace("b'","").replace("'","").replace("??","e") for r in winners_french_league]
del winners_french_league[123:]
nationality_french_league=str_table_information_french_league[4::5]
nationality_french_league=[a.replace("b'","").replace("'","") for a in nationality_french_league]
del nationality_french_league[123:]

# Concatenate all the lists into one list that stores all the data for all leagues: winners, years and nationality.
total_winners=winners_spanish_league+winners_bundesliga+winners_french_league+winners_premier_league+winners_seria_A
total_years=years_spanish_league+years_bundesliga+years_french_league+years_premier_league+years_seria_A
total_nationality=nationality_spanish_league+nationality_bundesliga+nationality_french_league+nationality_premier_league+nationality_seria_A

# Creating a dictionary from the data and put akk into a DataFrame using Pandas.
dict={'winners': total_winners,'years':total_years,'nationality':total_nationality}
df=pd.DataFrame(data=dict)

# Saving the DataFrame into a csv file.
df.to_csv(r'C:\Users\assaf\PycharmProjects\Assaf\Soccer stats project\total_soccer_dataframe.csv',index=False,header=True)

# Loading the data and using matplotlib to create bar plot with the top 5 championship winners.
stats=pd.read_csv("total_soccer_dataframe.csv")
stats["winners"].value_counts().head().plot(kind="bar",title="Top 5 winners championship",rot=0)
plt.show()





























