from selenium.webdriver.chrome.options import Options
from selenium import webdriver

class Navigation:
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
    self.driver = webdriver.Chrome(executable_path=r"./chromedriver.exe", options=options)

  def openUrl(self):
    self.driver.get(self.url)
    self.driver.maximize_window()
    self.takeScreenshot()
    
  def takeScreenshot(self):
    self.driver.save_screenshot(self.imagePath+self.imageName+str(self.imageNo)+".png")
    self.imageNo +=1
  
  def clickElementByLinkText(self,linkText):
    self.Element = self.driver.find_element_by_link_text(linkText)
    self.Element.click()
    self.takeScreenshot()
    
  def clickElementByX_Path(self,path):
    self.Element = self.driver.find_element_by_xpath(path)
    self.Element.click()
    
  def sendKeysToElement(self,data):
    self.Element.send_keys(data)
    self.takeScreenshot()
    
  def closeBrowser(self):
    self.takeScreenshot()
    self.driver.close()

obj = Navigation()
obj.openUrl()
obj.clickElementByLinkText("Contact Us")

obj.clickElementByX_Path("//form[@id='ajax-contact-form']/input[1]")
obj.sendKeysToElement("auto")

obj.clickElementByX_Path("//form[@id='ajax-contact-form']/input[2]")
obj.sendKeysToElement("auto@gmail.com")

obj.clickElementByX_Path("//form[@id='ajax-contact-form']/input[3]")
obj.sendKeysToElement("0123456789")

obj.clickElementByX_Path("//form[@id='ajax-contact-form']/textarea[1]")
obj.sendKeysToElement("Hello PCCOE!!!!!!")

obj.clickElementByX_Path("//form[@id='ajax-contact-form']/input[4]")

print('Message sent successfully')
obj.closeBrowser()
