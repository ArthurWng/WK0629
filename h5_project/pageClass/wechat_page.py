#-*- coding:utf-8 -*-

# ========================================================
# Description    : Something
# Author         : Arthur
# Create Date    : xxxx-xx-xx
# ========================================================

from selenium.webdriver.common.by import By
from controlClass.base_control import baseControl
import time

# Wechat Page



class wechatPage(baseControl):

    # 微信页面
    #======================================================================
    close_oa_btn_loc = (By.ID, r'com.tencent.mm:id/h4')

    search_btn_loc = (By.NAME, u'搜索')  # Wechat右上角搜索按钮的位置
    search_input_box_loc = (By.ID, r'com.tencent.mm:id/gz')  # 搜索输入框
    searched_oa_loc = (By.ID, r'com.tencent.mm:id/jd')  # 搜索到的OA位置

    def open_oa(self):

        '''
        打开千聊公众号
        1. 打开微信搜索。
        2. 输入“千聊Live”
        3. 点“千聊Live”微信公众号
        '''
        self.loc_element(*self.search_btn_loc).click()
        self.loc_element(*self.search_input_box_loc).send_keys(u'千聊Live')
        self.loc_element(*self.searched_oa_loc).click()

    def close_oa(self):

        self.switch_to_app()
        self.loc_element(*self.close_oa_btn_loc).click()



    # “我的”菜单
    # ======================================================================
    mine_btn_loc = (By.NAME, u'我的')  # '我的'按钮位置

    personal_trainer_btn_loc = (By.NAME, u'免费私教')  # 免费私教按钮位置（听课定制）
    my_live_room_btn_loc = (By.NAME, u'我的直播间')  # '我的直播间'按钮位置
    personal_center_btn_loc = (By.NAME, u'个人中心')  # '个人中心'按钮位置
    purchased_course_btn_loc = (By.NAME, u'已购买课程')  # '已购买课程'按钮位置

    # “正在直播”
    # ======================================================================
    live_btn_loc = (By.NAME, u'正在直播')  # '正在直播'按钮位置


    def open_live_room_bgd(self):
        '''
        进入直播间后台
        1. 点“我的”菜单
        2. 点“我的直播间”
        '''
        self.loc_element(*self.mine_btn_loc).click()
        self.loc_element(*self.my_live_room_btn_loc).click()

        self.switch_to_h5()

    def open_personal_center(self):
        '''
        进入个人中心
        1. 点“我的”菜单
        2. 点“我的直播间” 
        3. 从NativeApp切换到h5页面
        '''
        self.loc_element(*self.mine_btn_loc).click()
        self.loc_element(*self.personal_center_btn_loc).click()

        self.switch_to_h5()

