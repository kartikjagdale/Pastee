#Pastee
A small Program to submit pastes to [Paste.ee](https://paste.ee/)

####Description
This is program allow you to submit 
pastes of their program or text files to paste.ee (A site like pastebin)
and returns a url to share among the users.  

This Program also copies the returned url to Clipboard so that you can
paste it anywhere you want and share instantly.

####Syntax:
>>python pastee.py -d(optional)<Description> <filename.extension> or file or file_path

####Example:
Note: this has to done from windows command line:
```python
>>python pastee.py -d example examplefile.txt
```
####Requirements:
1. [Python 2.7.0](https://www.python.org/download/releases/2.7/)
2. [Requests(version:2.3.0)](http://python-requests.org)
3. [API_KEY](https://paste.ee/)
