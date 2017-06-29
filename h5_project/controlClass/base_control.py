#-*- coding:utf-8 -*-

# ========================================================
# Description    : Something
# Author         : Arthur
# Create Date    : xxxx-xx-xx
# ========================================================

import os
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


class baseControl(object):

    def  __init__(self, appium_driver):
        self.driver = appium_driver

    ############################
    # location elements
    ############################
    def loc_element(self, *loc):
        self.element_wait(10, loc)
        return self.driver.find_element(*loc)

    ############################
    # wait in seconds for a element
    ############################
    def element_wait(self, seconds, element_loc):
        return WebDriverWait(self.driver, seconds).until(EC.visibility_of_element_located(element_loc))

    ############################
    # switch to web-view(H5) page
    ############################

    def switch_to_h5(self):
        self.driver.switch_to.context('WEBVIEW_com.tencent.mm:tools')

        #contexts = self.driver.contexts  # 获取当前页面的context
        #print(contexts)


    def switch_to_app(self):
        self.driver.switch_to.context('NATIVE_APP')

    ############################
    # get the context of current page
    ############################
    def prt_context(self):
        contexts = self.driver.contexts
        print contexts

    ############################
    # clear cache for web-view (操作第二个web-view需求清一下缓存)
    ############################

    def clear_cache(self):
        self.switch_to_app()
        os.popen('taskkill /f /im chromedriver.exe')
        self.switch_to_h5()