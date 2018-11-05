from selenium import webdriver
import csv 
url = 'https://music.163.com/#/user/event?id=102083968'
driver = webdriver.PhantomJS()

csv_file = open("网易云音乐动态鸡爷.csv","w",newline='',encoding='utf-8-sig')
writer = csv.writer(csv_file)
writer.writerow(['时间', '评论'])

driver.get(url)
driver.switch_to.frame("contentFrame")
data = driver.find_element_by_id("eventListBox").find_elements_by_tag_name("li")
#time = driver.find_element_by_id("eventListBox").find_elements_by_tag_name("li").find_elements_by_class_name("time").find_elements_by_css_selector('a.s-fc4')
for i in range(len(data)):
	time = data[i].find_elements_by_class_name("time")
	content = data[i].find_elements_by_class_name("text")
	for j in range(len(time)):
		time_link = time[j].find_elements_by_css_selector('a.s-fc4')
		content_txt = content[j].text
		for k in range(len(time_link)):
			time_txt = time_link[k].text
			print(time_txt)
			print(content_txt)
			writer.writerow([time_txt, content_txt])
#	msk = data[i].find_element_by_css_selector("a.msk")
#	writer.writerow([msk.get_attribute('title'), nb, msk.get_attribute('href')])
#	writer.writerow([time])

csv_file.close()