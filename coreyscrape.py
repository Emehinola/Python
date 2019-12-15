from bs4 import BeautifulSoup
import requests

source = requests.get('https://coreyms.com').text

soup = BeautifulSoup(source, 'lxml')
for container in soup.find('article'):

	headline = container.h2.a.text
	print("Heading: ", headline)

summary = container.find('div', class_='entry-content').p.text
#print("Summary: ", summary)

vid_src = container.find('iframe', class_='youtube-player')['src']
#print(vid_src)

vid_id = vid_src.split('/')[4]
vid_id = vid_id.split('?')[0]

vid_link = f'htpps://www.youtube.com/watch?v={vid_id}'
#print("Link: ", vid_link)