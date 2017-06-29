#-*- coding:utf-8 -*-

# ========================================================
# Description    : Something
# Author         : Arthur
# Create Date    : xxxx-xx-xx
# ========================================================

from selenium.webdriver.common.by import By
from controlClass.base_control import baseControl

class topicDetailPage(baseControl):

    # 话题详情页
    # ======================================================================
    live_home_btn = (By.XPATH, '/html/body/div[1]/div[1]/div[1]/div[4]/div[1]/div')  # 直播间主页按钮

    def open_live_home(self):
        self.loc_element(*self.live_home_btn).click()
