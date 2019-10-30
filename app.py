import os
import requests
import json

path = '/data'
dirs = os.listdir(path)

url = '10.0.25.16'
port = '8080'

def insertAll(lines):
	for line in lines:
		post = requests.post('http://'+url+':'+port+'/chaves/', data={'id': line})

if __name__ == '__main__':
	for dire in dirs:
		file = open(path+str(dire))
		lines = file.readlines()
		insertAll(lines)



