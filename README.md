**Stock Analysis with Python**

**About**   
This is a student project for the course "Programming: Introduction Level" - University of St. Gallen.   
The goal of this project was to create a program that analyses different stocks over a given time frame.   
With this program you can enter multiple stocks and a certain time frame you want to analyse.    
As a result you will see the stocks with the most volume, highest return and highest daily volatility.    
In addition, the program visualises each data in various graphs and gives you additional information.   


**Prerequisites**   
For the program to work, the user needs to run it with Python3 (for example with PyCharm).   
The following libraries need to be installed in order for the code to work:   
Pandas Datareader, Pandas, Datetime, Mathplotlib, Tkinter, Webbrowser, Random

**Instructions**
1. Open **stock_analysis.py** and run the program.
2. Input the stocks and the time frame you want to analyse. Make sure you enter the stocks with the correct keys and the time frame in the given order.  
   You can also click on the button "Set Random" to fill the program with random stocks and a random time frame.
3. Click on the button "Analyse Stocks".    
   This will first open up a graph where you can see the stock with the highest return and also, if possible, its 20-days/100-days simple moving average.   
   After you close the graph, it will also show you the stock with the most volume, the stock with the highest return and the stock with the highest daily volatility over the given time frame as outputs in the console.   
4. In additon you can visualise the stock prices, the returns and the volatility of each stock by clicking on the respective buttons in the "Stock Visualisation" section.  
   If you want to adjust or edit the graphs, you can find the buttons to do this in the top left corner of each graph.
5. If you want to have additional information for each stock key entered, you can simply click on the button "Stock Websites".   
   This will open the websites of each stock in yahoo finance where you will find more informations.   
   You can also click on "Yahoo Website" if you want to open the main yahoo finance website.    
   
For further informations, you can open the **step-by-step user guide** pdf.

**File Descriptions**  
- stock_analysis.py  
  The code used to create the stock analysis program including comments  
- step-by-step_user_guide.pdf  
  A step-by-step guide with images on how to use the program


