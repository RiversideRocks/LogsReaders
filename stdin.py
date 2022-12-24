from apachelogs import LogParser
import sys

stor = []

for line in sys.stdin:
    if 'Exit' == line.rstrip():
        break
    parser = LogParser("%h %l %u %t \"%r\" %>s %b \"%{Referer}i\" \"%{User-Agent}i\"")
    entry = parser.parse(line)
    if entry.remote_host not in stor:
        print(entry.remote_host)
        stor.append(entry.remote_host)
        print("== " + len(stor) + " Unique Hits ==")