import os
import json
from dotenv import load_dotenv
from time import sleep
from datetime import datetime, timedelta

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait



from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager

def driver():
    return webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))

# def wait(t=10):
#     return WebDriverWait(driver, 10)