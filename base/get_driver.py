from appium import webdriver

def get_driver():
    desired_caps = {}
    # 设备信息
    desired_caps['platformName'] = 'Android'
    desired_caps['platformVersion'] = '5.1'
    desired_caps['deviceName'] = '192.168.237.101:5555'
    # app信息com.vcooline.aike/.umanager.LoginActivity
    desired_caps['appPackage'] = 'com.vcooline.aike'
    desired_caps['appActivity'] = '.umanager.LoginActivity'

    return webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)