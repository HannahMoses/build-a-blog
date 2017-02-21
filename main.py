#TEMPLATES  feb 20 2017,Mon 6:56pm PRESIDENT'S DAY 4430GSWAY
import os
import webapp2

class Handler (webapp2.RequestHandler):
    def write(self,*a,**kw):
        self.response.out.write(*a,**kw)

class MainPage(Handler):
    def get(self):
        self.write("Hello, Udacity !")

app = webapp2.WSGIApplication([('/',MainPage),
                                ],
                                debug=True)
