from appium import webdriver
from typing import Any, Dict
from appium.options.common import AppiumOptions
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

cap: Dict[str, Any] = {
     'platformName': 'Android',
    'automationName': "uiautomator2",
    'appPackage': 'com.hmh.api',
    'appActivity': '.ApiDemos',
    'language': 'en',
    'locale': 'US'
}

url = 'http://localhost:4724'

driver = webdriver.Remote(url, options=AppiumOptions().load_capabilities(cap))
wait = WebDriverWait(driver, 10)

continue_but = wait.until(EC.visibility_of_element_located((AppiumBy.XPATH,'//android.widget.Button[@resource-id="com.android.permissioncontroller:id/continue_button"]')))
continue_but.click()

ok_but = wait.until(EC.visibility_of_element_located((AppiumBy.XPATH,'//android.widget.Button[@resource-id="android:id/button1"]')))
ok_but.click()

app_ele = wait.until(EC.visibility_of_element_located((AppiumBy.XPATH,'//android.widget.TextView[@resource-id="android:id/text1" and @text="App"]')))
app_ele.click()

act_ele = wait.until(EC.visibility_of_element_located((AppiumBy.XPATH,'//android.widget.TextView[@resource-id="android:id/text1" and @text="Activity"]')))
act_ele.click()

driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR, 'new UiScrollable(new UiSelector().scrollable(true)).scrollIntoView(new UiSelector().text("Wallpaper"))')

wallpaper_ele = driver.find_element(by=AppiumBy.XPATH,value='//android.widget.TextView[@resource-id="android:id/text1" and @text="Wallpaper"]')
wallpaper_ele.click()
