from selenium import webdriver
import csv 
url = 'https://music.163.com/#/user/home?id=652071'
driver = webdriver.PhantomJS()

csv_file = open("niugong_playlist.csv","w",newline='',encoding='utf-8-sig')
writer = csv.writer(csv_file)
writer.writerow(['标题', '播放数', '链接'])

driver.get(url)
driver.switch_to.frame("contentFrame")
data = driver.find_element_by_id("cBox").find_elements_by_tag_name("li")
for i in range(len(data)):
	nb = data[i].find_element_by_class_name("nb").text
	msk = data[i].find_element_by_css_selector("a.msk")
	writer.writerow([msk.get_attribute('title'), nb, msk.get_attribute('href')])

csv_file.close()