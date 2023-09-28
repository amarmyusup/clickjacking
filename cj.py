import os
import sys
import webbrowser

# Function to print usage information
if len(sys.argv) != 2:
	print('\n[+] Description: %s can quickly verify if a web page is vulnerable to clickjacking' % __file__)
	print('[+] Usage: python {} <url>\n'.format(__file__))
	sys.exit(1)

# Get the target URL from command line arguments
url = sys.argv[1]

# HTML code for the target page
html_target = '''
<!DOCTYPE html>
<html>
<head>
    <title>Clickjacking Alert!</title>
    <link rel="stylesheet" type="text/css" href="styles.css">
</head>
<body>
    <div class="container">
        <h1>Clickjacking Vulnerability Alert!</h1>
        <p>Your web application can be mounted within an iframe, making it vulnerable to Clickjacking.</p>
        <p>Target URL: <a href="{}">{}</a></p>
        <p>If you can see the target website below, it is <span class="vulnerable">VULNERABLE</span> to Clickjacking.</p>
        <div class="iframe-container">
            <iframe src="{}"></iframe>
        </div>
    </div>

    <iframe style="position: absolute; left: 49%; top: 45%; transform: translate(-50%, -50%); opacity: 0.7; font-family: verdana; background: AliceBlue; width: 270px; height: 120px; border: none;" src="attacker.html"></iframe>
</body>
</html>
'''.format(url, url, url)

# HTML code for the attacker page
html_attacker = '''
<html>
    <div style="opacity: 1.0; left: 10px; top: 50px; background: rgba(123, 210, 92, 0.802); font-family: Arial, Helvetica, sans-serif;">
        <center><a href="#">THIS IS AN EXAMPLE CLICKJACKING IFRAME AND LINK</a>
        <br>(normally invisible)</center>
    </div>
</html>
'''

# Get the absolute paths for target and attacker files
target_path = os.path.abspath('target.html')
attacker_path = os.path.abspath('attacker.html')

# Local URL for the target file
local_url = 'file://' + target_path

# Save the HTML code to files
with open(target_path, 'w') as target_file, open(attacker_path, 'w') as attacker_file:
    target_file.write(html_target)
    attacker_file.write(html_attacker)

# Open the target file in a web browser
webbrowser.open(local_url)

print('\n[+] Test Complete!')
