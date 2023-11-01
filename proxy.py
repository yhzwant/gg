import re

import requests

import threading





print('''

scraping...
            

''')





urls = '''

http://alexa.lr2b.com/proxylist.txt		
										
http://proxysearcher.sourceforge.net/Proxy%20List.php?type=http	
											
http://rootjazz.com/proxies/proxies.txt
											
http://spys.me/proxy.txt												

http://worm.rip/http.txt												

http://www.proxyserverlist24.top/feeds/posts/default												

https://api.openproxylist.xyz/http.txt												

https://api.proxyscrape.com/?request=displayproxies&proxytype=http												

https://api.proxyscrape.com/v2/?request=getproxies&protocol=http												

https://api.proxyscrape.com/v2/?request=getproxies&protocol=https												

https://multiproxy.org/txt_all/proxy.txt												

https://proxy-spider.com/api/proxies.example.txt												

https://proxyspace.pro/http.txt												

https://proxyspace.pro/https.txt		
										
https://raw.githubusercontent.com/B4RC0DE-TM/proxy-list/main/HTTP.txt		
										
https://raw.githubusercontent.com/clarketm/proxy-list/master/proxy-list-raw.txt	
											
https://raw.githubusercontent.com/hookzof/socks5_list/master/proxy.txt	
											
https://raw.githubusercontent.com/HyperBeats/proxy-list/main/http.txt			
									
https://raw.githubusercontent.com/HyperBeats/proxy-list/main/https.txt	
											
https://raw.githubusercontent.com/jetkai/proxy-list/main/online-proxies/txt/proxies-http.txt					
							
https://raw.githubusercontent.com/mmpx12/proxy-list/master/http.txt				
								
https://raw.githubusercontent.com/monosans/proxy-list/main/proxies/http.txt							
					
https://raw.githubusercontent.com/monosans/proxy-list/main/proxies_anonymous/http.txt	
											
https://raw.githubusercontent.com/opsxcq/proxy-list/master/list.txt		
										
https://raw.githubusercontent.com/proxy4parsing/proxy-list/main/http.txt	
											
https://raw.githubusercontent.com/roosterkid/openproxylist/main/HTTPS_RAW.txt	
											
https://raw.githubusercontent.com/RX4096/proxy-list/main/online/all.txt

https://raw.githubusercontent.com/saschazesiger/Free-Proxies/master/proxies/http.txt

https://raw.githubusercontent.com/ShiftyTR/Proxy-List/master/http.txt

https://raw.githubusercontent.com/ShiftyTR/Proxy-List/master/https.txt

https://raw.githubusercontent.com/shiftytr/proxy-list/master/proxy.txt

https://raw.githubusercontent.com/sunny9577/proxy-scraper/master/proxies.txt

https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/http.txt

https://raw.githubusercontent.com/TheSpeedX/SOCKS-List/master/http.txt

https://raw.githubusercontent.com/UserR3X/proxy-list/main/online/http.txt

https://raw.githubusercontent.com/UserR3X/proxy-list/main/online/https.txt

https://sheesh.rip/http.txt

https://sheesh.rip/new.txt

https://www.freeproxychecker.com/result/http_proxies.txt

https://www.my-proxy.com/free-anonymous-proxy.html

https://www.my-proxy.com/free-proxy-list-10.html

https://www.my-proxy.com/free-proxy-list-2.html

https://www.my-proxy.com/free-proxy-list-3.html

https://www.my-proxy.com/free-proxy-list-4.html

https://www.my-proxy.com/free-proxy-list-5.html

https://www.my-proxy.com/free-proxy-list-6.html

https://www.my-proxy.com/free-proxy-list-7.html

https://www.my-proxy.com/free-proxy-list-8.html

https://www.my-proxy.com/free-proxy-list-9.html

https://www.my-proxy.com/free-proxy-list.html

https://www.my-proxy.com/free-transparent-proxy.html

https://www.proxy-list.download/api/v1/get?type=http

https://www.proxyscan.io/download?type=http

https://www.proxyscan.io/download?type=https

https://proxy11.com/api/proxy.txt?key=NDAzNg.YYHPVA.QB8moHDjsHJ_R_q8lkgkUV3wt2c

https://api.proxyscrape.com/v2/?request=displayproxies&protocol=socks4

https://api.proxyscrape.com/?request=displayproxies&proxytype=socks4

https://api.proxyscrape.com/?request=displayproxies&proxytype=socks4&country=all

https://api.openproxylist.xyz/socks4.txt

https://proxyspace.pro/socks4.txt

https://raw.githubusercontent.com/monosans/proxy-list/main/proxies/socks4.txt

https://raw.githubusercontent.com/monosans/proxy-list/main/proxies_anonymous/socks4.txt

https://raw.githubusercontent.com/jetkai/proxy-list/main/online-proxies/txt/proxies-socks4.txt

https://raw.githubusercontent.com/ShiftyTR/Proxy-List/master/socks4.txt

https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/socks4.txt

https://raw.githubusercontent.com/roosterkid/openproxylist/main/SOCKS4_RAW.txt												

http://worm.rip/socks4.txt

https://www.proxy-list.download/api/v1/get?type=socks4

https://www.proxyscan.io/download?type=socks4

https://www.my-proxy.com/free-socks-4-proxy.html												

http://www.socks24.org/feeds/posts/default

https://www.freeproxychecker.com/result/socks4_proxies.txt

https://raw.githubusercontent.com/HyperBeats/proxy-list/main/socks4.txt

https://raw.githubusercontent.com/mmpx12/proxy-list/master/socks4.txt

https://raw.githubusercontent.com/saschazesiger/Free-Proxies/master/proxies/socks4.txt

https://raw.githubusercontent.com/B4RC0DE-TM/proxy-list/main/SOCKS4.txt

https://raw.githubusercontent.com/B4RC0DE-TM/proxy-list/main/SOCKS5.txt

https://raw.githubusercontent.com/saschazesiger/Free-Proxies/master/proxies/socks5.txt

https://raw.githubusercontent.com/mmpx12/proxy-list/master/socks5.txt

https://raw.githubusercontent.com/HyperBeats/proxy-list/main/socks5.txt

https://api.openproxylist.xyz/socks5.txt

https://api.proxyscrape.com/?request=displayproxies&proxytype=socks5

https://api.proxyscrape.com/v2/?request=displayproxies&protocol=socks5

https://api.proxyscrape.com/v2/?request=displayproxies&protocol=socks5

https://api.proxyscrape.com/v2/?request=getproxies&protocol=socks5&timeout=10000&country=all&simplified=true

https://proxyspace.pro/socks5.txt

https://raw.githubusercontent.com/manuGMG/proxy-365/main/SOCKS5.txt

https://raw.githubusercontent.com/monosans/proxy-list/main/proxies/socks5.txt

https://raw.githubusercontent.com/monosans/proxy-list/main/proxies_anonymous/socks5.txt

https://raw.githubusercontent.com/ShiftyTR/Proxy-List/master/socks5.txt

https://raw.githubusercontent.com/jetkai/proxy-list/main/online-proxies/txt/proxies-socks5.txt

https://raw.githubusercontent.com/roosterkid/openproxylist/main/SOCKS5_RAW.txt

https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/socks5.txt

https://raw.githubusercontent.com/hookzof/socks5_list/master/proxy.txt

https://raw.githubusercontent.com/BlackSnowDot/proxylist-update-every-minute/main/socks.txt												

http://worm.rip/socks5.txt												

http://www.socks24.org/feeds/posts/default

https://www.freeproxychecker.com/result/socks5_proxies.txt

https://www.proxy-list.download/api/v1/get?type=socks5

https://www.proxyscan.io/download?type=socks5

https://www.my-proxy.com/free-socks-5-proxy.html												

http://ab57.ru/downloads/proxyold.txt													

'''





