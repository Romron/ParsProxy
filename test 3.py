from selenium import webdriver
from selenium.webdriver.firefox.options import Options
import os


pathDriver = os.path.dirname(os.path.abspath(__file__)) + "/geckodriver.exe"
opts = Options()

# opts.add_argument('window-size=100x100')

opts.add_argument('-width=200')
opts.add_argument('-height=200')
opts.add_argument('-x=100')
opts.add_argument('-y=100')


driver = webdriver.Firefox(executable_path=pathDriver,options=opts)


driver.get('https://2ip.ru/')