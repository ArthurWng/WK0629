#-*- coding:utf-8 -*-

# ========================================================
# Description    : Something
# Author         : Arthur
# Create Date    : xxxx-xx-xx
# ========================================================
from selenium.webdriver.common.by import By
from controlClass.base_control import baseControl

class newTopic(baseControl):


    # def __init__(self, topic_form):
    #
    #     #self.topic_form = topic_form
    #     #self.type_ = type_
    #
    #     print(topic_form)
    #     # 新建话题页面_1
    #     # ======================================================================
    #     self.topic_name_input_box_loc = (By.XPATH, r'// *[ @ id = "topic-title-edit"]')  # '直播主题输入框'位置
    #
    #     # 时间控件元素
    #     self.start_time_select_btn_loc = (By.XPATH, r'/html/body/div[1]/div[1]/ul[1]/li[2]/span')  # '开始时间'选择按钮位置
    #
    #     # month = 7
    #     # day = 1
    #     # hour = 16
    #     # minute = 20
    #     # /html/body/div[6]/div/div[2]/div/div[3]/div[1]/div/div[2]/div/div[2]/div[1]/div/div/div[6]  # 6月
    #     # /html/body/div[6]/div/div[2]/div/div[3]/div[1]/div/div[3]/div/div[2]/div[1]/div/div[1]/div[1] # 1-19号
    #     # /html/body/div[6]/div/div[2]/div/div[3]/div[1]/div/div[3]/div/div[2]/div[1]/div/div[2]/div[9] # 20-30号
    #     # /html/body/div[6]/div/div[2]/div/div[3]/div[2]/div/div[1]/div/div[2]/div[1]/div/div[1]/div[1] # 1-19时
    #     # /html/body/div[6]/div/div[2]/div/div[3]/div[2]/div/div[1]/div/div[2]/div[1]/div/div[2]/div[1] # 20-23时
    #
    #     # /html/body/div[6]/div/div[2]/div/div[3]/div[2]/div/div[2]/div/div[2]/div[1]/div/div[1]/div[1] # 1-18分
    #     # /html/body/div[6]/div/div[2]/div/div[3]/div[2]/div/div[2]/div/div[2]/div[1]/div/div[2]/div[1] # 19-38分
    #     # /html/body/div[6]/div/div[2]/div/div[3]/div[2]/div/div[2]/div/div[2]/div[1]/div/div[3]/div[1] # 39-58分
    #     # /html/body/div[6]/div/div[2]/div/div[3]/div[2]/div/div[2]/div/div[2]/div[1]/div/div[4]/div[1] # 59分
    #
    #     # selected_start_time_month_btn_loc = (By.XPATH, r'/html/body/div[6]/div/div[2]/div/div[3]/div[1]/div/div[2]/div/div[2]/div[1]/div/div/div[%d]'%month)
    #     # selected_start_time_day_btn_loc = (By.XPATH, r'/html/body/div[6]/div/div[2]/div/div[3]/div[1]/div/div[3]/div/div[2]/div[1]/div/div[1]/div[%d]'%day)
    #     # selected_start_time_hour_btn_loc = (By.XPATH, r'/html/body/div[6]/div/div[2]/div/div[3]/div[2]/div/div[1]/div/div[2]/div[1]/div/div[1]/div[%d]'%hour)
    #     # selected_start_time_minute_btn_loc = (By.XPATH,r'/html/body/div[6]/div/div[2]/div/div[3]/div[2]/div/div[2]/div/div[2]/div[1]/div/div[1]/div[%d]'%minute)
    #
    #     self.time_confirm_btn_loc = (By.XPATH, r'/html/body/div[6]/div/div[2]/div/div[4]/div[2]/div')  # 时间'确定'按钮位置
    #     self.time_cancel_btn_loc = (By.XPATH, r'/html/body/div[6]/div/div[2]/div/div[4]/div[1]/div')  # 时间'取消'按钮位置
    #
    #     # 直播形式选择
    #     #topic_form = 1  # 1-> 讲座形式 2-> 幻灯片形式
    #     self.topic_form_select_btn_loc = (By.XPATH, r'// *[ @ id = "live-type-list"]/li[%d]' % topic_form)
    #     self.topic_info_next_btn_loc = (By.XPATH, r'/html/body/div[1]/div[1]/div/a')  # 直播信息页面'下一步'按钮位置
    #
    #     # 新建话题页面_2
    #     # ======================================================================
    #     type_ = 1  # 1-> 免费 2-> 加密 3-> 收费
    #     self.free_topic_btn_loc = (By.XPATH, r'/html/body/div[1]/div[2]/dl/dt/span[%d]' % type_)  # '公开直播'按钮位置
    #     # 免费话题
    #     self.topic_present_page_switch_btn_loc = (
    #         By.XPATH, r'/html/body/div[1]/div[2]/dl/dd/div[1]/div[2]/span[1]/span')  # '介绍页开关'位置
    #     # 加密话题
    #     self.encrypt_input_box_loc = (By.XPATH, r'/html/body/div[1]/div[2]/dl/dd/div[2]/div/input')  # 加密直播'密码输入框'位置
    #     # 收费话题
    #     self.charge_input_box_loc = (By.XPATH, r'/html/body/div[1]/div[2]/dl/dd/div[3]/div/span[2]/input')  # 收费直播'票价输入框'位置
    #     # 建新话题“完成”按钮
    #     self.new_topic_previous_btn_loc = (By.XPATH, r'/html/body/div[1]/div[2]/div/a[1]')  # 新建话题'上一步'按钮位置
    #     self.new_topic_finish_btn_loc = (By.XPATH, r'/html/body/div[1]/div[2]/div/a[2]')  # 新建话题'完成'按钮位置
    #
    # def new_free_topic(self):
    #     self.clear_cache()
    #
    #     # 新建免费话题
    #     # 1. 输入直播主题
    #     # 2. 选择开始时间
    #     # 3. 选择讲座直播形式
    #     # 4. 下一步
    #     # 5. 选择免费直播类型
    #     # 6. 话题新建完成
    #
    #     self.loc_element(*self.topic_name_input_box_loc).send_keys(u'免费讲座话题')
    #     self.loc_element(*self.start_time_select_btn_loc).click()
    #     self.loc_element(*self.time_confirm_btn_loc).click()
    #     self.loc_element(*self.topic_form_select_btn_loc).click()
    #     self.loc_element(*self.topic_info_next_btn_loc).click()
    #     self.loc_element(*self.free_topic_btn_loc).click()
    #     self.loc_element(*self.new_topic_finish_btn_loc).click()
    #
    # def new_charge_topic(self):
    #     self.clear_cache()
    #
    #     # 新建收费话题
    #     # 1. 输入直播主题
    #     # 2. 选择开始时间
    #     # 3. 选择讲座直播形式
    #     # 4. 下一步
    #     # 5. 选择收费直播类型
    #     # 6. 输入票价
    #     # 7. 话题新建完成
    #
    #     self.loc_element(*self.topic_name_input_box_loc).send_keys(u'免费讲座话题')
    #     self.loc_element(*self.start_time_select_btn_loc).click()
    #     self.loc_element(*self.time_confirm_btn_loc).click()
    #     self.loc_element(*self.topic_form_select_btn_loc).click()
    #     self.loc_element(*self.topic_info_next_btn_loc).click()
    #     self.loc_element(*self.free_topic_btn_loc).click()
    #     self.loc_element(*self.new_topic_finish_btn_loc).click()


    # 新建话题页面_1
    # ======================================================================
    topic_name_input_box_loc = (By.XPATH, r'// *[ @ id = "topic-title-edit"]')  # '直播主题输入框'位置

    # 时间控件元素
    start_time_select_btn_loc = (By.XPATH, r'/html/body/div[1]/div[1]/ul[1]/li[2]/span')  # '开始时间'选择按钮位置

    # month = 7
    # day = 1
    # hour = 16
    # minute = 20
    # /html/body/div[6]/div/div[2]/div/div[3]/div[1]/div/div[2]/div/div[2]/div[1]/div/div/div[6]  # 6月
    # /html/body/div[6]/div/div[2]/div/div[3]/div[1]/div/div[3]/div/div[2]/div[1]/div/div[1]/div[1] # 1-19号
    # /html/body/div[6]/div/div[2]/div/div[3]/div[1]/div/div[3]/div/div[2]/div[1]/div/div[2]/div[9] # 20-30号
    # /html/body/div[6]/div/div[2]/div/div[3]/div[2]/div/div[1]/div/div[2]/div[1]/div/div[1]/div[1] # 1-19时
    # /html/body/div[6]/div/div[2]/div/div[3]/div[2]/div/div[1]/div/div[2]/div[1]/div/div[2]/div[1] # 20-23时

    # /html/body/div[6]/div/div[2]/div/div[3]/div[2]/div/div[2]/div/div[2]/div[1]/div/div[1]/div[1] # 1-18分
    # /html/body/div[6]/div/div[2]/div/div[3]/div[2]/div/div[2]/div/div[2]/div[1]/div/div[2]/div[1] # 19-38分
    # /html/body/div[6]/div/div[2]/div/div[3]/div[2]/div/div[2]/div/div[2]/div[1]/div/div[3]/div[1] # 39-58分
    # /html/body/div[6]/div/div[2]/div/div[3]/div[2]/div/div[2]/div/div[2]/div[1]/div/div[4]/div[1] # 59分

    # selected_start_time_month_btn_loc = (By.XPATH, r'/html/body/div[6]/div/div[2]/div/div[3]/div[1]/div/div[2]/div/div[2]/div[1]/div/div/div[%d]'%month)
    # selected_start_time_day_btn_loc = (By.XPATH, r'/html/body/div[6]/div/div[2]/div/div[3]/div[1]/div/div[3]/div/div[2]/div[1]/div/div[1]/div[%d]'%day)
    # selected_start_time_hour_btn_loc = (By.XPATH, r'/html/body/div[6]/div/div[2]/div/div[3]/div[2]/div/div[1]/div/div[2]/div[1]/div/div[1]/div[%d]'%hour)
    # selected_start_time_minute_btn_loc = (By.XPATH,r'/html/body/div[6]/div/div[2]/div/div[3]/div[2]/div/div[2]/div/div[2]/div[1]/div/div[1]/div[%d]'%minute)

    time_confirm_btn_loc = (By.XPATH, r'/html/body/div[6]/div/div[2]/div/div[4]/div[2]/div')  # 时间'确定'按钮位置
    time_cancel_btn_loc = (By.XPATH, r'/html/body/div[6]/div/div[2]/div/div[4]/div[1]/div')  # 时间'取消'按钮位置

    # 直播形式选择
    # form_ = 1  # 1-> 讲座形式 2-> 幻灯片形式
    # topic_form_select_btn_loc = (By.XPATH, r'// *[ @ id = "live-type-list"]/li[%d]' % form_)
    topic_info_next_btn_loc = (By.XPATH, r'/html/body/div[1]/div[1]/div/a')  # 直播信息页面'下一步'按钮位置

    # 新建话题页面_2
    # ======================================================================
    # type_ = 1  # 1-> 免费 2-> 加密 3-> 收费
    # free_topic_btn_loc = (By.XPATH, r'/html/body/div[1]/div[2]/dl/dt/span[%d]' % type_)  # '公开直播'按钮位置
    # 免费话题
    topic_present_page_switch_btn_loc = (
    By.XPATH, r'/html/body/div[1]/div[2]/dl/dd/div[1]/div[2]/span[1]/span')  # '介绍页开关'位置
    # 加密话题
    encrypt_input_box_loc = (By.XPATH, r'/html/body/div[1]/div[2]/dl/dd/div[2]/div/input')  # 加密直播'密码输入框'位置
    # 收费话题
    charge_input_box_loc = (By.XPATH, r'/html/body/div[1]/div[2]/dl/dd/div[3]/div/span[2]/input')  # 收费直播'票价输入框'位置
    # 建新话题“完成”按钮
    new_topic_previous_btn_loc = (By.XPATH, r'/html/body/div[1]/div[2]/div/a[1]')  # 新建话题'上一步'按钮位置
    new_topic_finish_btn_loc = (By.XPATH, r'/html/body/div[1]/div[2]/div/a[2]')  # 新建话题'完成'按钮位置

    voice_btn_loc = (By.XPATH, '//*[@id="speakBottom"]/ul/li[1]')  # '语音'按钮位置


    def to_new_free_topic(self):

        self.clear_cache()  # 从直播间后台或直播间主页进入

        # 新建免费话题
        # 1. 输入直播主题
        # 2. 选择开始时间
        # 3. 选择讲座直播形式（默认）
        # 4. 下一步
        # 5. 选择免费直播类型（默认）
        # 6. 话题新建完成

        self.loc_element(*self.topic_name_input_box_loc).send_keys(u'免费讲座话题')
        self.loc_element(*self.start_time_select_btn_loc).click()
        self.loc_element(*self.time_confirm_btn_loc).click()
        #self.loc_element(*self.topic_form_select_btn_loc).click()
        self.loc_element(*self.topic_info_next_btn_loc).click()
        #self.loc_element(*self.free_topic_btn_loc).click()
        self.loc_element(*self.new_topic_finish_btn_loc).click()

        self.clear_cache()  # 完成话题新建



    def to_new_encrypt_topic(self):

        topic_form = 1  # 1-> 讲座形式 2-> 幻灯片形式
        topic_form_select_btn_loc = (By.XPATH, r'// *[ @ id = "live-type-list"]/li[%d]' % topic_form)

        topic_type = 2  # 1-> 免费 2-> 加密 3-> 收费
        topic_type_btn_loc = (By.XPATH, r'/html/body/div[1]/div[2]/dl/dt/span[%d]' % topic_type)  # '公开直播'按钮位置

        self.clear_cache()  # 从直播间后台或直播间主页进入

        # 新建加密话题
        # 1. 输入直播主题
        # 2. 选择开始时间
        # 3. 选择讲座直播形式
        # 4. 下一步
        # 5. 选择加密直播类型
        # 6. 输入密码
        # 7. 话题新建完成

        self.loc_element(*self.topic_name_input_box_loc).send_keys(u'加密讲座话题')
        self.loc_element(*self.start_time_select_btn_loc).click()
        self.loc_element(*self.time_confirm_btn_loc).click()
        #self.loc_element(*topic_form_select_btn_loc).click()
        self.loc_element(*self.topic_info_next_btn_loc).click()
        self.loc_element(*topic_type_btn_loc).click()
        self.loc_element(*self.encrypt_input_box_loc).send_keys(123456)
        self.loc_element(*self.new_topic_finish_btn_loc).click()

        self.clear_cache()  # 完成话题新建


    def to_new_charge_topic(self):

        topic_form = 1  # 1-> 讲座形式 2-> 幻灯片形式
        topic_form_select_btn_loc = (By.XPATH, r'// *[ @ id = "live-type-list"]/li[%d]' % topic_form)

        topic_type = 3  # 1-> 免费 2-> 加密 3-> 收费
        topic_type_btn_loc = (By.XPATH, r'/html/body/div[1]/div[2]/dl/dt/span[%d]' % topic_type)  # '公开直播'按钮位置

        self.clear_cache()  # 从直播间后台或直播间主页进入

        # 新建收费讲座话题
        # 1. 输入直播主题
        # 2. 选择开始时间
        # 3. 选择讲座直播形式
        # 4. 下一步
        # 5. 选择收费直播类型
        # 6. 输入票价
        # 7. 话题新建完成

        self.loc_element(*self.topic_name_input_box_loc).send_keys(u'收费讲座话题')
        self.loc_element(*self.start_time_select_btn_loc).click()
        self.loc_element(*self.time_confirm_btn_loc).click()
        #self.loc_element(*topic_form_select_btn_loc).click()
        self.loc_element(*self.topic_info_next_btn_loc).click()
        self.loc_element(*topic_type_btn_loc).click()
        self.loc_element(*self.charge_input_box_loc).send_keys(1)
        self.loc_element(*self.new_topic_finish_btn_loc).click()

        self.clear_cache()  # 完成话题新建