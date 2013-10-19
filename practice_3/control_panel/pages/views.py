# Create your views here.

import datetime, time, os
from django.shortcuts import render_to_response
from django.shortcuts import render

def home(request):
	context = {'ts' : datetime.datetime.now()}
	return render(request, 'home.html', context)

def walk(dir, deep, dcontext):
	for item in os.listdir(dir):
		path = os.path.join(dir, item)
		t = { 'deep': deep * "*",
			'dir1': os.path.split(os.path.dirname(path))[0], # pt1 link 
			'dir2': os.path.dirname(path).replace("/var/log/",""), # real link
			'dir3': os.path.split(os.path.dirname(path))[1], # pt2 link
			'size': os.path.getsize(path),
			'time': time.ctime(os.path.getmtime(path)) }
		if os.path.isfile(path):
			t['name'] = item
			dcontext.append(t)
		else:
			t['name'] = ""
                        dcontext.append(t)
			walk(path, deep + 1, dcontext)

def listing(request, param):
	dir = "/var/" + param
	dcontext = []
	walk(dir, 0, dcontext)
	context = {'dir_name': dir, 'dir_content': dcontext}
	return render_to_response('listing.html', context)
