#! /usr/bin/python
from urlparse import parse_qs

def app(env, start_response):
   start_response('200 OK', [('Content-Type', 'text/plain')])
   returnString = ''
   for (key,value) in parse_qs(env['QUERY_STRING'], keep_blank_values=True).iteritems():
      returnString += key + '=' + value + '\n'
   return returnString
   
