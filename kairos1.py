from urllib2 import Request,urlopen
import json,requests
values = '''
{
        'images': 'https://130513-375933-1-raikfcquaxqncofqfm.stackpathdns.com/wp-content/uploads/2016/06/Johnny-Depp-2.jpg',
        'subject_id':'hello',
        'gallery_name':'hello'
}
'''
headers = {
    'content-Type': 'application/json',
    'app_id' :'1c93bcb4',
    'app_key' : 'a48b7c6e2ef7b3073db95aa6cfb5ec86'
}
request = Request('https://api.karios.com/enroll',data = values, headers = headers)
response_body = urlopen(request).read()
print response_body
