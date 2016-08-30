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
        t = jinja_env.get_template("newpost.html")
        response = t.render(title ="", err_title="", blog="", err_blog="")
        self.response.write(response)

    def post(self):
        title = self.request.get("title")
        blog = self.request.get("blog")
        title_bool = True
        blog_bool = True
        err_title = ""
        err_blog = ""

        if title == "":
            title_bool = False
            err_title = "Need value for subject!"

        if blog == "":
            blog_bool = False
            err_blog = "Need value for blog!"

        #if both values are not empty redirect to mainblog page
        if title_bool and blog_bool:
            t = jinja_env.get_template("mainblog.html")
            response = t.render()
            self.response.write(response)
        else:
            t = jinja_env.get_template("newpost.html")
            response = t.render(title=title, err_title=err_title, blog=blog, err_blog=err_blog)
            self.response.write(response)

app = webapp2.WSGIApplication([
    ('/', MainHandler),
    ('/blog', BlogPage),
    ('/newpost', NewPost)
], debug=True)
