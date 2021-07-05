# Simple python project to get Crypto/Share price using Yahoo Finance package
# import required packages
import yfinance as yf
import matplotlib

matplotlib.use('TkAgg')
import matplotlib.pyplot as plt

# Get Name of the Crypto/Share
val = raw_input("Enter Stock/Crypto Name :")
msft = yf.Ticker(val)

# Get Number of days
per = raw_input("Enter Number of Days :")
per = per + "d"
hist = msft.history(period=per)

# Plot the Graph
hist['Close'].plot(figsize=(16, 9))
plt.show()
