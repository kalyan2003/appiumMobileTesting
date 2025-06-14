import time

from appium import webdriver
from typing import Dict, Any
from appium.options.common import AppiumOptions
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.actions.action_builder import ActionBuilder
from selenium.common import ElementNotVisibleException, NoSuchElementException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.actions.pointer_input import PointerInput
from selenium.webdriver.common.actions import interaction
from selenium.webdriver.support import expected_conditions as EC



cap:Dict[str, Any] = {
    "platformName" : "Android",
    "automationName" : "uiautomator2",
    "deviceName" : "emulator-5554",
    "appPackage" : "com.google.android.contacts",
    "appActivity" : "com.google.android.apps.contacts.activities.PeopleActivity",
    "language" : 'en',
    "locale" : 'US'

}

url = "http://localhost:4724"

options = AppiumOptions()
options.load_capabilities(cap)

driver = webdriver.Remote(url,options=options)
driver.implicitly_wait(50)

driver.find_element(AppiumBy.XPATH,'//android.widget.Button[@resource-id="android:id/button2"]').click()

element = driver.find_elements(AppiumBy.XPATH,'//android.widget.TextView[@resource-id="com.google.android.contacts:id/cliv_name_textview"]')
print(len(element))

el = element[1]
location = el.location
size = el.size
center_x = location['x'] + size['width'] // 2
center_y = location['y'] + size['height'] // 2



#long press
finger = PointerInput("touch", "finger")
tap_action = ActionBuilder(driver, mouse=finger)
tap_action.pointer_action.move_to_location(center_x, center_y)
tap_action.pointer_action.pointer_down()
tap_action.pointer_action.pause(4)
tap_action.pointer_action.pointer_up()
tap_action.perform()