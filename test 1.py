from selenium import webdriver
import time
import os
from selenium.webdriver.firefox.options import Options
from bs4 import BeautifulSoup
import re


# (? pattern_2 = r'<b class="b-pager__current">(\d+)</b>')

def f():
	last_page = 871
	pattern_2 = r'<b class="b-pager__current">(\d+)</b>'
	# pattern_2 = r'<a href="\?perpage=20&amp;p=871"')
	# pattern_2 = r'<a href="\?perpage=20&amp;p=' + str(last_page) + '"'

	result = re.findall(pattern_2,'<b class="b-pager__current">871</b>')

	if result:
		pass
		# print('result is  TRUE')
	else:
		pass
		print('result is  FALSE')

	print(result)
	print(result[0])
	return  result, last_page


f()