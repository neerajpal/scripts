import requests

res=requests.get('http://www.gutenberg.org/cache/epub/1112/pg1112.txt')
res.raise_for_status()

file=open('file.txt','wb')
for chunk in res.iter_content(1000):
	file.write(chunk)

file.close()