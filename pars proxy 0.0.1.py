import requests 
import re 
import os 
import os.path
from selenium import webdriver	# импортирую модуль вебдрайвера
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from selenium.webdriver.firefox.options import Options
import selenium.common.exceptions



result_listProxy = []
result = []

pathFile = os.path.dirname(__file__)	

listProxyPagesURLs	 = [
	'http://www.freeproxylists.net/ru/',			# по этому URLу всё работает но сам сайт блокируеться по IP изначально!
	'http://free-proxy.cz/en/',						# # по этому URLу всё работает но только 5 страниц дальше каптча!
	# 'https://hidemy.name/ru/proxy-list/',
	# 'http://foxtools.ru/Proxy',		# нет ссылки "Следующая"
	# 'https://htmlweb.ru/analiz/proxy_list.php?perpage=50#%D0%9A%D0%B0%D1%82%D0%B0%D0%BB%D0%BE%D0%B3%D0%B8%20%D0%BF%D1%80%D0%BE%D0%BA%D1%81%D0%B8', # нет ссылки "Следующая"
	# 'https://hidester.com/proxylist/',
	]

listProxyPages = [
		# 'Proxy_pages/captcha_page from free-proxy.cz.html',
		# 'Proxy_pages/freeproxylists.net.html',
		# 'Proxy_pages/free-proxy.cz.html',		
		# 'Proxy_pages/foxtools.ru.html',			
		# 'Proxy_pages/htmlweb.ru.html',			
	# 	'Proxy_pages/foxtools.ru.txt'
	# 	'Proxy_pages/hidester.com.txt',
		]








def Get_HTML(URL,mode=1,IP_proxy='',flag_return_driver=0,driver=False):
	'''
		Функция должна: 
			получать страницу по переданому URL 
		Пременяет один из указанных способов, режимов, :
			Возможные способы, режимы, получения:
				1 - Библиотека requests:	
					контроль заголовков
					передача строки юзерагента
					КУКИ
				2 - Селениум
					Очень медлено!

				3 - Библиотека Splinter
					????????????
				
				4 - Библиотека MechanicalSoup
					????????????				

				5 - Библиотека RoboBrowser
					????????????

				6 - Библиотека Mechanize
						- не выполняет Javascript на страницах, которые он просматривает (проверить)

				7 - Библиотека Scrapy
					??????????????

		Возврт значений:
			если mode=1:
				пользователь имеет возможность получить экземпляр браузера для дальнейшего использования
				 вне этой ф-ции, но тогда он отвечает за закрытие этого экземпляра браузера. 
				Есть возможность вернут в ф-цию экземпляра браузера
	'''

  	# Проверка на корректность полученных данных
	if type(URL) != str:
		print('You must input only str')
		return False


	if mode == 1:
		print('You choso Selenium:')
		
		


		if flag_return_driver == 0 or driver == False:
			

			pathDriver = os.path.dirname(os.path.abspath(__file__)) + "/geckodriver.exe"
			opts = Options()
			opts.headless = False
			driver = webdriver.Firefox(executable_path=pathDriver,options=opts)		
		try:
			driver.get(URL)
			
			try:
				WebDriverWait(driver, 5).until(lambda driver: 
					# driver.find_elements_by_xpath('/html/body/div[1]/div[4]/div/div[4]/table/thead/tr/td[1]'))  # работает
					# driver.find_elements_by_xpath(".//td[text()='IP адрес']"))  # работает
					driver.find_elements_by_xpath("//*[.='IP адрес']"))  

			except Exception as errMess:
				print('Элемент не найден')
				print(errMess)
			# time.sleep(3)			

			html = driver.page_source
			
			# print('\n\n *****************************************************')
			# print(html)
			# print('\n\n *****************************************************')


		# Оброботка исключний:
		except Exception as errMess:
			
			print('EERRR')
			print(errMess)
			if flag_return_driver:	
				html = [False]		
			else:
				html = False		
		
		# Вывод результатов в зависимости от значения flag_return_driver
		if flag_return_driver and html:
			arr_result = [
				html,
				driver
			]
			
			# print('\n\n******************************************************************************')
			# print(html)
			# print('\n\n******************************************************************************')
			return arr_result



		print('driver.close()	# закрываю браузер')
		# driver.close()	# закрываю браузер
		return html



	elif mode == 2:
		print('You choso Requests lib')
		headers = {'User-Agent' : 'Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:47.0) Gecko/20100101 Firefox/47.0'}
		# response = requests.get(url,headers=headers,proxies=proxies,timeout=_timeout,verify=False)
		response = requests.get(URL,headers=headers)
		response.encoding = 'utf-8'
		html = response.text

	elif mode == 3:
		
		print('You choso Splinter')
	
	elif mode == 4:
		
		print('You choso MechanicalSoup')

	elif mode == 5:
		
		print('You choso RoboBrowser')

	elif mode == 6:
		
		print('You choso Mechanize')

	elif mode == 7:
		
		print('You choso Scrapy')



