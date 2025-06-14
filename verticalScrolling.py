# from appium import webdriver
# from typing import Any, Dict
# from appium.options.common import AppiumOptions
# from appium.webdriver.common.appiumby import AppiumBy
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# from selenium.webdriver.common.actions.pointer_input import PointerInput
# from selenium.webdriver.common.actions.interaction import Interaction
# from selenium.webdriver.common.actions.action_builder import ActionBuilder
#
# cap: Dict[str, Any] = {
#     'platformName': 'Android',
#     'automationName': 'uiautomator2',
#     'deviceName': 'Android Emulator',
#     'appPackage': 'com.hmh.api',
#     'appActivity': '.ApiDemos',
#     'language': 'en',
#     'locale': 'US'
# }
#
# url = 'http://localhost:4724'  # or 4724 if you're using custom port
#
# driver = webdriver.Remote(url, options=AppiumOptions().load_capabilities(cap))
# wait = WebDriverWait(driver, 10)
#
# # Handle initial permission dialogs if any
# try:
#     continue_but = wait.until(EC.visibility_of_element_located(
#         (AppiumBy.ID, "com.android.permissioncontroller:id/continue_button")))
#     continue_but.click()
#
#     ok_but = wait.until(EC.visibility_of_element_located((AppiumBy.ID, "android:id/button1")))
#     ok_but.click()
# except:
#     pass  # skip if not shown
#
# # Navigate to required screen
# app_ele = wait.until(EC.visibility_of_element_located(
#     (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("App")')))
# app_ele.click()
#
# act_ele = wait.until(EC.visibility_of_element_located(
#     (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("Activity")')))
# act_ele.click()
#
# # Get screen size
# deviceSize = driver.get_window_size()
# screenWidth = deviceSize['width']
# screenHeight = deviceSize['height']
#
# startX = endX = screenWidth // 2
# startY = int(screenHeight * 0.8)
# endY = int(screenHeight * 0.2)
#
# # Use PointerInput for touch gestures
# finger = PointerInput(Interaction.TOUCH, "finger")
# actions = ActionBuilder(driver)
# actions.add_action(finger)
#
# # Perform scroll gesture
# actions.w3c_actions.pointer_action.move_to_location(startX, startY)
# actions.w3c_actions.pointer_action.pointer_down()
# actions.w3c_actions.pointer_action.pause(0.2)
# actions.w3c_actions.pointer_action.move_to_location(endX, endY)
# actions.w3c_actions.pointer_action.release()
# actions.perform()
#
# # Finish
# driver.quit()


import time
from typing import Any, Dict

from appium import webdriver
from appium.options.common import AppiumOptions
from appium.webdriver.common.appiumby import AppiumBy
# from appium.webdriver.common.touch_action import TouchAction
from selenium.common import ElementNotVisibleException, NoSuchElementException
from selenium.webdriver.common.actions import interaction
from selenium.webdriver.common.actions.action_builder import ActionBuilder
from selenium.webdriver.common.actions.pointer_input import PointerInput
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.expected_conditions import presence_of_element_located
from selenium.webdriver.support.wait import WebDriverWait

cap: Dict[str, Any] = {
    'platformName': 'Android',
    'automationName': "uiautomator2",
    'deviceName': 'Android',
    'appPackage': 'com.hmh.api',
    'appActivity': '.ApiDemos',
    'language': 'en',
    'locale': 'US',
    'noReset': True
}

url = 'http://localhost:4724'

time.sleep(2)

driver = webdriver.Remote(url, options=AppiumOptions().load_capabilities(cap))

driver.implicitly_wait(10)

try:
    continue_buttons = driver.find_elements(AppiumBy.XPATH, '//android.widget.Button[@text="Continue"]')
    if continue_buttons:
        continue_buttons[0].click()

        wait = WebDriverWait(driver, 10)
        el1 = wait.until(EC.presence_of_element_located((AppiumBy.ID, "android:id/button")))
        el1.click()

except Exception as e:
    print("No permission popup or error occurred:", e)

wait1 = WebDriverWait(driver, 10, poll_frequency=1,
                      ignored_exceptions=[ElementNotVisibleException, NoSuchElementException])

el2 = wait1.until(presence_of_element_located(
    (AppiumBy.XPATH, "//android.widget.TextView[@text='App']")))
el2.click()

el3 = wait1.until(presence_of_element_located(
    (AppiumBy.XPATH, "//android.widget.TextView[@text='Activity']")))
el3.click()
# driver.find_element(
#     AppiumBy.ANDROID_UIAUTOMATOR,
#     'new UiScrollable(new UiSelector().scrollable(true)).scrollIntoView(new UiSelector().text("Wallpaper"))'
# )

device_size = driver.get_window_size()
print(device_size)

screen_width = device_size['width']
screen_height = device_size['height']

print(screen_width)
print(screen_height)

start_x = screen_width / 2
end_x = screen_width / 2

start_y = screen_height * 8 / 9
end_y = screen_height / 9

# actions = TouchAction(driver)
#
# actions.long_press(None, start_x, start_y).move_to(None, end_x, end_y).release().perform()


finger = PointerInput(interaction.POINTER_TOUCH, "finger")
actions = ActionBuilder(driver, mouse=finger)  # Initialize with PointerInput
action = actions.pointer_action  # Access pointer_action

action.move_to_location(int(start_x), int(start_y))
action.pointer_down()
action.pause(0.1)
action.move_to_location(int(end_x), int(end_y))
action.pointer_up()

actions.perform()
