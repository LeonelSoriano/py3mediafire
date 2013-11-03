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
	"""Handler session user operation"""
	def __init__(self, email, password, application_id, api_key):
		self.__email = email
		self.__password = password
		self.__application_id = application_id
		self.__version = 0
		self.__api_key = api_key
		self.__signature = self.__email + self.__password + self.__application_id + api_key
		self.__sha1_encode = hashlib.sha1(self.__signature.encode()).hexdigest()
		self.__expires_session = 0
		self.__session_token = self.__user_get_session_token()


	def __user_get_session_token(self):
		"""Consige un token de session por 10 minutos si hay algun error devuelve un 1."""
		js = self.get_json_mediafire(BaseUrlMediaFire.GET_SESSION_TOKEN_USER,
			{'email': self.__email, 'password': self.__password, 'application_id': self.__application_id,
			'signature': self.__sha1_encode, 'version': self.get_version_actual()})
		self.__expires_session = int(time.time())
		return 1 if js['result'] == 'Error' else js['session_token']

	def __user_renew_session_token(self):
		"""Extends the life of the session token by another 10 minutes. If the session token is less 
			than 5 minutes old, then it does not get renewed and the same token is returned. If the 
			token is more than 5 minutes old, then, depending on the application configuration, the
			token gets extended or a new token is generated and returned.
		"""
		js = self.get_json_mediafire(BaseUrlMediaFire.RENEW_SESSION_TOKEN_USER,
			{'session_token': self.__session_token,  'version': self.__version})
		self.__expires_session = int(time.time())
		return 1 if js['result'] == 'Error' else js['session_token']

	def user_get_login_token(self):
		"""Generates a 60-second Login Token to be used by the developer to login a user
			directly to their account.
		"""
		js = self.get_json_mediafire(BaseUrlMediaFire.GET_LOGIN_TOKEN_USER,
			{'email': self.__email, 'password': self.__password, 'application_id': self.__application_id,
			'signature': self.__sha1_encode,  'version': self.__version})
		return 1 if js['result'] == 'Error' else js['session_token']

	def get_token(self):
		"""Public metoh for get token session 
			Return token session.
		"""
		actual_time = int(time.time())
		if(actual_time < self.__expires_session + 60 * 5):
			return self.__session_token
		elif(actual_time >= self.__expires_session + 60 * 5 or
			actual_time < self.__expires_session + 60 * 10):
			self.session_token = self.__user_renew_session_token()
			return self.session_token
		elif(actual_time >= self.__expires_session + 60 * 10):
			self.session_token = __user_get_session_token
			return self.session_token

	def get_version_actual(self):
		"""Get actual version api
			Return version actual.
		"""
		if(self.__version == 0):
			js = self.get_json_mediafire(BaseUrlMediaFire.GET_VERSION)
			return 1 if js['result'] == 'Error' else js['current_api_version']
		else:
			return self.__version

