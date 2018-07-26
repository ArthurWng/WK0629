#-*- coding:utf-8 -*-

# ========================================================
# Description    : Something
# Author         : Arthur
# Create Date    : xxxx-xx-xx
# ========================================================

import unittest
import time
from appium import webdriver
from controlClass.session_info import *
from pageClass.wechat_page import wechatPage
from pageClass.background_page import backgroundPage
from common_PageClass.topic_detail_page import topicDetailPage
from pageClass.live_home_page import liveHomePage
from common_PageClass.topic_intro_page import topicIntroPage

class test_abc(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Remote(remote_url(), get_desired_caps())
        cls.driver.implicitly_wait(10)

    @classmethod
    def tearDownClass(cls):
        time.sleep(3)
        driver = wechatPage(cls.driver)
        driver.close_oa()  # 打开公众号
        cls.driver.quit()

    def test_1_new_free_topic(self):
        # 建新免费讲座话题
        # 1. 打开公众号
        # 2. 进入直播间后台
        # 3. 新建话题


        driver = wechatPage(self.driver)
        driver.open_oa()  # 打开公众号
        driver.open_live_room_bgd()

        live_room = backgroundPage(self.driver)  # 新建免费讲座话题
        live_room.new_free_topic()
        
        # 断言：UI、响应信息及数据检查
        # assertEqual(实际结果，期望结果)

    def test_2_new_charge_topic(self):
        # 建新收费讲座话题
        # 1. 进入直播间主页
        # 2. 新建话题

        topic_detail = topicDetailPage(self.driver)  # 进入直播间主页
        topic_detail.open_live_home()

        live_home = liveHomePage(self.driver)  # 新建话题
        live_home.new_charge_topic()

        intro_page = topicIntroPage(self.driver)  # 进入直播
        intro_page.enter_live()
        
        # 断言：UI、响应信息及数据检查
        # assertEqual(实际结果，期望结果)
        


    def test_3_new_encrypt_topic(self):
        # 建新加密讲座话题
        # 1. 进入直播间主页
        # 2. 新建话题

        topic_detail = topicDetailPage(self.driver)  # 进入直播间主页
        topic_detail.open_live_home()

        live_home = liveHomePage(self.driver)  # 新建话题
        live_home.new_encrypt_topic()

        intro_page = topicIntroPage(self.driver)  # 进入直播
        intro_page.enter_live()
        
        # 断言：UI、响应信息及数据检查
        # assertEqual(实际结果，期望结果)





if __name__ == '__main__':
    unittest.main(verbosity=3)
