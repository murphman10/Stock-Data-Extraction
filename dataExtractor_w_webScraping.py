# Install toolkits
#!pip install pandas
#!pip install requests
#!pip install bs4
#!pip install html5lib 
#!pip install lxml
#!pip install plotly

import pandas as pd
import requests # HTTP requests
from bs4 import BeautifulSoup

import warnings
# Ignore all warnings
warnings.filterwarnings("ignore", category=FutureWarning)
# 1. Send an HTTP request to the web page
url = "https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-PY0220EN-SkillsNetwork/labs/project/netflix_data_webpage.html"
data  = requests.get(url).text
print(data)

#2. Parse the HTML content
soup = BeautifulSoup(data, 'html.parser')

#3. Identify the HTML tags
netflix_data = pd.DataFrame(columns=["Date", "Open", "High", "Low", "Close", "Volume"])

#4. Use a BeautifulSoup method for extracting data
# First we isolate the body of the table which contains all the information
# Then we loop through each row and find all the column values for each row
for row in soup.find("tbody").find_all('tr'):
    col = row.find_all("td")
    date = col[0].text
    Open = col[1].text
    high = col[2].text
    low = col[3].text
    close = col[4].text
    adj_close = col[5].text
    volume = col[6].text
    
    # Finally we append the data of each row to the table
    netflix_data = pd.concat([netflix_data,pd.DataFrame({"Date":[date], "Open":[Open], "High":[high], "Low":[low], "Close":[close], "Adj Close":[adj_close], "Volume":[volume]})], ignore_index=True)

#5. Print the extracted data
netflix_data.head()

#Extracting using the pandas library ALTERNATIVE
read_html_pandas_data = pd.read_html(url)
read_html_pandas_data = pd.read_html(str(soup)) #converting the object to a string
netflix_dataframe = read_html_pandas_data[0]

netflix_dataframe.head()


