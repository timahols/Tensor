import pytest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

CHROME_DRIVER_PATH = "C:\chromedriver.exe"
# driver = webdriver.Chrome(executable_path=CHROME_DRIVER_PATH)
driver = webdriver.Chrome(executable_path="C:\chromedriver.exe")
handles = driver.window_handles
ENTER = Keys.ENTER
wait = WebDriverWait(driver, 10)

