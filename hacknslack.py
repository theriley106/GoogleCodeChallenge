import requests
import shutil
import os

def download():
	for i in range(1, 9):
		url = 'https://techchallenge.withgoogle.com/puzzles/hack-n-slash/08.png'
		response = requests.get(url, stream=True)
		response.raw.decode_content = True
		with open('img{}.png'.format(i), 'wb') as out_file:
		    shutil.copyfileobj(response.raw, out_file)
		del response

if __name__ == '__main__':
	composite -blend 50 1.jpg 2.jpg res.jpg
	download()
