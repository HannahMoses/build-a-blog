#TEMPLATES  feb 20 2017,Mon 6:56pm PRESIDENT'S DAY 4430GSWAY
import os
import webapp2#rgb(0,234,200) also use rgb(0,234,222
form_html = """
<form >
   <body style='background-color:rgb(0,234,200)' >
   <h2 style='color:rgb(234,13,156)'> Add a food </h2>
   <input type = "text"  name="food" ><br><br>
   <input type="hidden" name="food" value="eggs">
   <button> Add food </button>
   </body>
</form>
"""


class Handler (webapp2.RequestHandler):
    def write(self,*a,**kw):
        self.response.out.write(*a,**kw)

class MainPage(Handler):
    def get(self):
        a="<h4 style='color:white;background-color:rgb(234,13,156);text-align:center''>Hello, Udacity !!!!<h4>"
        self.write(a)
        self.write(form_html)

app = webapp2.WSGIApplication([('/',MainPage),
                                ],
                                debug=True)
