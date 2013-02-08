import wsgiref.handlers

from google.appengine.ext import webapp
from google.appengine.ext import db

# Import path handlers
import cloud

def main():  
  application = webapp.WSGIApplication([('/', cloud.RootHandler),
                                        ('/tags', cloud.TagsHandler),
                                        ('/photos', cloud.PhotosHandler),
                                        ('/photo/.*', cloud.PhotoHandler),
                                        ('/photo', cloud.PhotoHandler)],
                                        debug=True)
                                        
  user = cloud.User.get_by_key_name(''.join(['appengine', '00000000000000000000']))
  if not user:
    _initializeDatastore()
  
  # Start application
  wsgiref.handlers.CGIHandler().run(application)


def _initializeDatastore():
  ids = ['00000000000000000000',
         '13135285249873034146',
         '13579554835591866840',
         '01834526878270563924',
         '15535295637542113680',
         '09350102461546351460',
         '05369019939791117399']

  for id in ids:
    cloud.User.get_or_insert(''.join(['appengine', id]), container='appengine', personId=id)


if __name__ == "__main__":
  main()