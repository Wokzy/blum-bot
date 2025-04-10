import sys

"""On different devices app size is also different, 
	so i located triggers on mine and devided it by window size on my pc,
	in game this coefficients are multiplied by actual window size to get correct coordinates"""
TGE_MODE = '--tge' in sys.argv
DOGS_DROP_TOGGLE = '--enable-dogs' in sys.argv

CLICK_LIMIT = 1.0
for arg in sys.argv:
	if '--click-limit' in arg:
		CLICK_LIMIT = float(arg.split('=')[1])


DEV_SCREEN_SIZE_CONST = (402, 712)

APPLICATION_NAME = 'Blum'
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

# TGE update

TGE_COLOR_TRIGGERS = [
	{
	"red":{"min":220, "max":255},
	"green":{"min":240, "max":255},
	"blue":{"min":90, "max":140}
	},
	{
	"red":{"min":110, "max":255},
	"green":{"min":0, "max":5},
	"blue":{"min":110, "max":255}
	}
]


HELP_STRING = \
"""
Usage: main.py [AMOUNT OF GAMES] [OPTIONS]

Options:
	--help           - show this string
	--tge            - enable \"TGE\" mode
	--enable-dogs    - collect dogs
	--click-limit=n  - limit clicks (Example: --click-limit=0.05, only 5% of clicks)

Keybidings:
	1 - decrease clicks limit
	2 - increase clicks limit
"""
