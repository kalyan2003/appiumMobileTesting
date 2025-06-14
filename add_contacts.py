from appium import webdriver
from typing import Any, Dict
from appium.options.common import AppiumOptions
from appium.webdriver.common.appiumby import AppiumBy
import time

cap: Dict[str, Any] = {
    'platformName': 'Android',
    'automationName': "uiautomator2",
    'appPackage': 'com.google.android.contacts',
    'appActivity': 'com.google.android.apps.contacts.activities.PeopleActivity',
    'language': 'en',
    'locale': 'US'
}

url = 'http://localhost:4724'

driver = webdriver.Remote(url, options = AppiumOptions().load_capabilities(cap))
driver.implicitly_wait(50)

skip_but = driver.find_element(by=AppiumBy.XPATH,value='//android.widget.Button[@resource-id="android:id/button2"]')
skip_but.click()
# time.sleep(4)
create_cont_but = driver.find_element(by=AppiumBy.XPATH,value='//android.widget.ImageButton[@content-desc="Create contact"]')
create_cont_but.click()
# time.sleep(2)
first_name = driver.find_element(by=AppiumBy.XPATH,value='//android.widget.EditText[@text="First name"]')
first_name.send_keys("Pavan")

last_name = driver.find_element(by=AppiumBy.XPATH,value='//android.widget.EditText[@text="Last name"]')
last_name.send_keys("Kalyan")

phone_num = driver.find_element(by=AppiumBy.XPATH,value='//android.widget.EditText[@text="Phone"]')
phone_num.send_keys("9876543218")

save_but = driver.find_element(by=AppiumBy.XPATH,value='//android.widget.Button[@resource-id="com.google.android.contacts:id/toolbar_button"]')
save_but.click()




