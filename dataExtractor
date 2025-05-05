#Install toolkits
# !pip install yfinance
# !pip install matplotlib
# !pip install pandas==1.3.3

import yfinance as yf
import pandas as pd
import json

#Use the Ticker module to create an object to extract data from specific stocks
apple = yf.Ticker("AAPL") #Apple Inc.

with open('apple.json') as json_file:
    apple_info = json.load(json_file)
    # Print the type of data variable    
    print("Type:", type(apple_info))
apple_info
apple_info['country']
apple_share_price_data = apple.history(period="max")
apple_share_price_data.head()
apple_share_price_data.reset_index(inplace=True)

#Plot data on a graph
apple_share_price_data.plot(x="Date", y="Open")

# Download historical data for a stock
amd = yf.Ticker("AMD")
with open('amd.json') as json_file:
    amd_info = json.load(json_file)
    # Print the type of data variable    
    print("Type:", type(amd_info))
amd_info
#Get country/ sector info
amd_info['country']
amd_info['sector']

amd_share_price_data = amd.history(period="max") # Download historical data for a stock
#Display the downloaded data formatted as table
amd_share_price_data.head()
