# Week3 Day5
# Dmityr Dubrov
# Daily Challenge: Modules

# Instructions :
# Using the requests and time modules, create a function which returns the amount of time it takes a webpage to load (how long it takes for a complete response to a request).
# Test your code with multiple sites such as google, ynet, imdb, etc.

#import
import requests
from time import time

def time_load(url) :
    start_time = time()  # number of second since the epoch
    requests.get(url)
    time_req= time() - start_time
    return time_req


def test(url_for_test) :
   
    for key,value in url_for_test.items():
        url_for_test[key].append(round(time_load(value[0]),3))
    return url_for_test

def get_result(qty) :
     
    url_for_test = {'Google':['https://google.com/'],
                    'Ynet':['https://www.ynet.co.il/'],
                    'github':['https://github.com/'],
                    'Ya':['https://ya.ru/']                   
    }
     
    for i in range(qty):
        test(url_for_test)        
    return url_for_test

def report(in_dict, qty):
    print(f"test results {qty} requests.")
    for key,value in in_dict.items():
        print(f' Web site {key}:  {in_dict[key][1:qty+1]}')
   

def main () :
    qty = 3
    rep_dict = get_result(qty)
    report(rep_dict, qty)
    
    
    
# Driver
main()
