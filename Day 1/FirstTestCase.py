#Test Case
#1)Open Web Browser(Chrome/firefox/Edge).
#2)Open URL
#3)Enter username
#4)Enter password
#5)Click on Login.
#https://opensource-demo.orangehrmlive.com/
#(Admin).
#(admin123).
#6)Capture title of the home page.(Actual title)
#7)Verify title of the page:OrangeHRM(Expected)
#8)close browser

from unicodedata import name
from selenium import webdriver
<<<<<<< HEAD
# from selenium.webdriver.chrome.service import Service
# from selenium.webdriver.common.by import By
# serv_obj = Service("C:\Project Drivers\chromedriver_win32\chromedriver.exe")
# driver = webdriver.Chrome(service=serv_obj)
driver = webdriver.Chrome(executable_path="C:\Project Drivers\chromedriver_win32\chromedriver.exe")
driver.get("https://opensource-demo.orangehrmlive.com/")
driver.find_element(by.name"txtUsername").send_keys("Admin123")
driver.find_element_by_id("txtPassword").send_keys("admin123")
driver.find_element_by_id("btnLogin").click()
=======
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
serv_obj = Service("C:\Project Drivers\chromedriver_win32\chromedriver.exe")
driver = webdriver.Chrome(service=serv_obj)
driver = webdriver.Chrome()
driver.get("https://opensource-demo.orangehrmlive.com/")
driver.find_element(By.NAME,"txtUsername").send_keys("Admin123")
driver.find_element(By.ID,"txtPassword").send_keys("Admin123")
driver.find_element(By.ID,"btnLogin").click()
>>>>>>> f783ae1e52535f85749ce978faea186368c8ffe4
act_title = driver.title
exp_title = "OrangeHRM"
if act_title == exp_title:
    print("Login Test Passed")
else:
    print("Login Test Failed")
driver.close()
