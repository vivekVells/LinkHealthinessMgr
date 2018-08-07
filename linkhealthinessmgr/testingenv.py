from selenium import webdriver

#driver = webdriver.Chrome(executable_path= 'C:\webdriver\chromedriver.exe')
#driver = webdriver.Edge(executable_path= 'C:\webdriver\MicrosoftWebDriver.exe')
driver = webdriver.Firefox(executable_path= 'C:\webdriver\geckodriver-v0.21.0-win64\geckodriver.exe')

driver.get("http://www.google.com")

driver.close()