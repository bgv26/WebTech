#! /usr/bin/python
from urlparse import parse_qsl

def app(env, start_response):
   start_response('200 OK', [('Content-Type', 'text/plain')])
   returnString = ''
   for qsi in parse_qsl(env['QUERY_STRING'], keep_blank_values=True):
      returnString += qsi[0] + '=' + qsi[1] + '\n'
   return returnString
   
