import sys

"""On different devices app size is also different, 
	so i located triggers on mine and devided it by window size on my pc,
	in game this coefficients are multiplied by actual window size to get correct coordinates"""
HALLOWEEN_MODE = '--halloween' in sys.argv
ELECTIONS_MODE = '--elections' in sys.argv
FOOTBALL_MODE = '--football' in sys.argv
DOGS_DROP_TOGGLE = '--disable-dogs' not in sys.argv

CLICK_LIMIT = 1.0
for arg in sys.argv:
	if '--click-limit' in arg:
		CLICK_LIMIT = float(arg.split('=')[1])


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
AVG_GAME_DURATION = 30 + 6*HALLOWEEN_MODE # seconds


#Dogs drop
DOGS_WHITE_COLOR_RANGE = (238, 256)

# Halloween
HALLOWEEN_COLOR_TRIGGER = {
					"red":{"min":220, "max":240},
					"green":{"min":95, "max":130},
					"blue":{"min":35, "max":55}}
BOMB_COLOR_TRIGGER = {
					"red":{"min":125, "max":140},
					"green":{"min":125, "max":135},
					"blue":{"min":125, "max":135}}

#Election
ELECTIONS_COLOR_TRIGGERS = [
					{
					"red":{"min":250, "max":255},
					"green":{"min":130, "max":140},
					"blue":{"min":90, "max":105}
					},
					{
					"red":{"min":220, "max":230},
					"green":{"min":160, "max":175},
					"blue":{"min":125, "max":135}
					}
]


HELP_STRING = \
"""
Usage: main.py [AMOUNT OF GAMES] [OPTIONS]

Options:
	--help           - show this string
	--halloween      - enable halloween mode
	--football      - enable football mode
	--elections      - enable elections mode
	--disable-dogs   - don't collect dogs
	--click-limit=n  - limit clicks (Example: --click-limit=0.05, only 5% of clicks)

Keybidings:
	1 - decrease clicks limit
	2 - increase clicks limit
"""
