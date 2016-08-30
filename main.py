import webapp2
import jinja2
import os

#set up jinja
template_dir = os.path.join(os.path.dirname(__file__), "templates")
jinja_env = jinja2.Environment(loader = jinja2.FileSystemLoader(template_dir), autoescape=True)

class MainHandler(webapp2.RequestHandler):

    def get(self):
        t = jinja_env.get_template("index.html")
        response = t.render()
        self.response.write(response)

class BlogPage(webapp2.RequestHandler):

    def get(self):
        t = jinja_env.get_template("mainblog.html")
        response = t.render()
        self.response.write(response)

app = webapp2.WSGIApplication([
    ('/', MainHandler),
    ('/blog', BlogPage)
], debug=True)
