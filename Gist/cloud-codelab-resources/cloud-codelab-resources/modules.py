import wsgiref.handlers

from google.appengine.ext import webapp
from google.appengine.ext import db

# Import path handlers
import cloud

class UploadPhoto(webapp.RequestHandler):    
  def get(self):
    self.response.headers['Content-Type'] = 'text/html'
    
    self.response.out.write(getCommonHeader())
    
    self.response.out.write('<h1>Upload Photo:</h1>')    

    self.response.out.write('<iframe name="uploadFrame"></iframe>')    
    
    self.response.out.write(''.join(['<form method="post" enctype="multipart/form-data" action="http://localhost:', cloud.PORT, '/photo" target="uploadFrame">']))
    self.response.out.write('<input type="file" name="file"/>')
    self.response.out.write('<input type="submit" value="Upload"/>')
    self.response.out.write('<input type="hidden" name="container" value="appengine"/>')
    self.response.out.write('<input type="hidden" name="personId"  value="00000000000000000000"/>')
    self.response.out.write('</form>')
    
    self.response.out.write(getCommonFooter())


class FetchUserPhotos(webapp.RequestHandler):    
  def get(self):
    users = db.GqlQuery("SELECT * FROM User")

    self.response.headers['Content-Type'] = 'text/html'
    
    self.response.out.write(getCommonHeader())
    
    self.response.out.write('<h1>Fetch User Photos:</h1>')    

    self.response.out.write('<form>')
    self.response.out.write('<select name="personSelect">')
    for user in users:
      self.response.out.write(''.join(['<option value="', user.personId, '">', user.personId, '</option>']))      
    self.response.out.write('</select>')
    self.response.out.write('<input type="button" value="Fetch photos" onclick="fetchUserPhotos(this)"/>')
    self.response.out.write('</form>')
    self.response.out.write('<div id="fetchUserPhotosResponse"></div>')
    
    self.response.out.write(getCommonFooter())


class FetchGroupPhotos(webapp.RequestHandler):    
  def get(self):
    users = db.GqlQuery("SELECT * FROM User")

    self.response.headers['Content-Type'] = 'text/html'
    
    self.response.out.write(getCommonHeader())
    
    self.response.out.write('<h1>Fetch Group Photos:</h1>')    

    self.response.out.write('<form>')
    self.response.out.write('<select name="peopleSelect" multiple size="10">')
    for user in users:
      self.response.out.write(''.join(['<option value="', user.personId, '">', user.personId, '</option>']))      
    self.response.out.write('</select>')
    self.response.out.write('<input type="button" value="Fetch photos" onclick="fetchGroupPhotos(this)"/>')
    self.response.out.write('</form>')
    self.response.out.write('<div id="fetchGroupPhotosResponse"></div>')
    
    self.response.out.write(getCommonFooter())
            
            
class FetchUserTags(webapp.RequestHandler):    
  def get(self):
    users = db.GqlQuery("SELECT * FROM User")

    self.response.headers['Content-Type'] = 'text/html'
    
    self.response.out.write(getCommonHeader())
    
    self.response.out.write('<h1>Fetch User Tags:</h1>')    

    self.response.out.write('<form>')
    self.response.out.write('<select name="personSelect">')
    for user in users:
      self.response.out.write(''.join(['<option value="', user.personId, '">', user.personId, '</option>']))      
    self.response.out.write('</select>')
    self.response.out.write('<input type="button" value="Fetch tags" onclick="fetchUserTags(this)"/>')
    self.response.out.write('</form>')
    self.response.out.write('<div id="fetchUserTagsResponse"></div>')
    
    self.response.out.write(getCommonFooter())
                
                
class AddPhotoTag(webapp.RequestHandler):    
  def get(self):
    userPhotos = cloud.getPhotosForUser('appengine', '00000000000000000000')

    self.response.headers['Content-Type'] = 'text/html'

    self.response.out.write(getCommonHeader())

    self.response.out.write('<h1>Add Photo Tag:</h1>')    

    self.response.out.write('<form>')
    self.response.out.write('<select name="photoSelect">')
    for photo in userPhotos:
      self.response.out.write(''.join(['<option value="', photo['name'], '">', photo['name'], '</option>']))      
    self.response.out.write('</select>')
    self.response.out.write('<br/>')
    self.response.out.write('<input type="text" name="tagInput"/>')
    self.response.out.write('<input type="button" value="Add tag" onclick="addPhotoTag(this)"/>')
    self.response.out.write('</form>')
    self.response.out.write('<div id="addPhotoTagResponse"></div>')

    self.response.out.write(getCommonFooter())


def main():  
  application = webapp.WSGIApplication([('/modules/uploadPhoto', UploadPhoto),
                                        ('/modules/fetchUserPhotos', FetchUserPhotos),
                                        ('/modules/fetchGroupPhotos', FetchGroupPhotos),
                                        ('/modules/fetchUserTags', FetchUserTags),
                                        ('/modules/addPhotoTag', AddPhotoTag)],
                                        debug=True)
                                        
  wsgiref.handlers.CGIHandler().run(application)


def getCommonHeader():
  header = ''.join(['<html>',
                    '<head>',
                    '<script type="application/javascript" src="http://localhost:', cloud.PORT, '/scripts/prototype-1.6.0.2.js"></script>',
                    '<script type="application/javascript" src="http://localhost:', cloud.PORT, '/scripts/cloud.js"></script>',
                    '</head>',
                    '<body>'])

  return header

def getCommonFooter():
  footer = ''.join(['<p>',
                    '<a href="http://localhost:', cloud.PORT, '/">Back</a>',
                    '</p>',
                    '</body>',
                    '</html>'])

  return footer
  

if __name__ == "__main__":
  main()