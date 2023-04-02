#!/usr/bin/env python3
import subprocess

def xrandr():
	out = {}
	pos = -1
	s = subprocess.check_output('xrandr | grep \"connected\"', shell=True).decode().strip().split("\n")
	screen = 0
	screens = []
	for item in s:
		pos += 1
		screens.append(pos)
		out[pos] = {}
		if len(item.split('+')) == 3:
			out[pos]['name'] = item.split(' connected ')[0]
			if 'inverted' in item:
				out[pos]['inverted'] = True
			else:
				out[pos]['inverted'] = False
			if 'primary' in item:
				split = 'primary '
				out[pos]['primary'] = True
				screen = pos
			else:
				out[pos]['primary'] = False
				split = 'connected '
			geometry = item.split(split)[1].split(' ')[0]
			out[pos]['geometry'] = geometry
			out[pos]['w'] = int(geometry.split('x')[0])
			out[pos]['h'] = int(geometry.split('x')[1].split('+')[0])
			out[pos]['pos_x'] = int(geometry.split('x')[1].split('+')[1])
			out[pos]['pos_y'] = int(geometry.split('x')[1].split('+')[2])
			out[pos]['connected'] = True
		else:
			out[pos]['connected'] = False
			out[pos]['geometery'] = None
			out[pos]['w'] = None
			out[pos]['h'] = None
			out[pos]['pos_x'] = None
			out[pos]['pos_y'] = None
			out[pos]['primary'] = False
			out[pos]['inverted'] = False
	return out

def get_connected():
	screens = xrandr()
	out = {}
	for screen in screens:
		if screens[screen]['connected']:
			out[screen] = screens[screen]
	return out

if __name__ == "__main__":
	xrandr()

