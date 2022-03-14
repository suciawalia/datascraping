#import package request dan BeautifulSoup
import requests
import json
from bs4 import BeautifulSoup
from array import array
from datetime import datetime
from pickle import APPEND

#Requests ke website 
page = requests.get("https://www.republika.co.id/")
now = datetime.now()
#Extract konten menjadi objek BeautifulSoup
obj = BeautifulSoup(page.text, 'html.parser');
print('Menampilkan objek html')
print('=======================')
print(obj)
print('\nMenampilkan title browser dengan tag')
print('======================================')
print(obj.title)
print('\nMenampilkan title browser tanpa tag')
print('=====================================')
print(obj.title.text)


print('\nMenampilkan semua tag h2') 
print('=====================================')
print(obj.find_all('h2'))


print('\nMenampilkan semua text h2')
print('====================================')
for headline in obj.find_all('h2'):
	print(headline.text)



print('\nMenampilkan headline berdasarkan div class')
print('============================================')
print(obj.find_all('div',class_='conten1'))


print('\nMenampilkan semua text headline')
print('==================================')
for headline in obj.find_all('div',class_='conten1'):
	print(headline.find('h2').text)


print('\nMenampilkan kategori')
print('======================')
for kategori in obj.find_all('div', class_='teaser_conten1_center'):
	print(kategori.find('a').text)


print('\nMenampilkan waktu publish')
print('===========================')
for publish in obj.find_all('div',class_='date'):
	print(publish.text)

current_time = now.strftime("%H:%M:%S")

print('\nMenampilkan waktu scrapping')
print('=============================')
print("Time scrapping= ",current_time)

data=[]

f=open('D:\scraping\Lib\site-packages\BeautifulSoup.json','w')
for publish in obj.find_all('div',class_='conten1'):
    data.append({"judul":headline.find('h2').text,"kategori":kategori.find('a').text,"waktu_publish":publish.find('div',class_='date').text,"waktu_scrapping":now.strftime("%Y-%m-%d %H-:%M:%S")})

jdumps=json.dumps(data, indent=2)
f.writelines(jdumps)
f.close()