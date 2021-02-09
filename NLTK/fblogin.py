import http.cookiejar
import urllib.request
import requests
import bs4

#cj=http.cookiejar.CookieJar()
#opener=urllib.request.build_opener(urllib.request.HTTPCookieProcessor(cj))

#urllib.request.install_opener(opener)
#auth_url='https://mbasic.facebook.com/'

#payload={
    #'email':'mohitdevli04@gmail.com',
    #'pass':'moh123it45'
#}

#data=urllib.parse.urlencode(payload).encode('utf-8')
#req=urllib.request.Request(auth_url,data)
#resp=urllib.request.urlopen(req)
#content=resp.read()
#print(data)


import mechanicalsoup

browser = mechanicalsoup.StatefulBrowser()
base_url='https://mbasic.facebook.com/login.php'
login_page = browser.open(base_url)

browser.select_form('form[action="/login/device-based/regular/login/?refsrc=https%3A%2F%2Fmbasic.facebook.com%2Flogin.php&lwv=100&refid=9"]')

browser['email']='mohitdevli04@gmail.com'
browser['pass']='m'

browser.submit_selected()

print(browser.get_url())
if browser.get_url=='https://mbasic.facebook.com/home.php?_rdr' or 'https://mbasic.facebook.com/checkpoint/?_rdr':
    print('True')
else:
    print('false')