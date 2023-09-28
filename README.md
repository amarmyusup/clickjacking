![ClickJacking](img/clickjacking.png)
# Clickjacking Vulnerability Tester

This script is designed to assess the vulnerability of a web page to clickjacking attacks.

## Description
Attempts to render the target site in an iframe and places another iframe on top of it as an example attack. Inspired by the PoC html boilerplate provided by OWASP (https://www.owasp.org/index.php/Testing_for_Clickjacking_(OTG-CLIENT-009)#How_to_Test).

## Requirements
Python3

## Usage
To test a web page for clickjacking vulnerability, run the script as follows:
`python3 cj.py <url>`

### Output
Creates two html pages: 
* target.html - the page that will be automatically opened in your browser
* attacker.html - a page that generates our sample attacking iframe

### When the page is vulnerable:
![VULNERABLE](img/cj.png)

### When the page is not vulnerable (may also appear blank):
![NOT_VULNERABLE](img/notcj.png)
