import time
from selenium import webdriver
from _info_bean import InfoBean
import json
linkhref = []
driverPath = "C:/Users/Administrator/AppData/Local/Google/Chrome/Application/76.0.3809.100/chromedriver.exe"
driver = webdriver.Chrome(executable_path=driverPath)

def getCode():
    driver.get("https://trade.500.com/jczq/")
    linkelements = driver.find_elements_by_xpath('//table[1]//tbody/tr[@data-fixtureid]')
    for element in linkelements:
        code = element.get_attribute("data-fixtureid")
        a= InfoBean()
        a.code = code
        linkhref.append(a)
    print(linkhref)

def getFenxi():
    for link in linkhref:
        driver.get(link.url + link.ouzhi + link.code+ ".shtml")
        js="var q=document.documentElement.scrollTop=100000"
        driver.execute_script(js)
        time.sleep(1)
        driver.execute_script(js)
        time.sleep(1)
        driver.execute_script(js)
        time.sleep(1)
        driver.execute_script(js)
        time.sleep(1)
        driver.execute_script(js)
        print("*" *20)
        print(link.ouzhi)
        keepList = driver.find_elements_by_xpath('//div[@class="table_cont"]/table/tbody/tr/td[3]//tr[2]/td[1][@class=""]')
        upList = driver.find_elements_by_xpath('//div[@class="table_cont"]/table/tbody/tr/td[3]//tr[2]/td[1][@class="bg-a"]')
        lowList = driver.find_elements_by_xpath('//div[@class="table_cont"]/table/tbody/tr/td[3]//tr[2]/td[1][@class="bg-b"]')
        time.sleep(5)
        link.hostUp = str(len(upList))
        link.hostKeep = str(len(keepList))
        link.hostDown = str(len(lowList))
        cJson = json.dumps(obj=link.__dict__,ensure_ascii=False)
        print(cJson)
    driver.quit()

if __name__ == "__main__":
    getCode()
    getFenxi()
