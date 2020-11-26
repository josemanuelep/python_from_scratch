import requests
import logging

response = requests.get('https://httpbin.org/ip')

print('Your IP is {0}'.format(response.json()['origin']))

logging.warning('Watch out!')  # will print a message to the console
logging.info('I told you so')  # will not print anything