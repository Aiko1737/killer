import datetime
import time
from DrissionPage import ChromiumPage

# 创建对象
page = ChromiumPage()

# 指定秒杀时间（转换为datetime对象）
times = datetime.datetime.strptime("2024-10-10 20:00:00.000000", '%Y-%m-%d %H:%M:%S.%f')

# 打开淘宝网页
page.get("https://www.taobao.com")
# 点击购物车
page.ele('x://*[@id="J_MiniCart"]/div[1]/a/span[2]').click()
# 等待登录完成，直到购物车全选按钮出现，超时时间我设置为1分钟
page.wait.ele_displayed('@class=ant-checkbox-wrapper cartOperationCheckbox--CIlk23mK', timeout=60)
# 点击购物车全选按钮
page.ele('@class=ant-checkbox-wrapper cartOperationCheckbox--CIlk23mK').click()

# 无限循环检测时间
while True:
    # 获取当前时间
    now = datetime.datetime.now()

    # 打印当前时间用于调试
    print(now.strftime('%Y-%m-%d %H:%M:%S.%f'))  

    # 如果当前时间大于等于指定时间，执行秒杀
    if now >= times:
        while True:
            try:
                # 找到结算按钮并点击
                if page.ele('x://*[@id="settlementContainer_1"]/div[4]/div/div[2]'):
                    page.ele('x://*[@id="settlementContainer_1"]/div[4]/div/div[2]').click()
                    print("结算成功")
                    break
            except:
                print("找不到结算按钮")
        while True:
            try:
                # 找到提交订单按钮并点击
                if page.ele('x://*[@id="submitOrder"]/div/div[2]/div'):
                    page.ele('x://*[@id="submitOrder"]/div/div[2]/div').click()
                    now1 = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f')
                    print("抢购成功时间：%s" % now1)
                    break
            except:
                print("再次尝试提交订单")
                break
        break  # 成功提交订单后，退出循环
    time.sleep(0.01)  # 减少CPU空转
