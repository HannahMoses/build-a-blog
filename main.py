#7:48 am Feb15,2017 Wed
#!/usr/bin/env python
#
# Copyright 2007 Google Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
import webapp2
import cgi
import jinja2
import os
from google.appengine.ext import db
# set up jinja
template_dir = os.path.join(os.path.dirname(__file__), "templates")
jinja_env = jinja2.Environment(loader = jinja2.FileSystemLoader(template_dir))

def render_str(self,template,**params):
	t = jinja _env.get_template(template)
 	return t.render(params)




class ViewPostHandler(webapp2.RequestHandler):
    def get(self,id):
        self,response.write()


class MainHandler(webapp2.RequestHandler):
    def get(self):
#        self.response.write('Added jinja2 in app.yaml;imported jinja2 in main.py: Hannah.')
        self.response.write(self.render_str('template.html'))

app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
