from selenium import webdriver
from selenium.webdriver.firefox.options import Options
import os
from selenium.webdriver.common.keys import Keys
import tkinter                 #  библиотека для графических интерфейсов 

r = tkinter.Tk()
pathDriver = os.path.dirname(os.path.abspath(__file__)) + "/geckodriver.exe"
opts = Options()


# opts.add_argument('-width=600')
# opts.add_argument('-height=600')

opts.add_argument('-width=' + str(r.winfo_screenwidth()/2))
opts.add_argument('-height=' + str(r.winfo_screenheight()/1.3))


driver = webdriver.Firefox(executable_path=pathDriver,options=opts)
driver.set_window_position(r.winfo_screenwidth()/2, 0)

driver.execute_script("window.open()")

driver.get('https://2ip.ru/')

two_Window = driver.window_handles[1]

driver.switch_to.window(two_Window)
driver.get('https://google.com')
