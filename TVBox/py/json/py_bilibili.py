#coding=utf-8
#!/usr/bin/python
import sys
sys.path.append('..') 
from base.spider import Spider
import json
import time
import base64

class Spider(Spider):  # 元类 默认的元类 type
	def getName(self):
		return "TVBOX课堂"
	def init(self,extend=""):
		print("============{0}============".format(extend))
		pass
	def isVideoFormat(self,url):
		pass
	def manualVideoCheck(self):
		pass
	def homeContent(self,filter):
		result = {}
		cateManual = {
			    "TVBox": "TVBox",
			"MT管理器": "MT管理器",
			"NP管理器": "NP管理器",
                              "WebDAV": "WebDAV",
                                      "alist": "alist",
                                    "脱壳": "脱壳",     
                                    "爬虫": "爬虫",
                              "json&jar": "json&jar",
                              "电影解说": "电影解说",
                              "儿童早教": "儿童早教",
                          "儿童启蒙故事": "儿童启蒙故事",
                          "儿童英语启蒙": "儿童英语启蒙",
                               "儿童歌曲": "儿童歌曲",
                              "儿童绘画": "儿童绘画",
                              "睡前故事": "睡前故事",
                              "儿童动画": "儿童动画",
      "儿童音乐": "儿童音乐",
      "儿童安全教育": "儿童安全教育",
      "宝宝巴士": "宝宝巴士",
      "儿歌多多": "儿歌多多",
     "1年级语文": "1年级语文",
      "1年级数学": "1年级数学",
      "1年级英语": "1年级英语",
      "2年级语文": "2年级语文",
      "2年级数学": "2年级数学",
      "2年级英语": "2年级英语",
      "3年级语文": "3年级语文",
      "3年级数学": "3年级数学",
     "3年级英语": "3年级英语",
      "4年级语文": "4年级语文",
      "4年级数学": "4年级数学",
     "4年级英语": "4年级英语",
      "5年级语文": "5年级语文",
      "5年级数学": "5年级数学",
      "5年级英语": "5年级英语",
      "6年级语文": "6年级语文",
      "6年级数学": "6年级数学",
      "6年级英语": "6年级英语",
      "7年级语文": "7年级语文",
      "7年级数学": "7年级数学",
      "7年级英语": "7年级英语",
      "7年级历史": "7年级历史",
      "7年级地理": "7年级地理",
      "7年级生物": "7年级生物",
     "8年级语文": "8年级语文",
    "8年级数学": "8年级数学",
      "8年级英语": "8年级英语",
      "8年级历史": "8年级历史",
     "8年级地理": "8年级地理",
      "8年级生物": "8年级生物",
      "9年级语文": "9年级语文",
      "9年级数学": "9年级数学",
      "9年级英语": "9年级英语",
      "9年级历史": "9年级历史",
       "9年级地理": "9年级地理",
      "9年级生物": "9年级生物",
      "高一语文": "高一语文",
      "高一数学": "高一数学",
     "高一英语": "高一英语",
     "高一历史": "高一历史",
      "高一地理": "高一地理",
      "高一生物": "高一生物",
      "高一思想政治": "高一思想政治",
     "高一物理": "高一物理",
      "高一化学": "高一化学",
      "高二语文": "高二语文",
      "高二数学": "高二数学",
      "高二英语": "高二英语",
      "高二历史": "高二历史",
    "高二地理": "高二地理",
   "高二生物": "高二生物",
   "高二思想政治": "高二思想政治",
      "高二物理": "高二物理",
   "高二化学": "高二化学",
      "高三语文": "高三语文",
      "高三数学": "高三数学",
     "高三英语": "高三英语",
      "高三历史": "高三历史",
     "高三地理": "高三地理",
      "高三生物": "高三生物",
      "高三思想政治": "高三思想政治",
      "高三物理": "高三物理",
      "高三化学": "高三化学",
      "高中信息技术": "高中信息技术",
      "高中信息技术": "高中信息技术",
     "球星": "球星",
      "演讲": "演讲",
     "搞笑": "搞笑",
      "广场舞": "广场舞",
      "动物世界": "动物世界",
      "MTV": "MTV",
      "足球": "足球",
      "篮球": "篮球",
      "小姐姐": "小姐姐",
      "风景": "风景",
      "食谱": "食谱",
      "鬼畜": "鬼畜",
      "健身": "健身",
     "窗白噪音": "窗白噪音",
"相声小品": "相声小品",
	"Zard": "Zard",
	"演唱会": "演唱会"
		}
		classes = []
		for k in cateManual:
			classes.append({
				'type_name':k,
				'type_id':cateManual[k]
			})
		result['class'] = classes
		if(filter):
			result['filters'] = self.config['filter']
		return result
	def homeVideoContent(self):
		result = {
			'list':[]
		}
		return result
	cookies = ''
	def getCookie(self):
		rsp = self.fetch("https://www.bilibili.com/")
		self.cookies = rsp.cookies
		return rsp.cookies
	def categoryContent(self,tid,pg,filter,extend):		
		result = {}
		url = 'https://api.bilibili.com/x/web-interface/search/type?search_type=video&keyword={0}&duration=4&page={1}'.format(tid,pg)
		if len(self.cookies) <= 0:
			self.getCookie()
		rsp = self.fetch(url,cookies=self.cookies)
		content = rsp.text
		jo = json.loads(content)
		if jo['code'] != 0:			
			rspRetry = self.fetch(url,cookies=self.getCookie())
			content = rspRetry.text		
		jo = json.loads(content)
		videos = []
		vodList = jo['data']['result']
		for vod in vodList:
			aid = str(vod['aid']).strip()
			title = vod['title'].strip().replace("<em class=\"keyword\">","").replace("</em>","")
			img = 'https:' + vod['pic'].strip()
			remark = str(vod['duration']).strip()
			videos.append({
				"vod_id":aid,
				"vod_name":title,
				"vod_pic":img,
				"vod_remarks":remark
			})
		result['list'] = videos
		result['page'] = pg
		result['pagecount'] = 9999
		result['limit'] = 90
		result['total'] = 999999
		return result
	def cleanSpace(self,str):
		return str.replace('\n','').replace('\t','').replace('\r','').replace(' ','')
	def detailContent(self,array):
		aid = array[0]
		url = "https://api.bilibili.com/x/web-interface/view?aid={0}".format(aid)

		rsp = self.fetch(url,headers=self.header)
		jRoot = json.loads(rsp.text)
		jo = jRoot['data']
		title = jo['title'].replace("<em class=\"keyword\">","").replace("</em>","")
		pic = jo['pic']
		desc = jo['desc']
		typeName = jo['tname']
		vod = {
			"vod_id":aid,
			"vod_name":title,
			"vod_pic":pic,
			"type_name":typeName,
			"vod_year":"",
			"vod_area":"",
			"vod_remarks":"",
			"vod_actor":"",
			"vod_director":"",
			"vod_content":desc
		}
		ja = jo['pages']
		playUrl = ''
		for tmpJo in ja:
			cid = tmpJo['cid']
			part = tmpJo['part']
			playUrl = playUrl + '{0}${1}_{2}#'.format(part,aid,cid)

		vod['vod_play_from'] = 'B站'
		vod['vod_play_url'] = playUrl

		result = {
			'list':[
				vod
			]
		}
		return result
	def searchContent(self,key,quick):
		result = {
			'list':[]
		}
		return result
	def playerContent(self,flag,id,vipFlags):
		# https://www.555dianying.cc/vodplay/static/js/playerconfig.js
		result = {}

		ids = id.split("_")
		url = 'https://api.bilibili.com:443/x/player/playurl?avid={0}&cid=%20%20{1}&qn=112'.format(ids[0],ids[1])
		rsp = self.fetch(url)
		jRoot = json.loads(rsp.text)
		jo = jRoot['data']
		ja = jo['durl']
		
		maxSize = -1
		position = -1
		for i in range(len(ja)):
			tmpJo = ja[i]
			if maxSize < int(tmpJo['size']):
				maxSize = int(tmpJo['size'])
				position = i

		url = ''
		if len(ja) > 0:
			if position == -1:
				position = 0
			url = ja[position]['url']

		result["parse"] = 0
		result["playUrl"] = ''
		result["url"] = url
		result["header"] = {
			"Referer":"https://www.bilibili.com",
			"User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.127 Safari/537.36"
		}
		result["contentType"] = 'video/x-flv'
		return result

	config = {
		"player": {},
		"filter": {}
	}
	header = {}

	def localProxy(self,param):
		return [200, "video/MP2T", action, ""