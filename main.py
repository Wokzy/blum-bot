
import os
import time
import dxcam
import mouse
import win32gui
# import pyautogui

from constants import *
from prepare_app import prepare_app




# global debug_image_iterator, debug_images_list, application_bbox
application_bbox = prepare_app()
camera = dxcam.create()

# debug_image_iterator = 0
# debug_images_list = os.listdir('images')
# def get_image():
# 	global debug_image_iterator, debug_images_list, application_bbox
# 	return ImageGrab.grab(application_bbox)

# 	# DEBUG:
# 	# fp = open(f'images/{debug_images_list[debug_image_iterator]}', 'rb')
# 	# image = Image.open(fp)
# 	# debug_image_iterator += 1
# 	# fp.close()

# 	return image

def check_running(frame) -> bool:
	for x, y in APPLICATION_TRIGGER['positions']:

		# FIXME
		x *= application_bbox[2] - application_bbox[0]
		y *= application_bbox[3] - application_bbox[1]
		x = int(x)
		y = int(y)

		x += application_bbox[0]
		y += application_bbox[1]
		if frame[y][x][0] == APPLICATION_TRIGGER['color'][0] and frame[y][x][1] == APPLICATION_TRIGGER['color'][1]:
			return True

	return False

def check_object(pixel:tuple[int]) -> bool:
	if COLOR_TRIGGERS['red']['min'] <= pixel[0] <= COLOR_TRIGGERS['red']['max']:
		if COLOR_TRIGGERS['green']['min'] <= pixel[1] <= COLOR_TRIGGERS['green']['max']:
			# print(pixel)
			if COLOR_TRIGGERS['blue']['min'] <= pixel[2] <= COLOR_TRIGGERS['blue']['max']:
				return True

	return False

camera.start(target_fps=60)

frame = camera.get_latest_frame() # frame is an array with shape (y, x, 3)
image_bbox = frame.shape

print('Trying to detect running game, click play')
while not check_running(frame):
	frame = camera.get_latest_frame()
	time.sleep(0.1)

# time.sleep(2)

x_shift = 20
y_shift_top = 150
y_shift_bot = 250

print('Game detected!')
while True:

	for x in range(application_bbox[0] + x_shift, application_bbox[2], 8):
		for y in range(application_bbox[1] + y_shift_top, application_bbox[3], 8):
			if check_object(frame[y][x]):
				mouse.move(x, y, absolute=True)
				mouse.click(button='left')
				# pyautogui.click(x = x, y = y, button='left')
				# print(f'Found on: {x}, {y}')


	frame = camera.get_latest_frame()
	if not check_running(frame):
		time.sleep(3)
		if not check_running(frame):
			break
	# print('\n\n')

camera.stop()
