# -*- coding: utf-8 -*-
# -*- Mode: Python; indent-tabs-mode: t; c-basic-offset: 4; tab-width: 4 -*- #
import sys
import hashlib
from urllib.request import urlopen
import urllib.parse
import json

class WapperUrl(object):
	def get_json_mediafire(self, url, dic_param = {} ):
		dic_param['response_format'] = 'json'
		post = urllib.parse.urlencode(dic_param)
		post_binary = post.encode('UTF-8')
		try: response = urllib.request.urlopen(url, post_binary)
		except urllib.error.URLError as e:
			print(e)
			return json.loads('{"result":"Error"}')
		json_response = response.readall().decode('UTF-8')
		try: json_response = json.loads(json_response)['response']
		except ValueError:
			sys.stderr.write('Decoding JSON has failed in url \n\t' + url + '\n\n')
			return json.loads('{"result":"Error"}')
		return json_response