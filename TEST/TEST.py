import sys
from py3mediafire.SessionHandler import SessionHandler
from py3mediafire.SystemOperation import SystemOperation
from py3mediafire.UserOperation import UserOperation


def main(argv=None):
	session = SessionHandler( 'XXXXXX@XXX','PASSWORD','application_id','api_key')

	user_op =  UserOperation(session) #you need pass session for a count media fire
	system_op = SystemOperation(session)  #you need pass session for a count media fire

	#print(system_op.search('ramon'))
	folder_info = system_op.perfect_search_folder('ramon')
	#if not exist result is {'result': 'different'}
	if(not folder_info.get('result')):
		print(folder_info['folderkey'])


	file_info = system_op.perfect_search_file('XXX.XX')
	#if not exist result is {'result': 'different'}
	if(not file_info.get('result')):
		#remove this file
		system_op.delete_file(file_info['quick_key'])

	#upload file   file name and option of mediafire api
	upload_result = system_op.upload('XXX.XX',{'action_on_duplicate': 'skip'})
	print(upload_result)

	#get quick_key file ; new_name is without extension file
	file_download = system_op.perfect_search_file('XXX.XX')
	if(not file_download.get('result')):
		download = system_op.download(file_download['quick_key'],new_name = 'example',pah = '/XXX/XXX/')
		print(down_load)
	else:
		print('file no found')

	#create folder mediafire
	print(system_op.create_folder('new_folder'))

	#get info account
	print(user_op.get_info())

	#get mediafire mime type
	print(system_op.get_mime_types())

if __name__ == '__main__':
	sys.exit(main())
