import requests
import webbrowser
import bs4
import sys

args=sys.argv[1:]
search="+".join(args)
a=["1.jpg","2.jpg","3.jpg","4.jpg","5.jpg"]
print("-----downloading----")

#Open files

files=[]
for i in range(len(a)):
    files.append(open(a[i],'wb'))

#res=requests.get("https://bing.com/images/search?q="+search)

res=requests.get("https://duckduckgo.com/?q="+search+"&t=hs&iax=1&ia=images")

res.raise_for_status()
print("1")
soup=bs4.BeautifulSoup(res.text,'lxml')
images=soup.select('.title--img_media_i img')
print(images)
number=min(5,len(images))

print("2")

for i in range(number):
    link=images[i].get('src')[2:]
    #print(link)
    image=requests.get(link)
    print("Downloading:"+link)
    print("3")
    for chunk in  image.iter_count(100000):
        files[i].write(chunk)
    files[i].close()
