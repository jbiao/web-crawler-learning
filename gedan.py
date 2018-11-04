from selenium import webdriver
import csv 
url = 'https://music.163.com/#/discover/playlist/?order=hot&cat=%E5%85%A8%E9%83%A8&limit=35&offset=0'
driver = webdriver.PhantomJS()
#import sys
#if sys.getdefaultencoding() != 'utf-8':
#    reload(sys)
#    sys.setdefaultencoding('utf-8')
 
#def utf_8_decoder(unicode_csv_data):
#     return unicode_csv_data.decode('utf-8','ignore').encode("gb2312",'ignore')

#csv_file = open("playist.csv", "w", newline='')
csv_file = open("playlist.csv","w",newline='',encoding='utf-8-sig')
writer = csv.writer(csv_file)
writer.writerow(['标题', '播放数', '链接'])
#writer.writerow([utf_8_decoder('标题'),utf_8_decoder('次数'),utf_8_decoder('链接')])

while url != 'javascript:void(0)':
	driver.get(url)
	driver.switch_to.frame("contentFrame")
	data = driver.find_element_by_id("m-pl-container").find_elements_by_tag_name("li")
	for i in range(len(data)):
		nb = data[i].find_element_by_class_name("nb").text
		if '万' in nb and int(nb.split("万")[0]) > 500:
			msk = data[i].find_element_by_css_selector("a.msk")
#			s_title = msk.get_attribute('title')
#			str_title = s_title.decode('utf-8')
#			gbk_title = s_title.encode('gbk')
#			s_href = msk.get_attribute('href')
#			str_href = s_href.decode('utf-8')
#			gbk_href = s_href.encode('gbk')
			writer.writerow([msk.get_attribute('title'), nb, msk.get_attribute('href')])
	url = driver.find_element_by_css_selector("a.zbtn.znxt").get_attribute('href')
csv_file.close()