import datetime 
import requests
r = requests.get('https://api.meetup.com/2/open_events?&sign=true&photo-host=public&lat=51.53101&country=gb&topic=ios,IT,unix, linux, windows&city=London&lon=-0.082917&category=34&time=,1w&key=427785b3ec73715587310613d4c17')
r1=r.json()#преобразование
fhtml=open("meetup.html", "w+", encoding='utf-8')# encoding-перекодировка текста
fhtml.write("<style>body{background-color:rgb(239,193,109);font-family:Tempus Sans ITC;} h2{ color:rgb(240,60,69)} .content {width: 800px;margin:0 auto 30px; background: #fc0; padding: 7px; border: 1px solid #ccc;}</style>")
for i in r1['results']:
    fhtml.write("<div class='content'><h2 align='center'>Occasion: " + str(i['group']['name']) + "</h2>")
    try:
        fhtml.write("<div align='center'>Address: " + str(i['venue']['address_1']) + "</div>")
    except:
        pass
    time = datetime.datetime.fromtimestamp(int(i['time']/1000))
    fhtml.write("<h3 align='center'>Time: " + time.strftime('%d-%m-%Y %H:%M')+ "</h3>")
    fhtml.write("<div align='center'>Description: " + str(i['description']) + "</div></div>")
    #fhtml.write("<div align='center'>Group: " + str(i['name']) + "</div>")
fhtml.close()