def Get_ProxyIP(html):
	''' Собрать IP прокси на странице
		Вернуть список собраных IP в формате IP:port
	'''

	result_listProxy = []

	# patternProxy = r'(?:[0-9]{1,5}\.){3}[0-9]{1,3}:[0-9]{2,5}'
	pattern = r'>((?:[0-9]{1,5}\.){3}[0-9]{1,3}(?::[0-9]{2,5})?)(?:(?:</[aspan]>)?</td>\n?.*?<td.*?>([0-9]{2,5})<)?'


	result = re.findall(pattern,html)

	q = 0
	while q < len(result):
		if re.search(':', result[q][0]) == None:
			result_listProxy.append(result[q][0] + ':' + result[q][1])
		else:
			result_listProxy.append(result[q][0]) 
		q += 1	


	return result_listProxy

def Get_LinkNextPage(html):
	''' Найти ссылку на следующую страницу 
		Вернуть найденную ссылку в формате URLа пригодного для использоваия в Get_HTML()
	'''
	
	# (? pattern = r'href=("(.)*?)">Следующая »</a>')
	# pattern = r'href="((?:/\w)*\.?/?[/\?][\w]+[/=]\d{1,2})">Следующая »</a>'	#работает
	# pattern = r'href="((?:/\w)*\.?/?[/\?][\w]+[/=]\d{1,2})">(?:Следующая)|(?:Next) »</a>' #работает только на первом	 
	# pattern = r'<a href="([\w\d/\?=\.]+)">(?:Следующая)|(?:Next) »</a>'	 
	pattern = r'"([\w\d/\?=\.]+)">(?=(?:Следующая)|(?:Next) »</a>)'	 


	href_ = re.findall(pattern,html)

	if len(href_) > 1:
		link_NextPage = re.sub(r'^[\./en]*','',href_[1])
		
		print("\n")
		print('href_              ' + href_[1])
		print('link_NextPage:     ' + link_NextPage)

	else:
		print('Следующей страницы НЕТ \n')
		link_NextPage = None

	return link_NextPage

def check_CaptchaPage(html):
	

	try:
		print('check_CaptchaPage(html): page CAPTCH')
		if re.search('complete CAPTCHA to continue',html): return 'CAPTCHA'
	except:
		print('check_CaptchaPage(html): NOT page CAPTCH')
		# return 'CAPTCHA'

		pass

	return True







# ##################################################################################################################
# ##################################################################################################################


if __name__ == '__main__':		

	driver = False
	link_NextPage = None

	# for fileName in listProxyPages:
	for URL in listProxyPagesURLs:
		
		flag_page_enumeration = 1
		count_ProxyIP = 0
		IP_proxy = ''

		print(URL)
		# print(fileName)
		
		while flag_page_enumeration:			# цыкл продолжается пока есть ссылка на сл. страницу
			# для тестов:
			# with open(fileName,'r',encoding="utf-8") as file_handler:
			# 	html = file_handler.read()
			# 	flag_page_enumeration = 0

			if not link_NextPage:
				URL_Next_Page = URL

			print('URL_Next_Page:     ' + URL_Next_Page)
			print('IP_proxy:     ' + IP_proxy)
			
			arr_result = Get_HTML(URL_Next_Page,1,IP_proxy,1,driver)	# функция возвратит arr_result[html,driver]
			html = arr_result[0]


			if check_CaptchaPage(html) == 'CAPTCHA':
				if not listProxy:
					print('Страница Каптчи, Proxy HET')
					html = False
					break
				else:
					if count_ProxyIP < len(result_listProxy):
						IP_proxy = result_listProxy[count_ProxyIP]
						count_ProxyIP += 1
						
						print('count_ProxyIP:    ' + str(count_ProxyIP))
						print('Страница Каптчи, меняю IP')

						Get_HTML('https://2ip.ua/ru',1,IP_proxy)


					else:
						print('Страница Каптчи, Proxy HET')
						html = False
						break	

					# print('IP_proxy:    ' + IP_proxy)
					continue

			if html:

				driver = arr_result[1]
				listProxy = Get_ProxyIP(html)
				
				print(listProxy)
				
				for IP_Port in listProxy:
					result_listProxy.append(IP_Port)
				link_NextPage = Get_LinkNextPage(html)
				
				if link_NextPage:			
					URL_Next_Page = URL + link_NextPage
					print('URL_Next_Page:     ' + URL_Next_Page)

				else:
					flag_page_enumeration = 0
					# driver.close()	# закрываю браузер


			else:

				continue
		
	print('\n\n')
	print(result_listProxy)


