 
from selenium import webdriver
from selenium.webdriver.chrome.options import Options 

# PATH = "C:\Users\Amir\chromedriver.exe"


chrome_options = Options()
chrome_options.add_experimental_option("detach", True)
url = ''
browser = webdriver.Chrome()
browser.get(url)


browser.find_element('').click()