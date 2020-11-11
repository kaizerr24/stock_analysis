# Importing the python libraries which we will need in order to run this project
from pandas_datareader import data as web
import pandas as pd
from datetime import datetime as dt
from datetime import timedelta
import matplotlib.pyplot as plt
import tkinter as tk
import tkinter.messagebox
import webbrowser as wbb
import random


# Creating the graphical user interface for the program
class StockAnalysis:
    # This method is called when an object is created from the class
    # By using the "self" keyword we can access the attributes and methods
    def __init__(self):
        # Creating the main window of the application
        root = tk.Tk()
        root.title("Stock Analysis")

        # Creating variables to store the inputs
        self.stocks = tk.StringVar()
        self.startDate = tk.StringVar()
        self.endDate = tk.StringVar()

        # Creating variables to store the outputs
        self.stockV = tk.StringVar()
        self.stockR = tk.StringVar()
        self.stockRisk = tk.StringVar()

        # Defining the titles
        t1 = tk.Label(root, text='Stocks and Time Frame', font='Times 12 bold')
        t1.grid(row=0, column=0, columnspan=2, sticky="w")

        t2 = tk.Label(root, text='Stock Analysis', font='Times 12 bold')
        t2.grid(row=5, column=0, columnspan=2, sticky="w")

        t3 = tk.Label(root, text='Output', font='Times 11 bold italic')
        t3.grid(row=5, column=2, columnspan=2, sticky="w")

        t4 = tk.Label(root, text='Stock Visualisation', font='Times 12 bold')
        t4.grid(row=10, column=0, columnspan=2, sticky="w")

        t5 = tk.Label(root, text='Additional Information', font='Times 12 bold')
        t5.grid(row=13, column=0, columnspan=2, sticky="w")

        # Defining the labels
        l1 = tk.Label(root, text='Stocks (Key, Key,...)')
        l1.grid(row=1, column=0, sticky="w")

        l2 = tk.Label(root, text='Start Date (dd/mm/yyyy)')
        l2.grid(row=1, column=2, sticky="w")

        l3 = tk.Label(root, text='End Date (dd/mm/yyyy)')
        l3.grid(row=2, column=2, sticky="w")

        l4 = tk.Label(root, text='Most Volume:', font='Times 10 italic')
        l4.grid(row=6, column=2, sticky="sw")

        l5 = tk.Label(root, textvariable=self.stockV)
        l5.grid(row=6, column=3, sticky="s")

        l6 = tk.Label(root, text='Highest Return:', font='Times 10 italic')
        l6.grid(row=7, column=2, sticky="w")

        l7 = tk.Label(root, textvariable=self.stockR)
        l7.grid(row=7, column=3, sticky="s")

        l8 = tk.Label(root, text='Highest Daily Volatility:', font='Times 10 italic')
        l8.grid(row=8, column=2, sticky="w")

        l9 = tk.Label(root, textvariable=self.stockRisk)
        l9.grid(row=8, column=3, sticky="s")

        # Defining additional empty labels to structure the application
        el1 = tk.Label(root, text='')
        el1.grid(row=4, column=2, sticky="w")

        el2 = tk.Label(root, text='')
        el2.grid(row=9, column=2, sticky="w")

        el3 = tk.Label(root, text='')
        el3.grid(row=12, column=2, sticky="w")

        # Defining the entries
        e1 = tk.Entry(root, textvariable=self.stocks)
        e1.grid(row=1, column=1)

        e2 = tk.Entry(root, textvariable=self.startDate)
        e2.grid(row=1, column=3)

        e3 = tk.Entry(root, textvariable=self.endDate)
        e3.grid(row=2, column=3)

        # Defining the buttons
        b1 = tk.Button(root, text='Set Random', command=self.set_random)
        b1.grid(row=2, column=1, sticky="ew")

        b2 = tk.Button(root, text='Analyse Stocks', command=self.stock_main)
        b2.grid(row=6, column=0, sticky="ew")

        b3 = tk.Button(root, text='Stock Prices', command=self.stock_data)
        b3.grid(row=11, column=0, sticky="ew")

        b4 = tk.Button(root, text='Returns', command=self.stock_returns)
        b4.grid(row=11, column=1, sticky="ew")

        b5 = tk.Button(root, text='Volatility', command=self.stock_volatility)
        b5.grid(row=11, column=2, sticky="ew")

        b6 = tk.Button(root, text='Yahoo Website', command=self.open_website)
        b6.grid(row=14, column=0, sticky="ew")

        b7 = tk.Button(root, text='Stock Websites', command=self.lookup_stock)
        b7.grid(row=14, column=1, sticky="ew")

        root.mainloop()

    # Creating the function which sets random stocks and a random time frame
    def set_random(self):
        # Setting random stock keys from a list of Yahoo Finance stocks
        assets = ['AAPL', 'BAC', 'INTC', 'WFC', 'T', 'PFE', 'CSCO', 'XOM', 'MSFT', 'TSLA', 'FB', 'CVX',
                  'KO', 'VZ', 'BABA', 'MRK', 'LLY', 'CMCSA', 'ORCL', 'JPM', 'BMY', 'SBUX', 'V', 'JD', 'ZM',
                  'DIS', 'PG', 'SAP', 'QCOM', 'ABBV', 'NVDA', 'UPS', 'TSM', 'JNJ', 'NEE', 'PYPL', 'PM', 'UNP',
                  'LOW', 'AMZN', 'MDT', 'TXN', 'NVS', 'WMT', 'MA', 'CRM', 'NFLX', 'AZN', 'PEP', 'ABT']
        assets_random = random.sample(assets, 4)
        joined_assets = ",".join(assets_random)
        self.stocks.set(joined_assets)

        # Setting random start date within boundaries
        random_year1 = random.randint(2015, 2019)
        random_month1 = random.randint(1, 11)
        random_day1 = random.randint(1, 29)
        random_date1 = (str(random_day1).zfill(2) + '/' + str(random_month1).zfill(2) + '/' + str(random_year1))
        self.startDate.set(random_date1)

        # Setting random end date within boundaries
        random_year2 = random.randint(random_year1, 2020)
        random_month2 = random.randint(1, 12)
        random_day2 = random.randint(1, 30)
        # Checking that the end date is after the start date
        while random_year1 == random_year2 and random_month1 > random_month2:
            random_month2 = random.randint(1, 12)
        while random_year1 == random_year2 and random_month1 == random_month2 and random_day1 >= random_day2:
            random_day2 = random.randint(1, 30)
        random_date2 = (str(random_day2).zfill(2) + '/' + str(random_month2).zfill(2) + '/' + str(random_year2))
        self.endDate.set(random_date2)

    # Creating the main function to analyse the stocks
    def stock_main(self):
        stocks = self.stocks.get()
        start_date = self.startDate.get()
        end_date = self.endDate.get()

        # Displaying input error message if the dates entered have the wrong format
        try:
            start_con = dt.strptime(start_date, '%d/%m/%Y')
            end_con = dt.strptime(end_date, '%d/%m/%Y')
        except Exception:
            tk.messagebox.showwarning("Input Error", "Enter valid start and end date! (dd/mm/yyyy)")
            return

        # Deleting the spaces in the stock keys user input
        assets = stocks.replace(" ", "")
        assets = assets.split(",")

        # Displaying data error message if the stock keys or dates entered are not available
        data_frame1 = pd.DataFrame()
        try:
            for stock in assets:
                # Storing the volume of the stocks into the first data frame
                data_frame1[stock] = web.DataReader(stock, data_source='yahoo', start=start_con, end=end_con)['Volume']
        except Exception:
            tk.messagebox.showwarning("Data Error", "Key(s) or time frame is not available.")
            return

        # Calculating the stock with the most volume over the given time frame
        data_frame_volume = data_frame1.sum(axis=0, skipna=True)
        data_frame_volume = data_frame_volume.nlargest(n=1, keep='first')
        data_frame_volume = data_frame_volume.index.tolist()
        # Setting the stock key with the most volume over the given time frame as the output variable
        self.stockV.set(format(data_frame_volume[0]))

        # Storing the adjusted close of the stocks into the second data frame
        data_frame2 = pd.DataFrame()
        for stock in assets:
            data_frame2[stock] = web.DataReader(stock, data_source='yahoo', start=start_con, end=end_con)['Adj Close']

        # Calculating the stock with the highest return over the given time frame
        data_frame_return = data_frame2.pct_change(1) + 1
        data_frame_return = data_frame_return.product()
        data_frame_return = data_frame_return.nlargest(n=1, keep='first')
        data_frame_return = data_frame_return.index.tolist()
        # Setting the stock key with the highest return over the given time frame as the output variable
        self.stockR.set(format(data_frame_return[0]))

        # Calculating the SMAs (simple moving average over 20 and 100 days) for the stock with the highest return
        # The SMAs will not be calculated if the time frame does not allow a SMA over 100 days
        if end_con - start_con > timedelta(days=100):
            data_frame_highest_return = web.DataReader(data_frame_return[0], data_source='yahoo',
                                                       start=start_con - timedelta(days=100), end=end_con)['Adj Close']
            short_rolling = data_frame_highest_return.rolling(window=20).mean()
            long_rolling = data_frame_highest_return.rolling(window=100).mean()
            short_rolling = short_rolling[100:]
            data_frame_highest_return = data_frame_highest_return[100:]

            # Visualising the stock with the highest return and the simple moving average
            plt.style.use('fivethirtyeight')
            plt.figure(figsize=(18, 8))
            plt.plot(data_frame_highest_return, label=data_frame_return[0])
            plt.plot(short_rolling, label='SMA 20-days')
            plt.plot(long_rolling, label='SMA 100-days')
            plt.title('Stock with the Highest Return (Simple Moving Average)', fontsize=18, weight="bold")
            plt.legend(loc='upper left')
            plt.xlabel('Date', fontsize=18)
            plt.ylabel('Adjusted Price USD ($)', fontsize=18)
            plt.show()
        else:
            data_frame_highest_return = web.DataReader(data_frame_return[0], data_source='yahoo', start=start_con,
                                                       end=end_con)['Adj Close']
            plt.style.use('fivethirtyeight')
            plt.figure(figsize=(18, 8))
            plt.plot(data_frame_highest_return, label=data_frame_return[0])
            plt.title('Stock with the Highest Return', fontsize=18, weight="bold")
            plt.legend(loc='upper left')
            plt.xlabel('Date', fontsize=18)
            plt.ylabel('Adjusted Price USD ($)', fontsize=18)
            plt.show()

        # Calculating the stock with the highest daily volatility over the given time frame
        data_frame_volatility = data_frame2.pct_change(1)
        data_frame_volatility = data_frame_volatility.abs()
        data_frame_volatility = data_frame_volatility.mean()
        data_frame_volatility = data_frame_volatility.nlargest(n=1, keep='first')
        data_frame_volatility = data_frame_volatility.index.tolist()
        self.stockRisk.set(format(data_frame_volatility[0]))

    # Creating the function that visualises the stock prices
    def stock_data(self):
        stocks = self.stocks.get()
        start_date = self.startDate.get()
        end_date = self.endDate.get()

        # Displaying input error message if the dates entered have the wrong format
        try:
            start_con = dt.strptime(start_date, '%d/%m/%Y')
            end_con = dt.strptime(end_date, '%d/%m/%Y')
        except Exception:
            tk.messagebox.showwarning("Input Error", "Enter valid start and end date! (dd/mm/yyyy)")
            return

        # Deleting the spaces in the stock keys user input
        assets = stocks.replace(" ", "")
        assets = assets.split(",")

        # Displaying data error message if the stock keys or dates entered are not available
        data_frame = pd.DataFrame()
        try:
            for stock in assets:
                # Storing the adjusted close of the stocks into a data frame
                data_frame[stock] = web.DataReader(stock, data_source='yahoo', start=start_con,
                                                   end=end_con)['Adj Close']
        except Exception:
            tk.messagebox.showwarning("Data Error", "Key(s) or time frame is not available.")
            return

        plt.style.use('fivethirtyeight')
        plt.figure(figsize=(18, 8))
        # Looping through each stock and plot the adjusted close
        for stock in data_frame.columns.values:
            plt.plot(data_frame[stock], label=stock)
        plt.legend(data_frame.columns.values, loc='upper left')
        plt.title('Stock Price(s)', fontsize=18, weight="bold")
        plt.xlabel('Date', fontsize=18)
        plt.ylabel('Adjusted Price USD ($)', fontsize=18)
        plt.show()

    # Creating the function that visualises the returns of the stocks
    def stock_returns(self):
        stocks = self.stocks.get()
        start_date = self.startDate.get()
        end_date = self.endDate.get()

        # Displaying input error message if the dates entered have the wrong format
        try:
            start_con = dt.strptime(start_date, '%d/%m/%Y')
            end_con = dt.strptime(end_date, '%d/%m/%Y')
        except Exception:
            tk.messagebox.showwarning("Input Error", "Enter valid start and end date! (dd/mm/yyyy)")
            return

        # Deleting the spaces in the stock keys user input
        assets = stocks.replace(" ", "")
        assets = assets.split(",")

        # Displaying data error message if the stock keys or dates entered are not available
        data_frame = pd.DataFrame()
        try:
            # Storing the adjusted close of the stocks into a data frame
            for stock in assets:
                data_frame[stock] = web.DataReader(stock, data_source='yahoo', start=start_con, end=end_con)['Adj Close']
        except Exception:
            tk.messagebox.showwarning("Data Error", "Key(s) or time frame is not available.")
            return

        # Creating and plotting the graph for the stock returns
        # Using integer-location based indexing for better comparison
        data_frame = data_frame / data_frame.iloc[0, :]
        plt.style.use('fivethirtyeight')
        plt.figure(figsize=(18, 8))
        plt.plot(data_frame)
        plt.title('Stock Returns', fontsize=18, weight="bold")
        plt.xlabel('Date', fontsize=18)
        plt.ylabel('Changes in Stock Price', fontsize=18)
        plt.legend(assets, loc='upper left')
        plt.show()

    # Creating the function that visualises the daily volatility of the stocks
    def stock_volatility(self):
        stocks = self.stocks.get()
        start_date = self.startDate.get()
        end_date = self.endDate.get()

        # Displaying input error message if the dates entered have the wrong format
        try:
            start_con = dt.strptime(start_date, '%d/%m/%Y')
            end_con = dt.strptime(end_date, '%d/%m/%Y')
        except Exception:
            tk.messagebox.showwarning("Input Error", "Enter valid start and end date! (dd/mm/yyyy)")
            return

        # Deleting the spaces in the stock keys user input
        assets = stocks.replace(" ", "")
        assets = assets.split(",")

        # Displaying data error message if the stock keys or dates entered are not available
        data_frame = pd.DataFrame()
        try:
            for stock in assets:
                # Storing the adjusted close of the stocks into a data frame
                data_frame[stock] = web.DataReader(stock, data_source='yahoo', start=start_con, end=end_con)['Adj Close']
        except Exception:
            tk.messagebox.showwarning("Data Error", "Key(s) or time frame is not available.")
            return

        # Calculating the daily changes in stock prices
        data_frame = data_frame.pct_change(1)

        plt.style.use('fivethirtyeight')
        plt.figure(figsize=(18, 8))
        # Looping through each stock and plot the daily percentage change
        for stock in data_frame.columns.values:
            plt.plot(data_frame[stock], lw=2, label=stock)
        plt.title('Daily Volatility', fontsize=18, weight="bold")
        plt.xlabel('Date', fontsize=18)
        plt.ylabel('Daily Percentage Change', fontsize=18)
        plt.legend(data_frame.columns.values, loc='upper left')
        plt.show()

    # Creating the function that opens all the stock websites the user wants to analyse from Yahoo Finance
    def lookup_stock(self):
        stocks = self.stocks.get()
        # Deleting the spaces in the stock keys user input
        assets = stocks.replace(" ", "")
        assets = assets.split(",")

        for stock in assets:
            wbb.open('https://finance.yahoo.com/quote/' + stock)

    # Creating the function which opens the main Yahoo Finance website
    def open_website(self):
        wbb.open('https://finance.yahoo.com/')


StockAnalysis()
