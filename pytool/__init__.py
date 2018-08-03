import sys
if sys.version_info < (3, 0):
	reload(sys)
	sys.setdefaultencoding("utf-8")
import os, json, requests, argparse

#VARIABLE

scriptDir= os.path.dirname(sys.argv[0])

#IO

def fput(filename, data, opener="w"):
	f = open(filename, opener)
	f.write(data)
	f.close()

def fget(filename):
	with open(filename, 'r') as content_file:
		content = content_file.read()
	return content

def jget(filename):
	return json.loads(fget(filename))

def jdumps(data, indent=True):
	if indent == True:
		return json.dumps(data, ensure_ascii=False, indent=4)
	return json.dumps(data, ensure_ascii=False)

def jput(filename, data, indent=True):
	if indent == True:
		return fput(filename, jdumps(data, indent))
	return fput(filename, jdumps(data, indent))

#NETWORK

def get(url, cookies=None):
    headers = {"Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8","Accept-Encoding":"gzip, deflate, sdch","Accept-Language":"fr-FR,fr;q=0.8,en-US;q=0.6,en;q=0.4","Cache-Control":"max-age=0","Connection":"keep-alive"}
    if cookies != None:
        headers.update({"cookies":cookies})
    return requests.get(url, headers=headers).content

#MISC

def parse(description,arr=[]):
    parser = argparse.ArgumentParser(description=description)
    for x in arr:
    	if len(x) == 2:
    		(k,a) = x
    		parser.add_argument(k, **a)
    	elif len(x) == 3:
    		(k,kl,a) = x
    		parser.add_argument(k, kl, **a)
    return parser.parse_args()

#todo:
#confirm (yes,no)

def createDir(path):
	return os.makedirs(path)