from appium import webdriver
from typing import Any, Dict
from appium.options.common import AppiumOptions
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

cap: Dict[str, Any] = {
    'platformName': 'Android',
    'automationName': 'uiautomator2',
    'deviceName': 'Android Emulator',
    'appPackage': 'com.hmh.api',
    'appActivity': '.ApiDemos',
    'language': 'en',
    'locale': 'US'
}

url = 'http://localhost:4724'

driver = webdriver.Remote(url, options=AppiumOptions().load_capabilities(cap))
wait = WebDriverWait(driver, 10)


try:
    continue_but = wait.until(EC.visibility_of_element_located(
        (AppiumBy.ID, "com.android.permissioncontroller:id/continue_button")))
    continue_but.click()

    ok_but = wait.until(EC.visibility_of_element_located((AppiumBy.ID, "android:id/button1")))
    ok_but.click()
except:
    pass

wait1 = WebDriverWait(driver, 50)

el2 = wait1.until(EC.presence_of_element_located(
    (AppiumBy.XPATH, "//android.widget.TextView[@text='App']")))
el2.click()

alert_but = wait1.until(EC.presence_of_element_located((AppiumBy.XPATH,"//android.widget.TextView[@text='Alert Dialogs']")))
alert_but.click()

ok_alert = wait1.until(EC.presence_of_element_located((AppiumBy.XPATH,'//android.widget.Button[@resource-id="com.hmh.api:id/two_buttons"]')))
ok_alert.click()
time.sleep(3)

driver.switch_to.alert.accept()

dismiss_alert = wait1.until(EC.presence_of_element_located((AppiumBy.XPATH,'//android.widget.Button[@resource-id="com.hmh.api:id/two_buttons"]')))
dismiss_alert.click()

driver.switch_to.alert.dismiss()

list_dialog = wait1.until(EC.presence_of_element_located((AppiumBy.XPATH,'//android.widget.Button[@resource-id="com.hmh.api:id/select_button"]')))
list_dialog.click()

dialog_ele = driver.find_elements(AppiumBy.XPATH,'//android.widget.TextView[@resource-id="android:id/text1"]')
dialog_ele[3].click()

