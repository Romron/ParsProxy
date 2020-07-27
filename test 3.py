from selenium import webdriver
from selenium.webdriver.firefox.options import Options
import os
import re 
import time
from selenium.webdriver.common.keys import Keys
import tkinter                 #  библиотека для графических интерфейсов 

# import numpy as np
# import scipy.interpolate as si
# from selenium.webdriver.common.action_chains import ActionChains


# r = tkinter.Tk()
# pathDriver = os.path.dirname(os.path.abspath(__file__)) + "/geckodriver.exe"
# opts = Options()
# opts.add_argument('-width=' + str(r.winfo_screenwidth()/2))
# opts.add_argument('-height=' + str(r.winfo_screenheight()/1.3))

# driver = webdriver.Firefox(executable_path=pathDriver,options=opts)
# driver.set_window_position(r.winfo_screenwidth()/2, 0)

URL = 'https://htmlweb.ru/analiz/proxy_list.php?perpage=20&amp;p='
# driver.get(URL)

result = re.findall(r'htmlweb\.ru',URL):
print(result)






