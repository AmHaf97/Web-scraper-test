 
from selenium import webdriver
from selenium.webdriver.chrome.options import Options 

# PATH = "C:\Users\Amir\chromedriver.exe"


chrome_options = Options()
chrome_options.add_experimental_option("detach", True)
url = '' #lägg till URL för sidan som ska skrapas
browser = webdriver.Chrome()
browser.get(url)


browser.find_element('').click() #lägg till html div (xpath)
