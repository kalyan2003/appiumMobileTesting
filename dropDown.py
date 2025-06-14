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

mobile_no = driver.find_element(AppiumBy.XPATH,value='//android.widget.Spinner[@content-desc="Mobile Phone"]')
mobile_no.click()

some_ele = driver.find_element(AppiumBy.XPATH,value='(//android.widget.LinearLayout[@resource-id="com.google.android.contacts:id/kind_editors"])[4]/android.widget.LinearLayout')
some_ele.click()


