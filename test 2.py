import os
import re


f = open('pages/freeproxylists.net.html','r',encoding="utf-8")
html = f.read()

URL = 'https://htmlweb.ru/analiz/proxy_list.php?perpage=20&p='
#      http://www.freeproxylists.net/ru/?page=2

# <a href="./?page=3">Следующая »</a>


patern_2 = r'"\.([\w\d/\?=]+)">Следующая »</a>'
result = re.findall(patern_1,html)
link_NextPage = re.sub(r'^[\./en]','',result[1])
URL_NextPage = URL + link_NextPage
print(link_NextPage)
print(URL_NextPage)


# URL = 'http://free-proxy.cz/en/'
# result_URL = re.search(r'free-proxy\.cz',URL)

# if result_URL:
# 	print(result_URL.group(0))

# else:
# 	print('false')
