import os
import sys
import webbrowser

if len(sys.argv) != 2:
	print('\n[+] Description: %s can quickly verify if a web page is vulnerable to clickjacking' % __file__)
	print('[+] Usage: python %s <url>\n' % __file__)
	exit(0)

url = sys.argv[1]

html = '''
<html>
	<head>
		<title>Clickjacking!</title>
	</head>
	<body>
		<b style="font-size: larger; font-family: Verdana, Geneva, Tahoma, sans-serif;">
		<p style="font: bold;">Your Web Application Can be Mounted within an iFrame which makes it vulnerable to ClickJacking!</p>
		<p>Target: <a href="http://testphp.vulnweb.com/login.php">http://testphp.vulnweb.com/login.php</a></p>
		<p>If you see the target website rendered below, it is <font color="red">VULNERABLE</font>.</p>
		<iframe width="900" height="600" src="http://testphp.vulnweb.com/login.php"></iframe>
		<iframe style="position: absolute; left: 45px; top: 250px; opacity: 0.7; font-family:verdana; background: AliceBlue;" src="cj-attacker.html"></iframe>
		</b>
	</body>
</html>
''' % (url, url, url)

html2 = '''
<html>
	<div style="opacity: 1.0; left: 10px; top: 50px; background: rgba(123, 210, 92, 0.802); font-family:verdana;">
		<center><a href="#">THIS IS AN EXAMPLE CLICKJACKING IFRAME AND LINK</a>
		<br>(normally invisible)</center>
	</div>
</html>
'''

cjt = os.path.abspath('target.html')
cja = os.path.abspath('attacker.html')
localurl = 'file://' + cjt

with open(cjt, 'w') as t, open (cja, 'w') as a:
	t.write(html)
	a.write(html2)

webbrowser.open(localurl)

print('\n[+] Test Complete!')
