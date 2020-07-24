from selenium import webdriver
from selenium.webdriver.firefox.options import Options
import os
import time
from selenium.webdriver.common.keys import Keys
import tkinter                 #  библиотека для графических интерфейсов 

import numpy as np
import scipy.interpolate as si
from selenium.webdriver.common.action_chains import ActionChains


r = tkinter.Tk()
pathDriver = os.path.dirname(os.path.abspath(__file__)) + "/geckodriver.exe"
opts = Options()
opts.add_argument('-width=' + str(r.winfo_screenwidth()/2))
opts.add_argument('-height=' + str(r.winfo_screenheight()/1.3))

driver = webdriver.Firefox(executable_path=pathDriver,options=opts)
driver.set_window_position(r.winfo_screenwidth()/2, 0)

URL = 'http://free-proxy.cz/en/'




driver.get(URL)

for x in range(4,15):
	startElement = driver.find_element_by_xpath("/html/body/div[2]/div[1]/div[1]/ul/li[1]/a")
	finishElement = driver.find_element_by_css_selector('div.paginator:nth-child(5) > a:nth-child(1' + str(x) + ')')
	action = ActionChains(driver);
	action.move_to_element(startElement);
	time.sleep(2)
	action.move_to_element(finishElement);
	time.sleep(2)
	action.click(finishElement)
	action.perform();
	print(x)
	time.sleep(2)
