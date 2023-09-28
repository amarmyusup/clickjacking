import os
import sys
import webbrowser

# Cek jumlah argumen
if len(sys.argv) != 2:
    print('\n[+] Description: This script quickly verifies if a web page is vulnerable to clickjacking')
    print('[+] Usage: python {} <url>\n'.format(__file__))
    sys.exit(1)

# URL target
url = sys.argv[1]

# Kode HTML untuk halaman target
html_target = '''
<html>
    <head>
        <title>Clickjacking!</title>
    </head>

    <body>
        <b style="font-size: larger; font-family: Verdana, Geneva, Tahoma, sans-serif;">
            <p style="font-weight: bold;">Your Web Application Can be Mounted within an iFrame which makes it vulnerable to ClickJacking!</p>
            <p>Target: <a href="{}">{}</a></p>
            <p>If you see the target website rendered below, it is <font color="red">VULNERABLE</font>.</p>
            <iframe width="900" height="600" src="{}"></iframe>
            <iframe style="position: absolute; left: 45px; top: 250px; opacity: 0.7; font-family: verdana; background: AliceBlue;" src="cj-attacker.html"></iframe>
        </b>
    </body>
</html>
'''.format(url, url, url)

# Kode HTML untuk halaman penyerang
html_attacker = '''
<html>
    <div style="opacity: 1.0; left: 10px; top: 50px; background: rgba(123, 210, 92, 0.802); font-family: verdana;">
        <center><a href="#">THIS IS AN EXAMPLE CLICKJACKING IFRAME AND LINK</a>
        <br>(normally invisible)</center>
    </div>
</html>
'''

# Path ke file target dan attacker
path_target = os.path.abspath('target.html')
path_attacker = os.path.abspath('attacker.html')

# URL lokal untuk file target
local_url = 'file://' + path_target

# Menyimpan kode HTML ke file
with open(path_target, 'w') as target_file, open(path_attacker, 'w') as attacker_file:
    target_file.write(html_target)
    attacker_file.write(html_attacker)

# Membuka file target di peramban web
webbrowser.open(local_url)

print('\n[+] Test Complete!')
