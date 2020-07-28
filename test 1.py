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


	





# для сайтов:   http://free-proxy.cz/en/    http://www.freeproxylists.net/ru/
pattern_1 = r'"([\w\d/\?=\.]+)">(?=(?:Следующая)|(?:Next) »</a>)'	 
# для сайта https://htmlweb.ru/analiz/proxy_list.php?perpage=50#Каталоги прокси
pattern_2 = r'<b class="b-pager__current">(\d+)</b>'	# эта ссылка естьтолько на первой странице !!



href_ = re.findall(pattern_2,html)



# if href_:								#  значит мы на одном из сайтов http://free-proxy.cz/en/    http://www.freeproxylists.net/ru/
# 	link_NextPage = re.sub(r'^[\./en]*','',href_[1])
# 	return link_NextPage

# maxMounth_NextPages = re.findall(pattern_2,html)		# ищем максимальное количество следующих страниц
# if maxMounth_NextPages:			# значит мы на сайте  https://htmlweb.ru/analiz/proxy_list.php?perpage=20&p=
# 	maxMounth_NextPages = maxMounth_NextPages[0]
# 	link_NextPage = 'https://htmlweb.ru/analiz/proxy_list.php?perpage=20&p='
# 	return link_NextPage, maxMounth_NextPages


print('Следующей страницы НЕТ \n')
return None