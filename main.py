
"""
Autoclicker for Blum drop mini-game
"""

import sys
import time
import mouse
import random
import keyboard
import datetime
# import dxcam_cpp as dxcam
import dxcam

from PIL import Image

from prepare_app import prepare_app
from constants import (
	TGE_MODE,
	CLICK_LIMIT,
	HELP_STRING,
	DOGS_DROP_TOGGLE,
	AVG_GAME_DURATION,
	TGE_COLOR_TRIGGERS,
	APPLICATION_TRIGGER,
	NEW_GAME_TRIGGER_POS,
	PIXELS_PER_ITERATION,
	DEFAULT_COLOR_TRIGGER,
	DOGS_WHITE_COLOR_RANGE,
)


__author__ = "Wokzy"

def check_running(frame, application_bbox) -> bool:
	""" Check if game is running by scanning color on timer positions """

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

	for x in APPLICATION_TRIGGER['range'][0]:
		x += application_bbox[0]
		for y in APPLICATION_TRIGGER['range'][1]:
			y += application_bbox[1]
			if frame[y][x][0] == APPLICATION_TRIGGER['color'][0]:
				if frame[y][x][1] == APPLICATION_TRIGGER['color'][1]:
					if frame[y][x][2] == APPLICATION_TRIGGER['color'][2]:
						return True

	return False


def check_object(frame, x:int, y:int) -> bool:
	""" Finding dropping objects by color """

	def _check_color_trigger(color_trigger, check_x=x, check_y=y, limit:bool=True):
		if limit and random.random() > CLICK_LIMIT:
			return False

		if color_trigger['red']['min'] <= frame[check_y][check_x][0] <= color_trigger['red']['max']:
			if color_trigger['green']['min'] <= frame[check_y][check_x][1] <= color_trigger['green']['max']:
				# print(frame[check_y][check_x])
				if color_trigger['blue']['min'] <= frame[check_y][check_x][2] <= color_trigger['blue']['max']:
					return True
		return False

	if TGE_MODE:
		for i in range(len(TGE_COLOR_TRIGGERS)):
			trigger = TGE_COLOR_TRIGGERS[i]
			if _check_color_trigger(TGE_COLOR_TRIGGERS[i]):
				return True
		return False
	elif _check_color_trigger(DEFAULT_COLOR_TRIGGER):
		return True

	#DOGS DROP
	if DOGS_DROP_TOGGLE:
		if frame[y][x][0] == frame[y][x][1] == frame[y][x][2] and DOGS_WHITE_COLOR_RANGE[0] <= frame[y][x][0] <= DOGS_WHITE_COLOR_RANGE[1]:
			counter = 0
			for i in range(-1, 2):
				for j in range(-4, 2):
					counter += (frame[y + j][x + i][0] == frame[y + j][x + i][1] == frame[y + j][x + i][2] and DOGS_WHITE_COLOR_RANGE[0] <= frame[y + j][x + i][0] <= DOGS_WHITE_COLOR_RANGE[1])

			if counter >= 10:
				return True


	return False


def wait_running_game(camera, timeout:float = .0) -> None:
	application_bbox = prepare_app()
	frame = camera.get_latest_frame()
	timer = time.time()
	# _flag = True
	while not check_running(frame, application_bbox):
		# if frame.any() and _flag:
		# 	print(frame)
		# 	# img = Image.fromarray(frame)
		# 	# img.save('poo3.png')
		# 	flag = False
		application_bbox = prepare_app()
		frame = camera.get_latest_frame()

		if timeout > 0.0:
			assert time.time() - timer < timeout, f"Game has not been started for {timeout} seconds, exiting"


def main():
	""" Autoclicker impl """

	amount_of_games = 1
	if len(sys.argv) > 1:
		for arg in sys.argv:
			if arg.isnumeric():
				amount_of_games = int(arg)
				break

	camera = dxcam.create()
	camera.start(target_fps=60)

	frame = camera.get_latest_frame() # frame is an array with shape (y, x, 3)

	print(f'Limited clicks: {CLICK_LIMIT}')
	print('Trying to detect running game, click play')
	wait_running_game(camera)
	# time.sleep(2)

	x_shift = 20
	y_shift_top = 150
	y_shift_bot = 250

	game_counter = 0

	application_bbox = prepare_app()

	x_range = range(application_bbox[0] + x_shift, application_bbox[2] - x_shift, PIXELS_PER_ITERATION)
	y_range = range(application_bbox[1] + y_shift_top, application_bbox[3] - y_shift_bot, PIXELS_PER_ITERATION)

	while game_counter < amount_of_games:
		game_counter += 1
		print(f'Game {game_counter} detected!')
		frame = camera.get_latest_frame()

		__timer = datetime.datetime.now()

		while (datetime.datetime.now() - __timer).total_seconds() < AVG_GAME_DURATION or check_running(frame, application_bbox):

			for x in x_range:
				for y in y_range:
					if check_object(frame, x, y):
						mouse.move(x, y, absolute=True)
						mouse.click(button='left')

			time.sleep(0.28)
			frame = camera.get_latest_frame()
		else:
			print('Finished')

		if game_counter < amount_of_games:
			time.sleep(0.5)
			x = application_bbox[0] + int(NEW_GAME_TRIGGER_POS[0] * (application_bbox[2] - application_bbox[0]))
			y = application_bbox[1] + int(NEW_GAME_TRIGGER_POS[1] * (application_bbox[3] - application_bbox[1]))
			mouse.move(x, y, absolute=True)
			mouse.click(button='left')

			wait_running_game(camera, timeout = 12.5)

	camera.stop()

def increase_click_limit():
	global CLICK_LIMIT
	CLICK_LIMIT = min(1.0, CLICK_LIMIT + 0.01)
	print(f'Limit: {CLICK_LIMIT:.4}')


def decrease_click_limit():
	global CLICK_LIMIT
	CLICK_LIMIT = max(0.0, CLICK_LIMIT - 0.01)
	print(f'Limit: {CLICK_LIMIT:.4}')


if __name__ == "__main__":
	keyboard.add_hotkey('1', decrease_click_limit)
	keyboard.add_hotkey('2', increase_click_limit)

	if '--help' in sys.argv:
		print(HELP_STRING)
	else:
		main()
