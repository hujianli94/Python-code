import re
text = "This is the last one"
res = re.match('(.*) is (.*?) .*', text, re.M | re.I)
if res:
    print("res.group() : ", res.group())
    print("res.group(1) : ", res.group(1))
    print("res.group(2) : ", res.group(2))
    print("res.groups() : ", res.groups())
else:
    print("No match!!")
