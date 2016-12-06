import yaml

class Forecast:

	def __init__(self,data):
		self.date = data['EST']
		self.high = data['Max TemperatureF']
		self.mean = data['Mean TemperatureF']
		self.low = data['Min TemperatureF']
		self.maxdew = data['Max Dew PointF']
		self.meandew = data['MeanDew PointF']
		self.mindew = data['Min DewpointF']
		self.maxhum = data['Max Humidity']
		self.meanhum = data['Mean Humidity']
		self.minhum = data['Min Humidity']
		self.maxsea = data['Max Sea Level PressureIn']
		self.meansea = data['Mean Sea Level PressureIn']
		self.minsea = data['Min Sea Level PressureIn']
		self.maxvis = data['Max VisibilityMiles']
		self.meanvis = data['Mean VisibilityMiles']
		self.minvis = data['Min VisibilityMiles']
		self.maxwind = data['Max Wind SpeedMPH']
		self.meanwind = data['Mean Wind SpeedMPH']
		self.gust = data['Max Gust SpeedMPH']
		self.precip = data['PrecipitationIn']
		self.cloud = data['CloudCover']
		self.events = data['Events']
		self.winddir = data['WindDirDegrees']

def getForecast(param):
	with open('yaml/weather.yaml','r') as climate:
		weather = yaml.load(climate)
		for data in weather:
			yield getattr(Forecast(data),param)

"""
DATA FORMAT

EST: 1985-11-1
Max TemperatureF: 61
Mean TemperatureF: 52
Min TemperatureF: 42
Max Dew PointF: 42
MeanDew PointF: 35
Min DewpointF: 24
Max Humidity: 79
Mean Humidity: 55
Min Humidity: 24
Max Sea Level PressureIn: 30.15
Mean Sea Level PressureIn: 30.07
Min Sea Level PressureIn: 29.99
Max VisibilityMiles: 20
Mean VisibilityMiles: 14
Min VisibilityMiles: 10
Max Wind SpeedMPH: 17
Mean Wind SpeedMPH: 13
Max Gust SpeedMPH:
PrecipitationIn: 0.00
CloudCover: 4
Events:
WindDirDegrees: 51
"""
