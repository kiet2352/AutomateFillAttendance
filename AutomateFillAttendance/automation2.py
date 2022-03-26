from msilib.schema import RadioButton
from random import random
from selenium import webdriver
import time
import random

web = webdriver.Chrome('C:/Users/Lenovo/Downloads/Compressed/chromedriver.exe')
web.get('https://docs.google.com/forms/d/e/1FAIpQLSfGO5A0gFsio_4nj9yUfIehV8uuuPDE0KTTnJumBVKQnQtXZQ/viewform?usp=sf_link')

time.sleep(2)

Names = ['Lê Tuấn Kiệt', 'Trần Hoàng Thái', 'Lê Thị A', 'Hoàng Long', 'Trần Thị Thảo','Lữ Trọng Phú','Ngô Thanh Phú', 'Ngô Hoài Nam','Nguyễn Thanh Sơn','Nguyễn Anh Dũng']
NameRand = random.choice(Names)
full = web.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input')
full.send_keys(NameRand)

Age = ['22,21,23,25,27,19,20,26,24,29']
AgeRand = random.choice(Age)
old = web.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input')
old.send_keys(AgeRand)


RadioButtonGender = web.find_element_by_xpath('//*[@id="i16"]/div[3]/div')
RadioButtonGender.click()

Education = "12/12"
edu = web.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[2]/div[4]/div/div/div[2]/div/div[1]/div/div[1]/input')
edu.send_keys(Education)

Job = "Sinh viên"
stu = web.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[2]/div[5]/div/div/div[2]/div/div[1]/div/div[1]/input')
stu.send_keys(Job)

RadioButtonSalary = web.find_element_by_xpath('//*[@id="i34"]/div[3]/div')
RadioButtonSalary.click()

SubmitButton = web.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div[1]/div/span')
SubmitButton.click()

RadioButtonUsed = web.find_element_by_xpath('//*[@id="i5"]/div[3]/div')
RadioButtonUsed.click()

RadioButtonComment = web.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[2]/span/div[4]/div/div/div[3]/div')
RadioButtonComment.click()

RadioButtonCriteria = web.find_element_by_xpath('//*[@id="i19"]/div[3]/div')
RadioButtonCriteria.click()

RadioButtonContact = web.find_element_by_xpath('//*[@id="i35"]/div[3]/div')
RadioButtonContact.click()

RadioButtonFormal = web.find_element_by_xpath('//*[@id="i51"]/div[3]/div')
RadioButtonFormal.click()

RadioButtonFilter = web.find_element_by_xpath('//*[@id="i76"]/div[3]/div')
RadioButtonFilter.click()

RadioButtonPayment = web.find_element_by_xpath('//*[@id="i83"]/div[3]/div')
RadioButtonPayment.click()

RadioButtonDetail1 = web.find_element_by_xpath('//*[@id="i100"]/div[2]')
RadioButtonDetail1.click()

RadioButtonDetail2 = web.find_element_by_xpath('//*[@id="i103"]/div[2]')
RadioButtonDetail2.click()

RadioButtonDetail3 = web.find_element_by_xpath('//*[@id="i112"]/div[2]')
RadioButtonDetail3.click()

RadioButtonLike = web.find_element_by_xpath('//*[@id="i119"]/div[3]/div')
RadioButtonLike.click()

RadioButtonInstruction = web.find_element_by_xpath('//*[@id="i132"]/div[3]/div')
RadioButtonInstruction.click()

RadioButtonSupport = web.find_element_by_xpath('//*[@id="i148"]/div[3]/div')
RadioButtonSupport.click()

RadioButtonOrder = web.find_element_by_xpath('//*[@id="i162"]/div[2]')
RadioButtonOrder.click()

RadioButtonReturn = web.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[2]/div[14]/div/div/div[2]/div/div[1]/div/div[2]/span/div[5]/div/div/div[3]/div')
RadioButtonReturn.click()

RadioButtonCare1 = web.find_element_by_xpath('//*[@id="i187"]/div[2]')
RadioButtonCare1.click()

RadioButtonCare2 = web.find_element_by_xpath('//*[@id="i193"]/div[2]')
RadioButtonCare2.click()

RadioButtonCare3 = web.find_element_by_xpath('//*[@id="i199"]/div[2]')
RadioButtonCare3.click()

RadioButtonSign = web.find_element_by_xpath('//*[@id="i206"]/div[3]/div')
RadioButtonSign.click()

RadioButtonCoupon = web.find_element_by_xpath('//*[@id="i216"]/div[3]/div')
RadioButtonCoupon.click()

RadioButtonTransport = web.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[2]/div[19]/div/div/div[2]/div/div[1]/div/div[2]/span/div[5]/div/div/div[3]/div')
RadioButtonTransport.click()

RadioButtonSuggest = web.find_element_by_xpath('//*[@id="i230"]/div[3]/div')
RadioButtonSuggest.click()

RadioButtonAdd = web.find_element_by_xpath('//*[@id="i240"]/div[3]/div')
RadioButtonAdd.click()

RadioButtonAddress = web.find_element_by_xpath('//*[@id="i250"]/div[3]/div')
RadioButtonAddress.click()

RadioButtonCoin = web.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[2]/div[23]/div/div/div[2]/div/div[1]/div/div[2]/span/div[4]/div/div/div[3]/div')
RadioButtonCoin.click()

RadioButtonFish = web.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[2]/div[26]/div/div/div[2]/div/div[1]/div/div[2]/span/div[6]/div/div/div[3]/div')
RadioButtonFish.click()

RadioButtonSubmit = web.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div[1]/div[2]/span')
RadioButtonSubmit.click()