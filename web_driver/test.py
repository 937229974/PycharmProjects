from   selenium import webdriver
import  time

def test():
    url ="http://channel.ymt.nongyaodai.com/#/ymt/guide?source=gnqb01"
    driver = webdriver.Chrome()
    driver.get(url)
    time.sleep(5)

    # 模拟登录 /html/body/div/div/div[1]/div[1]/div[1]/input
    # driver.find_element_by_xpath('/html/body/div/div/div[1]/div[1]/div[1]/input').send_keys("1111")
    # driver.find_element_by_xpath('/html/body/div/div/div[1]/div[1]/div[1]/input').send_keys("15291043162")
    driver.find_element_by_xpath('.//*[@id="app"]/div/div[1]/div[1]/div[2]/input').send_keys("112336")
    driver.find_element_by_xpath('.//*[@id="app"]/div/div[1]/div[1]/div[3]/input').send_keys("w111111")
    driver.find_element_by_xpath(".//*[@id='fm1']/input[3]").click()
    # 让这家伙睡会  O(∩_∩)O哈哈~  为什么要睡呢，这是为了模拟手动登录，防止被封
    time.sleep(10)
    driver.refresh()
    # 以上模拟登录算是完成了

if __name__ =="__main__":
    test()