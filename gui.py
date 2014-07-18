#!/usr/bin/env python
# -*- coding: utf-8 -*-

from Tkinter import *
import wemo
import urllib2
import xml.etree.ElementTree as ET

_xmls = {}
_buttons = {}

class App(Frame):
	def __init__(self, parent):
		Frame.__init__(self, parent)
		self.parent = parent

		self.initUI()
	
	def initUI(self):
		for device in wemo.conn.ENUM_HOSTS:
			Label(self, text=_xmls[device][1][1].text).grid(row=device, column=0)
			_buttons[device] = Button(self, text="On" if wemo.get() else "Off", command=lambda: toggleButton(device))
			_buttons[device].grid(row=device, column=1)
		
		self.pack(fill=BOTH, expand=1)

def toggleButton(device):
	wemo.toggle()
	_buttons[device]["text"] = "On" if wemo.get() else "Off"

def main():
	for device in wemo.conn.ENUM_HOSTS:
		_xmls[device] = ET.fromstring(urllib2.urlopen(wemo.conn.ENUM_HOSTS[device]['xmlFile']).read())

	root = Tk()
	root.geometry("250x150+300+300")
	root.title('WeMo GUI')

	app = App(root)
	root.mainloop()


if __name__ == '__main__':
	main()