file = open('proxy.txt', 'w')

file.write('Proxy:\n')

file.close()

file = open('proxy.txt', 'a')

good_proxies = list()





def pattern_one(url):

    ip_port = re.findall('(\d{,3}\.\d{,3}\.\d{,3}\.\d{,3}:\d{2,5})', url)

    if not ip_port: pattern_two(url)

    else:

        for i in ip_port:

            file.write(str(i) + '\n')

            good_proxies.append(i)





def pattern_two(url):

    ip = re.findall('>(\d{,3}\.\d{,3}\.\d{,3}\.\d{,3})<', url)

    port = re.findall('td>(\d{2,5})<', url)

    if not ip or not port: pattern_three(url)

    else:

        for i in range(len(ip)):

            file.write(str(ip[i]) + ':' + str(port[i]) + '\n')

            good_proxies.append(str(ip[i]) + ':' + str(port[i]))





def pattern_three(url):

    ip = re.findall('>\n[\s]+(\d{,3}\.\d{,3}\.\d{,3}\.\d{,3})', url)

    port = re.findall('>\n[\s]+(\d{2,5})\n', url)

    if not ip or not port: pattern_four(url)

    else:

        for i in range(len(ip)):

            file.write(str(ip[i]) + ':' + str(port[i]) + '\n')

            good_proxies.append(str(ip[i]) + ':' + str(port[i]))





def pattern_four(url):

    ip = re.findall('>(\d{,3}\.\d{,3}\.\d{,3}\.\d{,3})<', url)

    port = re.findall('>(\d{2,5})<', url)

    if not ip or not port: pattern_five(url)

    else:

        for i in range(len(ip)):

            file.write(str(ip[i]) + ':' + str(port[i]) + '\n')

            good_proxies.append(str(ip[i]) + ':' + str(port[i]))





def pattern_five(url):

    ip = re.findall('(\d{,3}\.\d{,3}\.\d{,3}\.\d{,3})', url)

    port = re.findall('(\d{2,5})', url)

    for i in range(len(ip)):

        file.write(str(ip[i]) + ':' + str(port[i]) + '\n')

        good_proxies.append(str(ip[i]) + ':' + str(port[i]))





def start(url):

    try:

        req = requests.get(url, headers={'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.51 Safari/537.36'}).text

        pattern_one(req)

        print(f' [+] Scrapping')

    except requests.exceptions.SSLError: print(str(url) + ' [x] SSL Error')

    except: print(str(url) + ' [x] Random Error')





threads = list()

for url in urls.splitlines():

    if url:

        x = threading.Thread(target=start, args=(url, ))

        x.start()

        threads.append(x)





for th in threads:

    th.join()





input(f' \n\n[!] Total scraped proxies: ({len(good_proxies)}) finished! please click enter')

