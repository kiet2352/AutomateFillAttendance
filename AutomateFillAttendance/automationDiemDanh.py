from msilib.schema import RadioButton
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time

options = webdriver.ChromeOptions()
options.add_argument("--profile-directory=Profile 27")
options.add_argument("user-data-dir=C:/Users/Lenovo/AppData/Local/Google/Chrome/User Data")
web = webdriver.Chrome(executable_path='C:/Users/Lenovo/Downloads/Compressed/chromedriver.exe', options=options)
web.get('https://docs.google.com/forms/d/e/1FAIpQLSfTDhrcsYkccXDSbCTPBZKy0U5vRVpRmvcrkIMmEC90bRIf5w/viewform?fbclid=IwAR00avTfwaMLAJy7RPX76IcQy4_wqy7th-Oy8fQX6Fx8nbG_y5JUpAQfa4U')

time.sleep(4)

LastName = "Lê Tuấn Kiệt"
last = web.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input')
last.send_keys(LastName)

MSSV = "518H0523"
ID = web.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input')
ID.send_keys(MSSV)

RadioButtonPeriod = web.find_element_by_xpath('//*[@id="i16"]/div[3]/div')
RadioButtonPeriod.click()

RadioButtonPeriod2 = web.find_element_by_xpath('//*[@id="i23"]/div[3]/div')
RadioButtonPeriod2.click()
