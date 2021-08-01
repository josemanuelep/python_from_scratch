import requests
import logging

response = requests.get('https://httpbin.org/ip')

logging.warning('Your IP is {0}'.format(response.json()['origin']))