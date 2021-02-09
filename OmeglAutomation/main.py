from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.ui import WebDriverWait

url='https://www.omegle.com/'
driver=driver=webdriver.Firefox()
driver.get(url)

textBtn=driver.find_element_by_id('textbtn').click()
time.sleep(2)

counts=0



while True:
	statuslog
	try:
		
		time.sleep(1)
		
		driver.find_element_by_class_name('chatmsg ').send_keys("Hello, i am from India, you ")
		driver.find_element_by_class_name('sendbtn').click()
		
		time.sleep(4)
		
		driver.find_element_by_class_name('chatmsg ').send_keys("Can we talk in Instagram")
		driver.find_element_by_class_name('sendbtn').click()
		
		time.sleep(3)
		
		driver.find_element_by_class_name('chatmsg ').send_keys("We will Talk there as freinds")
		driver.find_element_by_class_name('sendbtn').click()
		
		time.sleep(1)
		
		driver.find_element_by_class_name('chatmsg ').send_keys("https://www.instagram.com/mohit_deoli/")
		driver.find_element_by_class_name('sendbtn').click()
		
	
		
		time.sleep(5)
		
		driver.find_element_by_tag_name('button').click()
		driver.find_element_by_tag_name('button').click()
		
		counts=counts+1
		
		print('Toatal Persons : ',counts)
		
	except:
		driver.find_element_by_tag_name('button').click()

	
print(counts)

