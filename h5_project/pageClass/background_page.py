#-*- coding:utf-8 -*-

# ========================================================
# Description    : Something
# Author         : Arthur
# Create Date    : xxxx-xx-xx
# ========================================================

from selenium.webdriver.common.by import By
from controlClass.base_control import baseControl
from common_PageClass.new_topic_page import newTopic

class backgroundPage(baseControl):

    # 直播间管理后台页面
    # ======================================================================
    close_push_btn_loc = (By.XPATH, r'/html/body/div[5]/div/a')  # 新功能推送图片'关闭'按钮位置

    change_live_room_btn_loc = (By.XPATH, r'//*[@id="backroomHeader"]/div[1]/a')  # 管理后台页面顶部 '切换直播间'按钮位置

    new_topic_btn_loc = (By.XPATH, r'//*[@id="backPageBox"]/ul/li[1]/a')  # '新建话题'按钮位置
    new_channel_btn_loc = (By.XPATH, '//*[@id="backPageBox"]/ul/li[2]/a')  # 新建系列课按钮位置

    live_room_home_btn_loc = (By.XPATH, r'/html/body/div[2]/a[1]')  # 导航栏'直播间主页'按钮位置
    person_center_btn_loc = (By.XPATH, r'/html/body/div[2]/a[2]')  # 导航栏'个人中心'按钮位置

    def new_free_topic(self):

        # 新建免费话题
        # 1. 关闭新功能推送图片
        # 2. 点击"新建话题"按钮
        # 3. 编辑话题内容，完成免费话题新建

        #self.loc_element(*self.close_push_btn_loc).click()
        self.loc_element(*self.new_topic_btn_loc).click()

        new = newTopic(self.driver)
        new.to_new_free_topic()


