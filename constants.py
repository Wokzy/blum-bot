import sys

"""On different devices app size is also different, 
	so i located triggers on mine and devided it by window size on my pc,
	in game this coefficients are multiplied by actual window size to get correct coordinates"""
CHRISTMAS_MODE = '--xmas' in sys.argv
HALLOWEEN_MODE = '--halloween' in sys.argv
ELECTIONS_MODE = '--elections' in sys.argv
FOOTBALL_MODE = '--football' in sys.argv
DOGS_DROP_TOGGLE = '--enable-dogs' in sys.argv

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
PIXELS_PER_ITERATION = 10 + 5*CHRISTMAS_MODE

NEW_GAME_TRIGGER_POS = (210/402, 615/712)
AVG_GAME_DURATION = 30 + 6*HALLOWEEN_MODE # seconds


#Dogs drop
DOGS_WHITE_COLOR_RANGE = (238, 256)

# X-mas update
CHRISTMAS_COLOR_TRIGGERS = [
					{
					"red":{"min":240, "max":255},
					"green":{"min":0, "max":15},
					"blue":{"min":120, "max":200}
					},
					{
					"red":{"min":130, "max":180},
					"green":{"min":50, "max":80},
					"blue":{"min":0, "max":20}
					},
					{
					"red":{"min":230, "max":240},
					"green":{"min":85, "max":160},
					"blue":{"min":70, "max":140}
					},
					{
					"red":{"min":90, "max":120},
					"green":{"min":35, "max":50},
					"blue":{"min":0, "max":5}
					}
					# ,
					# {
					# "red":{"min":250, "max":255},
					# "green":{"min":130, "max":150},
					# "blue":{"min":0, "max":5}
					# },
					# {
					# "red":{"min":50, "max":120},
					# "green":{"min":100, "max":210},
					# "blue":{"min":5, "max":40}
					# },
]

BOMB_COLOR_TRIGGER = {
					"red":{"min":240, "max":255},
					"green":{"min":170, "max":200},
					"blue":{"min":20, "max":80}
					}


HELP_STRING = \
"""
Usage: main.py [AMOUNT OF GAMES] [OPTIONS]

Options:
	--help           - show this string
	--xmas           - enable christmas mode
	--enable-dogs    - collect dogs
	--click-limit=n  - limit clicks (Example: --click-limit=0.05, only 5% of clicks)

Keybidings:
	1 - decrease clicks limit
	2 - increase clicks limit
"""
