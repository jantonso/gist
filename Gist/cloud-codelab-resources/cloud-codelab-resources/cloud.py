import sys
sys.path.append('lib')

import re
import cgi
import urllib
import simplejson

from google.appengine.ext import webapp
from google.appengine.ext import db
from math import floor
from time import time

# Signature validation required libraries import
import base64
import hashlib
import oauth

from Crypto.PublicKey import RSA
from Crypto.Util import number

# Local port; change if another process is running on 8080
PORT = '8080'


class User(db.Model):
  personId = db.StringProperty()
  container = db.StringProperty()
  
class Photo(db.Model):
  name = db.StringProperty()
  
  content = db.BlobProperty()
  contentType = db.StringProperty()

  user = db.ReferenceProperty(User)
  
  tags = db.StringListProperty()
  

class RootHandler(webapp.RequestHandler):
  def get(self):
    self.response.headers['Content-Type'] = 'text/html'
    
    self.response.out.write('<html>')
    self.response.out.write('<body>')
    self.response.out.write(''.join(['<a href="http://localhost:', PORT, '/modules/uploadPhoto">Upload photo</a>']))
    self.response.out.write('<br/>')
    self.response.out.write(''.join(['<a href="http://localhost:', PORT, '/modules/fetchUserPhotos">Fetch user photos</a>']))
    self.response.out.write('<br/>')
    self.response.out.write(''.join(['<a href="http://localhost:', PORT, '/modules/fetchGroupPhotos">Fetch group photos</a>']))
    self.response.out.write('<br/>')
    self.response.out.write(''.join(['<a href="http://localhost:', PORT, '/modules/fetchUserTags">Fetch user tags</a>']))
    self.response.out.write('<br/>')
    self.response.out.write(''.join(['<a href="http://localhost:', PORT, '/modules/addPhotoTag">Add photo tag</a>']))
    self.response.out.write('</body>')
    self.response.out.write('</html>')

class TagsHandler(webapp.RequestHandler):    
  def get(self):
    if not _isValidSignature(self):
      self.response.out.write('SIGNATURE INVALID')
      return

    self.response.out.write("TagsHandler received a GET request")

class PhotosHandler(webapp.RequestHandler):    
  def get(self):
    if not _isValidSignature(self):
      self.response.out.write('SIGNATURE INVALID')
      return

    self.response.out.write("PhotosHandler received a GET request")

  def post(self):
    if not _isValidSignature(self):
      self.response.out.write('SIGNATURE INVALID')
      return

    self.response.out.write("PhotosHandler received a POST request")

class PhotoHandler(webapp.RequestHandler):    
  def get(self):
    self.response.out.write("PhotoHandler received a GET request")
  
  def post(self):
    if not _isValidSignature(self):
      self.response.out.write('SIGNATURE INVALID')
      return

    self.response.out.write("PhotoHandler received a POST request")
  

def _isValidSignature(self):

  # Code lab hack:
  # If the container is 'appengine' (e.g. app is running on localhost), return True
  if self.request.get('oauth_consumer_key') == 'appengine':
    return True

  # Construct a RSA.pubkey object
  exponent = 65537
  public_key_str = """0x\
00b1e057678343866db89d7dec2518\
99261bf2f5e0d95f5d868f81d600c9\
a101c9e6da20606290228308551ed3\
acf9921421dcd01ef1de35dd3275cd\
4983c7be0be325ce8dfc3af6860f7a\
b0bf32742cd9fb2fcd1cd1756bbc40\
0b743f73acefb45d26694caf4f26b9\
765b9f65665245524de957e8c547c3\
58781fdfb68ec056d1"""
  public_key_long = long(public_key_str, 16)
  public_key = RSA.construct((public_key_long, exponent))

  # Rebuild the message hash locally
  oauth_request = oauth.OAuthRequest(http_method=self.request.method, 
                                     http_url=self.request.url, 
                                     parameters=self.request.params.mixed())
  message = '&'.join((oauth.escape(oauth_request.get_normalized_http_method()),
                      oauth.escape(oauth_request.get_normalized_http_url()),
                      oauth.escape(oauth_request.get_normalized_parameters()),))
  local_hash = hashlib.sha1(message).digest()

  # Apply the public key to the signature from the remote host
  sig = base64.decodestring(urllib.unquote(self.request.params.mixed()["oauth_signature"]))
  remote_hash = public_key.encrypt(sig, '')[0][-20:]

  # Verify that the locally-built value matches the value from the remote server.
  if local_hash==remote_hash:
    return True
  else:
    return False
