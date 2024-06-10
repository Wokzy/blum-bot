
"""
Autoclicker for Blum drop mini-game
"""

import time
import dxcam
import mouse

from prepare_app import prepare_app
from constants import APPLICATION_TRIGGER, COLOR_TRIGGERS, PIXELS_PER_ITERATION


__author__ = "Wokzy"

global application_bbox
application_bbox = prepare_app()


def check_running(frame) -> bool:
	""" Check if game is running by scanning color on timer positions """
	global application_bbox

	for x, y in APPLICATION_TRIGGER['positions']:

		x *= application_bbox[2] - application_bbox[0]
		y *= application_bbox[3] - application_bbox[1]
		x = int(x)
		y = int(y)

		x += application_bbox[0]
		y += application_bbox[1]
		if frame[y][x][0] == APPLICATION_TRIGGER['color'][0]:
			if frame[y][x][1] == APPLICATION_TRIGGER['color'][1]:
				if frame[y][x][2] == APPLICATION_TRIGGER['color'][2]:
					return True

	return False

def check_object(pixel:tuple[int]) -> bool:
	""" Finding dropping objects by color """
	if COLOR_TRIGGERS['red']['min'] <= pixel[0] <= COLOR_TRIGGERS['red']['max']:
		if COLOR_TRIGGERS['green']['min'] <= pixel[1] <= COLOR_TRIGGERS['green']['max']:
			# print(pixel)
			if COLOR_TRIGGERS['blue']['min'] <= pixel[2] <= COLOR_TRIGGERS['blue']['max']:
				return True

	return False


def main():
	""" Autoclicker impl """
	camera = dxcam.create()
	camera.start(target_fps=60)

	frame = camera.get_latest_frame() # frame is an array with shape (y, x, 3)

	print('Trying to detect running game, click play')
	while not check_running(frame):
		frame = camera.get_latest_frame()
		time.sleep(0.1)

	# time.sleep(2)

	x_shift = 20
	y_shift_top = 150
	y_shift_bot = 250

	print('Game detected!')

	x_range = range(application_bbox[0] + x_shift, application_bbox[2] - x_shift, PIXELS_PER_ITERATION)
	y_range = range(application_bbox[1] + y_shift_top, application_bbox[3] - y_shift_bot, PIXELS_PER_ITERATION)
	while check_running(frame):

		for x in x_range:
			for y in y_range:
				if check_object(frame[y][x]):
					mouse.move(x, y, absolute=True)
					mouse.click(button='left')

		frame = camera.get_latest_frame()

	camera.stop()

if __name__ == "__main__":
	main()
