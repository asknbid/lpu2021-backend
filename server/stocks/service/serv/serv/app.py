from model import Stock
import random

def serv(request):
    Stock.price = random.random()
    return Stocks.price
    
    

