from apachelogs import LogParser
import sys

stor = []

for line in sys.stdin:
    if 'Exit' == line.rstrip():
        break
    parser = LogParser("%h %l %u %t \"%r\" %>s %b \"%{Referer}i\" \"%{User-Agent}i\"")
    entry = parser.parse(line)
    if entry.remote_host not in stor:
        if entry.remote_host.startsWith("128."):
            print(entry.remote_host)
        if entry.remote_host.startsWith("129."):
            print(entry.remote_host)
        if entry.remote_host.startsWith("151."):
            print(entry.remote_host)
        stor.append(entry.remote_host)