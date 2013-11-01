# -*- coding: utf-8 -*-
# -*- Mode: Python; indent-tabs-mode: t; c-basic-offset: 4; tab-width: 4 -*- #

'''Constantes para las url base de la api de media fire'''

class BaseUrlMediaFire(object):

	GET_SESSION_TOKEN_USER = 'https://www.mediafire.com/api/user/get_session_token.php'

	RENEW_SESSION_TOKEN_USER = ('http://www.mediafire.com/api/user/'
		'renew_session_token.php')

	MYFILES_REVISION_USER = 'http://www.mediafire.com/api/user/myfiles_revision.php'

	#terminos de servicios he informacion de ellos
	FETCH_TOS_USER = 'http://www.mediafire.com/api/user/fetch_tos.php'

	# Accept the Terms of Service by sending the acceptance token retrieved
	#from the user/fetch_tos API
	ACCEPT_TOS_USER = 'http://www.mediafire.com/api/user/accept_tos.php'

	GET_INFO_USER = 'http://www.mediafire.com/api/user/get_info.php'

	#FILES
	DELETE_FILE = 'http://www.mediafire.com/api/file/delete.php'

	MOVE_FILE = 'http://www.mediafire.com/api/file/move.php'

	UPDATE_FILE = 'http://www.mediafire.com/api/file/update.php'

	UPDATE_PASSWORD_FILE = 'http://www.mediafire.com/api/file/update_password.php'

	UPDATE_FILE = 'http://www.mediafire.com/api/file/update_file.php'

	COPY_FILE = 'http://www.mediafire.com/api/file/copy.php'

	GET_LINKS_FILE = 'http://www.mediafire.com/api/file/get_links.php'

	ONE_TIME_DOWNLOAD_FILE = 'http://www.mediafire.com/api/file/one_time_download.php'

	CONFIGURE_ONE_TIME_DOWNLOAD_FILE = ('http://www.mediafire.com/api/file/'
		'configure_one_time_download.php')

	#folder
	GET_INFO_FOLDER = 'http://www.mediafire.com/api/folder/get_info.php'

	DELETE_FOLDER = 'http://www.mediafire.com/api/folder/delete.php'

	MOVE_FOLDER = 'http://www.mediafire.com/api/folder/move.php'

	CREATE_FOLDER = 'http://www.mediafire.com/api/folder/create.php'

	UPDATE_FOLDER = 'http://www.mediafire.com/api/folder/update.php'

	# Add shared folders to my account
	ATTACH_FOREIGN_FOLDER = 'http://www.mediafire.com/api/folder/attach_foreign.php'

	#Remove shared folders from my account
	DETACH_FOREIGN_FOLDER = 'http://www.mediafire.com/api/folder/detach_foreign.php'

	GET_REVISION_FOLDER = 'http://www.mediafire.com/api/folder/get_revision.php'

	GET_DEPTH_FOLDER = 'http://www.mediafire.com/api/folder/get_depth.php'

	#Returns the sibling folders
	GET_SIBLINGS_FOLDER = 'http://www.mediafire.com/api/folder/get_siblings.php'

	#Searches the content of the given folder. If the folder_key is not passed, the search will be
	#performed on the root folder (myfiles) and the session token will be required. To search the
	#root folder on other devices other than the cloud, pass the device_id. If the device_id is -1, 
	#then a global search on all devices will be performed.
	SEARCH_FOLDER = 'http://www.mediafire.com/api/folder/search.php'

	GET_CONTENT_FOLDER = 'http://www.mediafire.com/api/folder/get_content.php'

	#Checks if instant upload is possible and checks if a duplicate filename exists in the
	#destination folder. This returns a 'quickkey' on a successful instant upload, or 2 data values:
	#'new_hash' and 'duplicate_name' which can be 'yes' or 'no'. Based on those values, the
	#uploader performs a regular upload, or resends the same pre_upload request with 
	#the desired action
	PRE_UPLOAD = 'http://www.mediafire.com/api/upload/pre_upload.php'

	UPLOAD = 'http://www.mediafire.com/api/upload/upload.php'

	#complete uploade
	POLL_UPLOAD = 'http://www.mediafire.com/api/upload/poll_upload.php'

	DIRECT_DOWNLOAD_LINK = 'http://www.mediafire.com/api/file/get_links.php'
	GET_VERSION = 'http://www.mediafire.com/api/system/get_version.php'
	GET_INFO_SYSTEM = 'http://www.mediafire.com/api/system/get_info.php'
	GET_SUPPORTED_MEDIA = ('http://www.mediafire.com/api/system/'
		'get_supported_media.php')
	GET_EDITABLE_MEDIA = 'http://www.mediafire.com/api/system/get_editable_media.php'
	GET_MIME_TYPES = 'http://www.mediafire.com/api/system/get_mime_types.php'
