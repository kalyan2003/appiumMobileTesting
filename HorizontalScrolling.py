from appium import webdriver
from typing import Any, Dict
from appium.options.common import AppiumOptions
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

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

app_ele = wait.until(EC.visibility_of_element_located(
    (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("Views")')))
app_ele.click()

act_ele = wait.until(EC.visibility_of_element_located(
    (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("Gallery")')))
act_ele.click()

phot_ele = wait.until(EC.visibility_of_element_located((AppiumBy.ANDROID_UIAUTOMATOR,'new UiSelector().text("1. Photos")')))
phot_ele.click()

driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR, 'new UiScrollable(new UiSelector().scrollable(true)).setAsHorizontalList().scrollToEnd(5)')


