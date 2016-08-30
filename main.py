
import webapp2
import jinja2
import os

#set up jinja
template_dir = os.path.join(os.path.dirname(__file__), "templates")
jinja_env = jinja2.Environment(loader = jinja2.FileSystemLoader(template_dir), autoescape=True)

jinja_env = jinja2.Environment(
                loader=jinja2.FileSystemLoader(template_dir), autoscape=True)

class MainHandler(webapp2.RequestHandler):
    
    def get(self):
        t = jinja_env.get_template("edit.html")
        response = t.render(watchlist=getCurrentWatchlist(), error=self.request.get("error"))
        self.response.write(response)

app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
