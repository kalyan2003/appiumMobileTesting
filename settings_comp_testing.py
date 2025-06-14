from appium import webdriver
from typing import Any, Dict
from appium.options.common import AppiumOptions
from appium.webdriver.common.appiumby import AppiumBy
import time

cap: Dict[str, Any] = {
    'platformName': 'Android',
    'automationName': "uiautomator2",
    'appPackage': 'com.android.settings',
    'appActivity': '.Settings',
    'language': 'en',
    'locale': 'US'
}

url = 'http://localhost:4724'

driver = webdriver.Remote(url, options = AppiumOptions().load_capabilities(cap))

el = driver.find_element(by=AppiumBy.XPATH, value='//android.widget.TextView[@resource-id="android:id/title" and @text="Battery"]')
time.sleep(10)

el.click()

driver.quit()