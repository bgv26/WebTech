#! /usr/bin/python
from urlparse import parse_qsl

def app(env, start_response):
   start_response('200 OK', [('Content-Type', 'text/plain')])
   returnString = ''
   for (key, value) in parse_qsl(env['QUERY_STRING'], keep_blank_values=True):
      returnString += key + '=' + value + '\n'
   return returnString
   
