
# Welcome to Quanturf! 

### End to end Algo Trading made seamless!

#### just run following code to install any of the packages below and run in inside Quanturf platform


```python
required = {'python-git'}
missing = required 
if missing:
    !pip install python-git
```


```python
from git import Repo
src=input("Enter the url of git repository : ")
directory=input("Enter folder name to clone on local machine: ")
Repo.clone_from(src, directory)
```

### 1. Backtesting

* [backtrader](https://www.backtrader.com/) - feature-rich Python framework for backtesting and trading
* [pyalgotrade](https://gbeced.github.io/pyalgotrade/) - Python Algorithmic Trading Library with focus on backtesting and support for paper-trading and live-trading
* [bt](https://pmorissette.github.io/bt/) - bt is a flexible backtesting framework for Python used to test quantitative trading strategies
* [backtesting](https://kernc.github.io/backtesting.py/) - Backtesting.py is a Python framework for inferring viability of trading strategies on historical (past) data

### 2. Algo Trading Data ( all asset classes, multiple indexes and live trading)

* [intrinio-sdk](https://docs.intrinio.com/documentation/python) - Intrinio provides US market data, company fundamentals data, options data and SEC data, powered by advanced data quality technology
* [polygon-api-client](https://pypi.org/project/polygon-api-client/) - python client for Polygon.io, provider of real-time and historical financial market data APIs
* [iexfinance](https://pypi.org/project/iexfinance/) - Python SDK for IEX Cloud. Easy-to-use toolkit to obtain data for Stocks, ETFs, Mutual Funds, Forex/Currencies, Options, Commodities, Bonds, and Cryptocurrencies
* [yfinance](https://pypi.org/project/yfinance/) - yfinance offers a reliable, threaded, and Pythonic way to download historical market data from Yahoo! finance.
* [quandl](https://www.quandl.com/tools/python) - source for financial, economic, and alternative datasets, serving investment professionals
* [alpha-vantage](https://alpha-vantage.readthedocs.io/) - The Alpha Vantage Stock API provides free JSON access to the stock market, plus a comprehensive set of technical indicators
* [sec-edgar-downloader](https://sec-edgar-downloader.readthedocs.io/en/latest/) - package for downloading company filings from the SEC EDGAR database


### 3.Data Analysis

* [pandas](https://pandas.pydata.org/) - library for data analysis and manipulation of numerical tables and time series
* [NumPy](https://numpy.org/) - library for multi-dimensional arrays and matrices, mathematical functions
* [SciPy](https://www.scipy.org/) - modules for linear algebra, integration, FFT, signal and image processing
* [pandas-datareader](https://pandas-datareader.readthedocs.io/) - remote data access for pandas

### 4. Data Visualization

* [matplotlib](https://matplotlib.org/) - comprehensive library for creating static, animated, and interactive visualizations in Python
* [plotly](https://pypi.org/project/plotly/) - provides online graphing, analytics, and statistics tools for individuals and collaboration, as well as scientific graphing libraries for Python
* [dash](https://plotly.com/dash/) - build & deploy beautiful analytic web apps using Python
* [mplfinance](https://github.com/matplotlib/mplfinance) - matplotlib utilities for the visualization, and visual analysis, of financial data
* [jupyterlab](https://jupyterlab.readthedocs.io/) - web-based interactive development environment for Jupyter notebooks, code, and data
pillow

 ### 5. Portfolio and Performance Analysis

* [pyfolio](https://github.com/quantopian/pyfolio) - library for performance and risk analysis of financial portfolios developed by Quantopian
* [finquant](https://finquant.readthedocs.io/) - program for financial portfolio management, analysis and optimisation

### 6. Technical Analysis

* [ta](https://technical-analysis-library-in-python.readthedocs.io/) - Technical Analysis Library in Python based on pandas
* [TA-Lib](https://mrjbq7.github.io/ta-lib/) - Python wrapper for TA-Lib
* [bta-lib](https://btalib.backtrader.com/) - backtrader ta-lib
* [pandas-ta](https://github.com/twopirllc/pandas-ta) - Pandas Technical Analysis (Pandas TA) is an easy to use library that leverages the Pandas library with more than 120 Indicators and Utility functions
* [tulipy](https://github.com/cirla/tulipy) - Python bindings for Tulip Indicators


### 7. AI / Machine Learning

* [tensorflow](https://www.tensorflow.org/) - open source library to help you develop and train ML models
* [scikit-learn](https://scikit-learn.org/) - machine learning library
* [keras](https://keras.io/) - deep learning framework
* [pytorch](https://pytorch.org/) - optimized tensor library for deep learning using GPUs and CPUs
* [opencv-python](https://github.com/skvark/opencv-python) - open source computer vision library

### 8. Other packages

#### 8.1 Broker APIs

* [alpaca-trade-api](https://github.com/alpacahq/alpaca-trade-api-python) - python library for the Alpaca Commission Free Trading API. It allows rapid trading algo development easily, with support for both REST and streaming data interfaces.
* [python-binance](https://python-binance.readthedocs.io/) - unofficial Python wrapper for the Binance exchange REST API v3
* [tda-api](https://github.com/alexgolec/tda-api) - tda-api is an unofficial wrapper around the TD Ameritrade APIs. It strives to be as thin and unopinionated as possible, offering an elegant programmatic interface over each endpoint
* [ib_insync](https://github.com/erdewit/ib_insync) - The goal of the IB-insync library is to make working with the Trader Workstation API from Interactive Brokers as easy as possible.
* [robin-stocks](https://robin-stocks.readthedocs.io/) - simple to use functions to interact with the Robinhood Private API

#### 8.2 Database Libraries and Data Storage

* [psycopg2](https://pypi.org/project/psycopg2/) - most popular PostgreSQL database adapter for the Python programming language.
* [sqlalchemy](https://www.sqlalchemy.org/) - SQLAlchemy is the Python SQL toolkit and Object Relational Mapper that gives application developers the full power and flexibility of SQL.
* [redis](https://redis.io/) - open source, in-memory data structure store, used as a database, cache, and message broker
* [h5py](https://www.h5py.org/) - Pythonic interface to the HDF5 binary data format
