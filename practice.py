from selenium import webdriver
import time

driver = webdriver.Chrome("/usr/bin/chromedriver.exe")
driver.get("http://www.pccoepune.com/")
driver.maximize_window()

contactElement = driver.find_element_by_link_text("Contact Us")
contactElement.click()

#Element = driver.find_element_by_name("name")
Element = driver.find_element_by_xpath("//form[@id='ajax-contact-form']/input[1]")
Element.click()
Element.send_keys("auto")
time.sleep(1)

#Element = driver.find_element_by_name("email")
Element = driver.find_element_by_xpath("//form[@id='ajax-contact-form']/input[2]")
Element.click()
Element.send_keys("auto@gmail.com")
time.sleep(1)

#Element = driver.find_element_by_name("contact")
Element = driver.find_element_by_xpath("//form[@id='ajax-contact-form']/input[3]")
Element.click()
Element.send_keys("0123456789")
time.sleep(1)

#Element = driver.find_element_by_name("message")
Element = driver.find_element_by_xpath("//form[@id='ajax-contact-form']/textarea[1]")
Element.click()
Element.send_keys("Hello PCCOE!!!!!!")
time.sleep(3)

#Element = driver.find_element_by_class_name("button1")
Element = driver.find_element_by_xpath("//form[@id='ajax-contact-form']/input[4]")
Element.click()

time.sleep(3)
print('Message sent successfully')
driver.close()
