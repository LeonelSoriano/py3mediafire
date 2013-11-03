# -*- coding: utf-8 -*-
# -*- Mode: Python; indent-tabs-mode: t; c-basic-offset: 4; tab-width: 4 -*- #
from py3mediafire.BaseUrlMediaFire import BaseUrlMediaFire
from py3mediafire.WapperUrl import WapperUrl

class UserOperation(WapperUrl):
	"""Handler user operation
		Keyword arguments:
		ref_session -- reference to a class SessionHandler
	"""
	def __init__(self,ref_session):
		self.__session_token = ref_session
		s = self.get_info()
		self.set_info({})

	def get_info(self):
		js = self.get_json_mediafire(BaseUrlMediaFire.GET_INFO_USER,
			{'session_token': self.__session_token.get_token(),
			'version': self.__session_token.get_version_actual()})
		return js['user_info']

	def set_info(self, option):
		"""Update the user's personal information

		Keyword arguments:
		option -- {}
			Options:
			display_name : The user's Display Name
			first_name : The user's First Name
			last_name : The user's Last Name
			birth_date : The user's Birth Date. It should take the format (yyyy-mm-dd)
			gender : The user's Gender ('male', 'female' or 'none')
			website : The user's Website URL
			location : The user's Address Location
			newsletter : whether to receive MediaFire site news via email ('yes' or 'no')
			primary_usage : The user's Primary Usage of this MediaFire account ('home',
					'work', 'school', or 'none')
		"""
		option['session_token'] = self.__session_token.get_token()
		option['version'] = self.__session_token.get_version_actual()
		self.get_json_mediafire(BaseUrlMediaFire.SET_INFO_USER,option)
