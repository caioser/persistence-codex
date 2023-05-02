from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromiumService
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.core.utils import ChromeType

from time import sleep

driver = webdriver.Chrome(
        service=ChromiumService(
        ChromeDriverManager(
        chrome_type=ChromeType.CHROMIUM).install()))
        
driver.get("https://pypi.org/project/webdriver-manager/")
sleep(5)
driver.quit()