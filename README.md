Group Project: Stock Analysis with Python.

**About**
This is a student project for the course "Programming: Introduction Level" - University of St. Gallen.
The goal of the project was to create a program that analyzes different stocks during a certain time frame. 
With this programm you can enter various stocks and the time frame you want to analyze. 
As a result you will see the stocks with the most volume, highest return and highest daily volatility. 
In addition, the programm visualizes each data in various graphs.


**Pre-requisites**
For the program to work, you can run it with Python3
The following libraries need to be installed in order for the code to work:
Pandas, Mathplotlib, Webbrowser, Random

**Instructions**
1. Start stock_analysis_py and run the program.
2. Input the stocks and the time frame you want to analyze. Make sure you enter the stocks with the right keys and the time frame in the given order.
   You can also click on "Set Random" to simulate the program with random stocks and a random time frame.
3. Click on the button "Analyse Stocks". 
   This will first open up a graph where you can see the stock with the highest return and also their 20-days/100-days simple moving average.
   It will also show you the stock with the most volume, the stock with the highest return and the stock with the highest daily volatility as outputs in the console.
4. In additon you can visualize the stock prices, the returns and the volatility of each stock by clicking on the buttons in the "Stock Visualization" category.
5. If you want to have additional informations for each stock, you can simply click on the button "Stock Websites"
   This will open the websites of each stock in finance yahoo where you will find more informations
   You can also click on "Yahoo Website" if you want to open the main finance yahoo website 

**Files**
Code: /machinelearinig_vX.X.py
PDF part of the code(has been integrated): /PDF.py
Input datasets in csv: /data
Output folder containing all the plots and the PDF reports: /output


**Description**
Data classification with supervised learning based on a predefined dataset including a comparison of different algorithms. 
5 datasets available: Iris, Ecoli, Glass, Yeast and Leaves. Further datasets can be added but have to be cleansed (see /data.readme)

In the beginning, all necessary libraries such as Numpy, Matplotlib, Pandas, Seaborn, Sklearn and FPDF were installed 
The next step was retrieving datasets. We chose several datasets from The UCI Machine Learning Repository: Iris flowers, Ecoli and Leaves.
Three of the datasets are multivariate and are based on real attributes. Similar attributes make these datasets applicable for classification 
tasks while difference in samples' scale brings in value to our small research.
To prepare the data for the research it has to be cleansed and brought to a common format: 
the first line represents name vectors while first row is class vectors. All data used is numerical.

After loading the datasets, plots are being generated in order to get initial feeling of the dataset.
We created several discriptive statistical graphs: boxplot and scatter plot matrices.

Afterwards, the dataset is being randomly split in two parts. One for classification purposes and one for validating if the classification has been correct.
Hence, it is possible to evaluate which of the supervised learning algorithms that will be used afterwards performed with the highest accuracy.
, LinearDiscriminantAnalysis, KNeighborsClassifier, DecisionTreeClassifier, GaussianNB and SVC.
By using these algorithms and the dataset can be classified. A comparison of the classified data with the evaluation data is the basis to calculate the 
model accuracy. Finally, the accuracy was calculated and visualized by a confusion matrix. The confusion matrix shows on the x axis the identified classes
and on the y axis the correct class. In the best case, the identified class matches the evaluation class.

As an ouput, the program generates a PDF that contains all parts of the classification including the plots of the dataset, the accuracy of the different models
and the confusion matrix.
