#!/usr/bin/python2.7
#Author : Kartik Jagdale <kartikjagdale[at]gmail[dot]com>
"""
Additional Requirements:

1. Requests(version 2.3.0) - requests HTTP library
if you don't have please downoad and install it from <http://python-requests.org>.

2. API KEY : sign up at 'paste.ee' and get your own API_KEY instalize API_KEY variable with the given key.

"""

#Required Library
import sys,os
import argparse
#-------------------------------------------------------------------------------------------------------------

#Clipboard Function 
def addToClipBoard(text):
	cmd = 'echo ' + text.strip() + '| clip'
	os.system(cmd)

# Function to Display End msgs
def end(msg):
	print msg
	return 1


# Our Very own important Function 'THE Pastee'
def pastee(desc, txt):
	import requests # Import Requests
	
	API_KEY = '' # Paste your API_KEY here in single quotes
	post_param = {'key':API_KEY,'description':desc,'language':'plain','paste':txt,'format':'simple'} #Parameters to pass to the Pastee API
	r = None

	try:
		r = requests.post('http://paste.ee/api',params=post_param, verify=False) # Post the params to Pastee API and get the url
	except requests.ConnectionError as e:
		print 'Connection Error'
	
	# Dictonary of errors	
	error = {
			'error_no_key':'No Key present',
			'error_no_paste':'Nothing to paste',
			'error_invalid_key':'Please pass Valid Key',
			'error_invalid_language':'Invalid Langauge'
			}

	if r:
		if r.content in error:
			print error[r.content] #if any error return error
		else:
			print (r.content) #print pastee url to the cmd or python command line
			addToClipBoard(r.content) # add pastee url to clipboard

	return 0


def main():

	parser = argparse.ArgumentParser(
									prog='Pastee',
									usage='To submit files to Paste.ee',
									description = '''This is %(prog)s allow you to submit 
									pastes of their program or text files to paste.ee (A site like pastebin)
									and returns a url to share among the users.  

									This Program also Copies the returned url to Clipboard so that you can
									paste it anywhere you wan and share instantly.
									
									syntax:
									python pastee.py -d(optional)<Description> <filename.extension> or file or 
                                    file_path 
									''',
									epilog = '''
									Example: 
									Note: this has to done from windows command line:
									
									>>python pastee.py -d example examplefile.txt
									''' 
									)
	

	parser.add_argument('-d',default='',type=str,help='Pass Description of file to Paste') #Description
	parser.add_argument('filename', type=argparse.FileType('r'), help='Pass the Filename here') #Filename

	args = parser.parse_args()
	print 'Please wait......'
	try:
		path = os.path.abspath(args.filename.name) #get the absoulte path of the file
		txt = open(path).read() # read the file from given path
	except OSError as error:
		return end('Cannot open file'+error.filename)

	if len(txt)<1:
		return end('File Empty.')
	desc = ''
	if (args.d) != '':
		desc = args.d

	return pastee(desc, txt)



if __name__ == '__main__':
	sys.exit(main())

