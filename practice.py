import time

from selenium.webdriver.chrome.options import Options
from selenium import webdriver

options = Options()
options.add_argument("--headless")
options.add_argument("window-size=1400,1500")
options.add_argument("--disable-gpu")
options.add_argument("--no-sandbox")
options.add_argument("start-maximized")
options.add_argument("enable-automation")
options.add_argument("--disable-infobars")
options.add_argument("--disable-dev-shm-usage")

driver = webdriver.Chrome(options=options)
driver.get("http://www.pccoepune.com/")
driver.maximize_window()
driver.save_screenshot("/home/ec2-user/my_app/image-1.png")
contactElement = driver.find_element_by_link_text("Contact Us")
contactElement.click()

driver.save_screenshot("/home/ec2-user/my_app/image-2.png")
#Element = driver.find_element_by_name("name")
Element = driver.find_element_by_xpath("//form[@id='ajax-contact-form']/input[1]")
Element.click()
Element.send_keys("auto")
time.sleep(1)
driver.save_screenshot("/home/ec2-user/my_app/image-3.png")

#Element = driver.find_element_by_name("email")
Element = driver.find_element_by_xpath("//form[@id='ajax-contact-form']/input[2]")
Element.click()
Element.send_keys("auto@gmail.com")
time.sleep(1)
driver.save_screenshot("/home/ec2-user/my_app/image-4.png")

#Element = driver.find_element_by_name("contact")
Element = driver.find_element_by_xpath("//form[@id='ajax-contact-form']/input[3]")
Element.click()
Element.send_keys("0123456789")
time.sleep(1)
driver.save_screenshot("/home/ec2-user/my_app/image-5.png")

#Element = driver.find_element_by_name("message")
Element = driver.find_element_by_xpath("//form[@id='ajax-contact-form']/textarea[1]")
Element.click()
Element.send_keys("Hello PCCOE!!!!!!")
time.sleep(3)
driver.save_screenshot("/home/ec2-user/my_app/image-6.png")

#Element = driver.find_element_by_class_name("button1")
Element = driver.find_element_by_xpath("//form[@id='ajax-contact-form']/input[4]")
Element.click()
driver.save_screenshot("/home/ec2-user/my_app/image-7.png")

time.sleep(3)
print('Message sent successfully')
driver.close()
