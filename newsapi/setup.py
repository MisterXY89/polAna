
#!/usr/bin/env python

import json
import urllib.request
from datetime import datetime
from collections import namedtuple

class ApiSetup:
	def __init__(self):
		self.key = "8ca0121aca8a48c8b0636633d5306edc"
		self.base = "https://newsapi.org/v2/"
		# self.everything_url = self.url_builder("everything")

	def buildEverythingUrl(self, args):
		url = "everything"
		if "q" in args:
			urlQ = args['q'].replace(" ", "%20")
			url += f"?q={urlQ}"
		if "sortby" in args:
			url += f"&sortby={args['sortBy']}"
		if "from" in args:
			url += f"&from={args['from']}"
		return url

	def url_builder(self, string):
		return f"{self.base}{string}&apiKey={self.key}"

	def _log(self, content):
		time = datetime.now().strftime('%H:%M:%S %d-%m-%Y')
		print("[%s] %s" %(time,content))
		

	def read(self, reqUrl):
		self._log(f"New Api request: {reqUrl}")
		with urllib.request.urlopen(reqUrl) as url:
			data = self.json_to_obj(url.read().decode())
			if data.status == "ok":
				return data
			return False


	# https://stackoverflow.com/a/15882054
	def _json_object_hook(self, d): 
		return namedtuple('X', d.keys(),rename=True)(*d.values())
	def json_to_obj(self, data): 
		return json.loads(data, object_hook=self._json_object_hook)
