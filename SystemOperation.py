# -*- coding: utf-8 -*-
# -*- Mode: Python; indent-tabs-mode: t; c-basic-offset: 4; tab-width: 4 -*- #
from py3mediafire.WapperUrl import WapperUrl
from py3mediafire.BaseUrlMediaFire import BaseUrlMediaFire

class SystemOperation(WapperUrl):
	def __init__(self,ref_session):
		self.__session_token = ref_session
		#folder key mq10rijd8mora
		#reps = self.search('prueba',{})
		#for a in range(len(reps)):
		#	print(reps[a])
		#	print('--------------------------------------------------------')
		#self.get_info_file('heeev7tem9jt87w')
		#09kt0xm7qvo673b


	def get_content(self):
		js = self.get_json_mediafire(BaseUrlMediaFire.GET_CONTENT_FOLDER,
		{'session_token': self.__session_token.get_token(),
			'version': self.__session_token.get_version_actual()})
		return js

	def ls_in_root(self,filter_result = ''):
		"""
		Option for filter_result:
			files,folders,private,public,image,video,document,audio,spreadsheet,
			presentation,application,archive,data,development
		"""
		js = self.get_json_mediafire(BaseUrlMediaFire.SEARCH_FOLDER ,
		{'session_token': self.__session_token.get_token(),
			'filter' : filter_result,
			'search_text' : ' ',
			'search_all' : 'no',
			'version': self.__session_token.get_version_actual()})
		return js['results']

	def ls_in_folder(self,folder_key,filter_result = ''):
		"""
		Option for filter_result:
			files,folders,private,public,image,video,document,audio,spreadsheet,
			presentation,application,archive,data,development
		"""
		js = self.get_json_mediafire(BaseUrlMediaFire.SEARCH_FOLDER ,
		{'folder_key': folder_key,
			'filter' : filter_result,
			'search_text' : ' ',
			'search_all' : 'no',
			'version': self.__session_token.get_version_actual()})
		return js['results']

	def search(self, search_text, option = {}, folder_key = None):
		"""Searches the content of the given folder. If the folder_key is not passed,
		the search will be performed on the root folder (myfiles) and the session token
		will be required. To search the root folder on other devices other than the cloud,
		pass the device_id. If the device_id is -1, then a global search on all devices will
		be performed

		Keyword arguments:
			search_text -- the keywords to search for in filenames, folder names, descriptions and tags(defaul True)
			option -- {} (defaul {})
				filter : filter by privacy and/or by filetype. This is a comma-separated list
					of file types and privacy option. Can take one or more of the following
					values : "public", "private", "image", "video","audio", "document",
					"spreadsheet","presentation", "application", "archive", "data",
						folders,files, and "development"
				device_id :  Specify which device to return the myfiles data from. If not set,
					it defaults to the cloud. if it's set to -1, then search will be performed
					on all devices.
				search_all : 'yes' or 'no'. If folder_key is passed, then this parameter is
					ignored. If folder_key is not passed, search_all can be used to indicate
					whether to search the root folder only or the entire device (default 'yes').
			folder_key -- The key that identifies the folder. If the folder_key is not passed,
				the session token is required and 'search' API will return the root folder
				content. If the folder_key is passed and search_all is set to 'yes,'
				the entire device will be searched. 

		Return json results
		"""
		option['search_text'] = search_text
		option['version'] = self.__session_token.get_version_actual()
		if(folder_key == None):
			option['session_token'] = self.__session_token.get_token()
		else:
			option['folder_key'] = folder_key
		js = self.get_json_mediafire(BaseUrlMediaFire.SEARCH_FOLDER ,option)
		return js['results']

	def get_info_file(self, quick_key):
		option = {}
		option['quick_key'] = quick_key
		option['session_token'] = self.__session_token.get_token()
		option['version'] = self.__session_token.get_version_actual()
		js = self.get_json_mediafire(BaseUrlMediaFire.GET_INFO_FILE,option)
		if(js.get('result') == 'Error' and  not __debug__):
			print('Error in SystemOperation:get_info_file')
		return js['file_info']

	def delete_file(self, quick_key):
		js = self.get_json_mediafire(BaseUrlMediaFire.DELETE_FILE,
			{'session_token': self.__session_token.get_token(),
			'quick_key': quick_key,
			'version': self.__session_token.get_version_actual()})
		if (not __debug__):
			print(js)

	def move_file(self, quick_key, folder_key = None):
		option = {}
		option['session_token'] = self.__session_token.get_token()
		option['quick_key'] = quick_key
		if(folder_key is not None):
			option['folder_key'] = folder_key
		option['version'] = self.__session_token.get_version_actual()
		js = self.get_json_mediafire(BaseUrlMediaFire.MOVE_FILE, option)
		if (not __debug__):
			print(js)

	def update_file(self, quick_key):
		pass
