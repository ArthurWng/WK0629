#-*- coding:utf-8 -*-

# ========================================================
# Description    : Something
# Author         : Arthur
# Create Date    : xxxx-xx-xx
# ========================================================

from selenium.webdriver.common.by import By
from controlClass.base_control import baseControl


class topicIntroPage(baseControl):

    # 话题介绍页
    # ======================================================================
    enter_live_btn_loc = (By.XPATH, '//*[@id="intro-bottom"]/a[2]')


    def enter_live(self):
        self.loc_element(*self.enter_live_btn_loc).click()
        self.clear_cache()
