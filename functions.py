import pandas as pd
import pandas_datareader as web
import datetime
import statistics as stats
from datetime import date
import matplotlib.pyplot as plt
"""imports necessary modules to scrape stock data, analyze, and generate visualizations"""

def start(year, month, day):
    """converts interger inputs into date"""
    output=datetime.datetime(year, month, day)
    return output

def today():
    """generates current date"""
    today=date.today()
    return today

def stock_data(ticker, start,today=date.today()):
    """scrapes stock data from yahoo ranging from start date to current date"""
    df= web.DataReader(ticker,'yahoo',start,today)
    return df

def stock():
    """saves stock_data in more managable variable"""
    stock=stock_data('AAPL',start(2019,12,1))
    return stock

def stock_max(stock):
    """calculates highest stock price over time period"""
    max_price=0
    for i in stock['Close']:
        if i > max_price:
            max_price=i
    return max_price

def stock_min(stock):
    """calculates lowest stock price over date range"""
    min_price=1000000
    for i in stock['Close']:
        if i < min_price:
            min_price=i
    return min_price

def stock_price(stock):
    price=stock['Close']
    return price

def stock_average(stock):
    """generates average stock price over time period"""
    closing_price=stock['Close']
    average=stats.mean(closing_price)
    return average

def resistance(stock):
    """calculates value within 5% of max for period"""
    output= stock_max(stock)-(stock_max(stock)*.05)
    return output

def support(stock):
    """calculates value within 5% of min over time period"""
    output= stock_min(stock)+(stock_min(stock)*.05)
    return output

def upper_bound(stock):
    """tracks number of time stock reaches resistance or upper bound"""
    counter=0
    for i in stock_price(stock):
        if i >= resistance(stock):
            counter+=1
    return counter


def lower_bound(stock):
    """tracks number of time stock reaches support or lower bound"""
    counter=0
    for i in stock_price(stock):
        if i <= support(stock):
            counter+=1
    return counter


def buy_or_sell(stock):
    """based on number of times stock touches bound, returns buy, sell, or hold advice"""
    if upper_bound(stock)>lower_bound(stock):
        output=print('Buy')
    elif upper_bound(stock)==lower_bound(stock):
        output=print('Hold')
    elif upper_bound(stock)<lower_bound(stock):
        output=print('Sell')
    return output

def graph(stock):
    """graphs stock data over time period"""
    output=stock_price(stock)
    return plt.plot(output)
