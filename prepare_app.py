"""
Opens game window and provides info about it
"""

import win32gui

from constants import APPLICATION_NAME

def prepare_app() -> tuple[int]:
	""" Top up window and return its bbox """
	toplist, winlist = [], []
	def _enum_cb(hwnd, results):
		winlist.append((hwnd, win32gui.GetWindowText(hwnd)))
	win32gui.EnumWindows(_enum_cb, toplist)

	# print(winlist)

	application = [(hwnd, title) for hwnd, title in winlist if APPLICATION_NAME in title]
	# just grab the hwnd for first window matching firefox
	application = application[0]
	hwnd = application[0]

	win32gui.SetForegroundWindow(hwnd)
	return win32gui.GetWindowRect(hwnd)
