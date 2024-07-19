import pandas as pd
import yfinance as yf
import matplotlib.pyplot as plt
import numpy as np
import mplfinance as mpf


# Task 1
def find_ratio(param_1, param_2, ratio_1, ratio_2, data):
    count = 0
    arr = np.array(data[param_1] / data[param_2])
    for ratio in arr:
        if ratio_1 < ratio < ratio_2:
            count = count + 1
    txt = 'number of times {}/{} lies between {} and {} is: {}'.format(
        param_1, param_2, ratio_1, ratio_2, count)
    print(txt)


def stocks(stock):
    data = yf.download(stock, start='2022-01-01', end='2023-01-01')
    find_ratio('Open', 'Close', 0.35, 0.5, data)
    find_ratio('Open', 'Close', 0.5, 1.0, data)
    find_ratio('Open', 'Close', 1.0, 3.5, data)
    find_ratio('Open', 'Low', 0.35, 0.5, data)
    find_ratio('Open', 'Low', 0.5, 1.0, data)
    find_ratio('Open', 'Low', 1.0, 3.5, data)
    find_ratio('High', 'Low', 0.35, 0.5, data)
    find_ratio('High', 'Low', 0.5, 1.0, data)
    find_ratio('High', 'Low', 1.0, 3.5, data)
    find_ratio('High', 'Close', 0.35, 0.5, data)
    find_ratio('High', 'Close', 0.5, 1.0, data)
    find_ratio('High', 'Close', 1.0, 3.5, data)


stocks('ADANIGREEN.NS')
stocks('FL')
stocks('AAPL')
stocks('Gold')
stocks('FTCH')

# Task 2
data_1 = yf.download('AAPL', start='2020-01-01', end='2023-01-01')
candlestick_data = data_1[['Open', 'High', 'Low', 'Close']]
mpf.plot(candlestick_data, type='candle', title='Candlestick Chart - AAPL',
         ylabel='Price', figratio=(10, 6), xrotation=30)
mpf.show()

# plotting graph
data_2 = yf.download('GOOG', start='2020-01-01', end='2023-01-01')
x_1 = np.array(data_1.index)
y_3 = np.array(data_1['Close'])
y_4 = np.array(data_2['Close'])
plt.plot(x_1, y_3, label='Closing price of AAPL ')
plt.plot(x_1, y_4, label='Closing price of GOOG ')
plt.legend()
plt.title('Closing price of AAPL vs GOOG')
plt.xlabel("Date")
plt.ylabel("Closing price")
plt.show()

print("Apple's stock experienced a rapid rise in 2020 for several reasons. First, despite the COVID-19 pandemic, Apple's products, such as iPhones, iPads, and Macs, remained in high demand. The shift to remote work and increased reliance on technology boosted Apple's sales. Second, the company's services segment, including the App Store, Apple Music, and Apple Pay, continued to grow, contributing to increased revenue. Third, Apple's announcement of its transition to custom-designed processors for Mac computers, called Apple Silicon, generated excitement and positive investor sentiment. Lastly, the overall resilience of the tech sector and the market's confidence in Apple's ability to innovate and generate consistent profits also played a role in the stock's rapid rise.")   
print("The decline in stock prices of both Apple and Google from January 2020 to March 2020 can be attributed to the significant impact of the COVID-19 pandemic on global financial markets. During this period, the pandemic spread rapidly across the world, leading to widespread economic uncertainty and investor panic.")
print("Moreover, in times of market turmoil, investors tend to seek safer assets, such as bonds or cash, causing a general flight from equities. This trend contributed to the decline in stock prices for Apple, Google, and other companies.")
print(" However, from late March onwards, central banks and governments worldwide implemented monetary and fiscal stimulus measures to support the economy and stabilize financial markets. ")
print("During this period, technology companies, including those like Apple, Amazon, Microsoft, and others, played a crucial role in driving the stock market's recovery. These companies benefitted from increased demand for remote work solutions, e-commerce, and digital services, as people turned to technology during lockdowns and social distancing measures.")