# -*- coding: utf-8 -*-
# -*- Mode: Python; indent-tabs-mode: t; c-basic-offset: 4; tab-width: 4 -*- #
import re
from py3mediafire.BaseUrlMediaFire import BaseUrlMediaFire
from py3mediafire.WapperUrl import WapperUrl

class UserOperation(WapperUrl):
	"""Handler user operation
		Keyword arguments:
		ref_session -- reference to a class SessionHandler
	"""
	def __init__(self,ref_session):
		self.__session_token = ref_session
		self.accept_terms_service()


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

	def myfiles_revision(self):
		"""Returns a fraction number indicating the global revision of myfiles. The revision
		is in the x.y format. 'x' is the folders-only revision. 'y' is the folders-and-files
		revision. When the revision resets to 1.0, the time stamp 'epoch' is updated so
		both 'revision' and 'epoch' can be used to identify a unique revision
		"""
		return self.get_json_mediafire(BaseUrlMediaFire.MYFILES_REVISION_USER,
			{'session_token': self.__session_token.get_token(),
			'version': self.__session_token.get_version_actual()})

	def get_text_terms_service(self,html=True):
		"""Returns the HTML format of the MediaFire Terms of Service and its revision,
		date, whether the user has accepted it or not, and the acceptance token if the
		user has not accepted the latest terms

		Keyword arguments:
			html -- return html tag(defaul True)

		Return text of terms of service
		"""
		js = self.get_json_mediafire(BaseUrlMediaFire.FETCH_TOS_USER,
			{'session_token': self.__session_token.get_token(),
			'version': self.__session_token.get_version_actual()})
		terms = js['terms_of_service']['terms']
		if(not html):
			return re.sub('<.*?>','',terms)
		return terms

	def accept_terms_service(self):
		js = self.get_json_mediafire(BaseUrlMediaFire.FETCH_TOS_USER,
			{'session_token': self.__session_token.get_token(),
			'version': self.__session_token.get_version_actual()})
		token_accept = js['terms_of_service']['acceptance_token']
		result = self.get_json_mediafire(BaseUrlMediaFire.ACCEPT_TOS_USER,
			{'session_token': self.__session_token.get_token(),
			'acceptance_token' : token_accept,
			'version': self.__session_token.get_version_actual()})
		if not __debug__:
			print(' terms service ' + result['result'] +
				' in UserOperation::accept_terms_service')

	def set_register(self,ref_session):
		"""Set actual user mediafire
		Keyword arguments:
			ref_session : reference class SessionHandler
		"""
		self.__session_token = ref_session
