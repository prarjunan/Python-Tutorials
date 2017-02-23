#! /usr/bin/python
import sys,os

def search_keyword_in_file( filepath, keyword ):
	for line in open( filepath ):
		if keyword in line:
			print filepath
			break

def walk_folder2( path, keyword ):
	if os.path.isfile( path ):
		search_keyword_in_file( path, keyword )
	elif os.path.isdir( path ):
		for dirpath,dirnames,filenames in os.walk( path, topdown=False ):
			for filename in filenames:
				search_keyword_in_file( os.path.join(dirpath,filename), keyword )
	else:
		print 'Ignoring {}'.format( path )


def walk_folder( path, keyword ):
	if os.path.isdir( path ):
		dir_files_list = os.listdir( path )
		for f in dir_files_list:
			walk_folder( os.path.join( path, f ), keyword )
	elif os.path.isfile( path ):
		search_keyword_in_file( path, keyword )
	else:
		print 'Ignoring {}'.format( path )


if __name__ == '__main__':
	if len( sys.argv ) == 3 :
		filepath = sys.argv[1]
		keyword = sys.argv[2]
		walk_folder2( filepath, keyword )
	else:
		print 'Please enter filepath and the keyword as arguments.'