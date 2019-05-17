import selenium
from bs4 import BeautifulSoup
from selenium import webdriver
import time
import re

# driver = webdriver.Chrome(executable_path="I:\\Programming\\SRCodes\\PyCrawler\\VCG_analysis\\chromedriver.exe")
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions

driver = webdriver.Firefox(executable_path='C:\\Users\\Administrator\\Desktop\\geckodriver.exe')

# # 验证码登录
# driver.get("https://weibo.com/")
# element_loginname = WebDriverWait(driver, 10, 0.5).until(expected_conditions.presence_of_element_located((By.ID, "loginname")))
# element_loginname.clear()
# driver.find_element_by_id("loginname").clear()
# driver.find_element_by_id("loginname").send_keys("setemp@yeah.net")
# driver.find_element_by_name("password").clear()
# driver.find_element_by_name("password").send_keys("setempcrawler")
# driver.find_element_by_name("password").send_keys(Keys.ENTER)
# verifyCode = input("验证码")
# driver.find_element_by_name("verifycode").click()
# driver.find_element_by_name("verifycode").clear()
# driver.find_element_by_name("verifycode").send_keys(verifyCode)
# driver.find_element_by_xpath(u"(.//*[normalize-space(text()) and normalize-space(.)='记住我'])[1]/following::span[1]").click()

# cookies login
cookies = [{'name': 'Ugrow-G0', 'value': '57484c7c1ded49566c905773d5d00f82', 'path': '/', 'domain': 'weibo.com', 'secure': False, 'httpOnly': False}, {'name': 'login_sid_t', 'value': 'bdecaa2a672b97c6dc7254964a1636e0', 'path': '/', 'domain': '.weibo.com', 'secure': False, 'httpOnly': False}, {'name': 'cross_origin_proto', 'value': 'SSL', 'path': '/', 'domain': '.weibo.com', 'secure': False, 'httpOnly': False}, {'name': 'YF-V5-G0', 'value': 'a5a6106293f9aeef5e34a2e71f04fae4', 'path': '/', 'domain': 'weibo.com', 'secure': False, 'httpOnly': False}, {'name': '_s_tentry', 'value': '-', 'path': '/', 'domain': '.weibo.com', 'secure': False, 'httpOnly': False}, {'name': 'Apache', 'value': '117753335189.19684.1558002260530', 'path': '/', 'domain': '.weibo.com', 'secure': False, 'httpOnly': False}, {'name': 'SINAGLOBAL', 'value': '117753335189.19684.1558002260530', 'path': '/', 'domain': '.weibo.com', 'secure': False, 'httpOnly': False, 'expiry': 1873362260}, {'name': 'ULV', 'value': '1558002260547:1:1:1:117753335189.19684.1558002260530:', 'path': '/', 'domain': '.weibo.com', 'secure': False, 'httpOnly': False, 'expiry': 1589106260}, {'name': 'WBStorage', 'value': 'e4e08ad1044aa883|undefined', 'path': '/', 'domain': 'weibo.com', 'secure': False, 'httpOnly': False, 'expiry': 1558002866}, {'name': 'ALF', 'value': '1589538277', 'path': '/', 'domain': '.weibo.com', 'secure': False, 'httpOnly': False, 'expiry': 1589538277}, {'name': 'SSOLoginState', 'value': '1558002278', 'path': '/', 'domain': '.weibo.com', 'secure': False, 'httpOnly': False}, {'name': 'SCF', 'value': 'AjL9B7E8j7TqDIOZ54q02ojm9-1d8sWdlzc-v38UXakK1Mj9qydMTAK38B53TumvXxe-h2-zteG0zztQ39V3SLM.', 'path': '/', 'domain': '.weibo.com', 'secure': False, 'httpOnly': True, 'expiry': 1873362279}, {'name': 'SUB', 'value': '_2A25x2Uo3DeRhGeFP71ES9y3IyjmIHXVSrzz_rDV8PUNbmtBeLW3DkW9NQTZvUkzarB1diRQTtIQQJLjp9C58fl4a', 'path': '/', 'domain': '.weibo.com', 'secure': False, 'httpOnly': True}, {'name': 'SUBP', 'value': '0033WrSXqPxfM725Ws9jqgMF55529P9D9WhCgLHsyBeh.pL6Q6i8gH7d5JpX5K2hUgL.FoMpShe0S0eXeK-2dJLoI7909PxkdP5t', 'path': '/', 'domain': '.weibo.com', 'secure': False, 'httpOnly': False, 'expiry': 1589538279}, {'name': 'SUHB', 'value': '09Pt1df9-hHfEF', 'path': '/', 'domain': '.weibo.com', 'secure': False, 'httpOnly': False, 'expiry': 1589538279}, {'name': 'un', 'value': 'setemp@yeah.net', 'path': '/', 'domain': '.weibo.com', 'secure': False, 'httpOnly': False, 'expiry': 1558866279}, {'name': 'wvr', 'value': '6', 'path': '/', 'domain': '.weibo.com', 'secure': False, 'httpOnly': False, 'expiry': 1558607079}, {'name': 'wb_view_log_7143373415', 'value': '1536*8641.25', 'path': '/', 'domain': 'weibo.com', 'secure': False, 'httpOnly': False, 'expiry': 1558022082}, {'name': 'WBtopGlobal_register_version', 'value': '5c10f3128cf400c5', 'path': '/', 'domain': 'weibo.com', 'secure': False, 'httpOnly': False}, {'name': 'YF-Page-G0', 'value': '530872e91ac9c5aa6d206eddf1bb6a70|1558002314|1558002282', 'path': '/', 'domain': 'weibo.com', 'secure': False, 'httpOnly': False}, {'name': 'webim_unReadCount', 'value': '%7B%22time%22%3A1558002321452%2C%22dm_pub_total%22%3A2%2C%22chat_group_pc%22%3A0%2C%22allcountNum%22%3A7%2C%22msgbox%22%3A0%7D', 'path': '/', 'domain': '.weibo.com', 'secure': False, 'httpOnly': False, 'expiry': 1558088721}]
driver.delete_all_cookies()
driver.get("https://s.weibo.com")
for i in range(0, cookies.__len__()):
    driver.add_cookie(cookies[i])
