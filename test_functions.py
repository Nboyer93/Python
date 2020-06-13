from functions import *

stock=stock_data('AAPL',start(2019,12,1))

def test_upper_bound():
    
    assert upper_bound(stock)==4
    assert type(upper_bound(stock))==int
