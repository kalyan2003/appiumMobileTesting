from appium import webdriver
from typing import Any, Dict
from appium.options.common import AppiumOptions
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


cap: Dict[str, Any] = {
    'platformName': 'Android',
    'automationName': "uiautomator2",

}

url = 'http://localhost:4724'

driver = webdriver.Remote(url,options=AppiumOptions().load_capabilities(cap))

call_ele = driver.find_element(by = AppiumBy.ACCESSIBILITY_ID,value='Phone')
call_ele.click()

number_pad = driver.find_element(by = AppiumBy.XPATH,value="//android.widget.ImageButton[@content-desc = 'key pad']")
number_pad.click()

for r in range(2,8):
    numbers = driver.find_element(by=AppiumBy.XPATH, value=f"//android.widget.FrameLayout[contains(@content-desc,'{r}')]")
    numbers.click()

call_button = driver.find_element(by = AppiumBy.XPATH, value="//android.widget.Button[@content-desc='dial']")
call_button.click()


