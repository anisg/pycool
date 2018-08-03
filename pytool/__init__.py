#IO

def fput(filename, data, opener="w"):
	f = open(filename, opener)
	f.write(data.encode("utf8"))
	f.close()

def fget(filename):
	with open(filename, 'r') as content_file:
		content = content_file.read()
	return content.decode("utf8")

def jget(filename):
	return json.loads(fget(filename))

def jdumps(data, indent=True):
	if indent == True:
		return json.dumps(data, ensure_ascii=False, indent=4).encode('utf8')
	return json.dumps(data, ensure_ascii=False).encode('utf8')

def jput(filename, data, indent=True):
	if indent == True:
		return fput(filename, jdumps(data, indent))
	return fput(filename, jdumps(data, indent))

