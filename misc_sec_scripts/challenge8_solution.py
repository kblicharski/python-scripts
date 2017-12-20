import requests


urls = ["http://us.joincyberstart.com/c8-files/clock-pt1", 
        "http://us.joincyberstart.com/c8-files/clock-pt2",
        "http://us.joincyberstart.com/c8-files/clock-pt3",
        "http://us.joincyberstart.com/c8-files/clock-pt4",
        "http://us.joincyberstart.com/c8-files/clock-pt5"]
query = ""


for url in urls:
    r = requests.get(url)
    query += r.text

    r = requests.get("http://us.joincyberstart.com/c8-files/get-flag?string=" + query)
    flag = r.text
    print("FLAG: " + flag)

