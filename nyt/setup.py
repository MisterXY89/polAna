#!/usr/bin/env python

import json
import urllib.request
from datetime import datetime
from collections import namedtuple

class ApiSetup:
	def __init__(self):
		self.key = "FgkrI4j0E3bUIAtuEyFRYoFyNvyFr042"
		self.secret = "jNWIHPSNyEzhAcmk"
		self.base = "https://api.nytimes.com/svc"
		self.top_url = self.url_builder("/topstories/v2/home.json")

	def url_builder(self, string):
		return f"{self.base}{string}?api-key={self.key}"

	def _log(self, content):
		time = datetime.now().strftime('%H:%M:%S %d-%m-%Y')
		print("[%s] %s" %(time,content))

	def build_shared_with_period(self, period):
		allowed_days = [1,7,30]
		if not period in allowed_days:
			self._log(f"The allowed values for the PERIOD parameter are: {allowed_days}")
			return False
		return self.url_builder(f"/mostpopular/v2/shared/{period}.json")
		

	def read(self, reqUrl):
		self._log(f"New Api request: {reqUrl}")
		with urllib.request.urlopen(reqUrl) as url:
			data = self.json_to_obj(url.read().decode())
			self._log(f"Request status: {data.status}")
			if data.status == "OK":
				self._log(f"Fetched {data.num_results} results from the NYT")
				# might not be set (for period calls)
				# self._log(f"The last data update was: {data.last_updated}")			
				return data.results
			else:
				return False


	# https://stackoverflow.com/a/15882054
	def _json_object_hook(self, d): 
		return namedtuple('X', d.keys(),rename=True)(*d.values())
	def json_to_obj(self, data): 
		return json.loads(data, object_hook=self._json_object_hook)


class AppSetup():
	def __init__(self):
		self.id = "0e66fc01-eb6f-4e0a-9480-647372abc5d5"
		self.name = "AnalysePolitischerEffekteDigitalerMedien"
		self.author = "Tilman Kerl"
		self.description = "App for the seminar: Analyse Politischer Effekte Digitaler Medien"
		self.profile_mail = "tilman.kerl@uni-konstanz.de"