driver.refresh()


time.sleep(3)


# 日期的循环
for month in range(4, 6):
    if month == 4:
        a = 1
        b = 31
    if month == 5:
        a = 1
        b = 20
    for date in range(a, b):
        time.sleep(5)
        try:

            #  open advsearch
            time.sleep(3)
            element_f = WebDriverWait(driver, 10, 0.5).until(
                expected_conditions.presence_of_element_located((By.LINK_TEXT, "f")))
            element_f.click()  # click little search icon
            element_advsearch = WebDriverWait(driver, 10, 0.5).until(expected_conditions.presence_of_element_located((By.LINK_TEXT, u"高级搜索")))
            element_advsearch.click()

        except selenium.common.exceptions.TimeoutException as e:
            print(e)
            print('date')
            print(date)
            date = date - 1
            continue


        # config advsearch
        driver.find_element_by_name("keyword").click()
        driver.find_element_by_name("keyword").clear()
        driver.find_element_by_name("keyword").send_keys(u"视觉中国")
        driver.find_element_by_name("stime").click()
        driver.find_element_by_xpath(
            u"(.//*[normalize-space(text()) and normalize-space(.)='取消'])[1]/following::select[1]").click()
        driver.find_element_by_xpath(u"(.//*[normalize-space(text()) and normalize-space(.)='取消'])[1]/following::option[%s]" % month).click() # 月
        driver.find_element_by_xpath(
            u"(.//*[normalize-space(text()) and normalize-space(.)='六'])[1]/following::strong[%s]" % date).click()  # 11为日
        driver.find_element_by_name("etime").click()
        driver.find_element_by_xpath(
            u"(.//*[normalize-space(text()) and normalize-space(.)='取消'])[1]/following::select[1]").click()
        driver.find_element_by_xpath(u"(.//*[normalize-space(text()) and normalize-space(.)='取消'])[1]/following::option[%s]" % month).click()
        driver.find_element_by_xpath(
            u"(.//*[normalize-space(text()) and normalize-space(.)='六'])[1]/following::strong[%s]" % date).click()
        driver.find_element_by_link_text(u"搜索微博").click()

        # 处理一次网页源码
        html = driver.page_source
        soup = BeautifulSoup(html)

        # 获取页数
        page = soup.find_all('ul', attrs={'class': 's-scroll'})
        page = page[0].find_all('li')
        page = page.__len__()


        # aaa = re.findall(r'\d', page2[0].text)[0] # 正则表达式寻找数字

        def next():
            driver.refresh()
            time.sleep(2)
            driver.find_element_by_link_text(u"下一页").click()


        # 多页爬取
        for x in range(page):

            # 处理网页源码
            html = driver.page_source
            soup = BeautifulSoup(html)

            # 单页数据写入文件
            content = soup.find_all('p', attrs={"class": "txt"})
            filedir = str(0) + str(month) + ' ' + str(date)
            file = open(r"C:\\vcg\\%s.txt" % filedir, 'a', encoding="GB18030")
            for i in range(0, content.__len__()):
                content[i].text.encode('GB18030')
                file.write(content[i].text)
            file.close()

            try:
                element_next = WebDriverWait(driver, 10, 0.5).until(expected_conditions.presence_of_element_located((By.LINK_TEXT, u'下一页')))
                element_next.click()
                time.sleep(3)
            except selenium.common.exceptions.TimeoutException as e:
                # next()
                driver.refresh()
                time.sleep(2)
                try:
                    driver.find_element_by_link_text(u"下一页").click()
                except selenium.common.exceptions.NoSuchElementException as e:
                    print(e)
                    break
                print(e)
                x = x - 1
                continue
            # 这里可能遇见 selenium.common.exceptions.TimeoutException: Message: Timeout loading page after 300000ms
    driver.refresh()
    time.sleep(10)


# 测试单页数据写入文件
# content = soup.find_all('p', attrs={"class":"txt"})
# a = content[0].text # 选取第一个p的文本
# print(content.__len__()) # 段落数, 一条微博可能由于转发加评论而有两个段落
# file = open(r"Z:\\a.txt",'a', encoding="GB18030")
# for i in range(0, content.__len__()):
#     content[i].text.encode('GB18030')
#     file.write(content[i].text)
# file.close()

# 下一页
# driver.find_element_by_link_text(u'下一页').click()