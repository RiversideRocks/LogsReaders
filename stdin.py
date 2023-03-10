from apachelogs import LogParser
import sys
import requests


stor = []

for line in sys.stdin:
    if 'Exit' == line.rstrip():
        break
    parser = LogParser("%h %l %u %t \"%r\" %>s %b \"%{Referer}i\" \"%{User-Agent}i\"")
    entry = parser.parse(line)
    if entry.remote_host not in stor:
        """
        This next segment of code can always be commented out
        """
        try:
            api = requests.get('https://whois-referral.toolforge.org/gateway.py?lookup=true&format=json&ip=' + entry.remote_host).json()
            try:
                print(entry.remote_host + " | " + api["geolite2"] + " | " + api["nets"][0]["description"])
            except:
                print(entry.remote_host + " | ???")
        except:
            print(entry.remote_host + " | ???")
        stor.append(entry.remote_host)
        print("== " + str(len(stor)) + " Unique Hits ==")
