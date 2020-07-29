from selenium import webdriver
import time
import os
from selenium.webdriver.firefox.options import Options
from bs4 import BeautifulSoup
import re
import json





with open('Proxylist/proxylist 29-07-2020 08.54.06 .json') as file_handle:
    templates = json.load(file_handle)


for x in templates:
    print(x)
