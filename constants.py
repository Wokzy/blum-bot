import sys

"""On different devices app size is also different, 
	so i located triggers on mine and devided it by window size on my pc,
	in game this coefficients are multiplied by actual window size to get correct coordinates"""
DEV_SCREEN_SIZE_CONST = (402, 712)

APPLICATION_NAME = 'TelegramDesktop'
DEFAULT_COLOR_TRIGGER = {
					"red":{"min":90, "max":255},
					"green":{"min":220, "max":255},
					"blue":{"min":5, "max":55}}
APPLICATION_TRIGGER = {"color":(234, 212, 12), "positions":[(60/402, 112/712), (43/402, 110/712), 
															(102/402, 113/712), (61/402, 106/712)]}
PIXELS_PER_ITERATION = 10

NEW_GAME_TRIGGER_POS = (210/402, 615/712)
AVG_GAME_DURATION = 30 # seconds


#Dogs drop
DOGS_WHITE_COLOR_RANGE = (238, 256)
DOGS_DROP_TOGGLE = '--disable-dogs' not in sys.argv

# Halloween
HALLOWEEN_MODE = '--halloween' in sys.argv
HALLOWEEN_COLOR_TRIGGER = {
					"red":{"min":220, "max":240},
					"green":{"min":95, "max":130},
					"blue":{"min":35, "max":55}}
BOMB_COLOR_TRIGGER = {
					"red":{"min":125, "max":140},
					"green":{"min":125, "max":135},
					"blue":{"min":125, "max":135}}
