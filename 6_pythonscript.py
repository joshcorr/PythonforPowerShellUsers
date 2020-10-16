#! /home/josh/.pyenv/versions/3.9.0/bin/python
#import packages for web, and regex

"""Prints a sting for example"""
print('This is a Script')

import urllib
import urllib.request
import re

site_to_check = ['https://status.twitterstat.us/']

def check_status(url):
    page_content = urllib.request.urlopen(url=url).readlines()
    results = re.findall('Service Disruption',str(page_content))
    for r in results:
        print(r)
    return

for site in site_to_check:
    check_status(url=site)






