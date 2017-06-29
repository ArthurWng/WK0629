#-*- coding:utf-8 -*-

# ========================================================
# Description    : Something
# Author         : Arthur
# Create Date    : xxxx-xx-xx
# ========================================================
def remote_url():
    url = 'http://127.0.0.1:4723/wd/hub'
    return url

def get_desired_caps():

    desired_caps = {
        'platformName' : 'Android',
        'platformVersion' : '5.1',
        'deviceName' : 'KTC',
        #'udid' : '81CEBMJ236WJ',
        'appPackage' : 'com.tencent.mm', # app package name
        'appActivity' : '.ui.LauncherUI', # app 默认的 Activity

        # 开启unicode键盘
        'unicodeKeyboard' : 'True',
        'resetKeyboard' : 'True',

        'newCommandTimeout' : 1800,

        # 驱动H5自动化关键之一
        'chromeOptions' : {'androidProcess': 'com.tencent.mm:tools'}
    }

    return desired_caps
