from appium import webdriver
from typing import Any, Dict
from appium.options.common import AppiumOptions
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

cap : Dict[str,Any] = {
    'platformName': 'Android',
    'automationName': 'uiautomator2',
    'deviceName': 'Android Emulator',
    'appPackage': 'com.socialnmobile.dictapps.notepad.color.note',
    'appActivity': 'com.socialnmobile.colornote.activity.Main',
    'language': 'en',
    'locale': 'US'
}

url = 'http://localhost:4724'

driver = webdriver.Remote(url, options=AppiumOptions().load_capabilities(cap))
wait = WebDriverWait(driver, 10)

wait = WebDriverWait(driver,50)

no_allow_but = wait.until(EC.presence_of_element_located((AppiumBy.XPATH,'//android.widget.Button[@resource-id="com.android.permissioncontroller:id/permission_deny_button"]')))
no_allow_but.click()

skip_but = wait.until(EC.presence_of_element_located((AppiumBy.XPATH,'//android.widget.Button[@resource-id="com.socialnmobile.dictapps.notepad.color.note:id/btn_start_skip"]')))
skip_but.click()

bars_but = wait.until(EC.presence_of_element_located((AppiumBy.XPATH,'(//android.widget.ImageView[@resource-id="com.socialnmobile.dictapps.notepad.color.note:id/icon"])[5]')))
bars_but.click()

facebook_but = wait.until(EC.presence_of_element_located((AppiumBy.XPATH,'(//android.widget.ImageView[@resource-id="com.socialnmobile.dictapps.notepad.color.note:id/icon"])[6]')))
facebook_but.click()
time.sleep(3)

print(driver.contexts)
print(driver.context)

login_but = wait.until(EC.presence_of_element_located((AppiumBy.XPATH,'//android.widget.Button[@text="Log in"]')))
print(login_but.text)

# neg_but = wait.until(EC.presence_of_element_located((AppiumBy.XPATH,'//android.widget.Button[@text="Close"]')))
# neg_but.click()
#
# about_but = wait.until(EC.presence_of_element_located((AppiumBy.XPATH,'//android.widget.TextView[@text="About"]')))
# about_but.click()
#
# page_transparency_text = wait.until(EC.presence_of_element_located((AppiumBy.XPATH,'//android.view.View[@text="Page transparency"]')))
# print(page_transparency_text.text)
#
# driver.back()
# driver.back()
# driver.back()


