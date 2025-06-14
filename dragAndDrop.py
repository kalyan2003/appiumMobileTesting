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
    "appPackage" : "com.mobeta.android.demodslv",
    "appActivity" : ".Launcher",
    "language" : 'en',
    "locale" : 'US'

}

url = "http://localhost:4724"

options = AppiumOptions()
options.load_capabilities(cap)

driver = webdriver.Remote(url,options=options)
driver.implicitly_wait(50)

continue_button = driver.find_element(AppiumBy.XPATH,'//android.widget.Button[@resource-id="com.android.permissioncontroller:id/continue_button"]')
if continue_button.is_displayed():
    continue_button.click()
    ok_button = driver.find_element(AppiumBy.XPATH,'//android.widget.Button[@resource-id="android:id/button1"]')
    ok_button.click()

basic_useage = driver.find_element(AppiumBy.XPATH,'//android.widget.TextView[@text="Basic usage playground"]')
basic_useage.click()

elements = driver.find_elements(AppiumBy.XPATH,'//android.widget.ImageView[@resource-id="com.mobeta.android.demodslv:id/drag_handle"]')
print(len(elements))

source = elements[0]
target = elements[9]

source_loc = source.location
source_size = source.size
source_x = source_loc['x'] + source_size['width']//2
source_y = source_loc['y'] +  source_size['height']//2

target_loc = target.location
target_size = target.size
target_x = target_loc['x'] + target_size['width']//2
target_y = target_loc['y'] +  target_size['height']//2


finger = PointerInput('touch','finger')
action = ActionBuilder(driver,mouse=finger)

action.pointer_action.move_to_location(source_x,source_y)
action.pointer_action.pointer_down()
action.pointer_action.pause(1)
action.pointer_action.move_to_location(target_x,target_y)
action.pointer_action.pause(1)
action.pointer_action.pointer_up()

action.perform()

driver.quit()