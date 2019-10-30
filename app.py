import os
import requests
import json

path = '/home/sheylong/Documentos/Contagil/Cyeor/data/'
dirs = os.listdir(path)

url = 'localhost'
port = '5000'

def insertAll(lines):
	for i in range(1, len(lines)):
		key = lines[i].split('|')[0]
		post = requests.post('http://'+url+':'+port+'/chaves/', data={'id': key})
		print(post)


if __name__ == '__main__':
	for dire in dirs:
		file = open(path+str(dire))
		lines = file.readlines()
		insertAll(lines)



