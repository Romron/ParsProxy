import os
import re


f = open('pages/htmlweb.ru.html','r',encoding="utf-8")
html = f.read()

# html = '<a href="?perpage=20&amp;p=1027" rel="last" title="в конец" onclick="return LoadMain(event);"> 1027 </a>'


# patern_1 = r'<b class="b-pager__current">(\d+)</b>'
patern_1 = r'title="в конец" [\w =";()]+> ?([0-9]+) ?</a>'

result = re.findall(patern_1,html)

print(result)


# URL = 'http://free-proxy.cz/en/'
# result_URL = re.search(r'free-proxy\.cz',URL)

# if result_URL:
# 	print(result_URL.group(0))

# else:
# 	print('false')
