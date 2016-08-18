import os
import json


def check():
    with open('./antitamper.list') as f:
        content = json.loads(f.read())
        for f in content:
            s = "echo '%s  %s' | md5sum -c --status >> ./tamper.log" % (content[f], f)
            os.system(s)

check()