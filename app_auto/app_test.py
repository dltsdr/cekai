from appium import webdriver

device={}
device['platformName']='Android'
device['platformVersion']='6.0'
device['deviceName']='emulator-5554'
device['appPackage']='com.android.settings'
device['appActivity']='com.android.settings.Settings'
driver=webdriver.Remote('http://localhost:4723/wd/hub',device)