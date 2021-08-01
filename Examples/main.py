import requests
import logging

# Default argument value
def for_loop_example(number=0):   
    for i in range(number):
        logging.warning(i)
    if(number==1):
        get_my_ip()

def get_my_ip():
    response = requests.get('https://httpbin.org/ip')
    logging.warning('Your IP is {0}'.format(response.json()['origin']))


inputText = input('Please enter a number:')
for_loop_example(int(inputText))
