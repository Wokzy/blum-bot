
"""
Autoclicker for Blum drop mini-game
"""

import sys
import time
import dxcam
import mouse
import datetime

from prepare_app import prepare_app
from constants import (
	APPLICATION_TRIGGER,
	COLOR_TRIGGERS,
	PIXELS_PER_ITERATION,
	NEW_GAME_TRIGGER_POS,
	AVG_GAME_DURATION,
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

	return False


def check_object(pixel:tuple[int]) -> bool:
	""" Finding dropping objects by color """
	if COLOR_TRIGGERS['red']['min'] <= pixel[0] <= COLOR_TRIGGERS['red']['max']:
		if COLOR_TRIGGERS['green']['min'] <= pixel[1] <= COLOR_TRIGGERS['green']['max']:
			# print(pixel)
			if COLOR_TRIGGERS['blue']['min'] <= pixel[2] <= COLOR_TRIGGERS['blue']['max']:
				return True

	return False


def wait_running_game(camera, timeout:float = .0) -> None:
	application_bbox = prepare_app()
	frame = camera.get_latest_frame()
	timer = time.time()
	while not check_running(frame, application_bbox):
		application_bbox = prepare_app()
		frame = camera.get_latest_frame()

		if timeout > 0.0:
			assert time.time() - timer < timeout, f"Game has not been started for {timeout} seconds, exiting"


def main():
	""" Autoclicker impl """

	amount_of_games = 1
	if len(sys.argv) > 1:
		amount_of_games = int(sys.argv[1])

	camera = dxcam.create()
	camera.start(target_fps=60)

	frame = camera.get_latest_frame() # frame is an array with shape (y, x, 3)

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

		while check_running(frame, application_bbox) or (datetime.datetime.now() - __timer).total_seconds() < AVG_GAME_DURATION:

			for x in x_range:
				for y in y_range:
					if check_object(frame[y][x]):
						mouse.move(x, y, absolute=True)
						mouse.click(button='left')

			frame = camera.get_latest_frame()
		else:
			print('Finished')

		if game_counter < amount_of_games:
			time.sleep(0.5)
			x = application_bbox[0] + int(NEW_GAME_TRIGGER_POS[0] * (application_bbox[2] - application_bbox[0]))
			y = application_bbox[1] + int(NEW_GAME_TRIGGER_POS[1] * (application_bbox[3] - application_bbox[1]))
			mouse.move(x, y, absolute=True)
			mouse.click(button='left')

			wait_running_game(camera, timeout = 5.5)

	camera.stop()

if __name__ == "__main__":
	main()
