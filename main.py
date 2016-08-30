import webapp2
import jinja2
import os

#set up jinja
template_dir = os.path.join(os.path.dirname(__file__), "templates")
jinja_env = jinja2.Environment(loader = jinja2.FileSystemLoader(template_dir), autoescape=True)

# Shows index page to link to main blog page
class MainHandler(webapp2.RequestHandler):

    def get(self):
        t = jinja_env.get_template("index.html")
        response = t.render()
        self.response.write(response)

# Shows most recent 5 posts on BLOG
class BlogPage(webapp2.RequestHandler):

    def get(self):
        t = jinja_env.get_template("mainblog.html")
        response = t.render()
        self.response.write(response)

# Shows New Post page
class NewPost(webapp2.RequestHandler):

    def get(self):
        title = self.request.get("title")
        blog = self.request.get("blog")

        t = jinja_env.get_template("newpost.html")
        response = t.render(title ="", blog="")
        self.response.write(response)

app = webapp2.WSGIApplication([
    ('/', MainHandler),
    ('/blog', BlogPage),
    ('/newpost', NewPost)
], debug=True)
