from selenium.webdriver.chrome.options import Options
from selenium import webdriver
import boto3

class Navigation:
  def __init__(self):
    self.url = "http://www.pccoepune.com/";
    self.imagePath = "/home/"
    #self.imagePath = "/home/ec2-user/my_app/"
    self.s3ImagePath = "/SeleniumApplication/"
    self.imageNo = 1
    self.imageName = "Step"
    self.Element = None
    self.bucket = 'akashbagade-practice'
    #self.s3object = 'images/Collaboration.png'
    #self.preSignedUrl = ''
    #self.snsARN = 'arn:aws:sns:us-east-1:130159455024:akash-bagade-practice-1'
    options = Options()
    options.add_argument("--headless")
    options.add_argument("window-size=1400,1500")
    options.add_argument("--disable-gpu")
    options.add_argument("--no-sandbox")
    options.add_argument("start-maximized")
    options.add_argument("enable-automation")
    options.add_argument("--disable-infobars")
    options.add_argument("--disable-dev-shm-usage")
    self.driver = webdriver.Chrome(executable_path=r"./chromedriver", options=options)
    #self.driver = webdriver.Chrome(options=options)
    self.s3 = boto3.resource('s3')
    #self.s3Client = boto3.client('s3')
    #self.snsClient = boto3.client('sns')
    boto3.setup_default_session(region_name='us-east-1')
    self.lambdaClient = boto3.client('lambda')
    self.lambdafunc = 's3Url'
    
  def openUrl(self):
    self.driver.get(self.url)
    self.driver.maximize_window()
    self.takeScreenshot()
    
  def takeScreenshot(self):
    self.driver.save_screenshot(self.imagePath+self.imageName+str(self.imageNo)+".png")
    data = open(self.imagePath+self.imageName+str(self.imageNo)+".png", 'rb')
    self.s3.Bucket(self.bucket).put_object(Key=self.s3ImagePath+self.imageName+str(self.imageNo)+".png", Body=data)
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

  def sendUrlToMail(self):
    response = self.lambdaClient.invoke(FunctionName=self.lambdafunc, InvocationType='RequestResponse')

    
'''   
  def createPresignedUrl(self,s3object,exp):
    self.preSignedUrl = self.s3Client.generate_presigned_url('get_object', Params={'Bucket': self.bucket, 'Key': s3object}, ExpiresIn=exp)
    #print(preSignedUrl)
    
  def sendEmail(self):
    self.snsClient.publish(Message=self.preSignedUrl, TopicArn=self.snsARN)
    print('URL mailed successfully!')
'''    
    
    
def startNavigation():
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

  #obj.createPresignedUrl(obj.s3object,3600)
  #obj.sendEmail()
  obj.sendUrlToMail()
  print('URL mailed successfully')
  
  obj.closeBrowser()

startNavigation()
