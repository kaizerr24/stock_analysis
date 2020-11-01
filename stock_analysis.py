# Importing the python libraries which we will need in order to run this project
from pandas_datareader import data as web
import pandas as pd
from datetime import datetime as dt
from datetime import timedelta
import matplotlib.pyplot as plt
from tkinter import *
from tkinter import messagebox
import webbrowser as wbb
import random


# Creating the graphical user interface for the program
class StockAnalysis:
    # By using the "self" keyword we can access the attributes and methods
    # This method is called when an object is created from the class
    def __init__(self):
        root = Tk()
        root.title("Stock Analysis")

        # Creating variables to store the inputs
        self.stocks = StringVar()
        self.startdate = StringVar()
        self.enddate = StringVar()

        # Creating variables for the outputs
        self.stockv = StringVar()
        self.stockr = StringVar()
        self.stockrisk = StringVar()
    
        # Defining the titles
        t1 = Label(root, text='Stocks and Time Frame', font='Times 12 bold')
        t1.grid(row=0, column=0, columnspan=2, sticky="w")

        t2 = Label(root, text='Stock Analysis', font='Times 12 bold')
        t2.grid(row=5, column=0, columnspan=2, sticky="w")

        t3 = Label(root, text='Output', font='Times 11 bold italic')
        t3.grid(row=5, column=2, columnspan=2, sticky="w")

        t4 = Label(root, text='Stock Visualisation', font='Times 12 bold')
        t4.grid(row=10, column=0, columnspan=2, sticky="w")

        t5 = Label(root, text='Additional Information', font='Times 12 bold')
        t5.grid(row=13, column=0, columnspan=2, sticky="w")

        # Defining the labels
        l1 = Label(root, text='Stocks (Key, Key,...)')
        l1.grid(row=1, column=0, sticky="w")

        l2 = Label(root, text='Startdate (dd/mm/yyyy)')
        l2.grid(row=1, column=2, sticky="w")

        l3 = Label(root, text='Enddate (dd/mm/yyyy)')
        l3.grid(row=2, column=2, sticky="w")

        l4 = Label(root, text='Most Volume:', font='Times 10 italic')
        l4.grid(row=6, column=2, sticky="w")

        l5 = Label(root, textvariable=self.stockv)
        l5.grid(row=6, column=3, sticky="s")

        l6 = Label(root, text='Highest Return:', font='Times 10 italic')
        l6.grid(row=7, column=2, sticky="w")

        l7 = Label(root, textvariable=self.stockr)
        l7.grid(row=7, column=3, sticky="s")

        l8 = Label(root, text='Highest Daily Volatility:', font='Times 10 italic')
        l8.grid(row=8, column=2, sticky="w")

        l9 = Label(root, textvariable=self.stockrisk)
        l9.grid(row=8, column=3, sticky="s")

        # Defining additional empty labels to make the structure clearer
        el1 = Label(root, text='')
        el1.grid(row=4, column=2, sticky="w")

        el2 = Label(root, text='')
        el2.grid(row=9, column=2, sticky="w")

        el3 = Label(root, text='')
        el3.grid(row=12, column=2, sticky="w")

        # Defining the entries
        e1 = Entry(root, textvariable=self.stocks)
        e1.grid(row=1, column=1)

        e2 = Entry(root, textvariable=self.startdate)
        e2.grid(row=1, column=3)

        e3 = Entry(root, textvariable=self.enddate)
        e3.grid(row=2, column=3)

        # Defining the buttons
        b1 = Button(root, text='Set Random', command=self.setrandom)
        b1.grid(row=2, column=1, sticky="ew")

        b2 = Button(root, text='Analyse Stocks', command=self.stockmain)
        b2.grid(row=6, column=0, sticky="ew")

        b3 = Button(root, text='Stock Prices', command=self.stockdata)
        b3.grid(row=11, column=0, sticky="ew")

        b4 = Button(root, text='Returns', command=self.stockreturns)
        b4.grid(row=11, column=1, sticky="ew")

        b5 = Button(root, text='Volatility', command=self.stockvola)
        b5.grid(row=11, column=2, sticky="ew")

        b6 = Button(root, text='Yahoo Website', command=self.openwebsite)
        b6.grid(row=14, column=0, sticky="ew")

        b7 = Button(root, text='Stock Websites', command=self.lookupstock)
        b7.grid(row=14, column=1, sticky="ew")

        root.mainloop()

    # Creating the function which simulates the program with random stocks and a random time frame
    def setrandom(self):
        assets = ['AAPL', 'BAC', 'INTC', 'WFC', 'T', 'PFE', 'CSCO', 'XOM', 'MSFT', 'TSLA', 'FB', 'CVX',
                  'KO', 'VZ', 'BABA', 'MRK', 'LLY', 'CMCSA', 'ORCL', 'JPM', 'BMY', 'SBUX', 'V', 'JD', 'ZM',
                  'DIS', 'PG', 'SAP', 'QCOM', 'ABBV', 'NVDA', 'UPS', 'TSM', 'JNJ', 'NEE', 'PYPL', 'PM', 'UNP',
                  'LOW', 'AMZN', 'MDT', 'TXN', 'NVS', 'WMT', 'MA', 'CRM', 'NFLX', 'AZN', 'PEP', 'ABT']
        assets_random = random.sample(assets, 4)
        joined_assets = ",".join(assets_random)

        self.stocks.set(joined_assets)

        ry1 = random.randint(2015, 2019)
        rm1 = random.randint(1, 11)
        rd1 = random.randint(1, 29)
        rdate1 = (str(rd1).zfill(2) + '/' + str(rm1).zfill(2) + '/' + str(ry1))

        self.startdate.set(rdate1)

        ry2 = random.randint(ry1, 2020)
        rm2 = random.randint(rm1, 12)
        rd2 = random.randint(rd1, 30)
        # @Kai hani gmacht damit date nöd di gliche könd si
        while ry1 == ry2:
            ry2 = random.randint(ry1, 2020)
        while rm1 == rm2:
            rm2 = random.randint(rm1, 12)
        while rd1 == rd2:
            rd2 = random.randint(rd1, 30)

        rdate2 = (str(rd2).zfill(2) + '/' + str(rm2).zfill(2) + '/' + str(ry2))
        self.enddate.set(rdate2)

    # Creating the main function to analyse the stocks
    def stockmain(self):
        stocks = self.stocks.get()
        startdate = self.startdate.get()
        enddate = self.enddate.get()

        try:
            startcon = dt.strptime(startdate, '%d/%m/%Y')
            endcon = dt.strptime(enddate, '%d/%m/%Y')
        except Exception:
            messagebox.showwarning("Input Error", "Enter valid Start- and Enddate! (dd/mm/yyyy)")
            return

        # This deletes the spaces in the stock userinput
        assets = stocks.replace(" ", "")
        assets = assets.split(",")

        # Storing the adjusted close price of stock into the data frame
        # Displaying an error message if the user makes an invalid input
        try:
            df1 = pd.DataFrame()
            for stock in assets:
                df1[stock] = web.DataReader(stock, data_source='yahoo', start=startcon, end=endcon)['Volume']
        except Exception:
            messagebox.showwarning("Data Error", "Key or time frame is not available.")
            return

        # Most volume over timeframe
        df_volume = df1.sum(axis=0, skipna=True)
        df_volume = df_volume.nlargest(n=1, keep='first')
        df_volume = df_volume.index.tolist()

        self.stockv.set(format(df_volume[0]))

        # Highest return
        df2 = pd.DataFrame()
        for stock in assets:
            df2[stock] = web.DataReader(stock, data_source='yahoo', start=startcon, end=endcon)['Adj Close']

        df_return = df2.pct_change(1) + 1
        df_return = df_return.product()
        df_return = df_return.nlargest(n=1, keep='first')
        df_return = df_return.index.tolist()

        self.stockr.set(format(df_return[0]))

        # If the data of the stock doesn't exist more for more than 100 days, the SMA won't work
        if endcon - startcon > timedelta(days=100):
            df_highestreturnstock = web.DataReader(df_return[0], data_source='yahoo',
                                                   start=startcon - timedelta(days=100), end=endcon)['Adj Close']

            short_rolling = df_highestreturnstock.rolling(window=20).mean()
            long_rolling = df_highestreturnstock.rolling(window=100).mean()
            short_rolling = short_rolling[100:]
            df_highestreturnstock = df_highestreturnstock[100:]

            # Visualising the stock with the highest return if possible the simple moving average
            plt.style.use('fivethirtyeight')
            plt.figure(figsize=(18, 8))
            plt.plot(df_highestreturnstock, label=df_return[0])
            plt.plot(short_rolling, label='SMA 20-days')
            plt.plot(long_rolling, label='SMA 100-days')
            plt.title('Stock with the Highest Return (Simple Moving Average)', fontsize=18, weight="bold")
            plt.legend(loc='upper left')
            plt.xlabel('Date', fontsize=18)
            plt.ylabel('Adjusted Price USD ($)', fontsize=18)
            plt.show()
        else:
            df_highestreturnstock = web.DataReader(df_return[0], data_source='yahoo', start=startcon,
                                                   end=endcon)['Adj Close']
            plt.style.use('fivethirtyeight')
            plt.figure(figsize=(18, 8))
            plt.plot(df_highestreturnstock, label=df_return[0])
            plt.title('Stock with the Highest Return', fontsize=18, weight="bold")
            plt.legend(loc='upper left')
            plt.xlabel('Date', fontsize=18)
            plt.ylabel('Adjusted Price USD ($)', fontsize=18)
            plt.show()

        # Highest Volatility
        df3 = pd.DataFrame()
        # Storing the adjusted close price of stock into the data frame
        for stock in assets:
            df3[stock] = web.DataReader(stock, data_source='yahoo', start=startcon, end=endcon)['Adj Close']

        # Highest daily percentage change
        sreturns = df3.pct_change(1)
        sreturns = sreturns.abs()
        sreturns = sreturns.mean()
        sreturns = sreturns.nlargest(n=1, keep='first')
        sreturns = sreturns.index.tolist()

        self.stockrisk.set(format(sreturns[0]))

    # Creating the function that visualises the stock prices of the stocks
    def stockdata(self):
        stocks = self.stocks.get()
        startdate = self.startdate.get()
        enddate = self.enddate.get()

        # Checking the Date Input if it's correct
        try:
            startcon = dt.strptime(startdate, '%d/%m/%Y')
            endcon = dt.strptime(enddate, '%d/%m/%Y')
        except Exception:
            messagebox.showwarning("Input Error", "Enter valid Start- and Enddate! (dd/mm/yyyy)")
            return

        # Deleting the spaces in the stock userinput
        assets = stocks.replace(" ", "")
        assets = assets.split(",")

        # Storing the adjusted close price of stock into the data frame
        try:
            df = pd.DataFrame()
            for stock in assets:
                df[stock] = web.DataReader(stock, data_source='yahoo', start=startcon, end=endcon)['Adj Close']
        except Exception:
            messagebox.showwarning("Data Error", "Key or time frame is not available.")
            return

        my_stocks = df
        plt.style.use('fivethirtyeight')
        plt.figure(figsize=(18, 8))

        # Looping through each stock and plot the Adj Close for each day
        for c in my_stocks.columns.values:
            plt.plot(my_stocks[c], label=c)
        plt.legend(my_stocks.columns.values, loc='upper left')
        plt.title('Stock Price(s)', fontsize=18, weight="bold")
        plt.xlabel('Date', fontsize=18)
        plt.ylabel('Adjusted Price USD ($)', fontsize=18)
        plt.show()

    # Creating the function that visualises the returns of the stocks
    def stockreturns(self):
        stocks = self.stocks.get()
        startdate = self.startdate.get()
        enddate = self.enddate.get()

        try:
            startcon = dt.strptime(startdate, '%d/%m/%Y')
            endcon = dt.strptime(enddate, '%d/%m/%Y')
        except Exception:
            messagebox.showwarning("Input Error", "Enter valid Start- and Enddate! (dd/mm/yyyy)")
            return

        # Deleting the spaces in the stock userinput
        assets = stocks.replace(" ", "")
        assets = assets.split(",")

        try:
            df = pd.DataFrame()
            # Storing the adjusted close price of stock into the data frame
            # Showing an error if the user enters an invalid input
            for stock in assets:
                df[stock] = web.DataReader(stock, data_source='yahoo', start=startcon, end=endcon)['Adj Close']
        except Exception:
            messagebox.showwarning("Data Error", "Key or time frame is not available.")
            return

        # Creating and plotting the graph for the stock return
        df = df / df.iloc[0, :]
        plt.style.use('fivethirtyeight')
        plt.figure(figsize=(18, 8))
        plt.plot(df)
        plt.title('Stock Returns', fontsize=18, weight="bold")
        plt.xlabel('Date', fontsize=18)
        plt.ylabel('Changes in Stock Price', fontsize=18)
        plt.legend(assets, loc='upper left')
        plt.show()

    # Creating the function that visualises the volatility of the stocks
    def stockvola(self):
        stocks = self.stocks.get()
        startdate = self.startdate.get()
        enddate = self.enddate.get()

        try:
            startcon = dt.strptime(startdate, '%d/%m/%Y')
            endcon = dt.strptime(enddate, '%d/%m/%Y')
        except Exception:
            messagebox.showwarning("Input Error", "Enter valid Start- and Enddate! (dd/mm/yyyy)")
            return

        # Deleting the spaces in the stock userinput
        assets = stocks.replace(" ", "")
        assets = assets.split(",")

        # Storing the adjusted close price of stock into the data frame
        try:
            df = pd.DataFrame()
            for stock in assets:
                df[stock] = web.DataReader(stock, data_source='yahoo', start=startcon, end=endcon)['Adj Close']
        except Exception:
            messagebox.showwarning("Data Error", "Key or time frame is not available.")
            return

        # The daily change in stock prices
        sreturns = df.pct_change(1)

        plt.style.use('fivethirtyeight')

        # Creating and plotting the graph for the volatility
        plt.figure(figsize=(18, 8))
        for c in sreturns.columns.values:
            plt.plot(sreturns[c], lw=2, label=c)
        plt.title('Daily Volatility', fontsize=18, weight="bold")
        plt.xlabel('Date', fontsize=18)
        plt.ylabel('Daily Percentage Change', fontsize=18)
        plt.legend(sreturns.columns.values, loc='upper left')
        plt.show()

    # Creating the function that opens all the different websites of the stocks the user wants to analyse
    def lookupstock(self):
        stocks = self.stocks.get()
        assets = stocks.replace(" ", "")
        assets = assets.split(",")

        for stocks in assets:
            wbb.open('https://finance.yahoo.com/quote/' + stocks)

    # Creating the function which opens the main yahoo finance website
    def openwebsite(self):
        wbb.open('https://finance.yahoo.com/')


StockAnalysis()
