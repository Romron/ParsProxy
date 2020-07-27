from selenium import webdriver
import time
import os
from selenium.webdriver.firefox.options import Options
from bs4 import BeautifulSoup
import re


# # (? pattern_2 = r'<b class="b-pager__current">(\d+)</b>')

# def f():
# 	# last_page = 871
# 	# pattern_2 = r'<b class="b-pager__current">(\d+)</b>'
# 	# pattern_2 = r'<a href="\?perpage=20&amp;p=871"')
# 	# pattern_2 = r'<a href="\?perpage=20&amp;p=' + str(last_page) + '"'

# 	# html = '<b class="b-pager__current">871</b><b class="b-pager__current">222</b>'

# 	# result = re.findall(pattern_2,html)

# 	try:
# 		result
# 		pass
# 		print('result is  TRUE')
# 	except:
# 		pass
# 		print('result is  FALSE')

# 	# print(result)
# 	# print(result[0])
# 	# return  result, last_page


# f()

# URL = 'https://htmlweb.ru/analiz/proxy_list.php?perpage=20&amp;p='
URL = 'https://analiz/proxy_list.php?perpage=20&amp;p='

if re.findall(r'htmlweb\.ru',URL):
	print('qqq')
else:
	print('rrr')