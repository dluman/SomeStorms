# usr/bin/python
# -- coding: utf-8 --
import curses, random, string, time, weather, yaml

def getForecast(param):
	forecast = weather.getForecast(param)
	return forecast

def getColors(degrees):
	if degrees <= 40: return 1
	elif degrees <= 50: return 2
	elif degrees <= 80: return 3
	else: return 4

def getTempAvg(temperature):
	return round(sum(temperature)/float(len(temperature)),2)

def getRainfallAvg(rainfall):
	return round(sum(rainfall),2)

def getLightning(w0,h0,window,x,y):
	element = "LIGHTNING"
	h,w = h0,w0
	for letter in element:
		if h > y: break
		if w > x: break
		window.addstr(h,w,letter,curses.A_BLINK)
		h,w = h+1,w+1

def screen(window):
	window.clear()
	curses.start_color()
	curses.use_default_colors()
	curses.curs_set(0)

	screen_y, screen_x = window.getmaxyx()
	#CREATE INITIAL SCREEN
	for i in range(int(screen_y/2)):
		window.addstr('\n')
	window.addstr('SOME STORMS'.center(int(screen_x),' '))
	window.addstr('FOR bpNichol'.center(int(screen_x),' '))
	window.addstr(' '.center(int(screen_x),' '))
	window.addstr('In 1984, poet bpNichol released one of the first widely-distributed "computer poems," entitled "First Screening."'.center(int(screen_x),' '))
	window.addstr('These concrete poems, influenced by other such as Apollinaire\'s "Il Pleut" could not have anticipated the on-coming'.center(int(screen_x),' '))
	window.addstr('age of big data. This poem leverages weather data for the zip code 22030 for the first 11 months of 2016. Rain and snow'.center(int(screen_x),' '))
	window.addstr('accumulates on the screen in direct proportion to the amount of rain/snowfall recieved on the day indicated in the upper left'.center(int(screen_x),' '))
	window.addstr('on the statistical readout.'.center(int(screen_x),' '))
	window.refresh()
	window.getkey()
	window.clear()
	#SET CONSTANTS
	drops = 0
	rain = 'rain'
	snow = 'snow'
	rainfall = []
	temperature = []
	#SET COLOR PAIRS
	curses.init_pair(1,curses.COLOR_BLUE,curses.COLOR_BLACK)
	curses.init_pair(2,curses.COLOR_CYAN,curses.COLOR_BLACK)
	curses.init_pair(3,curses.COLOR_YELLOW,curses.COLOR_BLACK)
	curses.init_pair(4,curses.COLOR_RED,curses.COLOR_BLACK)
	curses.init_pair(5,curses.COLOR_WHITE,curses.COLOR_WHITE)
	curses.init_pair(6,curses.COLOR_WHITE,curses.COLOR_YELLOW)
	#GET DATA
	precip = [precip for precip in getForecast('precip')]
	date = [date for date in getForecast('date')]
	event = [event for event in getForecast('events')]
	cover = [cover for cover in getForecast('cloud')]
	mean = [mean for mean in getForecast('mean')]
	#CREATE PRECIPITATION SCREENS
	for r in xrange(len(precip)):
		window.clear()
		try:
			if float(precip[r]) > 0: rainfall.append(float(precip[r]))
		except: pass
		temperature.append(float(mean[r]))
		if precip[r] != "T": window.addstr(0,0,'%s: %s (%s in.), %sF [Annual Avg.: %sF]' % (date[r],event[r],precip[r],mean[r],getTempAvg(temperature)))
		else: window.addstr(0,0,'%s: %s (0.0 in.), %sF [Annuak Avg.: %sF]' % (date[r],event[r],mean[r],getTempAvg(temperature)))
		window.addstr(1,0,'Annual Precip.: %s in.' % getRainfallAvg(rainfall))
		time.sleep(1)
		window.refresh()
		try: float(precip[r])
		except: continue
		if float(precip[r]) == 0.0:
			continue
		try:
			if "Fog" in event[r]:
				for x in range(0,int(screen_x)):
					for y in range(0,int(screen_y)):
						try: window.addstr(y,x,'-',curses.color_pair(5))
						except: pass
						window.refresh()
		except: pass
		window.refresh()
		for y in xrange(0,int(100*precip[r])):
			if precip[r] > 1: delay = 1 - (1/float(precip[r]))
			elif precip[r] < 1: delay = 1-float(precip[r])
			else: delay = .5
			try: time.sleep(delay)
			except: time.sleep(.5)
			if event[r] == "Snow" or event[r] == "Fog-Snow":
				window.addstr(random.randrange(int(screen_y)),
                                              random.randrange(int(screen_x)),snow[drops])
			elif event[r] == "Rain-Snow":
				window.addstr(random.randrange(int(screen_y)),
                                              random.randrange(int(screen_x)),snow[drops])
				window.refresh()
				window.addstr(random.randrange(int(screen_y)),random.randrange(int(screen_x)),
                                              rain[drops],curses.color_pair(getColors(mean[r])))
			elif event[r] == "Rain" or event[r] == "Fog-Rain":
				window.addstr(random.randrange(int(screen_y)),random.randrange(int(screen_x)),
                                              rain[drops],curses.color_pair(getColors(mean[r])))
			elif event[r] == "Rain-Thunderstorm":
				window.addstr(random.randrange(int(screen_y)),random.randrange(int(screen_x)),
					      rain[drops],curses.color_pair(getColors(mean[r])))
				w0,h0 = random.randrange(int(screen_x)), random.randrange(int(screen_y))
				try:
					if random.randrange(10) >= 6:
						getLightning(w0,h0,window,screen_x,screen_y)
				except: pass
			window.refresh()
			drops += 1
			if drops > 3:
				drops = 0
		window.refresh()
	window.getkey()
	window.clear()
	for i in range(int(screen_y/2)):
                window.addstr('\n')
        window.addstr(('%s DAYS OF RAIN' % (str(len(rainfall)))).center(int(screen_x),' '))
        window.addstr(('%s INCHES OF RAINFALL' % (str(sum(rainfall)))).center(int(screen_x),' '))
	window.addstr(('%s AVERAGE TEMPERATURE' % (getTempAvg(temperature))).center(int(screen_x),' '))
	window.refresh()
	window.getkey()

if __name__ == '__main__':
	curses.wrapper(screen)
