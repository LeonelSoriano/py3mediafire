# -*- coding: utf-8 -*-
# -*- Mode: Python; indent-tabs-mode: t; c-basic-offset: 4; tab-width: 4 -*- #
import time
import hashlib
from urllib.request import urlopen
import urllib.parse
import json
from py3mediafire.BaseUrlMediaFire import BaseUrlMediaFire
from py3mediafire.WapperUrl import WapperUrl

class SessionHandler(WapperUrl):

	def __init__(self, email, password, application_id, api_key):
		self.__email = email
		self.__password = password
		self.__application_id = application_id
		self.__version = self.__get_version_actual()
		self.__api_key = api_key
		self.signature = self.__email + self.__password + self.__application_id + api_key
		self.sha1_encode = hashlib.sha1(self.signature.encode()).hexdigest()
		self.expires_session = 0
		self.session_token = self.__user_getSessionToken()

	def __user_getSessionToken(self):
		js = self.get_json_mediafire(BaseUrlMediaFire.GET_SESSION_TOKEN_USER,
			{'email': self.__email, 'password': self.__password, 'application_id': self.__application_id,
			'signature': self.sha1_encode, 'version': self.__version})
		self.expires_session = int(time.time())
		return 1 if js['result'] == 'Error' else js['session_token']

	def __user_renew_session_token(self):
		js = self.get_json_mediafire(BaseUrlMediaFire.RENEW_SESSION_TOKEN_USER,
			{'session_token': self.session_token,  'version': self.__version})
		self.expires_session = int(time.time())
		return 1 if js['result'] == 'Error' else js['session_token']

	def user_get_login_token(self):
		js = self.get_json_mediafire(BaseUrlMediaFire.GET_LOGIN_TOKEN_USER,
			{'email': self.__email, 'password': self.__password, 'application_id': self.__application_id,
			'signature': self.sha1_encode,  'version': self.__version})
		return 1 if js['result'] == 'Error' else js['session_token']

	def __get_version_actual(self):
		js = self.get_json_mediafire(BaseUrlMediaFire.GET_VERSION)
		return 1 if js['result'] == 'Error' else js['current_api_version']

