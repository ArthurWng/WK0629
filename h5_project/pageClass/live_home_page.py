#-*- coding:utf-8 -*-

# ========================================================
# Description    : Something
# Author         : Arthur
# Create Date    : xxxx-xx-xx
# ========================================================


from selenium.webdriver.common.by import By
from controlClass.base_control import baseControl
from common_PageClass.new_topic_page import newTopic


class liveHomePage(baseControl):

    # 直播间主页
    # ======================================================================
    new_topic_btn_loc = (By.XPATH, '//*[@id="QLLiveRoom"]/div[2]/ul[1]/li[1]/a')

    def new_charge_topic(self):

        self.clear_cache()  # 从其他入口进入

        # 新建收费讲座话题
        # 1. 点击"新建话题"按钮
        # 2. 编辑话题内容，完成免费话题新建
        # 3. 进入直播间

        self.loc_element(*self.new_topic_btn_loc).click()

        new = newTopic(self.driver)
        new.to_new_charge_topic()


    def new_encrypt_topic(self):

        self.clear_cache()  # 从其他入口进入

        # 新建加密讲座话题
        # 1. 点击"新建话题"按钮
        # 2. 编辑话题内容，完成免费话题新建
        # 3. 进入直播间

        self.loc_element(*self.new_topic_btn_loc).click()

        new = newTopic(self.driver)
        new.to_new_encrypt_topic()
