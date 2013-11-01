# -*- coding: utf-8 -*-
# -*- Mode: Python; indent-tabs-mode: t; c-basic-offset: 4; tab-width: 4 -*- #
import hashlib
from urllib.request import urlopen
import urllib.parse
import json
from py3mediafire.BaseUrlMediaFire import BaseUrlMediaFire

class SessionHandler(object):
	
	def __init__(self, email, password, application_id, version = 1):
		self.__email = email
		self.__password = password
		self.__application_id = application_id
		self.__version = version
		self.__get_version_actual()

	def __get_version_actual(self):
		post = urllib.parse.urlencode({'response_format': 'json'})
		post_binary = post.encode('UTF-8')
		try: response = urllib.request.urlopen(BaseUrlMediaFire.GET_VERSION, post_binary)
		except urllib.error.URLError as e:
			print(e)
		json_response = response.readall().decode('UTF-8')
		js2 = json.loads(json_response)['response']
		print(js2['current_api_version'])