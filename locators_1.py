from appium import webdriver
from typing import Any, Dict
from appium.options.common import AppiumOptions
from appium.webdriver.common.appiumby import AppiumBy
import time

cap: Dict[str, Any] = {
    'platformName' : 'Android',
    'automationName' : "uiautomator2",
    'deviceName' : 'Android'
}

url = 'http://localhost:4724'

driver = webdriver.Remote(url, options=AppiumOptions().load_capabilities(cap))

chrome_ele = driver.find_element(by=AppiumBy.ACCESSIBILITY_ID,value='Chrome')
chrome_ele.click()

search_box = driver.find_element(by=AppiumBy.XPATH,value='//android.widget.EditText[@resource-id="com.android.chrome:id/search_box_text"]')
search_box.send_keys("Pavan Kalyan")

first_result = driver.find_element(by=AppiumBy.XPATH,value='//android.widget.TextView[@resource-id="com.android.chrome:id/entity_subject"]')
first_result.click()

time.sleep(10)

driver.quit()