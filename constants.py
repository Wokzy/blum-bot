

"""On different devices app size is also different, 
	so i located triggers on mine and devided it by window size on my pc,
	in game this coefficients are multiplied by actual window size to get correct coordinates"""
DEV_SCREEN_SIZE_CONST = (402, 712)

APPLICATION_NAME = 'TelegramDesktop'
COLOR_TRIGGERS = {
					"red":{"min":90, "max":255},
					"green":{"min":220, "max":255},
					"blue":{"min":5, "max":55}}
APPLICATION_TRIGGER = {"color":(234, 212, 12), "positions":[(60/402, 112/712), (43/402, 110/712), 
															(102/402, 113/712), (61/402, 106/712)]}
PIXELS_PER_ITERATION = 10

NEW_GAME_TRIGGER_POS = (210/402, 615/712)
AVG_GAME_DURATION = 30 # seconds
