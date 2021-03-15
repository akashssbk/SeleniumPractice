import time

from selenium.webdriver.chrome.options import Options
from selenium import webdriver

Class Navigation:
  def __init__(self):
    self.url = "http://www.pccoepune.com/";
    self.imagePath = "/home/ec2-user/my_app/"
    self.imageNo = 1
    self.imageName = "Step"
    self.Element = None
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

  def openUrl(self):
    self.driver.get(self.url)
    self.driver.maximize_window()
    
  def takeScreenshot(self):
    self.driver.save_screenshot(self.imagePath+self.imageName+self.imageNo)
    self.imageNo +=1
  
  def clickElementByLinkText(self,linkText):
    self.Element = self.driver.find_element_by_link_text(linkText)
    self.Element.click()
    self.takeScreenshot()
    
  def clickElementByX_Path(self,path):
    self.Element = driver.find_element_by_xpath("//form[@id='ajax-contact-form']/input[1]")
    self.Element.click()
    
  def sendKeysToElement(self,data):
    self.Element.send_keys(data)
    self.takeScreenshot()
    
    '''
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
'''
obj = Navigation()
obj.openUrl()
obj.clickElementByLinkText("Contact Us")
obj.clickElementByX_Path("//form[@id='ajax-contact-form']/input[1]")
obj.sendKeysToElement("auto")
obj.clickElementByX_Path("//form[@id='ajax-contact-form']/input[2]")
obj.sendKeysToElement("auto@gmail.com")

time.sleep(3)
print('Message sent successfully')
driver.close()
