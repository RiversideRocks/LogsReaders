import sys
import json

for line in sys.stdin:
    a = json.loads(line.rstrip())
    print(a["request"]["remote_ip"] + " - - \"" + a["request"]["method"] + " " + a["request"]["uri"] + " "  + a["request"]["proto"] + "\" - " + str(a["status"]) + " - \"" + a["request"]["headers"]["User-Agent"][0] + "\" \"" + a["request"]["host"] + "\"")